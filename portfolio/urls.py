from django.urls import path
from . import views

app_name = 'portfolio'  # Pour l'espace de noms dans les templates

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('experience/', views.ExperienceView.as_view(), name='experience'),
    path('education/', views.EducationView.as_view(), name='education'),
    path('projects/', views.ProjectsView.as_view(), name='projects'),
    path('cv/', views.CVView.as_view(), name='cv'),
    path('cv/print/', views.cv_print_version, name='cv_print'),  # Version imprimable du CV
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('search/', views.search_view, name='search'),  # Nouvelle URL pour la recherche
]
