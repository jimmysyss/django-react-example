from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hello', views.poll_get, name='poll_get')
]

router = DefaultRouter()
router.register(r'poll', views.PollViewSet, base_name='poll')
urlpatterns += router.urls
