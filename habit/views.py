from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

from habit.models import Award, Habit
from habit.pagination import ListPaginator
from habit.permissions import IsModerator, IsOwner, IsSuperUser
from habit.serializers import AwardSerializer, HabitSerializer


class CreateHabitCreateAPIView(generics.CreateAPIView):
    """ Эндпоинт создания привычки """
    serializer_class = HabitSerializer
    pagination_class = ListPaginator
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.user = self.request.user
        new_habit.save()


class HabitUpdateAPIView(generics.UpdateAPIView):
    """ Эндпоинт на обновление информации о привычки """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    pagination_class = ListPaginator
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]

class HabitRetrieveAPIView(generics.RetrieveAPIView):
    """ Эндпоинт на получение подробной информации о привычки """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    pagination_class = ListPaginator
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]

class HabitListAPIView(generics.ListAPIView):
    """ Эндпоинт на получение списка привычек"""

    serializer_class = HabitSerializer
    pagination_class = ListPaginator

    def get_queryset(self):
        if self.request.user.is_staff:
            queryset = Habit.objects.all()
        elif self.request.user.is_authenticated:
            queryset = Habit.objects.filter(user=self.request.user)
        else:
            queryset = Habit.objects.filter(is_public=True)

        return queryset

class HabitDestroyAPIView(generics.DestroyAPIView):
    """ Эндпоинт удаления привычки"""
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsSuperUser | IsOwner]


class AwardViewSet(viewsets.ModelViewSet):
    """ CRUD для награды """
    serializer_class = AwardSerializer
    queryset = Award.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = ListPaginator
