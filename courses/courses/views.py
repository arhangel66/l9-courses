from rest_framework import viewsets, routers

# Create your views here.
from courses.courses.models import Course, Lesson
from courses.courses.serializers import CourseSerializer, LessonSerializer

router = routers.SimpleRouter()


class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class LessonViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


router.register(r"courses", CourseViewSet)
router.register(r"lessons", LessonViewSet)
