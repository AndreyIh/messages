from django.urls import path

from .views import home_view


urlpatterns = [
    path('', home_view, name='home'),
    path('author-<int:author>/last-<int:time>-hours/reverse-<str:reverse>/', home_view, name='home_sorted'),
]
