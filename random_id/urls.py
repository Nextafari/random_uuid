from django.urls import path
from . import views

urlpatterns = [
    path(
        "random_id",
        views.RandomUUID.as_view(),
        name="random_id"
    )
]
