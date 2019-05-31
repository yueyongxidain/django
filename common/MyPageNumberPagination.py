from rest_framework.pagination import PageNumberPagination

class MyPageNumberPagination(PageNumberPagination):
    page_size = 2
    max_page_size = 5
    page_size_query_param = 'size'
    page_query_param = 'page'