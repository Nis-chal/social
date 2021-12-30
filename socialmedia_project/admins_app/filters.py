import django_filters

from django_filters import CharFilter
from django.contrib.auth.models import User


class UsersFilter(django_filters.FilterSet):
    email_contains = CharFilter(field_name='email', lookup_expr='icontains')
    class Meta:
        model = User
        fields = []

