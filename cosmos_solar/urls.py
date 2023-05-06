from django.urls import path, include
from .views import home


from django.conf import settings

urlpatterns = [
    path("", home, name="home"),
]


