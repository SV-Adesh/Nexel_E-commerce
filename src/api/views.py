from django.http import JsonResponse

def api_status(request):
    return JsonResponse({"status": "API is running"}) 