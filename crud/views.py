from django.contrib import messages
from django.contrib.auth import get_user_model
from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse, request
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from crud.forms import CreateStudentClassForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.contrib.auth.mixins import LoginRequiredMixin 

from crud.models import StudentClass
from users.models import Role

# Create your views here.

User = get_user_model()

class HomeView(LoginRequiredMixin, View):

    def get(self, request):
        if not request.user.role:
            return HttpResponse("You dont have any role assigned.", status=401)

        if request.user.role.id == Role.STUDENT:
            context = {
                'object': request.user
            }
            return render(request, 'crud/user-details.html', context)
        elif request.user.role.id == Role.TEACHER:
            students = User.objects.filter(role__id = Role.STUDENT, is_active=True).order_by('-id')
            context = {
                'students': students
            }
            return render(request, 'crud/home.html', context)

        return HttpResponse("Sorry, you dont have the required role to access the app.", status=401)


class StudentDetailView(LoginRequiredMixin, DetailView):
    model           = User
    template_name   = 'crud/user-details.html'
    success_url     = reverse_lazy('crud:HomeView')

class GradeUpdateView(LoginRequiredMixin, UpdateView):
    model           = StudentClass
    fields          = ['class_id', 'grade']
    template_name   = 'crud/update-student-grade.html'
    success_url     = reverse_lazy('crud:HomeView')

class GradeDeleteView(LoginRequiredMixin, DeleteView):
    model           = StudentClass
    template_name   = 'crud/delete-student-grade.html'
    success_url     = reverse_lazy('crud:HomeView')


class GradeCreateView(View):
    def get(self, request, student_id):
        student = get_object_or_404(User, id=student_id)
        form = CreateStudentClassForm()
        context = {
            'form': form
        }
        return render(request, 'crud/create-student-grade.html', context)
    
    def post(self, request, student_id):
        student = get_object_or_404(User, id=student_id)
        class_id = request.POST.get('class_id', None)
        class_ins = student.classes.filter(class_id=class_id).first()
        form = CreateStudentClassForm(request.POST, instance=class_ins)
        if form.is_valid():
            class_ins = form.save(commit=False)
            class_ins.student = student
            class_ins.save()
            return redirect(reverse("crud:StudentDetailView", kwargs={'pk': student.pk}))

        context = {
            'form': form
        }
        return render(request, 'crud/create-student-grade.html', context)