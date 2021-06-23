from django.urls import path
from . import views
urlpatterns = [
    path("profile_saler/<int:user_id>", views.profileSaler.as_view(),
         name="profile_saler"),
    path("rating/<int:user_id>", views.RateUserView.as_view(),
         name="rating"),
    path("report/", views.ReportView.as_view(), name="report"),
    path("follow/", views.FollowView.as_view(), name="follow")
]