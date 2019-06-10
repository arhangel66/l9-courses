from django.contrib import admin

# Register your models here.
from courses.courses.models import Course, Lesson


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "title")


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("id",)
