from django.http import JsonResponse


def health_check(request):
    return JsonResponse({"message": "Welcome to Django Application"})
