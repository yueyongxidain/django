from django_filters import rest_framework as filters
from .models import goodlist

class GoodsFilter(filters.FilterSet):
    goodName = filters.CharFilter(field_name='goodName', lookup_expr='icontains')
    class Meta:
        model = goodlist
        fields = ['goodName']