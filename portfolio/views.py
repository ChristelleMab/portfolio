from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

# Create your views here.
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

def cv_print_version(request):
    """
    Vue pour afficher une version du CV optimisée pour l'impression/sauvegarde en PDF
    """
    return render(request, 'portfolio/cv_print.html', {
        'name': 'Christelle MABIKA',
        'title': 'Expert Financier en reconversion Data Analyst',
    })

def search_view(request):
    """
    Vue pour traiter les recherches sur le site
    """
    query = request.GET.get('q', '')
    results = []
    
    if query:
        # Définir les sections à rechercher et leur contenu
        sections = [
            {
                'title': 'À propos',
                'content': 'Forte de 10 ans d\'expérience en cabinet d\'expertise comptable, actuellement en reconversion vers l\'analyse de données. Combinaison d\'expertise financière et compétences en data analysis.',
                'url': 'portfolio:about',
                'type': 'page'
            },
            {
                'title': 'Expérience',
                'content': 'Manager Conseil Comptable chez Deloitte, Senior Conseil chez Advisory (BDO), Superviseur Audit & Comptabilité chez Horizons Conseils. Expertise en audit, comptabilité, fiscalité et analyse financière.',
                'url': 'portfolio:experience',
                'type': 'page'
            },
            {
                'title': 'Formation',
                'content': 'MBA Big Data & IA, MBA Management de l\'IA, MBA Expert Contrôle de Gestion & Audit, DSCG, Master en Finance.',
                'url': 'portfolio:education',
                'type': 'page'
            },
            {
                'title': 'Application de Gestion avec IA',
                'content': 'Application intégrant l\'intelligence artificielle pour optimiser les processus de gestion financière et comptable.',
                'url': 'portfolio:projects',
                'type': 'projet'
            },
            {
                'title': 'Application de Gestion Scolaire',
                'content': 'Système de gestion scolaire adapté aux besoins spécifiques des établissements d\'enseignement.',
                'url': 'portfolio:projects',
                'type': 'projet'
            },
            {
                'title': 'Recherche de Logement Inclusif',
                'content': 'Plateforme facilitant la recherche de logements à proximité d\'écoles inclusives pour les familles ayant des enfants à besoins spécifiques.',
                'url': 'portfolio:projects',
                'type': 'projet'
            },
            {
                'title': 'Conformité des factures grâce à l\'Intelligence Artificielle',
                'content': 'Projet de mémoire explorant l\'application de l\'intelligence artificielle pour automatiser la vérification de la conformité des factures. Utilise OCR, NLP, Classification ML et détection d\'anomalies.',
                'url': 'portfolio:projects',
                'type': 'projet de recherche'
            },
            {
                'title': 'CV',
                'content': 'Curriculum Vitae détaillant mon parcours professionnel, ma formation et mes compétences en finance et data analysis.',
                'url': 'portfolio:cv',
                'type': 'page'
            },
            {
                'title': 'Contact',
                'content': 'Formulaire de contact pour me joindre concernant des opportunités d\'alternance en Data Analysis ou des collaborations.',
                'url': 'portfolio:contact',
                'type': 'page'
            }
        ]
        
        # Rechercher le terme dans les sections
        query_lower = query.lower()
        for section in sections:
            if query_lower in section['title'].lower() or query_lower in section['content'].lower():
                results.append(section)
    
    return render(request, 'portfolio/search_results.html', {
        'query': query,
        'results': results,
        'count': len(results)
    })
