from django.urls import path
from . import views

urlpatterns = [
    path(
        "",views.HomeResturantListView.as_view(),name='post_list'
    )
]
