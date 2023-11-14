from celery import shared_task
from habit.service import check_habit_time


@shared_task
def periodical_task():
    """ """
    check_habit_time()
