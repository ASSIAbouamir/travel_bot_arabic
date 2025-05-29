# 🧳 Chatbot Agence de Voyage - Rasa

Un chatbot intelligent en arabe pour une agence de voyage, capable de gérer les réservations de vols et d'hôtels.

## ✨ Fonctionnalités

- *Interaction en arabe* : Communication naturelle en langue arabe
- *Réservation de vols* : Recherche et réservation de billets d'avion
- *Réservation d'hôtels* : Recherche et réservation d'hébergements
- *Gestion des options* : Modification et confirmation des réservations
- *Interface web* : Interface utilisateur moderne et responsive
- *API Integration* : Simulation d'APIs pour les recherches

## 🎯 Intents Supportés

1. *greet* - Salutations
2. *goodbye* - Au revoir
3. *book_flight* - Réservation de vol
4. *book_hotel* - Réservation d'hôtel
5. *select_option* - Sélection d'option
6. *change_option* - Modification d'option
7. *confirm_reservation* - Confirmation de réservation

## 🏗️ Architecture


├── data/
│   └── nlu.yml           # Données d'entraînement NLU
├── domain.yml            # Configuration du domaine
├── config.yml           # Configuration Rasa
├── stories.yml          # Scénarios de conversation
├── rules.yml            # Règles de conversation
├── actions.py           # Actions personnalisées
├── endpoints.yml        # Configuration des endpoints
├── credentials.yml      # Configuration des canaux
├── index.html          # Interface web
├── requirements.txt    # Dépendances Python
└── README.md          # Ce fichier


## 📦 Installation

### Prérequis
- Python 3.8 ou plus récent
- pip (gestionnaire de packages Python)

### Installation automatique

1. *Télécharger tous les fichiers* dans un dossier
2. *Rendre le script exécutable* :
   bash
   chmod +x setup.sh
   
3. *Lancer l'installation* :
   bash
   ./setup.sh
   

### Installation manuelle

1. *Créer un environnement virtuel* :
   bash
   python -m venv rasa_env
   

2. *Activer l'environnement virtuel* :
   bash
   # Linux/Mac
   source rasa_env/bin/activate
   
   # Windows
   rasa_env\Scripts\activate
   

3. *Installer les dépendances* :
   bash
   pip install -r requirements.txt
   

4. *Télécharger le modèle Spacy* :
   bash
   python -m spacy download xx_ent_wiki_sm
   

5. *Entraîner le modèle* :
   bash
   rasa train
   

## 🚀 Démarrage

### Démarrage automatique

bash
chmod +x start_chatbot.sh
./start_chatbot.sh


### Démarrage manuel

1. *Terminal 1 - Serveur Rasa* :
   bash
   source rasa_env/bin/activate
   rasa run --enable-api --cors "*" --port 5005
   

2. *Terminal 2 - Serveur d'actions* :
   bash
   source rasa_env/bin/activate
   rasa run actions --port 5055
   

3. *Ouvrir l'interface web* :
   - Double-cliquer sur index.html
   - Ou ouvrir dans le navigateur

## 🎮 Utilisation

### Exemples de commandes

*Réservation de vol :*
- "أريد حجز طيران من الرياض إلى لندن"
- "أريد تذكرة طيران يوم 15 يونيو"
- "أريد السفر الدرجة الأولى"

*Réservation d'hôtel :*
- "أريد حجز فندق في دبي"
- "أريد فندق 5 نجوم لشخصين"
- "أريد فندق في حي المارينا"

*Gestion des réservations :*
- "أختار الخيار الأول"
- "أريد تغيير التاريخ"
- "أؤكد الحجز"

## 🔧 Configuration

### Entités supportées

*Pour les vols :*
- ville_depart : Ville de départ
- ville_destination : Ville de destination
- date_depart : Date de départ
- date_retour : Date de retour
- classe : Classe de voyage
- type : Type de vol (aller-retour/simple)

*Pour les hôtels :*
- ville : Ville
- quartier : Quartier/Zone
- categorie : Catégorie d'hôtel
- nombre_personnes : Nombre de personnes

## 🧪 Tests

bash
# Test en ligne de commande
rasa shell

# Test du modèle NLU
rasa test nlu

# Test des histoires
rasa test


## 🔍 Dépannage

### Problèmes courants

1. *Erreur de connexion dans l'interface web* :
   - Vérifier que les serveurs Rasa tournent sur les ports 5005 et 5055
   - Vérifier les CORS dans la configuration

2. *Erreurs d'entraînement* :
   - Vérifier que le modèle Spacy est installé
   - Vérifier la syntaxe YAML des fichiers

3. *Actions ne fonctionnent pas* :
   - Vérifier que le serveur d'actions tourne
   - Vérifier la configuration dans endpoints.yml

### Logs et debugging

bash
# Logs détaillés
rasa run --debug

# Test d'une action spécifique
rasa run actions --debug


## 📚 Structure des données

### Format des vols (mock)
python
{
    "flight_number": "SV1001",
    "airline": "الخطوط الجوية السعودية", 
    "departure_time": "08:00",
    "arrival_time": "14:00",
    "price": 1500,
    "class": "اقتصادية"
}


### Format des hôtels (mock)
python
{
    "name": "فندق الريتز كارلتون دبي",
    "rating": "5 نجوم",
    "location": "وسط المدينة - دبي", 
    "price": 800,
    "amenities": ["واي فاي مجاني", "مسبح", "جيم"]
}


## 🔗 Intégration API

Les actions dans actions.py utilisent des données simulées. Pour intégrer de vraies APIs :

1. *APIs de vols* : Amadeus, Skyscanner, etc.
2. *APIs d'hôtels* : Booking.com, Hotels.com, etc.
3. *Modifier les méthodes* get_mock_flights() et get_mock_hotels()

## 📄 Licence

Ce projet est fourni à des fins éducatives et de démonstration.

## 🤝 Support

Pour toute question ou problème :
1. Vérifier la section dépannage
2. Consulter la documentation Rasa officielle
3. Vérifier les logs d'erreur dans la console

---

*Développé avec ❤️ pour l'apprentissage de Rasa et NLP en arabe*
