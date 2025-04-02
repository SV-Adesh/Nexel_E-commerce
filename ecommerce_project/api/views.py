from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth.models import User
from accounts.models import UserProfile
from products.models import Category, Product
from orders.models import Order, OrderItem
from .serializers import (
    UserSerializer, UserProfileSerializer,
    CategorySerializer, ProductSerializer,
    OrderSerializer, OrderItemSerializer
)
import stripe
from django.conf import settings
from rest_framework.permissions import AllowAny

stripe.api_key = settings.STRIPE_SECRET_KEY

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get_permissions(self):
        if self.action == 'create':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(request.data['password'])
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def me(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserProfile.objects.filter(user=self.request.user)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

    def get_queryset(self):
        queryset = Product.objects.all()
        category = self.request.query_params.get('category', None)
        if category is not None:
            queryset = queryset.filter(category__slug=category)
        return queryset

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Order.objects.all()
        return Order.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['post'])
    def create_payment_intent(self, request, pk=None):
        order = self.get_object()
        try:
            intent = stripe.PaymentIntent.create(
                amount=int(order.total_amount * 100),  # Convert to cents
                currency='usd',
                metadata={'order_id': order.id}
            )
            order.stripe_payment_intent = intent.id
            order.save()
            return Response({
                'clientSecret': intent.client_secret
            })
        except Exception as e:
            return Response({
                'error': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            return OrderItem.objects.all()
        return OrderItem.objects.filter(order__user=self.request.user)

@api_view(['GET'])
@permission_classes([AllowAny])
def initialize_sample_data(request):
    """
    Endpoint to initialize sample data if none exists.
    Call this endpoint to create sample categories and products.
    """
    # Check if we have any categories
    category_count = Category.objects.count()
    
    # Create a sample category if none exists
    sample_category = None
    if category_count == 0:
        try:
            sample_category = Category(
                name="Sample Category",
                description="A sample category for test products"
            )
            sample_category.save()
        except Exception as e:
            return Response({"error": f"Error creating sample category: {str(e)}"}, status=500)
    else:
        # Use the first existing category
        sample_category = Category.objects.first()
    
    # Check if we have any products
    product_count = Product.objects.count()
    
    # If no products, create a sample one
    if product_count == 0 and sample_category:
        from io import BytesIO
        from django.core.files.base import ContentFile
        from PIL import Image
        
        # Create a 600x400 RGB image with a blue background
        img = Image.new('RGB', (600, 400), color=(53, 121, 246))
        img_io = BytesIO()
        img.save(img_io, format='JPEG', quality=90)
        img_io.seek(0)
        placeholder_image = ContentFile(img_io.getvalue(), name="sample-product.jpg")
        
        try:
            sample_product = Product(
                name="Sample Product",
                price=100.0,
                description="Test product", 
                stock=10,
                slug="sample-product",
                category=sample_category,
                available=True
            )
            
            sample_product.image = placeholder_image
            sample_product.save()
        except Exception as e:
            return Response({"error": f"Error creating sample product: {str(e)}"}, status=500)
    
    # Create superuser if none exists
    if not User.objects.filter(is_superuser=True).exists():
        try:
            User.objects.create_superuser(
                username="admin",
                email="admin@example.com",
                password="admin123"
            )
        except Exception as e:
            pass  # Ignore superuser creation errors
    
    return Response({
        "message": "Sample data initialization complete",
        "categories": Category.objects.count(),
        "products": Product.objects.count()
    })
