from django.urls import path
from .views import SignUpView, FavoriteTalkList, FavoriteTalkCreate, FavoriteTalkUpdate, PublicFavoriteTalkList, LogoutView

app_name = "accounts"
urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("talks/", FavoriteTalkList.as_view(), name="favorite_talk_list"),
    path("talks/add/", FavoriteTalkCreate.as_view(), name="favorite_talk_add"),
    path("talks/<str:pk>/edit/", FavoriteTalkUpdate.as_view(), name="favorite_talk_edit"),
    path("public/talks/", PublicFavoriteTalkList.as_view(), name="public_favorite_talk_list"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
