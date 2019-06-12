from django_filters import rest_framework as filters
from .models import goodlist

class GoodsFilter(filters.FilterSet):
    goodName = filters.CharFilter(field_name='goodName', lookup_expr='icontains')
    goodType = filters.NumberFilter(field_name='goodType')
    isOnsale = filters.BooleanFilter(field_name='isOnsale')
    goodIsNew =filters.BooleanFilter(field_name='goodIsNew')
    class Meta:
        model = goodlist
        fields = ['goodName','goodType','isOnsale']