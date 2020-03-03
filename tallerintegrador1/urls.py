from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from Ultrasonic import views

router = routers.DefaultRouter()
router.register(r'measures', views.UltrasonicViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    path('admin/', admin.site.urls),
]