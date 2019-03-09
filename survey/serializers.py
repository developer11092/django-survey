from rest_framework import serializers
from rest_framework import exceptions
from .models import Survey, Question
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


# class QuestionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Question
#         fields = "__all__"

#         read_only_fields = {'survey', }

# class SurveySerializer(serializers.ModelSerializer):
#     questions = QuestionSerializer(many=True)

#     class Meta:
#         model = Survey
#         fields = [
#             "id",
#             "name",
#             "description",
#             "is_published",
#             "need_logged_user",
#             "display_by_question",
#             "template",
#             "allows_multiple_interviews",
#             "company",
#             "question", 
#         ]

class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = "__all__"




class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get("username", "")
        password = data.get("password", "")

        if username and password:
            user = authenticate(username = username, password = password)
            if user:
                if user.is_active:
                    data["user"] = user
                else:
                    msg = "User is deactivated."
                    raise exceptions.ValidationError(msg)
            else:
                msg = "Unable to login with given credentials."
                raise exceptions.ValidationError(msg)
        else:
            msg = "Must provide username and password both."
            raise exceptions.ValidationError(msg)
        return data