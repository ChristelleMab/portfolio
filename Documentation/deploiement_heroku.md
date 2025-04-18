Documentation complète pour le déploiement sur Heroku
Ce guide vous aidera à déployer votre application Django sur Heroku, de la configuration initiale jusqu'à la maintenance.
Table des matières

Prérequis
Configuration initiale
Préparation de l'application Django
Premier déploiement
Gestion de la base de données
Fichiers statiques
Mise à jour de l'application
Résolution de problèmes courants
Bonnes pratiques

Prérequis
Avant de commencer, assurez-vous d'avoir :

Git installé sur votre ordinateur
Un compte Heroku (gratuit pour commencer)
Heroku CLI installé : https://devcenter.heroku.com/articles/heroku-cli
Une application Django fonctionnelle

Configuration initiale
1. Connexion à Heroku CLI
bashheroku login
2. Création d'une application Heroku
bash# Dans le répertoire de votre projet
heroku create nom-de-votre-app
3. Vérification des remotes Git
bashgit remote -v
Vous devriez voir heroku dans la liste des remotes.
Préparation de l'application Django
1. Fichiers de configuration nécessaires
requirements.txt
Créez ou mettez à jour ce fichier pour inclure toutes les dépendances :
django>=4.2
gunicorn>=20.1.0
dj-database-url>=1.0.0
psycopg2-binary>=2.9.3
whitenoise>=6.2.0
Procfile
Créez ce fichier à la racine du projet :
web: gunicorn config.wsgi --log-file -
runtime.txt (optionnel)
Pour spécifier la version Python :
python-3.10.0
2. Configuration de settings.py
pythonimport os
import dj_database_url
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'votre-clé-de-développement')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = 'DEVELOPMENT' in os.environ

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '.herokuapp.com']

# Application definition
INSTALLED_APPS = [
    # Applications Django standard
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Vos applications
    'portfolio',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Ajouter juste après SecurityMiddleware
    # Autres middlewares...
]

# Configuration de la base de données
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Configuration pour Heroku (PostgreSQL)
if 'DATABASE_URL' in os.environ:
    DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)

# Fichiers statiques
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'portfolio/static'),
]

# Configuration de Whitenoise pour servir les fichiers statiques
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'
Premier déploiement
1. Configurer les variables d'environnement
bashheroku config:set SECRET_KEY="votre-clé-secrète-très-longue-et-aléatoire"
2. Initialiser l'application
bash# Commit de vos fichiers
git add .
git commit -m "Configuration pour déploiement Heroku"

# Déploiement
git push heroku master

# Si vous utilisez une branche autre que master
git push heroku votre-branche:master
3. Configurer la base de données
bashheroku run python manage.py migrate
4. Créer un superutilisateur (si nécessaire)
bashheroku run python manage.py createsuperuser
Gestion de la base de données
Sauvegarde de la base de données
bashheroku pg:backups:capture
heroku pg:backups:download
Restauration d'une base de données
bashheroku pg:backups:restore b101 DATABASE_URL
Fichiers statiques
Collecte des fichiers statiques
bashheroku run python manage.py collectstatic
Désactiver temporairement la collecte
bashheroku config:set DISABLE_COLLECTSTATIC=1
Réactiver la collecte
bashheroku config:unset DISABLE_COLLECTSTATIC
Mise à jour de l'application
1. Développement et test local
bash# Développez vos fonctionnalités localement
python manage.py runserver
2. Déploiement des mises à jour
bash# Ajouter les modifications
git add .
git commit -m "Description des modifications"

# Pousser vers GitHub (si utilisé)
git push origin master

# Pousser vers Heroku
git push heroku master

# Exécuter les migrations si nécessaire
heroku run python manage.py migrate

# Collecter les fichiers statiques si modifiés
heroku run python manage.py collectstatic
3. Redémarrer l'application
bashheroku restart
Résolution de problèmes courants
Consulter les logs
bashheroku logs --tail
Erreurs avec les fichiers statiques

Vérifiez la position du middleware WhiteNoise (juste après SecurityMiddleware)
Assurez-vous que STATIC_URL commence par un slash '/'
Collectez à nouveau les fichiers statiques :
bashheroku run python manage.py collectstatic


Erreurs de base de données

Vérifiez la configuration dans settings.py
Exécutez les migrations :
bashheroku run python manage.py migrate


Accéder à un shell sur Heroku
bashheroku run bash
Vérifier les variables d'environnement
bashheroku config
Bonnes pratiques

Sécurité

Ne stockez jamais les clés secrètes dans le code source
Utilisez des variables d'environnement pour les informations sensibles
Gardez DEBUG=False en production


Performance

Compressez les fichiers statiques (WhiteNoise le fait automatiquement)
Utilisez un CDN pour les bibliothèques JavaScript/CSS communes


Maintenance

Sauvegardez régulièrement votre base de données
Gardez vos dépendances à jour
Surveillez les logs pour détecter les problèmes


Déploiement

Testez toujours localement avant de déployer
Utilisez des commits descriptifs
Considérez l'utilisation d'intégration continue pour les déploiements




Cette documentation vous guidera tout au long du processus de déploiement et de maintenance de votre application Django sur Heroku. Adaptez les étapes selon les spécificités de votre projet.RéessayerClaude peut faire des erreurs. Assurez-vous de vérifier ses réponses.