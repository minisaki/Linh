from django.urls import path
from . import views
urlpatterns = [
    path("profile_saler/<int:user_id>", views.profileSaler.as_view(),
         name="profile_saler"),
    path("rating/<int:user_id>", views.RateUserView.as_view(),
         name="rating"),
]