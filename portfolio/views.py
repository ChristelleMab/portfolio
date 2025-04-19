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
                'content': 'Manager finance en reconversion vers la Data Science, combinant expertise métier et compétences techniques.',
                'url': 'portfolio:about',
                'type': 'page',
                'keywords': ['à propos', 'about', 'profil', 'reconversion', 'data']
            },
            {
                'title': 'Expérience Professionnelle',
                'content': 'Manager Conseil Comptable chez Deloitte, Senior Conseil chez Advisory (BDO), Superviseur Audit & Comptabilité chez Horizons Conseils. Expertise en audit, comptabilité, fiscalité et analyse financière.',
                'url': 'portfolio:experience',
                'type': 'page',
                'keywords': ['expérience', 'expertise', 'comptable', 'finance', 'manager', 'professionnel']
            },
            {
                'title': 'Formation',
                'content': 'MBA Big Data & IA, MBA Management de l\'IA, MBA Expert Contrôle de Gestion & Audit, DSCG, Master en Finance.',
                'url': 'portfolio:education',
                'type': 'page',
                'keywords': ['formation', 'éducation', 'big data', 'intelligence artificielle', 'MBA', 'audit', 'controle de gestion']
            },

            {
                'title': 'Projets',
                'type': 'page',
                'url': 'portfolio:projects',
                'content': 'Projets de data analyse et développement d\'applications intelligentes.',
                'keywords': ['projets', 'projects', 'data', 'analyse', 'applications', 'normx', 'edusync']
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
            },

            # Ajouter des projets spécifiques
            {
                'title': 'NormX-IA – Application de Gestion Intelligente',
                'type': 'projet',
                'url': 'portfolio:projects',
                'content': 'Solution SaaS de gestion des processus financiers automatisée intégrant l\'IA.',
                'keywords': ['normx', 'intelligence artificielle', 'gestion', 'saas', 'finance']
            },
            {
                'title': 'EduSync – Application de Gestion Scolaire',
                'type': 'projet',
                'url': 'portfolio:projects',
                'content': 'Plateforme de gestion scolaire augmentée par l\'IA pour les écoles.',
                'keywords': ['edusync', 'education', 'gestion scolaire', 'ia', 'école']
            },
            {
                'title': 'Recherche de Logement Inclusif',
                'type': 'projet',
                'url': 'portfolio:projects',
                'content': 'Plateforme de recherche de logements à proximité d\'écoles inclusives.',
                'keywords': ['logement', 'inclusif', 'école', 'recherche']
            },
            {
                'title': 'Conformité des factures grâce à l\'Intelligence Artificielle',
                'content': 'Projet de mémoire explorant l\'application de l\'intelligence artificielle pour automatiser la vérification de la conformité des factures. Utilise OCR, NLP, Classification ML et détection d\'anomalies.',
                'url': 'portfolio:projects',
                'type': 'projet de recherche'
            },
        ]
        
         # Recherche sur les titres, contenus et mots-clés
        for item in sections:  # Utiliser 'sections' au lieu de 'searchable_content'
            # Convertir la requête et les champs en minuscules pour une recherche insensible à la casse
            query_lower = query.lower()
            title_lower = item['title'].lower()
            content_lower = item['content'].lower()
            
            # Vérifier si la requête est présente dans le titre, le contenu ou les mots-clés
            if (query_lower in title_lower or 
                query_lower in content_lower or 
                any(query_lower in keyword.lower() for keyword in item.get('keywords', []))):
                results.append(item)
                
        # Recherche spécifique pour certains termes courants
        if query_lower in ['projets', 'projects', 'projet', 'project']:
            # Ajouter directement la page projets si pas déjà présente
            if not any(result['url'] == 'portfolio:projects' for result in results):
                for idx, section in enumerate(sections):
                    if section['url'] == 'portfolio:projects' and section['type'] == 'page':
                        results.insert(0, section)
                        break
        
        if query_lower in ['experience', 'expérience', 'experiences', 'expériences']:
            # Ajouter directement la page expérience si pas déjà présente
            if not any(result['url'] == 'portfolio:experience' for result in results):
                for idx, section in enumerate(sections):
                    if section['url'] == 'portfolio:experience':
                        results.insert(0, section)
                        break
    
    context = {
        'query': query,
        'results': results,
        'count': len(results)
    }
    
    return render(request, 'portfolio/search_results.html', context)