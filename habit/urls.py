from rest_framework import routers

from habit.apps import HabitConfig
from django.urls import path

from habit import views
from habit.views import AwardViewSet

router = routers.DefaultRouter()
router.register(r'award', AwardViewSet, basename='award')


app_name = HabitConfig.name

urlpatterns = [
    path('create/', views.HabitCreateAPIView.as_view(), name='habit_create'),
    path('list/', views.HabitListAPIView.as_view(), name='habit_list'),
    path('update/<int:pk>/', views.HabitUpdateAPIView.as_view(), name='habit_update'),
    path('retrieve/<int:pk>/', views.HabitRetrieveAPIView.as_view(), name='habit_retrieve'),
    path('destroy/<int:pk>/', views.HabitDestroyAPIView.as_view(), name='habit_destroy'),
] + router.urls
