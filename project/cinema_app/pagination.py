from rest_framework import pagination
from rest_framework.response import Response


# Paginacja - do edycji pól (zmienić w settings.py: REST_FRAMEWORK)
class CustomPagination(pagination.PageNumberPagination):
    def get_paginated_response(self, data):
        return Response({  # tutaj można zmienić
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'count': self.page.paginator.count,
            'results': data,
        })
