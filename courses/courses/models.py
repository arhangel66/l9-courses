from django.conf import settings

# Create your models here.
from django.db.models import ManyToManyField, ForeignKey, CASCADE, DateTimeField
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.models import TimeStampedModel, TitleDescriptionModel


class Course(TimeStampedModel, TitleDescriptionModel):
    teachers = ManyToManyField(
        settings.AUTH_USER_MODEL,
        verbose_name=_("teachers"),
        blank=True,
        related_name="teacher_courses",
    )

    # TODO make separate table for connect students and courses. Then we will see date of start and reason.
    students = ManyToManyField(
        settings.AUTH_USER_MODEL,
        verbose_name=_("students"),
        blank=True,
        related_name="student_courses",
    )

    class Meta:
        verbose_name_plural = _("courses")

    def __str__(self):
        return f"Course (#{self.pk}) {self.title}"


class Lesson(TimeStampedModel, TitleDescriptionModel):
    course = ForeignKey(
        Course, verbose_name=_("course"), related_name="lessons", on_delete=CASCADE,
    )
    start_date = DateTimeField(verbose_name=_("start date"), null=True, blank=True)


# class Enrollment(TimeStampedModel):
#     student = ForeignKey(
#         settings.AUTH_USER_MODEL,
#         verbose_name=_("student"),
#         related_name="enrollments",
#         on_delete=CASCADE,
#     )
#     course = ForeignKey(
#         Course,
#         verbose_name=_("course"),
#         related_name="enrollments",
#         on_delete=CASCADE,
#     )
