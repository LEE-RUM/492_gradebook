from django.urls import path
from . import views

#url paths for the crud part of website
app_name = "crud"

urlpatterns = [
    path('', views.HomeView.as_view(), name='HomeView'),
    path('details_student/<int:pk>/', views.StudentDetailView.as_view(), name='StudentDetailView'),

    path('create_grade/<int:student_id>/', views.GradeCreateView.as_view(), name='GradeCreateView'),
    path('update_grade/<int:pk>/', views.GradeUpdateView.as_view(), name='GradeUpdateView'),
    path('delete_grade/<int:pk>/', views.GradeDeleteView.as_view(), name='GradeDeleteView'),
]