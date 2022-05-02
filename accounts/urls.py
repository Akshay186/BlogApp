from django.urls import path, include
from .views import UserRegisterView, UserEditView, ChangePasswordView, ProfileView, CreateProfile

urlpatterns = [
    path('user_register/', UserRegisterView.as_view(), name='user_register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('password/', ChangePasswordView.as_view(), name='change_password'),
    path('profile/<int:pk>', ProfileView.as_view(), name='user-profile'),
    path('create_profile', CreateProfile, name='create-profile'),
]
