Documentation Technique du Projet Portfolio Django
1. Aperçu du Projet
Ce document présente la documentation technique du projet de portfolio personnel développé avec Django et déployé sur GitHub et Heroku. Le site est conçu pour mettre en valeur le profil, les compétences et l'expérience de Christelle MABIKA, Manager Financière en reconversion vers l'analyse de données.
2. Structure du Projet
2.1 Architecture Générale
Le projet suit l'architecture standard d'une application Django, organisée comme suit :
portfolio_project/              # Dossier racine du projet
│
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
│   │   │   ├── style.css       # Styles CSS principaux
│   │   │   ├── cv-styles.css   # Styles CSS pour le CV
│   │   ├── js/
│   │   ├── img/
│   │   └── pdf/
│   └── templates/              # Templates HTML
│       └── portfolio/
│           ├── base.html       # Template de base
│           ├── index.html      # Page d'accueil
│           ├── about.html      # À propos
│           ├── experience.html # Expérience professionnelle
│           ├── cv.html         # CV en ligne
│           └── cv_print.html   # Version imprimable du CV
│
└── Documentation/              # Dossier de documentation
    └── documentation.md        # Documentation technique
2.2 Technologies Utilisées

Backend : Django 4.2 (Python 3.10)
Frontend : HTML5, CSS3, JavaScript
Bibliothèques externes :

Font Awesome (icônes)
Boxicons (icônes additionnelles)


Base de données :

SQLite (développement)
PostgreSQL (production sur Heroku)


Déploiement :

Gestion de code source : GitHub
Hébergement : Heroku



3. Composants Principaux
3.1 Configuration du Projet
Le fichier config/settings.py a été adapté pour fonctionner à la fois en environnement de développement local et en production sur Heroku :
pythonimport os
import dj_database_url

# Configuration de base de données
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Configuration pour Heroku (PostgreSQL)
if 'DATABASE_URL' in os.environ:
    DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)

# Static files
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Middleware pour fichiers statiques
MIDDLEWARE = [
    # ... middleware existants ...
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

# Configuration de Whitenoise
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Sécurité
DEBUG = 'DEVELOPMENT' in os.environ
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '.herokuapp.com']
3.2 Templates et Structure HTML
Le site utilise un système de templates basé sur l'héritage, avec un template de base (base.html) qui contient la structure commune (en-tête, navigation, pied de page) et des templates spécifiques pour chaque page.
3.2.1 Harmonisation des Couleurs
Les couleurs ont été harmonisées entre tous les fichiers pour maintenir une identité visuelle cohérente :
css:root {
  --primary-color: #3498db;    /* Bleu principal */
  --secondary-color: #3498db;  /* Même bleu pour cohérence */
  --accent-color: #f39200;     /* Orange pour accent */
  --light-color: #f9f9f9;      /* Gris très clair */
  --dark-color: #222;          /* Gris foncé */
  --text-color: #333;          /* Gris texte */
  --text-light: #666;          /* Gris moyen */
  --background: #ffffff;       /* Blanc */
}
3.3 Fonctionnalités Principales
3.3.1 CV Interactif et Version Imprimable
Le site offre deux versions du CV :

Une version interactive en ligne (cv.html)
Une version optimisée pour l'impression (cv_print.html)

La version imprimable a été conçue avec des styles spécifiques pour garantir une mise en page correcte lors de l'impression ou de la sauvegarde en PDF.
3.3.2 Mise en Valeur des Compétences
Les compétences sont présentées avec une visualisation claire :

Séparation entre expertise confirmée et compétences en développement
Utilisation de barres de progression pour indiquer le niveau de maîtrise
Organisation en catégories (compétences techniques, linguistiques, soft skills)

3.3.3 Présentation des Projets
Une section spéciale met en valeur les projets, notamment :

Projet de recherche sur la conformité des factures avec l'IA
Solution SaaS NormX IA
Plateforme de gestion scolaire EduSync

4. Déploiement
4.1 Gestion de Code Source avec GitHub
Le code source du projet est hébergé sur GitHub à l'adresse : https://github.com/ChristelleMab/portfolio.git
4.1.1 Configuration de Git
Un fichier .gitignore a été créé pour exclure les fichiers non nécessaires au suivi de version :
# Python
__pycache__/
*.py[cod]
venv/

# Django
*.log
local_settings.py
db.sqlite3

# Environnements virtuels
.env

# Fichiers de l'éditeur
.idea/
.vscode/
4.1.2 Commandes Git Utilisées
bash# Initialisation du dépôt
git init

# Premier commit
git add .
git commit -m "Premier commit - Projet de portfolio Django"

# Connexion au dépôt distant
git remote add origin https://github.com/ChristelleMab/portfolio.git

# Envoi du code
git push -u origin master

# Récupération des modifications (README.md)
git pull

# Mise à jour du contenu
git add .
git commit -m "Mise à jour des styles et ajout du .gitignore"
git push
4.2 Déploiement sur Heroku
L'application a été déployée sur Heroku à l'adresse : https://christelle-portfolio-18d9b9c91344.herokuapp.com/
4.2.1 Configuration pour Heroku
Fichiers créés pour le déploiement Heroku :

Procfile (instructions pour démarrer l'application) :

web: gunicorn config.wsgi --log-file -

runtime.txt (spécifie la version Python) :

python-3.10.0

requirements.txt (dépendances Python) :

Django==4.2
gunicorn==20.1.0
dj-database-url==1.0.0
psycopg2-binary==2.9.3
whitenoise==6.2.0
4.2.2 Commandes de Déploiement Heroku
bash# Connexion à Heroku
heroku login

# Création de l'application
heroku create christelle-portfolio

# Configuration des variables d'environnement
heroku config:set DISABLE_COLLECTSTATIC=1

# Déploiement
git push heroku master
5. Maintenance et Évolution
5.1 Mises à Jour
Pour mettre à jour le contenu du site :

Modifier les templates HTML correspondants
Pour le CV, mettre à jour à la fois cv.html et cv_print.html
Synchroniser les changements avec GitHub et Heroku

5.2 Évolutions Possibles
Suggestions pour les futures améliorations :

Intégration d'un système d'authentification pour accéder à certaines sections
Ajout d'une section blog pour partager des articles sur la data science
Implémentation d'un portfolio dynamique pour les projets d'analyse de données
Intégration d'analyses de trafic (Google Analytics)
Ajout de projets interactifs de data visualization

6. Accès au Projet

GitHub : https://github.com/ChristelleMab/portfolio
Site web : https://christelle-portfolio-18d9b9c91344.herokuapp.com/

Ce document sera mis à jour au fur et à mesure que le projet évolue pour refléter les modifications et améliorations apportées.