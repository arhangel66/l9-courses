from django.urls import path, include

from .views import router

app_name = "users"
urlpatterns = [
    # endregion
    path("", include(router.urls)),
]
