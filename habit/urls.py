from rest_framework import routers

from habit.apps import HabitConfig
from django.urls import path

from habit import views
from habit.views import AwardViewSet

router = routers.DefaultRouter()
router.register(r'award', AwardViewSet, basename='award')


app_name = HabitConfig.name

urlpatterns = [
    path('habit_create/', views.CreateHabitCreateAPIView.as_view(), name='habit_create'),
    path('habit_list/', views.HabitListAPIView.as_view(), name='habit_list'),
    path('habit_update/<int:pk>/', views.HabitUpdateAPIView.as_view(), name='habit_update'),
    path('habit_retrieve/<int:pk>/', views.HabitRetrieveAPIView.as_view(), name='habit_retrieve'),
    path('habit_destroy/<int:pk>/', views.HabitDestroyAPIView.as_view(), name='habit_destroy'),
] + router.urls
