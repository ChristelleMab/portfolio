Documentation technique du projet Portfolio Personnel
1. Aperçu du projet
Ce document présente la documentation technique du projet de portfolio personnel développé avec Django. Le site est conçu pour mettre en valeur le profil, les compétences et l'expérience d'un expert financier en reconversion vers l'analyse de données.
2. Structure du projet
2.1 Architecture générale
Le projet suit l'architecture standard d'une application Django, organisée comme suit :
portfolio_project/              # Dossier racine du projet
│
├── manage.py                   # Script de gestion Django
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
    │   │   ├── style.css       # Styles CSS principaux
    │   │   ├── cv-styles.css   # Styles CSS pour le CV
    │   │   └── search-styles.css # Styles pour la recherche
    │   ├── js/
    │   │   └── main.js         # JavaScript principal
    │   ├── img/
    │   │   └── favicon/        # Icônes de favicon
    │   └── pdf/
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
            ├── cv_print.html   # Version imprimable du CV
            ├── search_results.html # Résultats de recherche
            └── contact.html    # Page de contact
2.2 Technologies utilisées

Backend : Django 4.2 (Python 3.10)
Frontend : HTML5, CSS3, JavaScript
Bibliothèques externes : Font Awesome (icônes)
Base de données : SQLite (développement)
Déploiement : Non spécifié pour le moment

3. Composants principaux
3.1 Configuration du projet (config/settings.py)
Principaux paramètres :
pythonINSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'portfolio',  # Notre application
]

# Configuration des fichiers statiques
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    # BASE_DIR / "static",  # Décommentez si nécessaire
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Configuration des fichiers média
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Internationalisation
LANGUAGE_CODE = 'fr-fr'
TIME_ZONE = 'Europe/Paris'

# Configuration des emails
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # Pour le développement
DEFAULT_FROM_EMAIL = 'noreply@example.com'
CONTACT_EMAIL = 'contact@example.com'
3.2 Routage URL
config/urls.py
pythonurlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio.urls')),  # Routes de l'application portfolio
]

# Pour servir les fichiers média en développement
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
portfolio/urls.py
pythonapp_name = 'portfolio'  # Pour l'espace de noms dans les templates

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
3.3 Vues
Les vues sont principalement basées sur des TemplateView de Django, avec quelques vues personnalisées pour des fonctionnalités spécifiques :
python# Vues basées sur les classes
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

# Vue personnalisée pour la version imprimable du CV
def cv_print_version(request):
    return render(request, 'portfolio/cv_print.html', {
        'name': 'Christelle MABIKA',
        'title': 'Expert Financier en reconversion Data Analyst',
    })

# Vue pour la fonctionnalité de recherche
def search_view(request):
    query = request.GET.get('q', '')
    results = []
    
    if query:
        # Code de recherche qui parcourt le contenu du site
        # ...
    
    return render(request, 'portfolio/search_results.html', {
        'query': query,
        'results': results,
        'count': len(results)
    })

# Vue pour le formulaire de contact
class ContactView(TemplateView):
    template_name = 'portfolio/contact.html'
    
    def post(self, request, *args, **kwargs):
        # Traitement du formulaire de contact
        # ...
3.4 Templates et structure HTML
Le site utilise un système de templates basé sur l'héritage, avec un template de base (base.html) qui contient la structure commune (en-tête, navigation, pied de page) et des templates spécifiques pour chaque page qui étendent ce template de base.
base.html
html{% load static %}
<!DOCTYPE html>
<html lang="fr">
<head>
    <!-- Méta-informations et liens CSS -->
    <title>{% block title %}Portfolio - Développeur & Expert Financier{% endblock %}</title>
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    {% block extra_css %}{% endblock %}
</head>
<body>
    <header>
        <!-- En-tête avec le logo et les infos de contact -->
    </header>
    
    <nav>
        <!-- Barre de navigation -->
        <ul class="nav-links">
            <li><a href="{% url 'portfolio:index' %}"><i class="fas fa-home"></i> Accueil</a></li>
            <!-- Autres liens de navigation -->
            <li class="search-container">
                <form action="{% url 'portfolio:search' %}" method="get">
                    <!-- Formulaire de recherche -->
                </form>
            </li>
        </ul>
    </nav>
    
    <main>
        {% block content %}{% endblock %}
    </main>
    
    <footer>
        <!-- Pied de page avec liens sociaux et copyright -->
    </footer>
    
    <script src="{% static 'js/main.js' %}"></script>
    {% block extra_js %}{% endblock %}
</body>
</html>
3.5 Gestion des fichiers statiques
Les fichiers statiques sont organisés dans le dossier portfolio/static/ avec la structure suivante :

css/ : Feuilles de style CSS
js/ : Scripts JavaScript
img/ : Images et favicon
pdf/ : Documents PDF (notamment le CV)

4. Fonctionnalités principales
4.1 Fonctionnalité de recherche
La fonctionnalité de recherche permet aux utilisateurs de trouver du contenu sur le site. Elle est implémentée de manière statique, sans base de données, en parcourant un ensemble prédéfini de sections du site.
Composants :

Formulaire de recherche dans la barre de navigation
Vue search_view dans views.py
Template search_results.html pour afficher les résultats

4.2 Génération de CV imprimable
Le site offre une version imprimable du CV qui peut être facilement convertie en PDF par l'utilisateur.
Composants :

Vue cv_print_version dans views.py
Template cv_print.html optimisé pour l'impression
Styles CSS adaptés à l'impression
JavaScript pour gérer l'impression

4.3 Formulaire de contact
Le formulaire de contact permet aux visiteurs d'envoyer des messages directement depuis le site.
Composants :

Formulaire HTML dans contact.html
Méthode post dans la vue ContactView
Configuration email dans settings.py

5. Guide de déploiement
5.1 Configuration locale

Cloner le dépôt
Créer un environnement virtuel Python
Installer les dépendances : pip install -r requirements.txt
Appliquer les migrations : python manage.py migrate
Démarrer le serveur de développement : python manage.py runserver

5.2 Préparation pour la production
Pour déployer l'application en production, plusieurs étapes sont nécessaires :

Configurer settings.py pour la production :

Désactiver DEBUG
Configurer ALLOWED_HOSTS
Configurer une base de données plus robuste (PostgreSQL recommandé)
Configurer un backend d'email fonctionnel


Collecter les fichiers statiques :
python manage.py collectstatic

Configurer un serveur web (Nginx, Apache) et un serveur d'application (Gunicorn, uWSGI).

5.3 Options de déploiement
Plusieurs options de déploiement sont possibles :

Hébergement VPS (DigitalOcean, Linode, AWS EC2)
Plateformes PaaS (Heroku, PythonAnywhere)
Conteneurisation avec Docker

6. Sécurité
Le site implémente plusieurs mesures de sécurité :

Protection CSRF pour les formulaires
Validation des entrées utilisateur
Configuration des en-têtes HTTP de sécurité
Utilisation de variables d'environnement pour les informations sensibles

7. Maintenance et évolution
7.1 Mises à jour
Pour mettre à jour le contenu du site :

Modifier les templates HTML correspondants
Pour le CV, mettre à jour à la fois cv.html et cv_print.html
Pour les compétences et projets, mettre à jour les sections correspondantes dans les templates

7.2 Évolutions possibles
Suggestions pour les futures améliorations :

Mise en place d'un CMS pour faciliter les mises à jour de contenu
Ajout d'une section blog
Intégration d'un système de portfolio dynamique pour les projets
Implémentation d'une authentification pour accéder à certaines sections
Intégration d'analyses de trafic (Google Analytics)

8. Dépannage
8.1 Problèmes courants

Fichiers statiques non chargés : Vérifier les paramètres STATIC_URL et STATICFILES_DIRS
Erreur lors de l'envoi d'emails : Vérifier la configuration du backend d'email
Problèmes d'affichage sur mobile : Vérifier les styles CSS responsives

8.2 Logs et débogage
En cas de problème :

Activer DEBUG = True dans settings.py
Vérifier les logs Django dans la console
Utiliser les outils de développement du navigateur pour détecter les problèmes côté client

9. Conclusion
Ce projet de portfolio personnel constitue une base solide pour présenter un profil professionnel de manière élégante et fonctionnelle. Sa structure modulaire facilite les évolutions futures et l'ajout de nouvelles fonctionnalités.