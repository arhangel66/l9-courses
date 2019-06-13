from rest_framework.serializers import ModelSerializer

from courses.users.models import User


class BaseUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "name")
        abstract = True


# Later StudentSerializer and TeacherSerializer will have different features.
class StudentSerializer(BaseUserSerializer):
    pass


class TeacherSerializer(BaseUserSerializer):
    pass
