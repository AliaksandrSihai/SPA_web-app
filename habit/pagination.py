from rest_framework.pagination import PageNumberPagination


class ListPaginator(PageNumberPagination):
    """ Пагинация вывода """
    page_size = 5
    page_query_param = 'page'
    page_size_query_param = 25
