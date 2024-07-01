from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Niveaux, Ressource, Lesson, Courses
from .forms import NiveauForm, RessourceForm, LessonForm, CourseForm

def acceuil(request):
    return render(request, 'base.html')

# Niveau views
class NiveauListView(ListView):
    model = Niveaux
    template_name = 'niveau_list.html'

class NiveauCreateView(CreateView):
    model = Niveaux
    form_class = NiveauForm
    template_name = 'niveau_form.html'
    success_url = reverse_lazy('niveau_list')

class NiveauUpdateView(UpdateView):
    model = Niveaux
    form_class = NiveauForm
    template_name = 'niveau_form.html'
    success_url = reverse_lazy('niveau_list')

class NiveauDeleteView(DeleteView):
    model = Niveaux
    template_name = 'niveau_confirm_delete.html'
    success_url = reverse_lazy('niveau_list')

# Ressource views
class RessourceListView(ListView):
    model = Ressource
    template_name = 'ressource_list.html'

class RessourceCreateView(CreateView):
    model = Ressource
    form_class = RessourceForm
    template_name = 'ressource_form.html'
    success_url = reverse_lazy('ressource_list')

class RessourceUpdateView(UpdateView):
    model = Ressource
    form_class = RessourceForm
    template_name = 'ressource_form.html'
    success_url = reverse_lazy('ressource_list')

class RessourceDeleteView(DeleteView):
    model = Ressource
    template_name = 'ressource_confirm_delete.html'
    success_url = reverse_lazy('ressource_list')

# Lesson views
class LessonListView(ListView):
    model = Lesson
    template_name = 'lesson_list.html'

class LessonCreateView(CreateView):
    model = Lesson
    form_class = LessonForm
    template_name = 'lesson_form.html'
    success_url = reverse_lazy('lesson_list')

class LessonUpdateView(UpdateView):
    model = Lesson
    form_class = LessonForm
    template_name = 'lesson_form.html'
    success_url = reverse_lazy('lesson_list')

class LessonDeleteView(DeleteView):
    model = Lesson
    template_name = 'lesson_confirm_delete.html'
    success_url = reverse_lazy('lesson_list')

# Course views
class CourseListView(ListView):
    model = Courses
    template_name = 'course_list.html'

class CourseCreateView(CreateView):
    model = Courses
    form_class = CourseForm
    template_name = 'course_form.html'
    success_url = reverse_lazy('course_list')

class CourseUpdateView(UpdateView):
    model = Courses
    form_class = CourseForm
    template_name = 'course_form.html'
    success_url = reverse_lazy('course_list')

class CourseDeleteView(DeleteView):
    model = Courses
    template_name = 'course_confirm_delete.html'
    success_url = reverse_lazy('course_list')
