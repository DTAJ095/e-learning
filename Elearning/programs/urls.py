from django.urls import path
from . import views


urlpatterns = [\
    path('acceuil/', views.acceuil, name="acceuil"),
    # Urls liées aux Niveaux
    path('niveaux/', views.NiveauListView.as_view(), name='niveau_list'),
    path('niveaux/create/', views.NiveauCreateView.as_view(), name='niveau_create'),
    path('niveaux/<int:pk>/update/', views.NiveauUpdateView.as_view(), name='niveau_update'),
    path('niveaux/<int:pk>/delete/', views.NiveauDeleteView.as_view(), name='niveau_delete'),

    # Urls liées aux Ressources
    path('ressources/', views.RessourceListView.as_view(), name='ressource_list'),
    path('ressources/create/', views.RessourceCreateView.as_view(), name='ressource_create'),
    path('ressources/<int:pk>/update/', views.RessourceUpdateView.as_view(), name='ressource_update'),
    path('ressources/<int:pk>/delete/', views.RessourceDeleteView.as_view(), name='ressource_delete'),

    # Urls liées aux Leçons
    path('lecons/', views.LessonListView.as_view(), name='lesson_list'),
    path('lecons/create/', views.LessonCreateView.as_view(), name='lesson_create'),
    path('lecons/<int:pk>/update/', views.LessonUpdateView.as_view(), name='lesson_update'),
    path('lecons/<int:pk>/delete/', views.LessonDeleteView.as_view(), name='lesson_delete'),

    # Urls liées aux Cours
    path('cours/', views.CourseListView.as_view(), name='course_list'),
    path('cours/create/', views.CourseCreateView.as_view(), name='course_create'),
    path('cours/<int:pk>/update/', views.CourseUpdateView.as_view(), name='course_update'),
    path('cours/<int:pk>/delete/', views.CourseDeleteView.as_view(), name='course_delete'),
]