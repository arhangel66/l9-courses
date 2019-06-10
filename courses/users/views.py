from rest_framework import viewsets
from rest_framework.routers import SimpleRouter

from courses.users.models import User

# Create your views here.
from courses.users.serializers import StudentSerializer, TeacherSerializer

router = SimpleRouter()


class StudentViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing accounts.
    """

    queryset = User.objects.filter(is_staff=False)
    serializer_class = StudentSerializer


class TeacherViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing accounts.
    """

    queryset = User.objects.filter(is_staff=True)
    serializer_class = TeacherSerializer


router.register("students", StudentViewSet)
router.register("teachers", TeacherViewSet)
