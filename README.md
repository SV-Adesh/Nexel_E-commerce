# E-Commerce Platform

A full-featured e-commerce platform built with Django REST Framework and React.js.

## Features

### Customer Portal
- User authentication and registration
- Browse products with categories and filters
- Shopping cart and wishlist functionality
- Secure checkout with Stripe integration
- Order history and tracking

### Admin Portal
- Role-based authentication
- Product and category management
- Order management
- Sales analytics

## Tech Stack

### Backend
- Django
- Django REST Framework
- MySQL
- Stripe API

### Frontend
- React.js
- Material-UI
- Axios
- React Router

## Setup Instructions

### Prerequisites
- Python 3.8+
- Node.js 14+
- MySQL

### Backend Setup

1. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root with the following variables:
```
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_NAME=ecommerce_db
DATABASE_USER=your-db-user
DATABASE_PASSWORD=your-db-password
DATABASE_HOST=localhost
DATABASE_PORT=3306
STRIPE_SECRET_KEY=your-stripe-secret-key
STRIPE_PUBLISHABLE_KEY=your-stripe-publishable-key
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Start the Django development server:
```bash
python manage.py runserver
```

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Create a `.env` file in the frontend directory:
```
REACT_APP_API_URL=http://localhost:8000
REACT_APP_STRIPE_PUBLISHABLE_KEY=your-stripe-publishable-key
```

4. Start the development server:
```bash
npm start
```

## API Endpoints

### Authentication
- POST `/api/token/` - Obtain JWT token
- POST `/api/token/refresh/` - Refresh JWT token

### Users
- GET `/api/users/me/` - Get current user
- POST `/api/users/` - Register new user
- GET `/api/profiles/me/` - Get user profile
- PATCH `/api/profiles/me/` - Update user profile

### Products
- GET `/api/products/` - List products
- POST `/api/products/` - Create product (admin only)
- GET `/api/products/:id/` - Get product details
- PATCH `/api/products/:id/` - Update product (admin only)
- DELETE `/api/products/:id/` - Delete product (admin only)

### Categories
- GET `/api/categories/` - List categories
- POST `/api/categories/` - Create category (admin only)
- GET `/api/categories/:id/` - Get category details
- PATCH `/api/categories/:id/` - Update category (admin only)
- DELETE `/api/categories/:id/` - Delete category (admin only)

### Orders
- GET `/api/orders/` - List user orders
- POST `/api/orders/` - Create order
- GET `/api/orders/:id/` - Get order details
- PATCH `/api/orders/:id/` - Update order status (admin only)
- POST `/api/orders/:id/create_payment_intent/` - Create Stripe payment intent

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License. 