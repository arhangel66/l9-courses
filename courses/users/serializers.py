from rest_framework.serializers import ModelSerializer

from courses.users.models import User


class StudentSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "name")


class TeacherSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "name")
