from django.urls import path
from . import views

urlpatterns = [
    path(
        "random-id",
        views.RandomUUID.as_view(),
        name="random_id"
    )
]
