Documentation Technique du Projet Portfolio Django - Version Finale
1. Aperçu du Projet
Ce document présente la documentation technique complète et mise à jour du projet de portfolio personnel développé avec Django et déployé sur Heroku. Le site est conçu pour mettre en valeur le profil, les compétences et l'expérience de Christelle MABIKA, Manager Financière en reconversion vers l'analyse de données.
1.1 Technologies Utilisées

Backend: Django 4.2 (Python 3.10)
Frontend: HTML5, CSS3, JavaScript
Bibliothèques externes: Font Awesome (icônes)
Base de données: SQLite (développement), PostgreSQL (production)
Déploiement: GitHub (gestion de code), Heroku (hébergement)

2. Structure du Projet
portfolio_project/              # Dossier racine du projet
├── manage.py                   # Script de gestion Django
├── Procfile                    # Configuration pour le déploiement Heroku
├── runtime.txt                 # Spécification de la version Python pour Heroku
├── requirements.txt            # Dépendances du projet
├── .gitignore                  # Fichier d'exclusion Git
│
├── config/                     # Configuration du projet Django
│   ├── __init__.py
│   ├── settings.py             # Paramètres du projet
│   ├── urls.py                 # URLs du projet
│   ├── asgi.py
│   └── wsgi.py
│
├── portfolio/                  # Application principale
│   ├── __init__.py
│   ├── admin.py                # Configuration de l'admin Django
│   ├── apps.py                 # Configuration de l'application
│   ├── models.py               # Modèles de données
│   ├── views.py                # Logique de vues
│   ├── urls.py                 # URLs de l'application
│   ├── migrations/             # Migrations de base de données
│   ├── static/                 # Fichiers statiques
│   │   ├── css/
│   │   │   ├── style.css           # Styles CSS principaux
│   │   │   ├── cv-styles.css       # Styles CSS pour le CV
│   │   │   ├── cv-print-styles.css # Styles pour le CV imprimable
│   │   │   └── search-styles.css   # Styles pour la recherche
│   │   ├── js/
│   │   │   └── main.js            # JavaScript principal
│   │   └── img/
│   │       ├── profile.jpg        # Photo de profil
│   │       └── favicon/           # Icônes de favicon
│   └── templates/              # Templates HTML
│       └── portfolio/
│           ├── base.html           # Template de base
│           ├── index.html          # Page d'accueil
│           ├── about.html          # À propos
│           ├── experience.html     # Expérience professionnelle
│           ├── education.html      # Formation
│           ├── projects.html       # Projets
│           ├── cv.html             # CV en ligne
│           ├── cv_print.html       # Version imprimable du CV
│           ├── search_results.html # Résultats de recherche
│           └── contact.html        # Page de contact
│
└── Documentation/              # Dossier de documentation
    └── documentation.md        # Documentation technique
3. Configuration du Projet
3.1 Configuration Django (config/settings.py)
pythonimport os
from pathlib import Path
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-9702yu-60qc%4&s&ofrx94q$=yhop&s6uwqu2!(b0imkrjqhwd'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = 'DEVELOPMENT' in os.environ

# Hôtes autorisés
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '.herokuapp.com']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'portfolio',  # Notre application
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Pour servir les fichiers statiques
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Configuration pour Heroku (PostgreSQL)
if 'DATABASE_URL' in os.environ:
    DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)

# Static files configuration
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'portfolio/static'),
]

# Whitenoise configuration
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Email configuration
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'noreply@example.com'
CONTACT_EMAIL = 'contact@example.com'

# Internationalization
LANGUAGE_CODE = 'fr-fr'
TIME_ZONE = 'Europe/Paris'
USE_I18N = True
USE_TZ = True
3.2 URLs Configuration (portfolio/urls.py)
pythonfrom django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('experience/', views.ExperienceView.as_view(), name='experience'),
    path('education/', views.EducationView.as_view(), name='education'),
    path('projects/', views.ProjectsView.as_view(), name='projects'),
    path('cv/', views.CVView.as_view(), name='cv'),
    path('cv/print/', views.cv_print_version, name='cv_print'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('search/', views.search_view, name='search'),
]
4. Fonctionnalités Principales
4.1 Bannière Professionnelle

Affichage dynamique avec photo de profil
Bandeau de contact intégré pleine largeur
Design responsive avec gradient de couleurs

4.2 Système de Recherche

Recherche complète dans tout le contenu du site
Support des termes en français et anglais
Recherche insensible à la casse et aux accents
Affichage des résultats avec type de contenu et extraits

4.3 CV en Ligne

Version interactive pour consultation en ligne
Version imprimable optimisée pour PDF
Styles spécifiques pour impression (cv-print-styles.css)
Gestion des conflits CSS entre les deux versions

4.4 Portfolio de Projets

Présentation des projets en cours et réalisés
Mise en valeur des compétences techniques (NormX-IA, EduSync, Logement Inclusif)

5. Déploiement
5.1 Configuration pour Heroku
Procfile
web: gunicorn config.wsgi --log-file -
runtime.txt
python-3.10.0
requirements.txt
Django==4.2
gunicorn==20.1.0
dj-database-url==1.0.0
psycopg2-binary==2.9.3
whitenoise==6.2.0
5.2 Commandes de Déploiement
bash# Initialisation du dépôt Git
git init
git add .
git commit -m "Premier commit - Projet de portfolio Django"

# Connexion au dépôt GitHub
git remote add origin https://github.com/ChristelleMab/portfolio.git
git push -u origin master

# Déploiement sur Heroku
heroku create christelle-portfolio
git push heroku master

# Configuration des variables d'environnement
heroku config:set SECRET_KEY="votre-clé-secrète"
heroku config:set DISABLE_COLLECTSTATIC=1  # Si nécessaire

# Collecte des fichiers statiques
heroku run python manage.py collectstatic

# Redémarrage de l'application
heroku restart

6. Maintenance et Évolution
6.1 Mises à Jour Régulières
bash# Mettre à jour le code localement
git add .
git commit -m "Description des modifications"

# Pousser vers GitHub
git push origin master

# Déployer sur Heroku
git push heroku master

# Appliquer les migrations si nécessaire
heroku run python manage.py migrate

# Collecter les fichiers statiques si modifiés
heroku run python manage.py collectstatic
6.2 Évolutions Futures Prévues

Intégration d'un système d'authentification
Ajout d'une section blog pour partager des articles sur la data science
Portfolio dynamique pour les projets d'analyse de données
Intégration de Google Analytics pour le suivi du trafic
Ajout de projets interactifs de data visualization

7. Sécurité

Protection CSRF activée
Variables sensibles gérées via les variables d'environnement
Mode DEBUG désactivé en production
ALLOWED_HOSTS configuré pour limiter les domaines autorisés
Middleware WhiteNoise pour servir les fichiers statiques de manière sécurisée

8. Accès au Projet

GitHub: https://github.com/ChristelleMab/portfolio
Site Web: https://christelle-portfolio-18d9b9c91344.herokuapp.com/

Cette documentation sera mise à jour au fur et à mesure que le projet évolue pour refléter les modifications et améliorations apportées.