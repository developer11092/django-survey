from django.shortcuts import render
from rest_framework import viewsets
from survey.models import Survey
from survey.serializers import SurveySerializer# , QuestionSerializer
from survey.serializers import LoginSerializer
from rest_framework.views import APIView
from django.contrib.auth import login as django_login, logout as django_logout
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny

class SurveyView(viewsets.ModelViewSet):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer

# class QuestionView(viewsets.ModelViewSet):
#     queryset = Question.objects.all()
#     serializer_class = QuestionSerializer

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        django_login(request, user)
        token, created = Token.objects.get_or_create(user = user)
        return Response({"token": token.key}, status = 200)

    def get_permissions(self):
        if self.action == 'retrieve':
            return [AllowAny(), ]        
        return super(LoginView, self).get_permissions()

# class LogoutView(APIView):
#     authentication_classes = (TokenAuthentication)

#     def post(self, request):
#         django_logout(request)
#         return Response(status = 204)



class LogoutView(APIView):
    def get(self, request):
        # simply delete the token to force a login
        user_token = request.user.auth_token
        user_token.delete()
        return Response(status= 204)