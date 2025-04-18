 // Fonction pour l'animation de défilement doux
document.addEventListener('DOMContentLoaded', function() {
    // Sélectionner tous les liens de navigation interne
    const links = document.querySelectorAll('a[href^="#"]');
    
    // Ajouter un écouteur d'événements à chaque lien
    links.forEach(link => {
        link.addEventListener('click', function(e) {
            // Empêcher le comportement par défaut
            e.preventDefault();
            
            // Récupérer l'ID de la cible
            const targetId = this.getAttribute('href').substring(1);
            const targetElement = document.getElementById(targetId);
            
            // Si l'élément existe, faire défiler jusqu'à lui
            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop - 70, // Ajuster pour la hauteur de la navbar
                    behavior: 'smooth'
                });
            }
        });
    });
    
    // Animation pour les éléments de timeline
    const timelineItems = document.querySelectorAll('.timeline-item');
    
    // Fonction pour vérifier si un élément est dans la fenêtre de visualisation
    function isInViewport(element) {
        const rect = element.getBoundingClientRect();
        return (
            rect.top >= 0 &&
            rect.left >= 0 &&
            rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
            rect.right <= (window.innerWidth || document.documentElement.clientWidth)
        );
    }
    
    // Fonction pour ajouter une classe si l'élément est visible
    function checkVisibility() {
        timelineItems.forEach(item => {
            if (isInViewport(item)) {
                item.classList.add('visible');
            }
        });
    }
    
    // Vérifier la visibilité au chargement et au défilement
    window.addEventListener('load', checkVisibility);
    window.addEventListener('scroll', checkVisibility);
    
    // Gestion des messages d'alerte (pour le formulaire de contact)
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        // Ajouter un bouton de fermeture si nécessaire
        const closeBtn = alert.querySelector('.close-btn');
        if (closeBtn) {
            closeBtn.addEventListener('click', () => {
                alert.style.display = 'none';
            });
            
            // Fermer automatiquement après 5 secondes
            setTimeout(() => {
                alert.style.display = 'none';
            }, 5000);
        }
    });
});

// Effet de parallaxe simple pour le header
window.addEventListener('scroll', function() {
    const header = document.querySelector('header');
    const scrollPosition = window.scrollY;
    
    if (header) {
        header.style.backgroundPosition = `center ${scrollPosition * 0.5}px`;
    }
});

// Fonction pour filtrer les projets (si implémenté sur la page projets)
function filterProjects(category) {
    const projects = document.querySelectorAll('.project-card');
    
    if (category === 'all') {
        projects.forEach(project => {
            project.style.display = 'block';
        });
    } else {
        projects.forEach(project => {
            const tags = project.querySelectorAll('.tech-tag');
            let hasCategory = false;
            
            tags.forEach(tag => {
                if (tag.textContent.toLowerCase() === category.toLowerCase()) {
                    hasCategory = true;
                }
            });
            
            project.style.display = hasCategory ? 'block' : 'none';
        });
    }
}

// Validation du formulaire de contact côté client
const contactForm = document.getElementById('contact-form');

if (contactForm) {
    contactForm.addEventListener('submit', function(e) {
        const nameField = document.getElementById('name');
        const emailField = document.getElementById('email');
        const messageField = document.getElementById('message');
        let isValid = true;
        
        // Vérifier le nom
        if (!nameField.value.trim()) {
            document.getElementById('name-error').textContent = 'Veuillez entrer votre nom';
            isValid = false;
        } else {
            document.getElementById('name-error').textContent = '';
        }
        
        // Vérifier l'email
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailField.value.trim() || !emailPattern.test(emailField.value)) {
            document.getElementById('email-error').textContent = 'Veuillez entrer une adresse email valide';
            isValid = false;
        } else {
            document.getElementById('email-error').textContent = '';
        }
        
        // Vérifier le message
        if (!messageField.value.trim()) {
            document.getElementById('message-error').textContent = 'Veuillez entrer votre message';
            isValid = false;
        } else {
            document.getElementById('message-error').textContent = '';
        }
        
        // Si le formulaire n'est pas valide, empêcher l'envoi
        if (!isValid) {
            e.preventDefault();
        }
    });
}
