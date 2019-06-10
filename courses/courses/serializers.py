from rest_framework.serializers import ModelSerializer

from courses.courses.models import Course, Lesson


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ("pk", "title", "description", "students", "teachers", "lessons")


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = ("pk", "title", "description", "start_date", "course")
