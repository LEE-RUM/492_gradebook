from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

#url paths for user section of project
app_name = "users"

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='RegisterView'),
    path('teacher_register/', views.TeacherRegisterView.as_view(), name='TeacherRegisterView'),
    path('profile/', views.ProfileView.as_view(), name='ProfileView'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]