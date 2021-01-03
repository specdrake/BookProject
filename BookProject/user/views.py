import json
from django.contrib.auth import authenticate, login
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from rest_framework import views



class CheckAuth(APIView):
    authentication_classes = [SessionAuthentication]
    def get(self, request):
        return Response({'detail': 'You\'re Authenticated'})






@ensure_csrf_cookie
def set_csrf_token(request):
    return JsonResponse({"details": "CSRF cookie set"})



@require_POST
def LoginView(request):
    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')
    if username is None or password is None:
        return JsonResponse({
            "errors": {
                "__all__": "Please enter both username and password"
            }
        }, status=400)
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return JsonResponse({"detail": "Success"})
    return JsonResponse(
        {"detail": "Invalid credentials"},
        status=400,
    )