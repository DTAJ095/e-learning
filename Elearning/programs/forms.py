from django import forms
from .models import Niveaux, Ressource, Lesson, Courses, Formation


class NiveauForm(forms.ModelForm):
    class Meta:
        model = Niveaux
        fields = ['nom', 'description']

class RessourceForm(forms.ModelForm):
    class Meta:
        model = Ressource
        fields = ['ressource_id', 'title', 'lesson_id']

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['lesson_id', 'course_id', 'title', 'description']

class CourseForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields = ['course_id', 'title', 'instructeur', 'description']

class FormationForm(forms.ModelForm):
    class Meta:
        model= Formation
        fields =['formation_id', 'tutorat', 'title']