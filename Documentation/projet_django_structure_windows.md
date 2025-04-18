# Structure de Projet Django - Portfolio Personnel (Windows)

Ce document décrit la structure recommandée pour un projet Django de portfolio personnel sur Windows, avec séparation claire des fichiers HTML, CSS et JavaScript.

## Installation initiale

```batch
:: Créer un dossier pour le projet
mkdir portfolio_project
cd portfolio_project

:: Créer et activer un environnement virtuel
python -m venv venv
venv\Scripts\activate

:: Installer Django
pip install django
```

## Création du projet

```batch
:: Créer le projet Django dans le dossier courant
:: Utilisation de "config" comme nom pour le dossier de configuration
django-admin startproject config .

:: Créer l'application portfolio
python manage.py startapp portfolio
```

## Structure de dossiers complète

```
portfolio_project/              # Dossier racine du projet
│
├── manage.py                   # Script de gestion Django (généré automatiquement)
├── venv/                       # Environnement virtuel Python
│
├── config/                     # Configuration du projet Django
│   ├── __init__.py
│   ├── settings.py             # Paramètres du projet
│   ├── urls.py                 # URLs du projet
│   ├── asgi.py
│   └── wsgi.py
│
└── portfolio/                  # Application principale
    ├── __init__.py
    ├── admin.py                # Configuration de l'admin Django
    ├── apps.py                 # Configuration de l'application
    ├── models.py               # Modèles de données
    ├── views.py                # Logique de vues
    ├── urls.py                 # URLs de l'application
    ├── migrations/             # Migrations de base de données
    │   └── __init__.py
    │
    ├── static/                 # Fichiers statiques
    │   ├── css/
    │   │   └── style.css       # Styles CSS principaux
    │   ├── js/
    │   │   └── main.js         # JavaScript principal
    │   ├── img/                # Images
    │   └── pdf/                # Fichiers PDF
    │       └── cv.pdf          # CV téléchargeable
    │
    └── templates/              # Templates HTML
        └── portfolio/
            ├── base.html       # Template de base
            ├── index.html      # Page d'accueil
            ├── about.html      # À propos
            ├── experience.html # Expérience professionnelle
            ├── education.html  # Formation
            ├── projects.html   # Projets
            ├── cv.html         # CV en ligne
            └── contact.html    # Page de contact
```

## Script Batch pour créer la structure

Copiez ce script dans un fichier `.bat` et exécutez-le après avoir créé le projet Django de base :

```batch
@echo off
echo Création de la structure du projet Django Portfolio...

:: Création des dossiers pour templates
mkdir portfolio\templates
mkdir portfolio\templates\portfolio

:: Création des dossiers pour fichiers statiques
mkdir portfolio\static
mkdir portfolio\static\css
mkdir portfolio\static\js
mkdir portfolio\static\img
mkdir portfolio\static\pdf

:: Création des fichiers templates HTML vides
type nul > portfolio\templates\portfolio\base.html
type nul > portfolio\templates\portfolio\index.html
type nul > portfolio\templates\portfolio\about.html
type nul > portfolio\templates\portfolio\experience.html
type nul > portfolio\templates\portfolio\education.html
type nul > portfolio\templates\portfolio\projects.html
type nul > portfolio\templates\portfolio\cv.html
type nul > portfolio\templates\portfolio\contact.html

:: Création des fichiers CSS et JS vides
type nul > portfolio\static\css\style.css
type nul > portfolio\static\js\main.js

:: Création du fichier urls.py dans l'application portfolio
type nul > portfolio\urls.py

echo Structure créée avec succès !
```

## Configuration du projet

### Mise à jour de config/settings.py

```python
# Ajouter l'application 'portfolio' à INSTALLED_APPS
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'portfolio',  # Notre application
]

# Configuration des fichiers statiques
import os  # Ajouter en haut du fichier

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    # BASE_DIR / "static",  # Décommentez si vous avez des fichiers statiques au niveau du projet
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Configuration des fichiers média
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Internationalisation
LANGUAGE_CODE = 'fr-fr'
TIME_ZONE = 'Europe/Paris'

# Configuration des emails (pour le formulaire de contact)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # Pour le développement
DEFAULT_FROM_EMAIL = 'noreply@example.com'
CONTACT_EMAIL = 'contact@example.com'
```

### Configuration de config/urls.py

```python
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio.urls')),  # Routes de l'application portfolio
]

# Pour servir les fichiers média en développement
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

### Configuration de portfolio/urls.py

```python
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
    path('contact/', views.ContactView.as_view(), name='contact'),
]
```

### Configuration de portfolio/views.py

```python
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

# Vues basées sur les classes
class IndexView(TemplateView):
    template_name = 'portfolio/index.html'

class AboutView(TemplateView):
    template_name = 'portfolio/about.html'

class ExperienceView(TemplateView):
    template_name = 'portfolio/experience.html'

class EducationView(TemplateView):
    template_name = 'portfolio/education.html'

class ProjectsView(TemplateView):
    template_name = 'portfolio/projects.html'

class CVView(TemplateView):
    template_name = 'portfolio/cv.html'

class ContactView(TemplateView):
    template_name = 'portfolio/contact.html'
    
    # Pour traiter le formulaire de contact
    def post(self, request, *args, **kwargs):
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')
        
        # Validation basique
        if not all([name, email, message]):
            messages.error(request, 'Veuillez remplir tous les champs du formulaire.')
            return self.get(request, *args, **kwargs)
        
        # Envoi de l'email
        try:
            send_mail(
                f'Message du portfolio de {name}',
                f'Message de: {name}\nEmail: {email}\n\n{message}',
                settings.DEFAULT_FROM_EMAIL,
                [settings.CONTACT_EMAIL],
                fail_silently=False,
            )
            messages.success(request, 'Votre message a été envoyé avec succès!')
        except Exception as e:
            messages.error(request, f'Une erreur est survenue lors de l\'envoi du message: {str(e)}')
        
        return self.get(request, *args, **kwargs)
```

## Lancement du projet

```batch
:: Appliquer les migrations
python manage.py makemigrations
python manage.py migrate

:: Créer un superutilisateur (facultatif)
python manage.py createsuperuser

:: Lancer le serveur de développement
python manage.py runserver
```

## Commandes utiles

```batch
:: Collecter les fichiers statiques (pour la production)
python manage.py collectstatic

:: Vérifier les problèmes potentiels
python manage.py check

:: Créer une nouvelle application
python manage.py startapp nom_application

:: Lister les commandes disponibles
python manage.py help
```

## Conseils pour éviter les erreurs

1. **Problème de URLs vides** : Assurez-vous que votre fichier `portfolio/urls.py` contient une liste `urlpatterns` avec au moins un chemin.

2. **Erreur d'importation circulaire** : Évitez les imports circulaires entre les fichiers (par exemple, urls.py qui importe views.py qui importe urls.py).

3. **Templates introuvables** : Vérifiez que les noms de templates dans vos vues correspondent aux fichiers créés dans le dossier templates.

4. **Fichiers statiques non chargés** : Utilisez `{% load static %}` en haut de vos templates et `{% static 'chemin/fichier' %}` pour référencer les fichiers statiques.

5. **Erreurs de migrations** : Si vous rencontrez des erreurs avec les migrations, essayez de supprimer le fichier `db.sqlite3` et le dossier `migrations` (sauf `__init__.py`), puis exécutez à nouveau `makemigrations` et `migrate`.

## Ressources utiles

- [Documentation Django](https://docs.djangoproject.com/)
- [Django pour les débutants sur Windows](https://docs.djangoproject.com/fr/4.2/howto/windows/)
- [Bootstrap pour le design](https://getbootstrap.com/) (optionnel)