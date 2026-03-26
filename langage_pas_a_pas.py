import streamlit as st
from datetime import datetime
import json
import pandas as pd
import plotly.express as px
import random
import uuid
import io

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor
from reportlab.lib.units import cm
from io import BytesIO
from reportlab.platypus import Image


import os, json, uuid

from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.platypus import HRFlowable

from reportlab.platypus import Image, Spacer

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet



VERSION_LOGICIEL = "1.0"

DOSSIER_DATA = "suivi_enfants"
os.makedirs(DOSSIER_DATA, exist_ok=True)

INDEX_PATH = os.path.join(DOSSIER_DATA, "_index.json")

# =========================
# 📚 ALPHABET COMPLET (LECTURE)
# =========================

ALPHABET = [
    {"lettre": "A", "script": "a", "cursive": "a", "son": "a"},
    {"lettre": "B", "script": "b", "cursive": "b", "son": "be"},
    {"lettre": "C", "script": "c", "cursive": "c", "son": "ke"},
    {"lettre": "D", "script": "d", "cursive": "d", "son": "de"},
    {"lettre": "E", "script": "e", "cursive": "e", "son": "e"},
    {"lettre": "F", "script": "f", "cursive": "f", "son": "fe"},
    {"lettre": "G", "script": "g", "cursive": "g", "son": "gue"},
    {"lettre": "H", "script": "h", "cursive": "h", "son": "ache"},
    {"lettre": "I", "script": "i", "cursive": "i", "son": "i"},
    {"lettre": "J", "script": "j", "cursive": "j", "son": "ji"},
    {"lettre": "K", "script": "k", "cursive": "k", "son": "ka"},
    {"lettre": "L", "script": "l", "cursive": "l", "son": "le"},
    {"lettre": "M", "script": "m", "cursive": "m", "son": "me"},
    {"lettre": "N", "script": "n", "cursive": "n", "son": "ne"},
    {"lettre": "O", "script": "o", "cursive": "o", "son": "o"},
    {"lettre": "P", "script": "p", "cursive": "p", "son": "pe"},
    {"lettre": "Q", "script": "q", "cursive": "q", "son": "ku"},
    {"lettre": "R", "script": "r", "cursive": "r", "son": "re"},
    {"lettre": "S", "script": "s", "cursive": "s", "son": "se"},
    {"lettre": "T", "script": "t", "cursive": "t", "son": "te"},
    {"lettre": "U", "script": "u", "cursive": "u", "son": "u"},
    {"lettre": "V", "script": "v", "cursive": "v", "son": "ve"},
    {"lettre": "W", "script": "w", "cursive": "w", "son": "double ve"},
    {"lettre": "X", "script": "x", "cursive": "x", "son": "iks"},
    {"lettre": "Y", "script": "y", "cursive": "y", "son": "i grec"},
    {"lettre": "Z", "script": "z", "cursive": "z", "son": "zède"},
]

# =========================
# 📚 CONTENU COMPLET LECTURE
# =========================

SYLLABES_COMPLETES = [
    "ba","be","bi","bo","bu",
    "ca","ce","ci","co","cu",
    "da","de","di","do","du",
    "fa","fe","fi","fo","fu",
    "ga","ge","gi","go","gu",
    "ja","je","ji","jo","ju",
    "ka","ke","ki","ko","ku",
    "la","le","li","lo","lu",
    "ma","me","mi","mo","mu",
    "na","ne","ni","no","nu",
    "pa","pe","pi","po","pu",
    "ra","re","ri","ro","ru",
    "sa","se","si","so","su",
    "ta","te","ti","to","tu",
    "va","ve","vi","vo","vu",
    "za","ze","zi","zo","zu",
    "cha","che","chi","cho","chu",
    "bra","bre","bri","bro","bru",
    "cra","cre","cri","cro","cru",
    "dra","dre","dri","dro","dru",
    "fra","fre","fri","fro","fru",
    "gra","gre","gri","gro","gru",
    "pla","ple","pli","plo","plu",
    "tra","tre","tri","tro","tru",
    "an","am","en","em","in","im","on","om","un",
    "ou","oi","ai","au","eu","eau",
    "tion","sion","ment","teur","trice","ette","elle","eur","ien","aine","oire"
]

MOTS_COMPLETS = [
    "papa","maman","bébé","chat","chien","lait","eau","lit","pain","main",
    "nez","bus","lapin","velo","robe","jupe",
    "maison","porte","fenêtre","table","chaise","canapé","lampe","tapis","mur",
    "cuisine","salon","chambre","bureau","cahier","stylo","livre","trousse","cartable","école",
    "pomme","poire","banane","fraise","orange","raisin","citron","gâteau","pain","beurre",
    "fromage","soupe","salade","carotte","tomate","riz","pâtes","poisson","poulet","chocolat",
    "chaton","lapin","souris","lion","tigre","zèbre","girafe","singe","éléphant",
    "canard","poule","cheval","vache","mouton","cochon","requin","baleine","dauphin",
    "soleil","lune","étoile","nuage","pluie","neige","vent","orage","arbre","fleur",
    "feuille","forêt","rivière","montagne","plage","sable","jardin","herbe","ciel","terre",
    "ballon","voiture","camion","bateau","avion","train","vélo","moto","tracteur",
    "téléphone","ordinateur","horloge","montre","clé","sac","valise","boîte","bouteille",
    "rouge","bleu","vert","jaune","rose","blanc","noir","grand","petit","rapide",
    "lent","chaud","froid","manger","boire","courir","jouer","dormir","lire","écrire"
]

PHRASES_COMPLETES = [
    "papa mange",
    "maman lit",
    "le chat dort",
    "le chien court",
    "bébé joue",
    "léo saute",
    "lina chante",
    "le soleil brille",
    "la pluie tombe",
    "le bébé dort",
    "papa mange une pomme",
    "maman lit un livre",
    "le chat dort sur le lit",
    "le chien court dans le jardin",
    "le bébé joue avec un jouet",
    "la voiture roule vite",
    "le lapin mange une carotte",
    "la fille tient un ballon",
    "le garçon joue dehors",
    "le bateau flotte sur l’eau",
    "la petite fille lit calmement",
    "le grand chien regarde la fenêtre",
    "maman coupe un bon gâteau",
    "le petit garçon boit du lait",
    "le canard nage dans la rivière",
    "la maîtresse montre un cahier",
    "la fleur pousse dans le jardin",
    "la lune brille dans le ciel",
    "le cheval court dans le champ",
    "la poule marche dans la cour",
    "le petit chat gris dort sur le canapé",
    "la voiture rouge roule sur la route",
    "les enfants jouent ensemble dans le parc",
    "le garçon ouvre la porte de la maison",
    "la maman prépare un gâteau au chocolat",
    "la maîtresse lit une histoire aux élèves",
    "le lapin blanc saute dans l’herbe verte",
    "le vent pousse les nuages dans le ciel",
    "la fillette range ses jouets dans sa chambre",
    "le chien noir court après la balle rouge",
    "la petite fille regarde un papillon dans le jardin",
    "le garçon écrit son prénom sur un cahier bleu",
    "la maman prépare le repas dans la cuisine",
    "le soleil chauffe le sable de la plage",
    "les oiseaux chantent dans les arbres du parc",
    "la voiture s’arrête devant la maison jaune",
    "le petit garçon met son cartable sur la chaise",
    "le lapin mange tranquillement sa carotte orange",
    "la maîtresse explique la leçon aux enfants",
    "le bateau avance doucement sur la rivière"
]



# ==================================================
# 📚 GÉNÉRATION AUTOMATIQUE DU PROGRAMME LECTURE
# ==================================================
def programme_lecture(niveau):

    lettres = [
        {"lettre": "A", "son": "a"},
        {"lettre": "B", "son": "b"},
        {"lettre": "C", "son": "k"},
        {"lettre": "D", "son": "d"},
        {"lettre": "E", "son": "e"},
        {"lettre": "F", "son": "f"},
        {"lettre": "G", "son": "g"},
        {"lettre": "H", "son": "h"},
        {"lettre": "I", "son": "i"},
        {"lettre": "J", "son": "j"},
        {"lettre": "K", "son": "k"},
        {"lettre": "L", "son": "l"},
        {"lettre": "M", "son": "m"},
        {"lettre": "N", "son": "n"},
        {"lettre": "O", "son": "o"},
        {"lettre": "P", "son": "p"},
        {"lettre": "Q", "son": "k"},
        {"lettre": "R", "son": "r"},
        {"lettre": "S", "son": "s"},
        {"lettre": "T", "son": "t"},
        {"lettre": "U", "son": "u"},
        {"lettre": "V", "son": "v"},
        {"lettre": "W", "son": "w"},
        {"lettre": "X", "son": "x"},
        {"lettre": "Y", "son": "i"},
        {"lettre": "Z", "son": "z"},
    ]

    syllabes = [
        "ba","be","bi","bo","bu",
        "ma","me","mi","mo","mu",
        "pa","pe","pi","po","pu",
        "la","le","li","lo","lu",
        "ta","te","ti","to","tu",
        "sa","se","si","so","su",
        "ra","re","ri","ro","ru",
        "fa","fe","fi","fo","fu"
    ]

    mots = [
        "papa","maman","bébé","chat","chien",
        "maison","lait","ballon","soleil","voiture",
        "livre","table","pomme","fleur","école",
        "gâteau","bateau","lapin","ami","étoile",
        "forêt","pluie","neige","carotte","jardin",
        "jouet","garçon","fille","roue","fenêtre"
    ]

    phrases = [
        "papa mange une pomme",
        "le chat dort sur le lit",
        "maman lit un livre",
        "le chien court dans le jardin",
        "la balle roule vite",
        "le bébé joue avec un jouet",
        "le soleil brille aujourd’hui",
        "la voiture est rouge",
        "le lapin mange une carotte",
        "l’enfant va à l’école",
        "la pluie tombe doucement",
        "le garçon joue dehors",
        "la fille tient un ballon",
        "le livre est sur la table",
        "maman coupe le gâteau",
        "le bateau flotte sur l’eau",
        "le chien regarde la fenêtre",
        "le lapin saute dans le jardin",
        "le soleil chauffe la maison",
        "la petite fille lit calmement"
    ]

    if niveau == "severe":
        return {
            "lettres": lettres,          # 26 lettres
            "syllabes": syllabes[:20],   # beaucoup de syllabes
            "mots": mots[:10],
            "phrases": phrases[:5]
        }

    elif niveau == "modere":
        return {
            "lettres": lettres,          # 26 lettres aussi
            "syllabes": syllabes,        # toutes les syllabes
            "mots": mots[:20],
            "phrases": phrases[:10]
        }

    else:  # leger
        return {
            "lettres": lettres,          # 26 lettres aussi
            "syllabes": syllabes,
            "mots": mots,
            "phrases": phrases
        }

# ==================================================
# 📄 GÉNÉRATION PDF LECTURE
# ==================================================

def generer_pdf_lecture(programme, section="tout"):

    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4)

    styles = getSampleStyleSheet()

    # 🎨 STYLES
    style_titre = ParagraphStyle(
        "Titre",
        parent=styles["Title"],
        textColor=HexColor("#e8aeb7"),
        spaceAfter=20
    )

    style_section = ParagraphStyle(
        "Section",
        parent=styles["Heading2"],
        textColor=HexColor("#d98c9c"),
        spaceAfter=15
    )

    style_texte = ParagraphStyle(
        "Texte",
        parent=styles["Normal"],
        fontSize=11,
        spaceAfter=6
    )

    elements = []

    # =========================
    # LOGO / COUVERTURE (PRO)
    # =========================

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    logo_path = os.path.join(BASE_DIR, "langage_pas_a_pas.png")
    cover_path = os.path.join(BASE_DIR, "lecture_cover.png")

    # 👉 LOGO (toujours affiché)
    if os.path.exists(logo_path):
        try:
            logo = Image(logo_path)

            ratio = logo.imageWidth / logo.imageHeight

            max_width = 280
            max_height = 120

            if (max_width / ratio) <= max_height:
                logo.drawWidth = max_width
                logo.drawHeight = max_width / ratio
            else:
                logo.drawHeight = max_height
                logo.drawWidth = max_height * ratio

            logo.hAlign = "CENTER"

            elements.append(logo)
            elements.append(Spacer(1, 20))

        except Exception as e:
            print("Erreur logo :", e)

    # 👉 COUVERTURE (seulement pour PDF complet)
    if section == "tout" and os.path.exists(cover_path):
        try:
            cover = Image(cover_path)
            cover.drawWidth = 400
            cover.drawHeight = 500

            cover.hAlign = "CENTER"

            elements.append(cover)
            elements.append(Spacer(1, 20))

        except Exception as e:
            print("Erreur couverture :", e)

    # =========================
    # TITRE
    # =========================

    titre_map = {
        "tout": "📚 Programme Lecture",
        "lettres": "🔤 Alphabet",
        "syllabes": "🔡 Syllabes",
        "mots": "🧩 Mots",
        "phrases": "🗣 Phrases",
        "conseils": "💡 Conseils pour les parents",
    }

    sous_titre_map = {
        "tout": "Méthode progressive pour enfants",
        "lettres": "Apprendre les lettres et leurs sons",
        "syllabes": "Assembler les sons pour lire",
        "mots": "Lire et comprendre des mots simples",
        "phrases": "Lire et comprendre des phrases",
        "conseils": "Conseils pratiques pour accompagner l’enfant",
    }

    elements.append(Paragraph(titre_map.get(section, "📚 Programme Lecture"), style_titre))
    elements.append(Spacer(1, 10))

    if section == "tout":
        elements.append(Paragraph(sous_titre_map.get(section, ""), style_texte))

    elements.append(Spacer(1, 20))

    # =========================
    # LETTRES
    # =========================
    if section in ["tout", "lettres"]:

        # 👉 afficher le titre dans tous les cas
        elements.append(Paragraph("🔤 Lettres", style_section))

        elements.append(Paragraph("👉 Dire le son et répéter 3 fois", style_texte))
        elements.append(Spacer(1, 8))

        lettres_pdf = programme.get("lettres") or ALPHABET

        for lettre in lettres_pdf:
            son = lettre.get("son", "")
            script = lettre.get("script", "")
            cursive = lettre.get("cursive", "")

            if script or cursive:
                texte = (
                    f"<b>{lettre['lettre']}</b> → "
                    f"Script : {script} | Cursive : {cursive} | Son : {son}"
                )
            else:
                texte = f"<b>{lettre['lettre']}</b> → {son}"

            elements.append(Paragraph(texte, style_texte))

        elements.append(Spacer(1, 20))

    # =========================
    # SYLLABES
    # =========================
    if section in ["tout", "syllabes"]:

        # 👉 afficher le titre dans tous les cas
        elements.append(Paragraph("🔡 Syllabes", style_section))

        elements.append(Paragraph("👉 Lire lentement puis normalement", style_texte))
        elements.append(Spacer(1, 8))

        syllabes_pdf = programme.get("syllabes") or [
            "ba","be","bi","bo","bu",
            "ma","me","mi","mo","mu",
            "pa","pe","pi","po","pu",
            "la","le","li","lo","lu",
            "ta","te","ti","to","tu",
            "sa","se","si","so","su",
            "ra","re","ri","ro","ru",
            "fa","fe","fi","fo","fu"
        ]

        for s in syllabes_pdf:
            elements.append(Paragraph(f"• {s}", style_texte))

        elements.append(Spacer(1, 20))

    # =========================
    # MOTS
    # =========================
    if section in ["tout", "mots"]:

        # 👉 afficher titre dans les 2 cas
        elements.append(Paragraph("🧩 Mots", style_section))

        elements.append(Paragraph("👉 Lire le mot puis expliquer sa signification", style_texte))
        elements.append(Spacer(1, 8))

        mots_pdf = programme.get("mots") or [
            "papa","maman","bébé","chat","chien",
            "maison","lait","ballon","soleil","voiture",
            "livre","table","pomme","fleur","école",
            "gâteau","bateau","lapin","ami","étoile"
        ]

        for mot in mots_pdf:
            elements.append(Paragraph(f"• {mot}", style_texte))

        elements.append(Spacer(1, 20))
        
    # =========================
    # PHRASES
    # =========================
    if section in ["tout", "phrases"]:
        elements.append(Paragraph("🗣 Phrases", style_section))
        elements.append(Paragraph("👉 Lire la phrase et répondre : Qui ? Que fait-il ?", style_texte))
        elements.append(Spacer(1, 8))

        phrases_pdf = programme.get("phrases") or [
            "papa mange une pomme",
            "le chat dort sur le lit",
            "maman lit un livre",
            "le chien court dans le jardin",
            "la balle roule vite",
            "le bébé joue avec un jouet",
            "le soleil brille aujourd’hui",
            "la voiture est rouge",
            "le lapin mange une carotte",
            "l’enfant va à l’école"
        ]

        for p in phrases_pdf:
            elements.append(Paragraph(f"• {p}", style_texte))

        elements.append(Spacer(1, 20))

    # =========================
    # CONSEILS
    # =========================

    if section in ["tout", "conseils"]:

        elements.append(Paragraph("💡 Conseils pour les parents", style_section))
        elements.append(Spacer(1, 8))  # 👉 espace après le titre

        elements.append(Paragraph("👉 Conseils simples pour accompagner l’enfant", style_texte))
        elements.append(Spacer(1, 6))  # 👉 petit espace

        conseils = [
            "5 minutes par jour suffisent",
            "Encourager sans corriger brutalement",
            "Répéter régulièrement",
            "Lire dans un environnement calme",
            "Toujours valoriser les efforts"
        ]

        for c in conseils:
            elements.append(Paragraph(f"• {c}", style_texte))

        elements.append(Spacer(1, 20))  # 👉 espace final pour aérer

    # 🔴 SÉCURITÉ IMPORTANTE
    if not elements:
        elements.append(Paragraph("Aucun contenu disponible", style_texte))

    doc.build(elements)

    buffer.seek(0)
    return buffer

def _load_index() -> dict:
    if os.path.exists(INDEX_PATH):
        try:
            with open(INDEX_PATH, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}

def _save_index(index: dict) -> None:
    with open(INDEX_PATH, "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False, indent=2)

def _make_child_id(prenom: str) -> str:
    return uuid.uuid4().hex[:8]

def lister_profils() -> list:
    index = _load_index()
    # renvoie la liste des prénoms enregistrés (triés)
    return sorted(index.keys())

def sauvegarder(data: dict, prenom: str) -> str:
    prenom_clean = prenom.strip()
    if not prenom_clean:
        raise ValueError("Prénom vide")

    # 1 enfant = 1 id stable (si déjà existant on le garde)
    if "id_enfant" not in data or not data["id_enfant"]:
        data["id_enfant"] = _make_child_id(prenom_clean)

    enfant_id = data["id_enfant"]
    filename = f"suivi_{prenom_clean.lower()}_{enfant_id}.json"
    path = os.path.join(DOSSIER_DATA, filename)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    # index = “prenom -> filename”
    index = _load_index()
    index[prenom_clean] = filename
    _save_index(index)

    return prenom_clean

def charger(prenom):

    prenom_clean = prenom.strip()

    index = _load_index()

    if prenom_clean not in index:
        return {}

    filename = index[prenom_clean]

    path = os.path.join(DOSSIER_DATA, filename)

    if not os.path.exists(path):
        return {}

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
    
# ==============================
# 🧠 BIBLIOTHÈQUE D'EXERCICES (150+)
# ==============================
# 5 compétences × 30 exercices = 150
EXERCICES_BIB = {

    "attention": [

        "Jeu du silence : rester immobile et silencieux pendant 30 secondes",
        "Jacques a dit : suivre deux consignes simples données par l'adulte",
        "Repérer une image précise parmi six images différentes",
        "Tri rapide : séparer des images d’animaux et d’objets",
        "Jeu stop/go : taper dans les mains quand on entend un mot choisi",
        "Cherche et trouve : retrouver un objet dans une grande image ou un livre",
        "Reproduire deux gestes simples montrés par l'adulte",
        "Observer une image pendant 10 secondes puis dire ce que l’on a vu",
        "Suivre un objet du regard que l'adulte déplace lentement",
        "Trouver l’intrus parmi quatre images (trois identiques et une différente)",
        "Taper dans les mains quand l'adulte prononce un mot précis",
        "Classer des objets selon leur couleur (trois couleurs différentes)",
        "Faire un puzzle simple de six pièces",
        "Jeu statue : rester immobile pendant 10 secondes",
        "Montrer la gauche ou la droite sur son corps",
        "Imiter un rythme simple tapé par l’adulte",
        "Imiter des sons simples prononcés par l’adulte (pa-ta-la)",
        "Deviner un bruit entendu (clé, eau, papier…)",
        "Suivre une consigne simple puis deux consignes successives",
        "Souffler sur une plume ou un coton pour le faire bouger",
        "Colorier un dessin simple pendant deux minutes",
        "Regarder l’objet montré par l’adulte (attention conjointe)",
        "Repérer un cercle ou un carré parmi plusieurs formes",
        "Chercher un objet caché avec un indice donné",
        "Petit parcours moteur simple avec deux actions",
        "Observer une carte puis dire ce qui était dessus",
        "Jeu de mémory simple avec quatre cartes",
        "Repérer un personnage dans une grande image",
        "Imiter une expression du visage (content ou triste)",
        "Attendre le signal 'go' avant de commencer une action",
        "Suivre un objet rouge parmi plusieurs objets",
        "Repérer une image identique parmi cinq images",
        "Écouter deux sons et dire s'ils sont identiques",
        "Jeu du feu rouge feu vert avec mouvement",
        "Trouver un objet caché dans la pièce",
        "Observer une image 5 secondes puis répondre à une question",
        "Jeu des différences entre deux images",
        "Repérer un animal dans une image chargée",
        "Imiter une séquence de deux gestes",
        "Imiter une séquence de trois gestes",
        "Jeu écoute et touche (touche ton nez)",
        "Repérer un objet bleu dans la pièce",
        "Jeu d'attente : attendre le signal pour commencer",
        "Trouver l'objet que l'adulte décrit",
        "Repérer un objet sonore dans la pièce",
        "Jeu des statues avec musique",
        "Jeu du chef d'orchestre (imiter un geste)",
        "Repérer un mot dans une phrase",
        "Suivre une balle du regard",
        "Repérer un bruit dans la maison",
        "Repérer un objet jaune dans la pièce",
        "Imiter trois gestes successifs",
        "Suivre un objet qui se déplace rapidement",
        "Repérer une image différente dans une série",
        "Jeu d'écoute : lever la main quand on entend un mot",
        "Observer deux images puis dire laquelle a changé",
        "Repérer un objet dans un dessin complexe",
        "Imiter un geste lent puis rapide",
        "Repérer une lettre parmi plusieurs lettres",
        "Trouver l'intrus dans une série d'images",
        "Jeu d'écoute avec deux mots clés",
        "Repérer une forme géométrique dans un dessin",
        "Observer une image puis répondre à une question",
        "Jeu stop/go avec musique",
        "Repérer un animal dans une image",
        "Imiter un geste fait par un camarade",
        "Suivre une consigne avec deux actions",
        "Repérer un objet caché sous un tissu",
        "Observer une scène puis dire ce qui manque",
        "Jeu de concentration avec cartes",
        "Repérer un bruit dans une pièce",
        "Jeu d'écoute avec clap des mains",
        "Suivre un objet qui tourne",
        "Repérer une couleur dans un dessin",
        "Jeu d'attention avec marionnettes",
        "Imiter une posture du corps",
        "Observer un objet puis le retrouver",
        "Repérer un mot dans une phrase",
        "Jeu de concentration avec sons",
        "Suivre une lumière avec les yeux",
        "Écouter un mot et lever la main quand on l'entend",
        "Repérer un son au début d'un mot",
        "Suivre une consigne orale très courte sans aide",
        "Attendre puis exécuter la consigne au signal",
    ],

    "comprehension": [

        "Exécuter la consigne simple : donne-moi le ballon [SIMPLE]",
        "Exécuter la consigne simple : mets le crayon sur la table [SIMPLE]",
        "Comprendre les mots dans / sur / sous avec un objet et une boîte [SIMPLE]",
        "Comprendre grand / petit avec deux images [MOYEN]",
        "Choisir l’image correcte parmi deux après description de l’adulte",
        "Répondre à la question simple : où est l’objet ?",
        "Associer une action à une image (ex : quelqu’un mange)",
        "Comprendre la question simple : qui est-ce ?",
        "Écouter une courte histoire puis répondre à une question",
        "Trouver un objet selon sa fonction (ex : on se brosse avec quoi ?)",
        "Comprendre les mots encore et stop pendant un jeu",
        "Comprendre le même ou différent entre deux images",
        "Comprendre la négation non avec deux choix [SIMPLE]",
        "Comprendre le mot et entre deux objets [MOYEN]",
        "Comprendre ou pour choisir entre deux objets",
        "Comprendre un / une / des avec des objets",
        "Pointer l’image correspondant à un verbe (courir, dormir)",
        "Reconnaître une émotion simple sur une image",
        "Comprendre la consigne simple : range cet objet",
        "Comprendre la consigne simple : viens ici [SIMPLE]",
        "Comprendre les actions ouvre et ferme",
        "Comprendre vite et lent dans un petit jeu",
        "Comprendre tout ou une partie d’un objet",
        "Comprendre premier et dernier dans une petite file",
        "Comprendre une devinette très simple",
        "Comprendre la différence entre je veux et je ne veux pas",
        "Comprendre pareil que entre deux objets",
        "Comprendre plus ou moins avec deux piles d’objets",
        "Comprendre propre ou sale avec des images",
        "Comprendre la consigne : donne-moi le plus grand objet",
        "Comprendre la consigne : mets le livre sous la table",
        "Comprendre qui fait l'action sur une image",
        "Comprendre une question simple sur une histoire",
        "Comprendre la différence entre chaud et froid",
        "Comprendre la consigne : prends deux objets",
        "Comprendre la question : qui mange ?",
        "Comprendre la question : où est le chien ?",
        "Comprendre la question : que fait-il ?",
        "Comprendre le mot pareil entre deux images",
        "Comprendre les actions courir sauter marcher",
        "Comprendre les notions plein vide",
        "Comprendre devant derrière",
        "Comprendre avant après dans une routine",
        "Comprendre la différence jour nuit",
        "Comprendre rapide lent",
        "Comprendre un ordre simple avec trois objets",
        "Comprendre la différence beaucoup peu",
        "Comprendre la question pourquoi simple [AVANCE]",
        "Comprendre la différence ouvert fermé",
        "Comprendre la consigne : mets le jouet dans la boîte",
        "Comprendre la consigne : donne-moi deux crayons",
        "Comprendre la question : qui dort ?",
        "Comprendre la question : que fait le chat ?",
        "Comprendre la différence entre haut et bas",
        "Comprendre la différence entre plein et vide",
        "Comprendre la consigne : touche ta tête",
        "Comprendre la consigne : ferme la porte",
        "Comprendre la question : pourquoi il pleure ? [AVANCE]",
        "Comprendre la consigne : prends le plus petit objet",
        "Comprendre la question : où va le personnage ?",
        "Comprendre la différence entre avant et après",
        "Comprendre la consigne : montre le rouge",
        "Comprendre la question : qui parle ?",
        "Comprendre la consigne : mets le livre sur la table",
        "Comprendre la question : qui mange ?",
        "Comprendre la différence entre chaud et froid",
        "Comprendre la question : que fait la fille ?",
        "Comprendre la consigne : prends trois objets",
        "Comprendre la question : où est le ballon ?",
        "Comprendre la différence entre long et court",
        "Comprendre la consigne : touche ton nez",
        "Comprendre la question : que voit le garçon ?",
        "Comprendre la consigne : range le jouet",
        "Comprendre la différence entre lourd et léger",
        "Comprendre la question : que fait le chien ?",
        "Comprendre la consigne : donne-moi le bleu",
        "Comprendre la question : où est la maison ?",
        "Comprendre la différence entre ouvert et fermé",
        "Comprendre la question : qui court ?",
        "Comprendre une consigne avec un seul objet",
        "Comprendre une consigne avec deux actions simples",
        "Comprendre qui fait quoi sur une image simple",
        "Comprendre une phrase courte puis montrer l'image",
        "Comprendre la différence entre avant et après",
        "Comprendre une consigne avec couleur et objet",
        "Comprendre une petite histoire très simple [AVANCE]",
        "Comprendre une question sur une image",
    ],

    "communication": [

        "Demander un objet avec un mot simple (ex : eau)",
        "Demander un objet avec un geste et un mot",
        "Choisir entre deux objets en disant ce que l'on veut",
        "Dire encore pour demander de continuer un jeu",
        "Dire stop pour demander d'arrêter un jeu",
        "Demander de l’aide quand l'enfant n'arrive pas à faire quelque chose",
        "Appeler un adulte par son prénom",
        "Répondre oui ou non correctement à une question",
        "Jeu à tour de rôle : lancer une balle chacun son tour",
        "Jeu du magasin : dire je veux + objet",
        "Exprimer j’aime ou j’aime pas",
        "Dire j’ai mal si quelque chose fait mal",
        "Dire merci ou s’il te plaît",
        "Montrer un objet intéressant et dire regarde",
        "Poser la question quoi ?",
        "Poser la question où ?",
        "Répondre à une question simple avec un mot",
        "Dire l’activité que l'on veut faire",
        "Demander un objet qui manque pour continuer une activité",
        "Dire fini pour signaler que le jeu ou l’activité est terminé",
        "Refuser poliment avec non merci",
        "Jeu de marionnettes pour faire parler deux personnages",
        "Exprimer une émotion simple (content ou triste)",
        "Faire une demande avec deux mots (ex : encore ballon)",
        "Utiliser des pictogrammes pour communiquer",
        "Jeu téléphone : dire allo puis le prénom",
        "Donner une information simple (ex : c'est rouge)",
        "Dire je veux + objet",
        "Demander à répéter en disant encore",
        "Jeu à toi / à moi pour apprendre le tour de rôle",
        "Demander à boire",
        "Demander un jouet précis",
        "Dire bonjour et au revoir",
        "Demander où est un objet",
        "Dire j'ai faim",
        "Demander de jouer",
        "Proposer un jeu à un adulte",
        "Dire merci après avoir reçu un objet",
        "Dire encore pour continuer un jeu",
        "Dire fini après une activité",
        "Dire aide quand une tâche est difficile",
        "Dire regarde pour montrer un objet",
        "Dire viens pour appeler quelqu'un",
        "Dire attends pour faire patienter",
        "Dire je veux jouer",
        "Demander une histoire",
        "Dire non je ne veux pas",
        "Dire oui j'aime",
        "Dire je suis content",
        "Dire je suis fatigué",
        "Dire le nom de cinq fruits",
        "Dire le nom de cinq animaux",
        "Décrire une image simple",
        "Dire une phrase avec je veux",
        "Dire une phrase avec j'ai",
        "Dire une phrase avec c'est",
        "Nommer les parties du corps",
        "Nommer les objets de la cuisine",
        "Nommer les objets de la salle de bain",
        "Dire ce que fait un animal",
        "Dire ce que fait une personne sur une image",
        "Compléter une phrase simple",
        "Dire deux mots pour décrire une image",
        "Dire trois mots pour décrire une scène",
        "Dire une petite phrase avec sujet verbe",
        "Dire une phrase avec et",
        "Dire une phrase avec parce que simple",
        "Décrire ce que l'enfant fait",
        "Dire ce qu'il voit dans la pièce",
        "Nommer les couleurs autour de lui",
        "Dire je veux jouer",
        "Dire je veux manger",
        "Dire je veux boire",
        "Dire bonjour à quelqu'un",
        "Dire au revoir",
        "Demander de l'aide",
        "Dire merci",
        "Dire s'il te plaît",
        "Demander un objet",
        "Dire encore pour continuer",
        "Dire stop pour arrêter",
        "Appeler un adulte",
        "Dire regarde",
        "Dire viens",
        "Dire attends",
        "Dire je suis content",
        "Dire je suis triste",
        "Dire j'ai faim",
        "Dire j'ai soif",
        "Dire j'aime ce jeu",
        "Dire je n'aime pas",
        "Dire je veux lire",
        "Dire je veux sortir",
        "Dire je veux dessiner",
        "Dire je veux jouer avec toi",
        "Dire regarde ça",
        "Dire écoute",
        "Dire viens ici",
        "Dire aide-moi",
        "Dire c'est à moi",
        "Dire je veux + objet en regardant l'adulte",
        "Demander de l'aide avec une petite phrase",
        "Dire une phrase simple pour raconter une image",
        "Répondre à qui ? quoi ? où ? sur une image",
    ],

    "expression": [

        "Nommer dix objets du quotidien montrés par l'adulte",
        "Nommer dix animaux à partir d'images",
        "Nommer des actions simples vues sur des images",
        "Faire une phrase simple : je veux + objet",
        "Faire une phrase simple : c'est + couleur",
        "Décrire une image avec deux mots",
        "Décrire une image avec trois mots",
        "Raconter une petite action faite aujourd’hui",
        "Compléter une phrase simple (ex : le chat dort)",
        "Trouver le mot manquant dans une phrase simple",
        "Répondre à une question avec une petite phrase",
        "Faire une phrase avec le mot et",
        "Utiliser correctement il ou elle dans une phrase",
        "Prononcer les syllabes pa ta ka",
        "Prononcer les sons simples m p b",
        "Jeu de rimes simples (chat / rat)",
        "Dire la première syllabe d’un mot",
        "Séparer un mot en deux syllabes",
        "Répéter une phrase courte",
        "Répéter une phrase un peu plus longue",
        "Raconter une mini-histoire avec début et fin",
        "Décrire une action sur une image",
        "Dire qui fait quoi sur une image",
        "Donner une consigne simple à un doudou",
        "Nommer les couleurs",
        "Nommer les vêtements",
        "Décrire une scène simple (qui fait quoi où)",
        "Utiliser dans ou sur dans une phrase",
        "Faire une phrase négative : je ne veux pas",
        "Jeu devine l’objet avec des indices",
        "Répéter deux mots simples",
        "Répéter trois mots simples",
        "Répéter une phrase courte",
        "Se souvenir de deux objets montrés",
        "Se souvenir de trois objets montrés",
        "Jeu mémoire avec quatre cartes",
        "Jeu mémoire avec six cartes",
        "Se souvenir d'une consigne donnée",
        "Se souvenir de deux consignes successives",
        "Répéter une liste de deux nombres",
        "Répéter une liste de trois nombres",
        "Compléter une comptine connue",
        "Dire la suite d'une comptine",
        "Se souvenir d'une action faite avant",
        "Se souvenir d'un personnage dans une histoire",
        "Se souvenir du lieu dans une image",
        "Jeu mémoire avec sons différents",
        "Jeu mémoire avec couleurs",
        "Jeu mémoire avec animaux",
        "Jeu mémoire avec objets",
        "Nommer cinq objets de la maison",
        "Nommer cinq aliments",
        "Nommer cinq animaux",
        "Dire ce que fait un animal",
        "Dire ce que fait une personne",
        "Décrire une image simple",
        "Dire une phrase avec je vois",
        "Dire une phrase avec je mange",
        "Dire une phrase avec je joue",
        "Nommer les couleurs",
        "Nommer les vêtements",
        "Nommer les parties du corps",
        "Dire ce qu'il voit autour de lui",
        "Dire ce qu'il entend",
        "Dire ce qu'il fait",
        "Dire une phrase avec je veux",
        "Dire une phrase avec j'ai",
        "Dire une phrase avec c'est",
        "Décrire une scène simple",
        "Dire deux mots pour décrire une image",
        "Dire trois mots pour décrire une scène",
        "Nommer les objets dans la pièce",
        "Dire ce que fait le personnage",
        "Dire ce que fait l'animal",
        "Compléter une phrase simple",
        "Dire une phrase avec et",
        "Dire une phrase avec parce que",
        "Dire une phrase avec je suis",
        "Dire une phrase avec tu es",
        "Dire une phrase avec il est",
        "Répéter des syllabes simples : pa pe pi po pu",
        "Répéter des syllabes simples : ta te ti to tu",
        "Répéter des syllabes simples : ka ke ki ko ku",
        "Répéter un mot en découpant les syllabes",
        "Dire la première syllabe d'un mot simple",
        "Assembler deux syllabes pour former un mot",
        "Faire une phrase de deux mots",
        "Faire une phrase de trois mots",
        "Compléter une phrase simple avec image",
        "Décrire une image avec sujet + verbe",
    ],

    "memoire": [

        "Répéter deux mots entendus",
        "Répéter trois mots entendus",
        "Répéter deux syllabes entendues",
        "Répéter trois syllabes entendues",
        "Jeu de mémory simple avec quatre cartes",
        "Jeu de mémory avec six cartes",
        "Retenir une consigne simple",
        "Retenir deux consignes successives",
        "Répéter une phrase courte entendue",
        "Répéter une phrase avec un mot changé",
        "Jeu mémoire : montrer trois objets puis en cacher un",
        "Se souvenir d’un personnage vu sur une image",
        "Se souvenir du lieu montré dans une image",
        "Observer trois images puis les retrouver",
        "Écouter trois sons puis dire lesquels",
        "Apprendre un nouveau mot et le répéter trois fois",
        "Chanter une petite comptine",
        "Compléter la fin d'une comptine",
        "Jeu mémoire avec deux sons différents",
        "Dire quelle action se passe avant ou après",
        "Rappeler deux éléments d'une histoire",
        "Rappeler trois éléments d'une histoire",
        "Remettre trois images dans le bon ordre",
        "Répéter une liste de deux mots",
        "Répéter une liste de trois mots",
        "Dire les jours de la semaine",
        "Répéter deux nombres",
        "Répéter trois nombres",
        "Jeu je pars en voyage avec un mot",
        "Jeu je pars en voyage avec deux mots",
        "Répéter une liste de quatre mots",
        "Répéter une phrase courte",
        "Se souvenir de deux images",
        "Se souvenir de trois images",
        "Se souvenir d'un mot entendu",
        "Jeu mémoire avec six cartes",
        "Jeu mémoire avec huit cartes",
        "Se souvenir d'une consigne",
        "Se souvenir de deux consignes",
        "Répéter une liste de nombres",
        "Répéter deux phrases simples",
        "Compléter une comptine",
        "Dire la suite d'une histoire",
        "Se souvenir d'un objet caché",
        "Se souvenir d'une action",
        "Se souvenir d'une image",
        "Se souvenir d'un personnage",
        "Répéter une phrase plus longue",
        "Se souvenir d'une suite d'actions",
        "Se souvenir d'un mot nouveau",
        "Se souvenir d'un bruit",
        "Se souvenir d'un son",
        "Jeu mémoire avec objets",
        "Jeu mémoire avec animaux",
        "Jeu mémoire avec couleurs",
        "Jeu mémoire avec chiffres",
        "Jeu mémoire avec lettres",
        "Se souvenir de trois mots",
        "Se souvenir d'une courte histoire",
        "Se souvenir d'une série de gestes",
        "Retenir une consigne courte puis agir",
        "Retenir deux mots puis les répéter",
        "Retenir deux syllabes puis les répéter",
        "Répéter une petite phrase de 3 mots",
        "Répéter une petite phrase de 4 mots",
    ],

    "regulation": [

        "Respiration lente : inspirer 3 secondes, expirer 3 secondes",
        "Pause calme : s’allonger 2 minutes sans parler",
        "Pression profonde : serrer un coussin contre soi",
        "Bouger puis s’arrêter au signal",
        "Sauter 10 fois puis se calmer",
        "Jeu stop et respiration",
        "Se concentrer sur un objet pendant 10 secondes",
        "Marcher lentement puis vite puis s’arrêter",
        "Imiter un animal calme (chat, tortue)",
        "Se balancer doucement sur place",
        "Boire un verre d’eau calmement",
        "Serrer puis relâcher les mains",
        "Regarder une image calme 20 secondes",
        "Écouter un son doux",
        "Faire un câlin au doudou",
    ]

}

# ==============================
# GENERER UNE CONSIGNE AUTOMATIQUE
# ==============================
def generer_consigne(exercice: str) -> str:

    ex = (exercice or "").lower()

    # 🔥 DETECTION MODE TDA
    tda = st.session_state.get("tda_mode", False)

    # --- Nommer / Vocabulaire ---
    if ex.startswith("nommer"):
        if "animaux" in ex:
            return "Montre 5 à 8 images d’animaux. L’enfant dit le nom. Aide avec 2 choix si besoin."
        if "vêtements" in ex:
            return "Sors 4–6 vêtements. L’enfant les nomme. Variante : “où est le t-shirt ?”"
        if "couleurs" in ex:
            return "Montre 3 à 5 objets colorés. L’enfant dit la couleur."
        if "objets" in ex:
            return "Prends 5 objets du quotidien. L’enfant les nomme. Aide si besoin."
        return "Montre quelques images. L’enfant nomme. Aide avec 2 choix."

    # --- Répéter / Articulation ---
    if "répéter" in ex or "syllabe" in ex or "sons" in ex or "prononcer" in ex:
        if "2" in ex:
            return "Dis 2 mots simples. L’enfant répète lentement."
        if "3" in ex:
            return "Dis 3 mots simples. L’enfant répète. Aide si besoin."
        return "Dis lentement, l’enfant répète. Garde un rythme calme."

    # --- Memory ---
    if "mémory" in ex or "paires" in ex:
        return "Retourne 2 cartes. L’enfant cherche les paires. Commence avec peu de cartes."

    if "qui manque" in ex:
        return "Montre 3 objets. Cache-en un. L’enfant dit lequel manque."

    # --- Compréhension ---
    if "comprendre" in ex or "consigne" in ex or "donne-moi" in ex:
        return "Donne 1 consigne simple. Montre si nécessaire. Répète doucement."

    # --- Décrire ---
    if "décrire" in ex or "raconter" in ex:
        return "Montre une image. Pose 2 questions simples. Aide l’enfant."

    # --- Communication ---
    if "demander" in ex or "je veux" in ex:
        return "Propose 2 choix. L’enfant dit ce qu’il veut. Aide avec modèle."

    # --- Jeux ---
    if "jacques a dit" in ex:
        return "Fais 2 consignes simples. Garde un rythme lent et ludique."

    if "stop/go" in ex:
        return "Jeu simple : STOP = on arrête, GO = on bouge."

    if "intrus" in ex:
        return "Montre 3 images + 1 intrus. L’enfant trouve."

    if "rimes" in ex:
        return "Dis 2 mots. L’enfant dit si ça rime."

    if "souffle" in ex:
        return "Souffler doucement sur une plume."

    if "rythme" in ex:
        return "Fais un rythme simple. L’enfant imite."

    # =========================
    # CONSIGNE REGULATION (TDA)
    # =========================

    if "respiration" in ex or "calme" in ex or "pause" in ex:

        if tda:
            return "🧠 Pause obligatoire : respiration lente 30 secondes + moment calme sans stimulation."

        return "Fais une pause calme avec l’enfant. Respiration lente."

    # =========================
    # VERSION TDA (fallback global)
    # =========================

    if tda:
        return (
            "Fais l’exercice très court (2–3 minutes). "
            "Montre un exemple. Aide beaucoup. "
            "Fais une pause dès que l’enfant fatigue."
        )

    # =========================
    # FALLBACK NORMAL
    # =========================

    return (
        "Lis l’exercice, montre un exemple, puis laisse l’enfant essayer. "
        "Aide si besoin et encourage."
    )

DOMAINES = ["attention", "comprehension", "communication", "expression", "memoire", "regulation"]

def _safe_child_id(data: dict) -> str:
    prenom = data.get("profil", {}).get("prenom", "enfant")
    cid = str(prenom).strip().lower().replace(" ", "_")
    return cid or "enfant"

def _init_hist(data: dict):
    """Historique anti-répétition par enfant."""
    if "exercices_hist" not in data:
        data["exercices_hist"] = {}  # {child_id: {"last_weeks": {week: {...}}, "used": {domain: [..]}}}

def _reset_used_if_needed(used_list: list, domain: str):
    # si on a tout utilisé, on recycle
    if len(used_list) >= len(EXERCICES_BIB[domain]) - 2:
        used_list.clear()

def niveau_difficulte_exercice(age_langage: int, semaine: int, niveau: str) -> str:
    """
    Détermine la difficulté selon l'âge de langage, le niveau et la semaine.
    """

    # base progression semaine
    progression = semaine // 4

    # ajustement selon niveau
    if niveau == "retard sévère":
        progression -= 1
    elif niveau == "retard modéré":
        progression += 0
    elif niveau == "retard léger":
        progression += 1
    elif niveau == "aucun retard":
        progression += 2

    # ajustement selon âge langage
    if age_langage <= 3:
        progression -= 1
    elif age_langage >= 6:
        progression += 1

    # bornes
    if progression <= 0:
        return "niveau facile"

    if progression == 1:
        return "niveau intermédiaire"

    return "niveau avancé"

def choisir_exercices_semaine(data: dict, niveau: str, semaine: int) -> list:
    """
    Retourne 5 exercices adaptés :
    - âge de langage
    - niveau (léger/modéré/sévère)
    - domaines faibles
    - progression semaine
    - adaptation TDA / fatigue / agitation
    """

    age_langage = st.session_state.get("age_langage", 4)

    # =========================
    # PROFIL UTILISATEUR (APP)
    # =========================
    profil_app = st.session_state.get(
        "profil_app",
        "Accompagnement classique"
    )


    _init_hist(data)
    child_id = _safe_child_id(data)

    child_hist = data["exercices_hist"].setdefault(
        child_id,
        {"last_weeks": {}, "used": {d: [] for d in DOMAINES}}
    )

    # =========================
    # 🔒 BLOQUER LES EXERCICES PAR SEMAINE
    # =========================

    if str(semaine) in child_hist["last_weeks"]:

        ancien = child_hist["last_weeks"][str(semaine)]

        if (
            ancien.get("niveau") == niveau
            and ancien.get("profil_app") == profil_app
        ):
            return ancien["exercices"]
    
    # =========================
    # DETECTION TDA
    # =========================

    profil = data.get("profil", {})
    diagnostic = profil.get("diagnostic", "").lower()
    tda = st.session_state.get("tda_mode", False) or "tda" in diagnostic or "tdah" in diagnostic

    # =========================
    # SI SEMAINE DEJA GENEREE
    # =========================

# if str(semaine) in child_hist["last_weeks"]:
#     ancien = child_hist["last_weeks"][str(semaine)]
#     if (
#         ancien.get("niveau") == niveau
#         and ancien.get("profil_app") == profil_app
#     ):
#         return ancien["exercices"]

    selection = []

    # =========================
    # DETECTION DOMAINES FAIBLES
    # =========================

    evaluation = data.get("evaluation", {})

    domaines = {
        "attention": evaluation.get("attention", []),
        "comprehension": evaluation.get("comprehension", []),
        "communication": evaluation.get("communication", []),
        "expression": evaluation.get("expression", []),
        "memoire": evaluation.get("memoire", [])
    }

    domaines_faibles = []

    for domaine, valeurs in domaines.items():
        if valeurs:
            ratio = sum(valeurs) / len(valeurs)
            if ratio >= 0.4:
                domaines_faibles.append(domaine)

    # =========================
    # PRIORISATION DOMAINES
    # =========================

    domaines_prioritaires = []

    for d in DOMAINES:
        if d in domaines_faibles:
            domaines_prioritaires.extend([d, d])
        else:
            domaines_prioritaires.append(d)

    # =========================
    # CHOIX DOMAINES (MODE TDA)
    # =========================

    if tda:
        domaines_a_traiter = ["regulation", "attention", "communication", "comprehension", "expression"]
    else:
        # =========================
        # ADAPTATION AUX FAIBLESSES
        # =========================

        domaines_a_traiter = []

        for d in DOMAINES:
            if d in domaines_faibles:
                domaines_a_traiter.extend([d, d, d])  # priorité forte
            else:
                domaines_a_traiter.append(d)

        # limite à 5 exercices
        domaines_a_traiter = domaines_a_traiter[:5]

    # =========================
    # SELECTION EXERCICES
    # =========================

    for d in domaines_a_traiter:

        used = child_hist["used"].setdefault(d, [])
        _reset_used_if_needed(used, d)

        pool_source = EXERCICES_BIB.get(d, [])
        pool = [x for x in pool_source if x not in used]

        # =========================
        # FILTRAGE PAR SEMAINE (CORRECT)
        # =========================

        if profil_app == "Stimulation renforcée (aller plus loin)":

            if semaine <= 8:
                pool = [x for x in pool if "[SIMPLE]" in x] or pool

            elif semaine <= 16:
                pool = [x for x in pool if "[MOYEN]" in x] or pool

            else:
                pool = [x for x in pool if "[AVANCE]" in x] or pool

        if not pool:
            pool = pool_source[:]

        if not pool:
            pool = EXERCICES_BIB[d][:]

        # =========================
        # PROGRESSION AUTOMATIQUE
        # =========================

        if profil_app == "Besoin d'aide (difficultés de compréhension ou langage)":
            pool = [x for x in pool if "[SIMPLE]" in x] or pool

        elif profil_app == "Stimulation renforcée (aller plus loin)":

            if semaine <= 8:
                pool = [x for x in pool if "[SIMPLE]" in x] or pool

            elif semaine <= 16:
                pool = [x for x in pool if "[MOYEN]" in x] or pool

            else:
                pool = [x for x in pool if "[AVANCE]" in x] or pool
            
        # =========================
        # FILTRE AGE
        # =========================

        if age_langage <= 3:
            pool = [
                x for x in pool
                if "phrase" not in x.lower()
                and "histoire" not in x.lower()
                and "raconter" not in x.lower()
                and "décrire" not in x.lower()
            ]

        if not pool:
            pool = EXERCICES_BIB[d][:]


        ex = random.choice(pool)

        # =========================
        # FORCER NIVEAU PAR SEMAINE
        # =========================

        if semaine <= 8:
            niveau_cible = "[SIMPLE]"
        elif semaine <= 16:
            niveau_cible = "[MOYEN]"
        else:
            niveau_cible = "[AVANCE]"

        # enlever anciens tags
        ex = ex.replace("[SIMPLE]", "").replace("[MOYEN]", "").replace("[AVANCE]", "").strip()

        # ajouter le bon niveau
        ex = ex + " " + niveau_cible


        # =========================
        # AJOUT AUTO NIVEAU SI MANQUANT
        # =========================

        if "[SIMPLE]" not in ex and "[MOYEN]" not in ex and "[AVANCE]" not in ex:

            if semaine <= 8:
                ex = ex + " [SIMPLE]"
            elif semaine <= 16:
                ex = ex + " [MOYEN]"
            else:
                ex = ex + " [AVANCE]"

        difficulte = niveau_difficulte_exercice(age_langage, semaine, niveau)


        if "[SIMPLE]" in ex:
            ex = f"🔴 {ex.replace('[SIMPLE]', '')} (aide nécessaire)"

        elif "[MOYEN]" in ex:
            ex = f"🟠 {ex.replace('[MOYEN]', '')} (intermédiaire)"

        elif "[AVANCE]" in ex:
            ex = f"🟢 {ex.replace('[AVANCE]', '')} (niveau avancé)"

        else:
            ex = f"{ex} ({difficulte})"

        used.append(ex)
        selection.append(ex)

    # =========================
    # AJOUT PAUSES INTELLIGENTES TDA
    # =========================

    if tda:
        nouvelle_selection = []

        for i, ex in enumerate(selection):
            nouvelle_selection.append(ex)

            if i % 2 == 1 and "pause" not in ex.lower():
                if semaine <= 8:
                    pause = "🔴 🧠 Pause régulation (calme simple)"
                elif semaine <= 16:
                    pause = "🟠 🧠 Pause régulation (respiration guidée)"
                else:
                    pause = "🟢 🧠 Pause régulation (relaxation + respiration)"

                nouvelle_selection.append(pause)

        selection = nouvelle_selection

    # =========================
    # ADAPTATION FATIGUE
    # =========================

    fatigue = st.session_state.get("fatigue", "Moyen")

    if fatigue == "Élevé":
        selection = selection[:3]

        while len(selection) < 5:
            selection.append("Repos / activité calme")

    # =========================
    # ADAPTATION NIVEAU
    # =========================

    if tda:
        selection = [
            f"{ex} (2–3 min max, ludique)"
            if "pause" not in ex.lower()
            else ex
            for ex in selection
        ]

    elif niveau == "retard sévère":
        selection = [f"{ex} (très court, guidé)" for ex in selection]

    elif niveau == "retard modéré":
        selection = [f"{ex} (guidé)" for ex in selection]

    else:
        selection = [f"{ex} (autonomie progressive)" for ex in selection]

    # =========================
    # SAUVEGARDE
    # =========================

    child_hist["last_weeks"][str(semaine)] = {
        "exercices": selection,
        "niveau": niveau,
        "profil_app": profil_app
    }

    prenom = profil.get("prenom", "enfant")
    sauvegarder(data, prenom)

    return selection

def fiche_exercice(exercice: str, age_langage: int | None = None) -> dict:
    """
    Retourne une mini-fiche guidée pour un exercice.
    age_langage = âge estimé du langage (pas l'âge réel).
    """

    e = exercice.strip().lower()

    if age_langage is None:
        age_langage = 4

    base = {
        "objectif": "Travailler le langage de façon simple et régulière.",
        "materiel": "Aucun (ou images/objets de la maison).",
        "etapes": [
            "Faites l'activité 3 minutes.",
            "Aidez beaucoup au début.",
            "Arrêtez avant que l'enfant se fatigue."
        ],
        "exemple_phrase": ""
    }

    # =========================
    # PHONOLOGIE / SONS
    # =========================

    if "syllabes" in e or "répéter" in e:

        return {
            "objectif": "Travailler les sons et les syllabes.",
            "materiel": "Aucun ou images simples.",
            "etapes": [
                "Prononcez lentement la syllabe ou le mot.",
                "Demandez à l'enfant de répéter.",
                "Découpez le mot en syllabes si besoin.",
                "Félicitez chaque tentative."
            ],
            "exemple_phrase": "Dis : pa... puis pou... puis poupée."
        }

    # =========================
    # CONSTRUCTION DE PHRASES
    # =========================

    if "phrase" in e:

        return {
            "objectif": "Aider l'enfant à construire des phrases.",
            "materiel": "Images simples.",
            "etapes": [
                "Montrez une image.",
                "Demandez : qui ?",
                "Puis : que fait-il ?",
                "Aidez l'enfant à faire une phrase."
            ],
            "exemple_phrase": "La fille mange."
        }

    # =========================
    # COMPRÉHENSION
    # =========================

    if "consigne" in e or "comprendre" in e:

        return {
            "objectif": "Améliorer la compréhension des consignes.",
            "materiel": "Objets de la maison.",
            "etapes": [
                "Donnez une consigne simple.",
                "Montrez si nécessaire.",
                "Faites refaire une seconde consigne.",
                "Augmentez progressivement la difficulté."
            ],
            "exemple_phrase": "Prends la balle."
        }

    # =========================
    # EXERCICES SPÉCIFIQUES
    # =========================

    if "Dire fini" in e or "dire fini" in e:

        return {
            "objectif": "Apprendre à dire que l'activité est terminée.",
            "materiel": "Un jeu simple.",
            "etapes": [
                "Jouez 30 secondes.",
                "Arrêtez et dites : fini.",
                "Aidez l'enfant à répéter."
            ],
            "exemple_phrase": "Fini le jeu."
        }

    if "encore" in e or "stop" in e:

        return {
            "objectif": "Apprendre encore et stop.",
            "materiel": "Bulles ou balle.",
            "etapes": [
                "Faites l'activité 3 secondes.",
                "Arrêtez.",
                "Demandez : encore ?"
            ],
            "exemple_phrase": "Encore ?"
        }

    if "stop/go" in e or "jeu stop/go" in e:

        return {
            "objectif": "Améliorer l'attention.",
            "materiel": "Vos mains.",
            "etapes": [
                "Quand je dis GO tu tapes.",
                "Quand je dis STOP tu arrêtes."
            ],
            "exemple_phrase": "GO ! STOP !"
        }

    if "nommer" in e:

        return {
            "objectif": "Augmenter le vocabulaire.",
            "materiel": "Images.",
            "etapes": [
                "Montrez une image.",
                "Demandez : c'est quoi ?",
                "Faites répéter."
            ],
            "exemple_phrase": "C'est un chat."
        }

    if "mémory" in e:

        return {
            "objectif": "Travailler mémoire et attention.",
            "materiel": "Cartes.",
            "etapes": [
                "Retournez deux cartes.",
                "Nommer l'image.",
                "Trouver la paire."
            ],
            "exemple_phrase": "Chat / chat."
        }

    # =========================
    # OBJECTIF INTELLIGENT (GÉNÉRAL)
    # =========================

    if "consigne" in e:
        base["objectif"] = "Améliorer la compréhension des consignes simples"

    elif "image" in e:
        base["objectif"] = "Développer l’attention visuelle et la compréhension"

    elif "répéter" in e or "répète" in e:
        base["objectif"] = "Renforcer la mémoire auditive et la production orale"

    elif "dire" in e or "parler" in e:
        base["objectif"] = "Stimuler l’expression orale et le langage spontané"

    elif "mémoire" in e or "mémory" in e:
        base["objectif"] = "Développer la mémoire et la concentration"

    elif "imiter" in e:
        base["objectif"] = "Améliorer l’imitation et les compétences langagières"

    elif "comprendre" in e:
        base["objectif"] = "Renforcer la compréhension du langage"

    elif "nommer" in e:
        base["objectif"] = "Développer le vocabulaire"

    else:
        base["objectif"] = "Stimuler le développement global du langage"

    return base





def generer_pdf_bilan(texte_bilan):

    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer, pagesize=A4)

    styles = getSampleStyleSheet()

    elements = []

    # =========================
    # LOGO (UNIFIÉ PRO)
    # =========================

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    logo_path = os.path.join(BASE_DIR, "langage_pas_a_pas.png")

    if os.path.exists(logo_path):
        try:
            logo = Image(logo_path)

            ratio = logo.imageWidth / logo.imageHeight

            max_width = 340
            max_height = 140

            if (max_width / ratio) <= max_height:
                logo.drawWidth = max_width
                logo.drawHeight = max_width / ratio
            else:
                logo.drawHeight = max_height
                logo.drawWidth = max_height * ratio

            logo.hAlign = "CENTER"

            elements.append(logo)
            elements.append(Spacer(1, 20))

        except Exception as e:
            print("Erreur logo :", e)

    # ---------------------------
    # TITRE
    # ---------------------------
    elements.append(Paragraph("BILAN LANGAGE PAS À PAS", styles["Heading1"]))
    elements.append(Spacer(1, 20))

    # ---------------------------
    # INTRO
    # ---------------------------
    elements.append(Paragraph(
        "Programme personnalisé basé sur l’analyse du langage de l’enfant.",
        styles["Italic"]
    ))
    elements.append(Spacer(1, 20))

    elements.append(Spacer(1, 10))
    elements.append(HRFlowable(width="100%", thickness=1, color=HexColor("#E8DCDC")))
    elements.append(Spacer(1, 10))

    # ---------------------------
    # RESULTATS
    # ---------------------------
    elements.append(Paragraph("📊 Résultats de l’évaluation", styles["Heading2"]))
    elements.append(Spacer(1, 10))

    for ligne in texte_bilan.split("\n"):
        ligne = ligne.strip()

        if ligne == "":
            elements.append(Spacer(1, 8))

        elif ligne.startswith("■") or ligne.startswith("📊") or ligne.startswith("💡"):
            elements.append(Paragraph(ligne, styles["Heading2"]))
            elements.append(Spacer(1, 12))

        else:
            elements.append(Paragraph(ligne, styles["Normal"]))

    elements.append(Spacer(1, 20))

    # ---------------------------
    # CONSEILS
    # ---------------------------

    elements.append(Spacer(1, 10))
    elements.append(HRFlowable(width="100%", thickness=1, color=HexColor("#E8DCDC")))
    elements.append(Spacer(1, 10))

    elements.append(Paragraph("💡 Recommandations", styles["Heading2"]))
    elements.append(Spacer(1, 10))

    elements.append(Paragraph(
        "Encouragez l’enfant, répétez les mots et privilégiez des exercices courts et réguliers.",
        styles["Normal"]
    ))
    elements.append(Spacer(1, 20))

    # ---------------------------
    # AVERTISSEMENT
    # ---------------------------
    elements.append(Paragraph(
        "Ce programme est un outil éducatif et ne remplace pas un professionnel de santé (orthophoniste, médecin…).",
        styles["Italic"]
    ))

    # ---------------------------
    # GÉNÉRATION PDF
    # ---------------------------
    doc.build(elements)

    buffer.seek(0)

    return buffer.getvalue()


def generer_pdf_guide():

    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import getSampleStyleSheet
    from io import BytesIO
    import os

    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4)

    styles = getSampleStyleSheet()
    elements = []

    # =========================
    # LOGO (UNIFIÉ PRO)
    # =========================

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    logo_path = os.path.join(BASE_DIR, "langage_pas_a_pas.png")

    if os.path.exists(logo_path):
        try:
            logo = Image(logo_path)

            ratio = logo.imageWidth / logo.imageHeight

            max_width = 340
            max_height = 140

            if (max_width / ratio) <= max_height:
                logo.drawWidth = max_width
                logo.drawHeight = max_width / ratio
            else:
                logo.drawHeight = max_height
                logo.drawWidth = max_height * ratio

            logo.hAlign = "CENTER"

            elements.append(logo)
            elements.append(Spacer(1, 20))

        except Exception as e:
            print("Erreur logo :", e)

    # =========================
    # CONTENU (TOUJOURS AFFICHÉ)
    # =========================

    elements.append(Paragraph("Guide d’accompagnement du langage", styles["Heading1"]))
    elements.append(Spacer(1, 20))

    elements.append(Paragraph(
        "Ce guide est conçu pour accompagner efficacement les parents dans la stimulation du langage de leur enfant.",
        styles["Normal"]
    ))
    elements.append(Spacer(1, 20))

    elements.append(Paragraph("Comment utiliser le programme :", styles["Heading2"]))
    elements.append(Spacer(1, 10))

    elements.append(Paragraph(
        "• 1 exercice par jour<br/>• 3 à 5 minutes<br/>• Régularité essentielle",
        styles["Normal"]
    ))
    elements.append(Spacer(1, 20))

    elements.append(Paragraph("Conseils :", styles["Heading2"]))
    elements.append(Spacer(1, 10))

    elements.append(Paragraph(
        "• Parler lentement<br/>• Encourager<br/>• Répéter souvent",
        styles["Normal"]
    ))
    elements.append(Spacer(1, 20))

    elements.append(Paragraph("À éviter :", styles["Heading2"]))
    elements.append(Spacer(1, 10))

    elements.append(Paragraph(
        "• Trop corriger<br/>• Aller trop vite<br/>• Séances trop longues",
        styles["Normal"]
    ))
    elements.append(Spacer(1, 20))

    elements.append(Paragraph(
        "Ce programme est un outil éducatif et ne remplace pas un professionnel de santé (orthophoniste, médecin…).",
        styles["Italic"]
    ))

    doc.build(elements)

    buffer.seek(0)
    return buffer.getvalue()


def analyse_intelligente_langage(domaines_faibles, age, age_langage):

    texte = []

    retard = age - age_langage

    if retard >= 3:
        texte.append("Le développement du langage présente un retard important.")

    elif retard == 2:
        texte.append("Le langage montre un retard modéré qui nécessite une stimulation régulière.")

    elif retard == 1:
        texte.append("Le langage est légèrement en dessous de l'âge attendu.")

    else:
        texte.append("Le développement du langage est globalement cohérent avec l'âge.")

    if "Compréhension" in domaines_faibles:
        texte.append("La compréhension semble fragile. Il est recommandé de privilégier des consignes simples accompagnées de gestes.")

    if "Expression" in domaines_faibles:
        texte.append("L'expression orale doit être stimulée par des jeux de phrases et de répétition.")

    if "Communication" in domaines_faibles:
        texte.append("Il est utile de favoriser les situations d'échange et les demandes verbales.")

    if "Mémoire verbale" in domaines_faibles:
        texte.append("Des jeux de répétition de mots et de petites phrases peuvent renforcer la mémoire verbale.")

    if "Attention" in domaines_faibles:
        texte.append("Des activités très courtes et variées permettront d'améliorer l'attention.")

    return "\n".join(texte)


def ajuster_difficulte_selon_progression(progress_pct, niveau):

    if progress_pct > 70:

        if niveau == "retard sévère":
            return "retard modéré"

        if niveau == "retard modéré":
            return "retard léger"

        return niveau

    if progress_pct < 20:

        if niveau == "retard léger":
            return "retard modéré"

    return niveau

def conseils_personnalises(domaines_faibles):

    conseils = []

    if "Attention" in domaines_faibles:
        conseils.append("faire des exercices très courts (3 minutes)")

    if "Compréhension" in domaines_faibles:
        conseils.append("utiliser des phrases simples et montrer les objets")

    if "Expression" in domaines_faibles:
        conseils.append("faire répéter des mots puis des phrases")

    if "Communication" in domaines_faibles:
        conseils.append("encourager l'enfant à demander ce qu'il veut")

    if "Mémoire verbale" in domaines_faibles:
        conseils.append("faire des jeux de répétition de mots")

    if not conseils:
        conseils.append("continuer les activités de langage quotidiennement")

    return conseils


def generer_pdf_programme(programme, profil=None, niveau=None, age_langage=None):

    from reportlab.platypus import Image, HRFlowable
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib.colors import HexColor
    import os

    buffer = BytesIO()

    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=2*cm,
        leftMargin=2*cm,
        topMargin=2*cm,
        bottomMargin=2*cm
    )

    styles = getSampleStyleSheet()

    titre = styles["Heading1"]
    normal = styles["Normal"]

    style_titre = ParagraphStyle(
        name='Titre',
        fontSize=14,
        leading=16,
        spaceAfter=10,
        spaceBefore=10,
        textColor=HexColor("#C97C8A")
    )

    # 🔥 IMPORTANT → DOIT ÊTRE AVANT TOUT
    elements = []

    # =========================
    # LOGO (UNIFIÉ PRO)
    # =========================

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    logo_path = os.path.join(BASE_DIR, "langage_pas_a_pas.png")

    if os.path.exists(logo_path):
        try:
            logo = Image(logo_path)

            ratio = logo.imageWidth / logo.imageHeight

            max_width = 340
            max_height = 140

            if (max_width / ratio) <= max_height:
                logo.drawWidth = max_width
                logo.drawHeight = max_width / ratio
            else:
                logo.drawHeight = max_height
                logo.drawWidth = max_height * ratio

            logo.hAlign = "CENTER"

            elements.append(logo)
            elements.append(Spacer(1, 20))

        except Exception as e:
            print("Erreur logo :", e)

    # =========================
    # SOUS TITRE
    # =========================

    elements.append(Paragraph(
        "Programme éducatif de stimulation du langage",
        styles["Heading3"]
    ))
    elements.append(Spacer(1, 20))

    # =========================
    # TITRE
    # =========================

    elements.append(Paragraph(
        "Bilan et Programme Langage Pas à Pas",
        titre
    ))
    elements.append(Spacer(1, 20))

    # =========================
    # PROFIL ENFANT
    # =========================

    if profil:

        elements.append(Paragraph("👶 Profil de l'enfant", style_titre))
        elements.append(Spacer(1, 6))
        elements.append(HRFlowable(width="100%", thickness=1, color=HexColor("#E8DCDC")))
        elements.append(Spacer(1, 10))

        prenom = profil.get("prenom", "")
        age = profil.get("age", "")

        elements.append(Paragraph(f"Prénom : {prenom}", normal))
        elements.append(Paragraph(f"Âge : {age} ans", normal))

        if age_langage:
            elements.append(Paragraph(f"Âge de langage estimé : {age_langage} ans", normal))

        if niveau:
            elements.append(Paragraph(f"Niveau détecté : {niveau}", normal))

        elements.append(Spacer(1, 20))

    # =========================
    # ANALYSE
    # =========================

    elements.append(Paragraph("🧠 Analyse du développement du langage", style_titre))
    elements.append(Spacer(1, 6))
    elements.append(HRFlowable(width="100%", thickness=1, color=HexColor("#E8DCDC")))
    elements.append(Spacer(1, 10))

    if niveau == "retard sévère":
        texte = """L'évaluation indique un retard important du développement du langage.

Le programme proposé vise à renforcer progressivement les compétences suivantes :

• Vocabulaire  
• Imitation  
• Compréhension  
• Communication  

Les exercices sont courts, progressifs et adaptés au rythme de l’enfant."""

    elif niveau == "retard modéré":
        texte = """L'enfant présente un retard modéré du langage.
Le programme vise à enrichir le vocabulaire et les phrases."""

    elif niveau == "retard léger":
        texte = """Le langage est présent mais certaines compétences doivent être renforcées."""
    else:
        texte = """Le développement du langage est cohérent avec l'âge."""

    elements.append(Paragraph(texte, normal))
    elements.append(Spacer(1, 20))

    # =========================
    # RESULTATS
    # =========================

    elements.append(Paragraph("📊 Résultats de l’évaluation", style_titre))
    elements.append(Spacer(1, 6))
    elements.append(HRFlowable(width="100%", thickness=1, color=HexColor("#E8DCDC")))
    elements.append(Spacer(1, 10))

    if age_langage:
        elements.append(Paragraph(f"Âge de langage estimé : <b>{age_langage} ans</b>", normal))

    if niveau:
        elements.append(Paragraph(f"Niveau estimé : <b>{niveau}</b>", normal))

    elements.append(Spacer(1, 20))

    # =========================
    # RECOMMANDATIONS
    # =========================

    elements.append(Paragraph("💡 Recommandations personnalisées", style_titre))
    elements.append(Spacer(1, 6))
    elements.append(HRFlowable(width="100%", thickness=1, color=HexColor("#E8DCDC")))
    elements.append(Spacer(1, 10))

    elements.append(Paragraph("• Utiliser des phrases simples et claires", normal))
    elements.append(Paragraph("• Encourager l'enfant à s'exprimer sans le corriger excessivement", normal))
    elements.append(Paragraph("• Répéter les mots et valoriser chaque tentative", normal))
    elements.append(Paragraph("• Privilégier des exercices courts et réguliers (3–5 min)", normal))

    elements.append(Spacer(1, 20))

    # =========================
    # PROGRAMME
    # =========================

    elements.append(Paragraph("📅 Programme personnalisé sur 6 mois", style_titre))

    elements.append(Spacer(1, 10))

    elements.append(Paragraph(
        "<font size=11><b>🧠 Programme intelligent personnalisé</b></font><br/>"
        "<font size=9>Ce programme s’adapte automatiquement au niveau et aux difficultés de l’enfant "
        "pour favoriser une progression naturelle, motivante et sans pression.</font>",
        styles["Normal"]
    ))

    elements.append(Spacer(1, 20))

    elements.append(HRFlowable(width="100%", thickness=1, color=HexColor("#E8DCDC")))
    elements.append(Spacer(1, 10))

    jours = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi"]

    for semaine, exercices in programme.items():

        elements.append(Paragraph(f"Semaine {semaine}", styles["Heading3"]))
        elements.append(Spacer(1, 6))

        data = [["Jour", "Exercice"]]

        for i, ex in enumerate(exercices[:5]):
            if i < len(jours):

                niveau_txt = ""

                if "🔴" in ex:
                    niveau_txt = "<font color='red'><b>Aide nécessaire</b></font>"
                elif "🟠" in ex:
                    niveau_txt = "<font color='orange'><b>Intermédiaire</b></font>"
                elif "🟢" in ex:
                    niveau_txt = "<font color='green'><b>Avancé</b></font>"

                ex_clean = ex.replace("🔴", "").replace("🟠", "").replace("🟢", "")

                # 🔥 SUPPRIME LES DOUBLONS TEXTE
                ex_clean = ex_clean.replace("(aide nécessaire)", "")
                ex_clean = ex_clean.replace("(intermédiaire)", "")
                ex_clean = ex_clean.replace("(niveau avancé)", "")
                ex_clean = ex_clean.replace("(guidé)", "")

                texte = f"{ex_clean}<br/><b>{niveau_txt}</b>"

                data.append([jours[i], Paragraph(texte, styles["Normal"])])

        # ✅ CRÉATION TABLE (MANQUANTE AVANT)
        table = Table(data, colWidths=[3 * cm, 13 * cm])

        table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), HexColor("#FDECEC")),
            ("GRID", (0, 0), (-1, -1), 0.5, HexColor("#dddddd")),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),

            ("LEFTPADDING", (0, 0), (-1, -1), 6),
            ("RIGHTPADDING", (0, 0), (-1, -1), 6),
            ("TOPPADDING", (0, 0), (-1, -1), 10),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 10),

            ("WORDWRAP", (0, 0), (-1, -1), 'CJK'),
        ]))

        elements.append(Spacer(1, 10))
        elements.append(table)
        elements.append(Spacer(1, 20))

    # =========================
    # AVERTISSEMENT
    # =========================

    elements.append(Spacer(1, 20))

    elements.append(Paragraph(
        "Ce programme est un outil éducatif et ne remplace pas un professionnel de santé (orthophoniste, médecin…).",
        styles["Italic"]
    ))

    doc.build(elements)

    buffer.seek(0)

    return buffer.getvalue()

def generer_pdf_fiches_semaine(exercices, semaine, profil=None):

    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import getSampleStyleSheet
    from io import BytesIO
    import os

    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4)

    styles = getSampleStyleSheet()
    elements = []

    # =========================
    # LOGO (UNIFIÉ PRO)
    # =========================

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    logo_path = os.path.join(BASE_DIR, "langage_pas_a_pas.png")

    if os.path.exists(logo_path):
        try:
            logo = Image(logo_path)

            ratio = logo.imageWidth / logo.imageHeight

            max_width = 340
            max_height = 140

            if (max_width / ratio) <= max_height:
                logo.drawWidth = max_width
                logo.drawHeight = max_width / ratio
            else:
                logo.drawHeight = max_height
                logo.drawWidth = max_height * ratio

            logo.hAlign = "CENTER"

            elements.append(logo)
            elements.append(Spacer(1, 20))

        except Exception as e:
            print("Erreur logo :", e)

    # =========================
    # TITRE
    # =========================
    elements.append(Paragraph(
        f"📘 Fiches exercices détaillées – Semaine {semaine}",
        styles["Heading1"]
    ))
    elements.append(Spacer(1, 10))

    # =========================
    # PROFIL ENFANT
    # =========================
    if profil:
        prenom = profil.get("prenom", "")
        age = profil.get("age", "")

        elements.append(Paragraph(f"👶 Enfant : {prenom}", styles["Normal"]))
        elements.append(Paragraph(f"Âge : {age} ans", styles["Normal"]))
        elements.append(Spacer(1, 10))

    # =========================
    # FICHES EXERCICES (NETTOYAGE + CORRECTION)
    # =========================

    for ex in exercices[:5]:

        # 🔥 NETTOYAGE TEXTE (IMPORTANT)
        ex_clean = (
            ex.replace("■", "")
              .replace("(aide nécessaire)", "")
              .replace("(intermédiaire)", "")
              .replace("(niveau avancé)", "")
              .replace("(très court, guidé)", "")
              .replace("(guidé)", "")
              .replace("(autonomie progressive)", "")
              .strip()
        )

        # 👉 on utilise le texte propre
        fiche = fiche_exercice(ex_clean, None)

        style_box = ParagraphStyle(
            name="Box",
            backColor=HexColor("#FFF4F4"),
            borderPadding=10,
            spaceAfter=10
        )

        elements.append(Paragraph(
            f"<b>🧠 Exercice</b><br/>{ex_clean}",
            style_box
        ))

        elements.append(Paragraph(
            f"<b>🎯 Objectif :</b> {fiche['objectif']}",
            styles["Normal"]
        ))

        elements.append(Paragraph(
            f"<b>🧰 Matériel :</b> {fiche['materiel']}",
            styles["Normal"]
        ))

        elements.append(Paragraph("✅ Étapes :", styles["Normal"]))

        for step in fiche["etapes"]:
            elements.append(Paragraph(f"- {step}", styles["Normal"]))

        if fiche.get("exemple_phrase"):
            elements.append(Paragraph(f"🗣 Exemple : {fiche['exemple_phrase']}", styles["Normal"]))

        elements.append(Spacer(1, 20))

    # =========================
    # TEXTE LÉGAL
    # =========================

    elements.append(Spacer(1, 20))
    elements.append(Paragraph(
        "⚠️ Ce programme ne remplace pas un professionnel de santé (orthophoniste, médecin…).",
        styles["Normal"]
    ))

    doc.build(elements)

    buffer.seek(0)
    return buffer.getvalue()

# =================================
# PAGE
# =================================
def render():



    # initialisation du prénom actif
    if "prenom_actif" not in st.session_state:
        st.session_state["prenom_actif"] = "enfant"

    if "lp_data" not in st.session_state:
        st.session_state["lp_data"] = charger(st.session_state.get("prenom_actif", "enfant"))

    data = st.session_state["lp_data"]


    profil = data.get("profil", {})
    child_id = str(profil.get("prenom", "enfant")).lower().replace(" ", "_")

    if "progression" in data:
        st.session_state["progression"] = data["progression"]

    st.markdown('<div class="lp-wrap">', unsafe_allow_html=True)

    # ==============================
    # STYLE (identique ANIMASOIN)
    # ==============================

    st.markdown("""
    <style>

    .lp-wrap{
        max-width:1100px;
        margin:auto;
        padding:8px 8px 30px 8px;
    }

    .lp-header{
        background:linear-gradient(90deg,#ffe6ee 0%,#fff2e8 60%,#ffffff 100%);
        border:1px solid #f4d6dc;
        border-radius:22px;
        padding:20px;
        margin-bottom:16px;
        box-shadow:0 10px 26px rgba(0,0,0,0.05);
    }

    .lp-title{
        font-size:34px;
        font-weight:800;
        color:#f08a5d;
    }

    .lp-card{
        background:white;
        border:1px solid #f1e2e6;
        border-radius:18px;
        padding:18px;
        margin:12px 0;
        box-shadow:0 10px 26px rgba(0,0,0,0.04);
    }

    .lp-soft{
        background:#fff3ef;
        border-left:6px solid #f2b6a0;
    }

    .lp-ok{
        background:#eaf7f0;
        border-left:6px solid #7bc8a4;
    }

    .lp-alert{
        background:#ffe3e3;
        border-left:6px solid #e57373;
    }

    /* ==============================
       CORRECTION ESPACE HAUT
    ============================== */

    .block-container {
        padding-top: 1rem !important;
    }

    div[data-testid="stAppViewContainer"] {
        padding-top: 0rem !important;
    }

    </style>
    """, unsafe_allow_html=True)

    # ==============================
    # HEADER PROPRE + LOGO
    # ==============================

    # 🔧 Réduction espace haut
    st.markdown("""
    <style>
    .block-container {
        padding-top: 1rem !important;
    }
    </style>
    """, unsafe_allow_html=True)

    # 🔧 HEADER
    col1, col2, col3 = st.columns([1,2,1])

    with col2:
        if os.path.exists("langage_pas_a_pas.png"):
            st.image("langage_pas_a_pas.png", width=500)
        else:
            st.warning("Logo non trouvé")

        st.markdown("""
        <div style="text-align:center; margin-top:-20px;">
            <div style="font-size:34px; font-weight:800; color:#f08a5d;">
                Langage Pas à Pas
            </div>
            <div style="font-size:15px; color:#6b6b6b; margin-top:4px;">
                Programme éducatif pour stimuler le développement du langage de l'enfant
            </div>
        </div>
        """, unsafe_allow_html=True)

    # ==============================
    # 👶 PROFIL DE DIFFICULTÉ (APP)
    # ==============================

    profil_app = st.selectbox(
        "Choisissez le niveau d'accompagnement",
        [
            "Besoin d'aide (difficultés de compréhension ou langage)",
            "Accompagnement classique",
            "Stimulation renforcée (aller plus loin)"
        ]
    )

    st.session_state["profil_app"] = profil_app

    # ==============================
    # SELECTION ENFANT
    # ==============================    

    st.markdown("""
    <div class='lp-card lp-soft'>
    <b>👶 Choisir un enfant existant</b><br><br>

    Si l’enfant possède déjà un profil, sélectionnez-le dans la liste ci-dessous.<br>
    Si aucun profil n’existe encore, allez dans l’onglet <b>👶 Profil</b> pour créer un profil enfant.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 👶 Choisir un enfant")

    fichiers = lister_profils()

    if not fichiers:
        st.info("Aucun profil enfant enregistré. Crée d'abord un profil.")
    else:
        # sécurité si prenom_actif n'existe pas
        if st.session_state.get("prenom_actif") not in fichiers:
            st.session_state["prenom_actif"] = fichiers[0]

        prenom_selection = st.selectbox(
            "Profil enfant",
            fichiers,
            index=fichiers.index(st.session_state["prenom_actif"])
        )

        if prenom_selection != st.session_state["prenom_actif"]:
            st.session_state["prenom_actif"] = prenom_selection
            st.session_state["lp_data"] = charger(prenom_selection)
            st.rerun()

    # et on récupère data après sélection
    data = st.session_state.get("lp_data", {}) or {}

    # ==============================
    # TABS
    # ==============================

    tabs = st.tabs([
        "🏠 Accueil",
        "👶 Profil",
        "🧠 Évaluation",
        "🔍 Analyse",
        "🪜 Programme",
        "🗓 Suivi",
        "📊 Tableau de bord",
        "💡 Conseils",
        "ℹ️ À propos",
        "📚 Lecture"
    ])

    tab_accueil, tab_profil, tab_eval, tab_analyse, tab_programme, tab_suivi, tab_dashboard, tab_conseils, tab_apropos, tab_lecture = tabs

    # ==============================
    # ACCUEIL
    # ==============================
    with tabs[0]:

        st.markdown("""
        <div class="lp-card lp-soft">

        <b>Bienvenue dans Langage Pas à Pas</b><br><br>

        Ce programme aide les parents à stimuler
        le développement du langage de leur enfant
        grâce à des exercices courts et progressifs.

        <br>

        Le logiciel permet de :
        <br><br>

        1️⃣ Renseigner le profil de l’enfant<br>
        2️⃣ Réaliser une évaluation du langage<br>
        3️⃣ Générer un programme personnalisé sur 24 semaines<br>
        4️⃣ Suivre les progrès semaine après semaine

        <br>

        Les exercices sont adaptés automatiquement
        au niveau et à l’âge de langage de l’enfant.

        </div>
        """, unsafe_allow_html=True)

        # =========================
        # GESTION FATIGUE (CORRECTION)
        # =========================

        fatigue = st.session_state.get("fatigue", "Moyen")

        if fatigue == "Élevé":
            st.info("💡 Séances très courtes recommandées (2–3 min + pauses fréquentes)")
        elif fatigue == "Faible":
            st.success("✅ Enfant en forme → programme complet recommandé")
        else:
            st.info("💡 Les exercices durent environ 3 à 10 minutes par jour.")

        # =========================
        # MESSAGE BONUS PRO
        # =========================

        st.markdown("""
        <div class='lp-card'>

        <b>🧠 Conseil important</b><br><br>

        ✔ Privilégiez la régularité plutôt que la durée<br>
        ✔ 3 à 5 minutes suffisent largement<br>
        ✔ Arrêtez avant que l’enfant se fatigue<br>
        ✔ Valorisez chaque réussite (même petite)

        </div>
        """, unsafe_allow_html=True)

    # ==============================
    # PROFIL (FIX)
    # ==============================
    with tabs[1]:

        st.markdown("""
        <div class='lp-card lp-soft'>
        <b>👶 Gestion des profils enfants</b><br><br>

        • <b>Créer un nouvel enfant :</b> remplissez les champs ci-dessous puis cliquez sur <b>Sauvegarder profil</b>.<br>
        • <b>Modifier un enfant existant :</b> sélectionnez-le d'abord dans le menu en haut, puis modifiez les informations.
        </div>
        """, unsafe_allow_html=True)

        # enfant actif (sert de suffixe pour éviter les conflits Streamlit)
        actif = st.session_state.get("prenom_actif", "enfant")

        # data + profil
        data = st.session_state.get("lp_data", data)
        profil = data.get("profil", {})

        # ✅ recharge automatique du mode TDA
        if "tda_mode" not in st.session_state:
            st.session_state["tda_mode"] = profil.get("tda_mode", False)

        # ✅ message persistant après rerun
        if st.session_state.get("profil_saved_ok", False):
            st.success("Profil enregistré ✔")
            st.session_state["profil_saved_ok"] = False

        prenom = st.text_input(
            "Prénom",
            value=profil.get("prenom", ""),
            key=f"profil_prenom_{actif}"
        )

        age_options = [2,3,4,5,6,7,8,9,10]
        age_defaut = profil.get("age", 4)
        if age_defaut not in age_options:
            age_defaut = 4

        age = st.radio(
            "Âge de l’enfant",
            age_options,
            horizontal=True,
            index=age_options.index(age_defaut),
            key=f"profil_age_{actif}"
        )

        diagnostic_options = ["Aucun / en cours", "Retard léger", "Retard modéré", "Retard sévère"]
        diagnostic_defaut = profil.get("diagnostic", "Aucun / en cours")
        if diagnostic_defaut not in diagnostic_options:
            diagnostic_defaut = "Aucun / en cours"

        diagnostic = st.selectbox(
            "Diagnostic",
            diagnostic_options,
            index=diagnostic_options.index(diagnostic_defaut),
            key=f"profil_diag_{actif}"
        )

        # =========================
        # MODE TDA
        # =========================

        tda_mode = st.checkbox(
            "🧠 Mode TDA / difficulté de concentration",
            key="tda_mode"
        )


        if st.button("💾 Sauvegarder profil", key=f"btn_save_profil_{actif}"):

            prenom_clean = prenom.strip()

            if prenom_clean == "":
                st.warning("Veuillez saisir un prénom.")
                st.stop()

            # ✅ met à jour data
            data["profil"] = {
                "prenom": prenom_clean,
                "age": int(age),
                "diagnostic": diagnostic,
                "tda_mode": st.session_state.get("tda_mode", False)
            }

            # ✅ sauvegarde fichier
            sauvegarder(data, prenom_clean)

            # ✅ met à jour l'enfant actif et recharge (si ton charger est corrigé)
            st.session_state["prenom_actif"] = prenom_clean
            st.session_state["lp_data"] = charger(prenom_clean) or data

            # ✅ flag pour afficher le succès APRÈS rerun
            st.session_state["profil_saved_ok"] = True

            st.rerun()

    # ==============================
    # EVALUATION
    # ==============================
    with tabs[2]:

        data = st.session_state.get("lp_data", {})

        st.markdown("""
        <div class='lp-card'>
        <h3>🧠 Évaluation complète du langage</h3>
        Cette évaluation permet d'estimer les difficultés dans différents domaines du langage.
        Coche uniquement les difficultés réellement observées chez l'enfant.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class='lp-card lp-ok'>
        💾 Les modifications sur cette page sont enregistrées automatiquement.
        </div>
        """, unsafe_allow_html=True)

        evaluation = data.get("evaluation", {})

        total_difficultes = 0


        # =============================
        # ATTENTION
        # =============================

        st.markdown("""
        <div class='lp-card lp-soft'>
        <b>🎯 Attention & régulation</b>
        </div>
        """, unsafe_allow_html=True)

        attention_q = [
            "Se déconcentre rapidement",
            "Difficulté à terminer un jeu",
            "Regard difficile à maintenir",
            "Fatigue cognitive rapide",
            "Passe vite d'une activité à l'autre",
            "Difficulté à écouter une histoire",
            "Difficulté à suivre une consigne simple",
            "Besoin de répétitions fréquentes"
        ]

        # récupérer les réponses sauvegardées
        attention_vals = evaluation.get("attention", [])

        # sécurité si la taille ne correspond pas
        if len(attention_vals) != len(attention_q):
            attention_vals = [False] * len(attention_q)

        new_attention = []

        for i, q in enumerate(attention_q):

            val = st.checkbox(
                q,
                value=attention_vals[i],
                key=f"att_{child_id}_{i}"
            )

            new_attention.append(val)

            if val:
                total_difficultes += 1

        # =============================
        # COMPREHENSION
        # =============================

        st.markdown("""
        <div class='lp-card lp-soft'>
        <b>🧠 Compréhension</b>
        </div>
        """, unsafe_allow_html=True)

        comprehension_q = [
            "Ne comprend pas certaines consignes",
            "Difficulté avec phrases longues",
            "Difficulté à comprendre une histoire",
            "Ne comprend pas certaines questions",
            "Difficulté à suivre une conversation",
            "Comprend mieux avec gestes",
            "Difficulté avec notions spatiales",
            "Comprend difficilement plusieurs consignes"
        ]

        # récupérer les réponses sauvegardées
        comprehension_vals = evaluation.get("comprehension", [])

        # sécurité si la longueur ne correspond pas
        if len(comprehension_vals) != len(comprehension_q):
            comprehension_vals = [False] * len(comprehension_q)

        new_comprehension = []

        for i, q in enumerate(comprehension_q):

            val = st.checkbox(
                q,
                value=comprehension_vals[i],
                key=f"comp_{child_id}_{i}"
            )

            new_comprehension.append(val)

            if val:
                total_difficultes += 1

        # =============================
        # COMMUNICATION
        # =============================

        st.markdown("""
        <div class='lp-card lp-soft'>
        <b>💬 Communication fonctionnelle</b>
        </div>
        """, unsafe_allow_html=True)

        communication_q = [
            "Demande rarement ce qu'il veut",
            "Utilise surtout des gestes",
            "Répond difficilement aux questions",
            "Initie peu la communication",
            "Semble frustré pour s'exprimer",
            "Utilise peu de mots spontanément",
            "Difficulté à maintenir un échange",
            "Réponses souvent hors sujet"
        ]

        # récupérer les réponses sauvegardées
        communication_vals = evaluation.get("communication", [])

        # sécurité si la taille ne correspond pas
        if len(communication_vals) != len(communication_q):
            communication_vals = [False] * len(communication_q)

        new_communication = []

        for i, q in enumerate(communication_q):

            val = st.checkbox(
                q,
                value=communication_vals[i],
                key=f"com_{child_id}_{i}"
            )

            new_communication.append(val)

            if val:
                total_difficultes += 1

        # =============================
        # EXPRESSION
        # =============================

        st.markdown("""
        <div class='lp-card lp-soft'>
        <b>🗣 Expression orale</b>
        </div>
        """, unsafe_allow_html=True)

        expression_q = [
            "Utilise surtout mots isolés",
            "Phrases très courtes",
            "Prononciation difficile",
            "Vocabulaire limité",
            "Oublie certains mots",
            "Difficulté à raconter une histoire",
            "Utilise peu de verbes",
            "Difficulté à structurer une phrase"
        ]

        # récupérer les réponses sauvegardées
        expression_vals = evaluation.get("expression", [])

        # sécurité si la taille ne correspond pas
        if len(expression_vals) != len(expression_q):
            expression_vals = [False] * len(expression_q)

        new_expression = []

        for i, q in enumerate(expression_q):

            val = st.checkbox(
                q,
                value=expression_vals[i],
                key=f"exp_{child_id}_{i}"
            )

            new_expression.append(val)

            if val:
                total_difficultes += 1

        # =============================
        # MEMOIRE VERBALE
        # =============================

        st.markdown("""
        <div class='lp-card lp-soft'>
        <b>🧩 Mémoire verbale</b>
        </div>
        """, unsafe_allow_html=True)

        memoire_q = [
            "Difficulté à répéter un mot",
            "Oublie une consigne",
            "Difficulté à retenir nouveaux mots",
            "Difficulté avec comptines",
            "Difficulté à répéter une phrase",
            "Difficulté à mémoriser une histoire",
            "Difficulté à retenir une suite de mots",
            "Difficulté à rappeler une information récente"
        ]

        # récupérer les réponses sauvegardées
        memoire_vals = evaluation.get("memoire", [])

        # sécurité si la taille ne correspond pas
        if len(memoire_vals) != len(memoire_q):
            memoire_vals = [False] * len(memoire_q)

        new_memoire = []

        for i, q in enumerate(memoire_q):

            val = st.checkbox(
                q,
                value=memoire_vals[i],
                key=f"mem_{child_id}_{i}"
            )

            new_memoire.append(val)

            if val:
                total_difficultes += 1

        st.divider()

        # =============================
        # SAUVEGARDE REPONSES
        # =============================

        data["evaluation"] = {
            "attention": new_attention,
            "comprehension": new_comprehension,
            "communication": new_communication,
            "expression": new_expression,
            "memoire": new_memoire
        }

        profil = data.get("profil", {})
        prenom = profil.get("prenom")

        # ne sauvegarde QUE si profil existe
        if prenom:
            sauvegarder(data, prenom)
            st.session_state["lp_data"] = data


        # =============================
        # ANALYSE AUTOMATIQUE
        # =============================

        if data.get("evaluation"):

            profil = data.get("profil", {})
            age_reel = profil.get("age")

            if age_reel is None:
                st.warning("Veuillez renseigner l'âge dans le profil.")
                st.stop()

            total_questions = 40
            score_capacite = total_questions - total_difficultes

            ratio_difficultes = total_difficultes / total_questions

            if ratio_difficultes <= 0.10:
                niveau = "aucun retard"
                couleur = "lp-ok"
                age_langage = age_reel

            elif ratio_difficultes <= 0.25:
                niveau = "retard léger"
                couleur = "lp-soft"
                age_langage = max(age_reel - 1, 2)

            elif ratio_difficultes <= 0.45:
                niveau = "retard modéré"
                couleur = "lp-soft"
                age_langage = max(age_reel - 2, 2)

            else:
                niveau = "retard sévère"
                couleur = "lp-alert"
                age_langage = max(age_reel - 3, 2)

            retard = age_reel - age_langage

            st.session_state["niveau_langage"] = niveau
            st.session_state["score_langage"] = score_capacite
            st.session_state["age_langage"] = age_langage
            st.session_state["retard_langage"] = retard

            # =========================
            # SAUVEGARDE SESSION
            # =========================

            st.session_state["niveau_langage"] = niveau
            st.session_state["score_langage"] = score_capacite
            st.session_state["age_langage"] = age_langage
            st.session_state["retard_langage"] = retard


            # =========================
            # AFFICHAGE RESULTAT
            # =========================

            st.markdown(
                f"""
                <div class='lp-card {couleur}'>
                <h3>Résultat de l'évaluation</h3>

                Difficultés observées : {total_difficultes} / {total_questions}<br>
                Score de capacité : {score_capacite} / {total_questions}<br><br>

                Âge réel : {age_reel} ans<br>
                Âge de langage estimé : {age_langage} ans<br>
                Retard estimé : {retard} an(s)<br><br>

                Niveau estimé : <b>{niveau}</b>
                </div>
                """,
                unsafe_allow_html=True
            )

    # ==============================
    # ANALYSE
    # ==============================
    with tabs[3]:

        st.markdown("""
        <div class='lp-card'>
        <h3>🔍 Analyse du langage</h3>
        Analyse automatique basée sur l'évaluation.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class='lp-card lp-ok'>
        💾 Les modifications sur cette page sont enregistrées automatiquement.
        </div>
        """, unsafe_allow_html=True)

        niveau = st.session_state.get("niveau_langage")
        score = st.session_state.get("score_langage")

        if not niveau:

            st.markdown("""
            <div class='lp-card lp-soft'>
            Faites d'abord l'évaluation dans l'onglet Évaluation.
            </div>
            """, unsafe_allow_html=True)

        else:

            st.markdown(
                f"""
                <div class='lp-card lp-ok'>
                Score obtenu : {score} / 40
                Niveau estimé : <b>{niveau}</b>
                </div>
                """,
                unsafe_allow_html=True
            )

            # =========================
            # AGE DE LANGAGE ESTIME
            # =========================

            profil = data.get("profil", {})
            age_reel = profil.get("age")

            age_langage = st.session_state.get("age_langage")
            retard = st.session_state.get("retard_langage")

            if age_reel and age_langage is not None:

                st.markdown(
                    f"""
                    <div class='lp-card'>
                    <b>Âge réel :</b> {age_reel} ans<br>
                    <b>Âge de langage estimé :</b> {age_langage} ans<br>
                    <b>Retard estimé :</b> {retard} an(s)
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            # =========================
            # INTERPRETATION DU NIVEAU
            # =========================

            if niveau == "aucun retard":

                st.markdown("""
                <div class='lp-card lp-ok'>
                Développement du langage dans la norme.<br>
                Continuez à stimuler le langage avec des jeux et des échanges quotidiens.
                </div>
                """, unsafe_allow_html=True)

            elif niveau == "retard léger":

                st.markdown("""
                <div class='lp-card lp-soft'>
                Difficultés légères de langage.<br>
                L'enfant a surtout besoin de stimulation régulière.
                </div>
                """, unsafe_allow_html=True)

            elif niveau == "retard modéré":

                st.markdown("""
                <div class='lp-card lp-soft'>
                Difficultés modérées de langage.<br>
                Un programme structuré est recommandé.
                </div>
                """, unsafe_allow_html=True)

            elif niveau == "retard sévère":

                st.markdown("""
                <div class='lp-card lp-alert'>
                Difficultés sévères de langage.<br>
                Un accompagnement intensif est conseillé.
                </div>
                """, unsafe_allow_html=True)

            # =========================
            # PROFIL DETAILLE DU LANGAGE
            # =========================

            st.markdown("### 🧠 Profil détaillé du langage")

            # simulation des scores par domaine
            # (peut être amélioré plus tard avec les vraies réponses)

            attention = min(5, score // 6 + 1)
            comprehension = min(5, score // 7 + 1)
            communication = min(5, score // 6 + 1)
            expression = min(5, score // 5 + 1)
            memoire = min(5, score // 7 + 1)

            scores = {
                "Attention": attention,
                "Compréhension": comprehension,
                "Communication": communication,
                "Expression": expression,
                "Mémoire verbale": memoire
            }

            df = pd.DataFrame(dict(
                r=list(scores.values()),
                theta=list(scores.keys())
            ))

            fig = px.line_polar(
                df,
                r='r',
                theta='theta',
                line_close=True
            )

            fig.update_traces(fill='toself')

            fig.update_layout(
                polar=dict(
                    radialaxis=dict(
                        visible=True,
                        range=[0,5]
                    )
                ),
                showlegend=False
            )


            st.plotly_chart(fig, use_container_width=True)

            # =========================
            # ANALYSE INTELLIGENTE
            # =========================

            # Sécurité : si la variable n'existe pas encore
            domaines_faibles = st.session_state.get("domaines_faibles", [])

            analyse = analyse_intelligente_langage(domaines_faibles, age_reel, age_langage)

            st.markdown("### 🧠 Analyse intelligente du langage")

            st.markdown(f"""
            <div class='lp-card lp-soft'>
            {analyse}
            </div>
            """, unsafe_allow_html=True)


            # =========================
            # CONSEIL GLOBAL
            # =========================

            st.markdown("""
            <div class='lp-card'>
            <b>Conseil :</b><br><br>
            Le programme proposé dans l'onglet <b>Programme</b> est adapté au niveau actuel de l'enfant.
            Une progression régulière (10 à 15 minutes par jour) permet généralement des améliorations visibles sur plusieurs semaines.
            </div>
            """, unsafe_allow_html=True)

    # ==============================
    # PROGRAMME
    # ==============================
    with tabs[4]:

        # =========================
        # FATIGUE ENFANT (TDA)
        # =========================

        st.markdown("### 🧠 État de l’enfant aujourd’hui")

        fatigue = st.selectbox(
            "Niveau de fatigue",
            ["Faible", "Moyen", "Élevé"],
            index=1  # ✅ Moyen par défaut
        )

        st.session_state["fatigue"] = fatigue

        if fatigue == "Élevé":
            st.warning("⚠️ Enfant fatigué → programme réduit et pauses renforcées")
        elif fatigue == "Faible":
            st.success("✅ Enfant en forme → programme complet")

        st.write("Age langage détecté :", st.session_state.get("age_langage"))
        st.write("Niveau :", st.session_state.get("niveau_langage"))

        st.markdown("""
        <div class='lp-card lp-soft'>

        <b>🪜 Programme d'exercices</b><br><br>

        <b>1.</b> Choisis une semaine<br>
        <b>2.</b> Fais <b>1 exercice par jour</b><br>
        <b>3.</b> Quand c'est fait, <b>coche la case</b>

        <br>

        💡 Les cases cochées sont enregistrées automatiquement et permettent de suivre la progression.

        </div>
        """, unsafe_allow_html=True)

        st.markdown("🔴 Aide nécessaire | 🟠 Intermédiaire | 🟢 Niveau avancé")

        niveau = st.session_state.get("niveau_langage")

        if not niveau:

            st.markdown("""
            <div class='lp-card lp-soft'>
            Faites d'abord l'évaluation pour générer le programme.
            </div>
            """, unsafe_allow_html=True)

        else:

            st.markdown(
                f"<div class='lp-card lp-ok'><b>Niveau détecté : {niveau}</b></div>",
                unsafe_allow_html=True
            )

            # =========================
            # PROGRESSION ACTUELLE
            # =========================

            progression = data.get("progression", {})

            total = 0
            fait = 0

            for s in progression.values():
                for ex in s.values():
                    total += 1
                    if ex:
                        fait += 1

            progression_pct = 0

            if total > 0:
                progression_pct = int((fait / total) * 100)

                niveau = ajuster_difficulte_selon_progression(progression_pct, niveau)


            if progression_pct >= 70:

                st.markdown("""
                <div class='lp-card lp-ok'>
                L'enfant progresse rapidement 👍<br>
                Les exercices deviennent progressivement plus complexes.
                </div>
                """, unsafe_allow_html=True)

            elif progression_pct >= 40:

                st.markdown("""
                <div class='lp-card lp-soft'>
                L'enfant progresse régulièrement.<br>
                Le programme évolue progressivement.
                </div>
                """, unsafe_allow_html=True)

            elif progression_pct >= 20:

                st.markdown("""
                <div class='lp-card lp-soft'>
                Progression modérée.<br>
                Continuez les exercices régulièrement.
                </div>
                """, unsafe_allow_html=True)

            else:

                st.markdown("""
                <div class='lp-card lp-alert'>
                Progression lente.<br>
                La régularité est importante, même 3 minutes par jour.
                </div>
                """, unsafe_allow_html=True)

            st.markdown(
                f"""
                <div class='lp-card'>
                Progression actuelle du programme : <b>{progression_pct}%</b>
                </div>
                """,
                unsafe_allow_html=True
            )

            st.info(f"Niveau utilisé pour générer les exercices : {niveau}")

            st.markdown("""
            <div class='lp-card lp-ok'>
            🧠 Programme intelligent : adapté automatiquement aux difficultés principales de l’enfant
            </div>
            """, unsafe_allow_html=True)

            # =====================
            # FREQUENCE CONSEILLEE
            # =====================

            st.markdown("""
            <div class='lp-card'>
            <b>📅 Fréquence recommandée</b><br><br>
            5 minutes par jour<br>
            1 exercice par jour suffit.<br>
            La régularité est plus importante que la durée.
            </div>
            """, unsafe_allow_html=True)

            # =====================
            # SELECTION SEMAINE
            # =====================

            semaine_courante = st.number_input(
                "Semaine à afficher",
                min_value=1,
                max_value=24,
                value=1,
                step=1,
                key="lp_week_view"
            )

            # 🔥 Toujours utiliser le programme dynamique
            exercices = choisir_exercices_semaine(data, niveau, int(semaine_courante))

            while len(exercices) < 5:
                exercices.append("Faire un petit jeu de langage simple avec l'enfant")

            jours = ["Lundi","Mardi","Mercredi","Jeudi","Vendredi"]

            st.markdown(
                f"""
                <div class='lp-card lp-soft'>
                <b>Semaine {int(semaine_courante)}</b>
                </div>
                """,
                unsafe_allow_html=True
            )

            if "progression" not in data:
                data["progression"] = {}

            week_key = str(int(semaine_courante))

            if week_key not in data["progression"]:
                data["progression"][week_key] = {
                    "0": False,
                    "1": False,
                    "2": False,
                    "3": False,
                    "4": False
                }

            child_id = profil.get("prenom", "enfant")

            for i in range(5):

                checkbox_key = f"prog_{child_id}_{week_key}_{i}"

                exercice = exercices[i]

                fait = st.checkbox(
                    f"📅 {jours[i]} — {exercice}",
                    value=data["progression"][week_key].get(str(i), False),
                    key=checkbox_key
                )

                data["progression"][week_key][str(i)] = fait

                age_langage = st.session_state.get("age_langage")
                fiche = fiche_exercice(exercice, age_langage)

                with st.expander("📌 Voir l'exercice expliqué", expanded=False):
                    st.markdown(f"**🎯 Objectif :** {fiche['objectif']}")
                    st.markdown(f"**🧰 Matériel :** {fiche['materiel']}")
                    st.markdown("**✅ Étapes (très simple) :**")
                    for step in fiche["etapes"]:
                        st.markdown(f"- {step}")
                    if fiche.get("exemple_phrase"):
                        st.markdown(f"**🗣 Exemple de phrase :** {fiche['exemple_phrase']}")

            # ===============================
            # 📥 PDF SEMAINE (À AJOUTER ICI)
            # ===============================

            pdf_semaine = generer_pdf_fiches_semaine(
                exercices,
                semaine=int(semaine_courante),
                profil=profil
            )

            if isinstance(pdf_semaine, bytes):
                st.download_button(
                    "📥 Télécharger les fiches exercices",
                    pdf_semaine,
                    file_name="fiches.pdf",
                    mime="application/pdf"
                )
            else:
                st.error("PDF non généré")

            # =====================
            # GENERER PROGRAMME 24 SEMAINES
            # =====================

            if st.button("📄 Générer le programme complet (24 semaines)"):

                programme = {}

                for semaine in range(1, 25):
                    programme[str(semaine)] = choisir_exercices_semaine(data, niveau, semaine)

                st.session_state["programme_24_semaines"] = programme
                data["programme_24_semaines"] = programme
                sauvegarder(data, profil.get("prenom"))

            programme = data.get("programme_24_semaines") or st.session_state.get("programme_24_semaines")

            if programme:

                st.markdown("### 📘 Programme complet sur 24 semaines")

                for semaine, exercices in programme.items():

                    st.markdown(f"#### Semaine {semaine}")

                    for i in range(min(5, len(exercices))):
                        st.write(f"{jours[i]} : {exercices[i]}")

                pdf_buffer = generer_pdf_programme(
                    programme,
                    profil=profil,
                    niveau=niveau,
                    age_langage=st.session_state.get("age_langage")
                )

                if isinstance(pdf_buffer, bytes):
                    st.download_button(
                        "📥 Télécharger le programme PDF",
                        pdf_buffer,
                        file_name="programme_langage_24_semaines.pdf",
                        mime="application/pdf"
                    )
                else:
                    st.error("❌ Erreur génération PDF programme")

                # =====================
                # CALENDRIER VISUEL
                # =====================

                st.markdown("### 🗓️ Calendrier visuel du programme")

                tableau = []

                for semaine, exercices in programme.items():

                    if int(semaine) <= 8:
                        phase = "🟢 Bases"
                    elif int(semaine) <= 16:
                        phase = "🟡 Progression"
                    else:
                        phase = "🔵 Consolidation"

                    ligne = {
                        "Phase": phase,
                        "Semaine": semaine,
                        "Lundi": exercices[0] if len(exercices) > 0 else "",
                        "Mardi": exercices[1] if len(exercices) > 1 else "",
                        "Mercredi": exercices[2] if len(exercices) > 2 else "",
                        "Jeudi": exercices[3] if len(exercices) > 3 else "",
                        "Vendredi": exercices[4] if len(exercices) > 4 else "",
                        
                    }

                    tableau.append(ligne)

                df = pd.DataFrame(tableau)
                st.dataframe(df, use_container_width=True)

            # =====================
            # SAUVEGARDE
            # =====================

            prenom = data.get("profil", {}).get("prenom")

            if prenom:
                sauvegarder(data, prenom)

            # =====================
            # CONSEIL PARENTS
            # =====================

            st.markdown("""
            <div class='lp-card lp-soft'>

            <b>💡 Conseil pour les parents</b><br><br>

            • Faites simplement <b>1 exercice par jour</b><br>
            • L'exercice dure environ <b>3 à 5 minutes</b><br>
            • Encouragez l'enfant et valorisez chaque progrès

            </div>
            """, unsafe_allow_html=True)

    # ==============================
    # 🗓 SUIVI (NOUVELLE VERSION — simple, lisible, reliée au programme)
    # ==============================
    with tabs[5]:

        st.markdown("""
        <div class='lp-card' style="background:#fff7f2; border-left:6px solid #ffb38a;">

        <h3>📘 Comment utiliser le suivi</h3>

        <div style="margin-top:10px">

        <b>① 🪜 Faire les exercices</b><br>
        Dans l’onglet <b>Programme</b>, réalise les exercices proposés pour la semaine.<br>
        Quand un exercice est fait, <b>coche la case correspondante</b>.

        </div>

        <br>

        <div>

        <b>② 📊 Suivre la progression</b><br>
        Les cases cochées permettent de calculer automatiquement la <b>progression du programme</b>.

        </div>

        <br>

        <div>

        <b>③ 📝 Ajouter une séance (optionnel)</b><br>
        Le bouton <b>➕ Enregistrer une séance</b> permet simplement de garder une trace :<br>
        durée, difficulté, notes ou observations.

        </div>

        <br>

        <div style="background:#eaf7ec;padding:10px;border-radius:6px">

        💡 <b>Conseil :</b><br>
        Pour une utilisation simple, il suffit de <b>cocher les exercices réalisés dans l’onglet Programme</b>.<br>
        La page <b>Suivi</b> sert surtout à voir la progression.

        </div>

        </div>
        """, unsafe_allow_html=True)

        data = st.session_state.get("lp_data", {})
        profil = data.get("profil", {})
        prenom = (profil.get("prenom") or "").strip()
        niveau = st.session_state.get("niveau_langage")

        # =========================
        # METADONNEES LOGICIEL
        # =========================

        if "version_logiciel" not in data:
            data["version_logiciel"] = "1.0"

        if "date_creation" not in data:
            data["date_creation"] = datetime.now().strftime("%Y-%m-%d")
                    
        if not prenom:
            st.markdown("""
            <div class='lp-card lp-soft'>
            Aucun profil actif.<br>
            ➜ Va dans l’onglet 👶 <b>Profil</b> pour créer un enfant, puis sélectionne-le dans le menu en haut.
            </div>
            """, unsafe_allow_html=True)
            st.stop()

        if not niveau:
            st.markdown("""
            <div class='lp-card lp-soft'>
            Le suivi est disponible après une évaluation.<br>
            ➜ Va dans l’onglet 🧠 <b>Évaluation</b>, puis clique sur “Analyser”.
            </div>
            """, unsafe_allow_html=True)
            st.stop()

        # ------------------------------
        # stockage central (fichier + session)
        # ------------------------------
        if "suivi_seances" not in data:
            data["suivi_seances"] = []  # liste de séances

        if "progression" not in data:
            data["progression"] = {}  # { semaine: {0:True,1:False...} }

        # ------------------------------
        # sélecteurs simples
        # ------------------------------
        colA = st.columns(1)[0]

        with colA:
            semaine = st.number_input("Semaine", min_value=1, max_value=24, value=1, step=1, key="suivi_semaine")

        jours = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi"]

        # ------------------------------
        # exercices de la semaine (réutilise ta fonction anti-répétition)
        # ------------------------------
        exercices = choisir_exercices_semaine(data, niveau, int(semaine))
        while len(exercices) < 5:
            exercices.append("Jeu de langage simple")

        # ------------------------------
        # raccourci : cocher la semaine comme dans Programme
        # ------------------------------
        st.markdown(f"<div class='lp-card lp-soft'><b>📌 Exercices de la semaine {int(semaine)}</b><br>"
                    "Coche ce qui a été fait (même logique que Programme, mais ici c’est plus clair).</div>",
                    unsafe_allow_html=True)

        prog = data["progression"].setdefault(str(semaine), {str(i): False for i in range(5)})

        checks = []
        for i in range(5):
            checks.append(
                st.checkbox(
                    f"{jours[i]} — {exercices[i]}",
                    value=bool(prog.get(str(i), False)),
                    key=f"suivi_check_{prenom}_{semaine}_{i}"
                )
            )
            prog[str(i)] = bool(checks[i])

        data["progression"][str(semaine)] = prog

        # ------------------------------
        # MODE AVANCÉ (optionnel)
        # ------------------------------
        st.markdown("### 🔽 Mode avancé (optionnel)")

        if st.checkbox("Afficher le mode avancé"):

            st.markdown("""
            <div class='lp-card'>
            <b>➕ Ajouter une séance (journal)</b><br>
            Utile si tu veux garder une trace : date, exercice, notes, humeur, etc.
            </div>
            """, unsafe_allow_html=True)

            ex_choice = st.selectbox(
                "Exercice fait (prérempli depuis la semaine)",
                exercices,
                key="suivi_ex_choice"
            )

            note = st.text_area(
                "Note (facultatif)",
                placeholder="Ex: très motivé / difficile / a réussi avec aide…",
                key="suivi_note"
            )

            col1, col2 = st.columns([1, 1])

            with col1:
                humeur = st.selectbox(
                    "Humeur",
                    ["🙂 Bien", "😐 Moyen", "🙁 Difficile"],
                    index=0,
                    key="suivi_humeur"
                )

            with col2:
                aide = st.selectbox(
                    "Aide",
                    ["Autonome", "Guidé", "Très guidé"],
                    index=1,
                    key="suivi_aide"
                )

            if st.button("✅ Enregistrer la séance", key=f"btn_add_seance_{prenom}_{semaine}"):

                data["suivi_seances"].append({
                    "date": datetime.now().strftime("%Y-%m-%d"),
                    "semaine": int(semaine),
                    "jour": f"Semaine {semaine}",
                    "exercice": ex_choice,
                    "duree": "auto",
                    "humeur": humeur,
                    "aide": aide,
                    "note": note.strip()
                })

                sauvegarder(data, prenom)
                st.session_state["lp_data"] = data

                st.success("Séance enregistrée ✔")
                st.rerun()


        # ------------------------------
        # 📊 RÉSUMÉ (TOUJOURS VISIBLE)
        # ------------------------------
        st.markdown("<div class='lp-card lp-ok'><b>📊 Résumé</b></div>", unsafe_allow_html=True)

        total = 0
        fait = 0

        for w, dct in data.get("progression", {}).items():
            for k, v in dct.items():
                total += 1
                if v:
                    fait += 1

        pct = int((fait / total) * 100) if total else 0
        st.progress(pct / 100 if total else 0)

        st.markdown(
            f"<div class='lp-card'><b>Programme complété :</b> {fait} / {total} → <b>{pct}%</b></div>",
            unsafe_allow_html=True
        )

        if total > 0:
            if pct > 70:
                st.markdown("""
                <div class='lp-card lp-ok'>
                Très bons progrès 👍<br>
                Tu peux augmenter légèrement la difficulté ou la durée.
                </div>
                """, unsafe_allow_html=True)
            elif 0 < pct < 30:
                st.markdown("""
                <div class='lp-card lp-alert'>
                Progression lente.<br>
                Astuce : fais <b>2–5 min</b> mais plus souvent (régularité &gt; durée).
                </div>
                """, unsafe_allow_html=True)

        # ------------------------------
        # historique séances (journal)
        # ------------------------------
        if data.get("suivi_seances"):
            st.markdown("<div class='lp-card'><b>📋 Dernières séances</b></div>", unsafe_allow_html=True)

            df = pd.DataFrame(data["suivi_seances"])
            df = df.sort_values(by=["date", "semaine"], ascending=False).head(20)

            st.dataframe(df, use_container_width=True)

            # mini graphe : nombre de séances par semaine
            try:
                agg = pd.DataFrame(data["suivi_seances"]).groupby("semaine").size().reset_index(name="seances")
                fig = px.bar(agg, x="semaine", y="seances", title="Séances enregistrées par semaine")
                st.plotly_chart(fig, use_container_width=True)
            except Exception:
                pass

        # ------------------------------
        # évolution âge langage (optionnel)
        # ------------------------------
        st.markdown("<div class='lp-card'><b>📈 Évolution du langage</b></div>", unsafe_allow_html=True)

        if "historique_langage" not in data:
            data["historique_langage"] = []

        age_reel = profil.get("age")
        score = st.session_state.get("score_langage")

        if age_reel and score is not None:

            if score >= 25:
                age_langage = age_reel
            elif score >= 20:
                age_langage = max(age_reel - 1, 2)
            elif score >= 15:
                age_langage = max(age_reel - 2, 2)
            elif score >= 10:
                age_langage = max(age_reel - 3, 2)
            else:
                age_langage = max(age_reel - 4, 2)

            st.markdown("""
            <div class='lp-card lp-soft'>

            <b>📈 Suivi de l'âge de langage</b><br><br>

            Ce bouton permet d'enregistrer l'évolution de l'âge de langage dans le temps.

            💡 Utilisez-le uniquement après une nouvelle évaluation du langage  
            (par exemple tous les 2 à 3 mois).

            Cela permet de suivre les progrès de l'enfant au fil du programme.

            </div>
""", unsafe_allow_html=True)

            if st.button("📌 Enregistrer un point (âge de langage)", key=f"btn_hist_lang_{prenom}"):
                data["historique_langage"].append({
                    "date": datetime.now().strftime("%Y-%m-%d"),
                    "age_langage": int(age_langage)
                })
                sauvegarder(data, prenom)
                st.session_state["lp_data"] = data
                st.success("Point enregistré ✔")
                st.rerun()

        # ------------------------------
        # sauvegarde finale (progression + suivi)
        # ------------------------------
        st.session_state["lp_data"] = data
        sauvegarder(data, prenom)

    # ==============================
    # TABLEAU DE BORD ENFANT
    # ==============================
    with tabs[6]:

        st.markdown("""
        <div class='lp-card'>
        <h3>📊 Tableau de bord enfant</h3>
        Suivi global du développement du langage.
        </div>
        """, unsafe_allow_html=True)

        profil = data.get("profil", {})

        if not profil:

            st.markdown("""
            <div class='lp-card lp-soft'>
            Renseignez d'abord le profil de l'enfant.
            </div>
            """, unsafe_allow_html=True)

        else:

            prenom = profil.get("prenom", "Enfant")
            age = profil.get("age")

            score = st.session_state.get("score_langage", 0)
            niveau = st.session_state.get("niveau_langage", "non évalué")

            st.markdown(
                f"<div class='lp-card'><b>👶 Enfant :</b> {prenom}</div>",
                unsafe_allow_html=True
            )

            if age:
                st.markdown(
                    f"<div class='lp-card'><b>Âge :</b> {age} ans</div>",
                    unsafe_allow_html=True
                )

            if score:

                st.markdown(
                    f"<div class='lp-card'><b>Score langage :</b> {score} / 40</div>",
                    unsafe_allow_html=True
                )

                st.markdown(
                    f"<div class='lp-card'><b>Niveau estimé :</b> {niveau}</div>",
                    unsafe_allow_html=True
                )

            # =========================
            # CALCUL PROGRESSION EXERCICES
            # =========================

            progression = data.get("progression", {})

            total = 0
            fait = 0

            for semaine in progression.values():

                for ex in semaine.values():

                    total += 1

                    if ex:
                        fait += 1

            progression_exercices = 0

            if total > 0:
                progression_exercices = int((fait / total) * 100)

            # =========================
            # SCORE GLOBAL PROGRESSION
            # =========================

            score_eval_pct = (score / 40) * 100
            score_global = int((score_eval_pct * 0.6) + (progression_exercices * 0.4))

            # couleur selon score
            if score_global < 40:
                couleur = "#ff6b6b"
                message = "Progression encore fragile"
            elif score_global < 70:
                couleur = "#f7b267"
                message = "Progression encourageante"
            else:
                couleur = "#6bcf8b"
                message = "Bonne progression 👍"

            st.markdown("""
            <div class='lp-card'>
            <h3>📈 Indice global de progression</h3>
            </div>
            """, unsafe_allow_html=True)

            st.progress(score_global / 100)

            st.markdown(
                f"""
                <div class='lp-card' style="border-left:6px solid {couleur};">
                Score actuel : <b>{score_global} / 100</b><br>
                {message}
                </div>
                """,
                unsafe_allow_html=True
            )

            st.markdown("""
            <div class='lp-card lp-soft'>

            <b>ℹ️ Comment est calculé cet indice ?</b><br><br>

            L'indice global combine deux éléments :

            • le résultat de l’évaluation du langage  
            • la progression dans les exercices du programme

            L’évaluation représente environ <b>60 %</b> du score  
            et la progression dans le programme environ <b>40 %</b>.

            Cet indice permet de visualiser l’évolution globale de l’enfant
            au fil du programme.

            </div>
            """, unsafe_allow_html=True)
                        
            # =========================
            # DETECTION DOMAINES FAIBLES
            # =========================

            evaluation = data.get("evaluation", {})

            domaines = {
                "Attention": evaluation.get("attention", []),
                "Compréhension": evaluation.get("comprehension", []),
                "Communication": evaluation.get("communication", []),
                "Expression": evaluation.get("expression", []),
                "Mémoire verbale": evaluation.get("memoire", [])
            }

            domaines_faibles = []

            for domaine, valeurs in domaines.items():

                if valeurs:

                    nb = sum(valeurs)
                    total_q = len(valeurs)

                    if total_q > 0:

                        ratio = nb / total_q

                        if ratio >= 0.4:
                            domaines_faibles.append(domaine)

            # affichage

            if domaines_faibles:

                st.markdown("""
                <div class='lp-card lp-soft'>
                <b>⚠️ Domaines à renforcer</b>
                </div>
                """, unsafe_allow_html=True)

                for d in domaines_faibles:

                    st.markdown(
                        f"<div class='lp-card'>• {d}</div>",
                        unsafe_allow_html=True
                    )

            else:

                st.markdown("""
                <div class='lp-card lp-ok'>
                Aucun domaine particulièrement faible détecté.
                </div>
                """, unsafe_allow_html=True)

            # =========================
            # RECOMMANDATIONS ADAPTATIVES
            # =========================

            recommandations = []

            if "Compréhension" in domaines_faibles:

                recommandations.append(
                    "utiliser des phrases simples et accompagner les consignes de gestes"
                )

            if "Expression" in domaines_faibles:

                recommandations.append(
                    "encourager l'enfant à répéter des mots et former de petites phrases"
                )

            if "Communication" in domaines_faibles:

                recommandations.append(
                    "multiplier les échanges verbaux dans les activités quotidiennes"
                )

            if "Mémoire verbale" in domaines_faibles:

                recommandations.append(
                    "faire des jeux de répétition de mots et de petites phrases"
                )

            if "Attention" in domaines_faibles:

                recommandations.append(
                    "privilégier des exercices très courts (3 à 5 minutes)"
                )

            if not recommandations:

                recommandations.append(
                    "continuer les activités de langage régulièrement"
                )

            # =========================
            # PDF BILAN AUTOMATIQUE
            # =========================

            st.markdown("### 💡 Conseils personnalisés")

            for c in conseils_personnalises(domaines_faibles):
                st.write("•", c)


            st.markdown("""
            <div class='lp-card'>
            <h3>📄 Générer un bilan PDF</h3>
            Un résumé du développement du langage peut être exporté.
            </div>
            """, unsafe_allow_html=True)

            rec_text = ""

            for r in recommandations:
                rec_text += f"• {r}\n"

            domaines_text = ""

            for d in domaines_faibles:
                domaines_text += f"• {d}\n"

            age_langage = st.session_state.get("age_langage")

            # =========================
            # DATE DU BILAN
            # =========================

            date_bilan = datetime.now().strftime("%d/%m/%Y")

            # =========================
            # ANALYSE AUTOMATIQUE
            # =========================

            analyse = ""

            if niveau == "retard sévère":

                analyse = """
L’évaluation indique un retard important du développement du langage.
Le programme proposé vise à renforcer les bases du langage :
- compréhension
- vocabulaire
- communication verbale
"""

            elif niveau == "retard modéré":

                analyse = """
Le développement du langage présente un retard modéré.
Le programme vise à enrichir progressivement le vocabulaire
et améliorer la construction des phrases.
"""

            elif niveau == "retard léger":

                analyse = """
Le langage est globalement présent mais certaines compétences
peuvent être renforcées pour consolider la communication.
"""

            else:

                analyse = """
Le développement du langage est cohérent avec l'âge de l'enfant.
Les exercices proposés visent à stimuler et enrichir le langage.
"""

            # =========================
            # CONCLUSION AUTOMATIQUE
            # =========================

            if niveau == "retard sévère":

                conclusion = """
Conclusion

Les résultats suggèrent un retard important du développement du langage.
Un accompagnement régulier est recommandé afin de renforcer les bases du langage
et favoriser l’émergence de la communication verbale.
"""

            elif niveau == "retard modéré":

                conclusion = """
Conclusion

Les résultats indiquent un retard modéré du développement du langage.
Des activités régulières peuvent permettre d'améliorer progressivement
la compréhension et l'expression verbale.
"""

            elif niveau == "retard léger":

                conclusion = """
Conclusion

Le développement du langage présente quelques fragilités.
Une stimulation régulière du vocabulaire et de la communication
peut aider l’enfant à consolider ses compétences.
"""

            else:

                conclusion = """
Conclusion

Le développement du langage est globalement adapté à l’âge de l’enfant.
La poursuite des échanges verbaux et des activités de langage est recommandée.
"""


            # =========================
            # TEXTE DU BILAN
            # =========================

            bilan = f"""
BILAN LANGAGE – PROGRAMME LANGAGE PAS À PAS

Date du bilan : {date_bilan}


Informations enfant
-------------------

Prénom : {prenom}
Âge : {age} ans
Âge de langage estimé : {age_langage} ans


Résultat de l'évaluation
------------------------

Score langage : {score} / 40
Niveau estimé : {niveau}


Analyse du développement du langage
-----------------------------------

{analyse}


Domaines à renforcer
--------------------

{domaines_text if domaines_text else "Aucun domaine faible détecté."}


Progression dans le programme
-----------------------------

Exercices réalisés : {progression_exercices} %
Score global progression : {score_global} / 100


Recommandations personnalisées
------------------------------

{rec_text}


{conclusion}


Programme Langage Pas à Pas

Programme personnalisé sur 24 semaines.
1 exercice par jour – environ 5 minutes.

Programme généré automatiquement par le logiciel
Langage Pas à Pas – programme éducatif de stimulation du langage.


Ce bilan est fourni à titre éducatif et ne remplace pas
l’évaluation réalisée par un professionnel de santé.
"""

            bilan_pdf = generer_pdf_bilan(bilan)

            # =========================
            # BOUTON TELECHARGEMENT PDF
            # =========================

            if bilan_pdf is not None and bilan_pdf != "":

                st.download_button(
                    "📥 Télécharger le bilan PDF",
                    data=bilan_pdf,
                    file_name="bilan_langage.pdf",
                    mime="application/pdf"
                )

            else:
                st.info("Le bilan PDF n'a pas encore été généré.")


            # ⭐ AJOUT DU GUIDE PARENT JUSTE EN DESSOUS

            pdf_guide = generer_pdf_guide()

            st.download_button(
                "📥 Télécharger le guide parent",
                pdf_guide,
                file_name="guide_langage.pdf",
                mime="application/pdf"
            )



            # =========================
            # EXPORT DONNÉES ENFANT
            # =========================

            st.markdown("""
            <div class='lp-card'>
            <h3>💾 Exporter les données de l'enfant</h3>
            Télécharger la sauvegarde complète afin de conserver
            toutes les informations et le suivi du programme.
            </div>
            """, unsafe_allow_html=True)

            prenom = profil.get("prenom")

            if prenom:

                fichiers = os.listdir(DOSSIER_DATA)

                fichier_enfant = None

                for f in fichiers:
                    if f.startswith(f"suivi_{prenom.lower()}"):
                        fichier_enfant = f
                        break

                if fichier_enfant:

                    path = os.path.join(DOSSIER_DATA, fichier_enfant)

                    with open(path, "rb") as file:

                        st.download_button(
                            "📥 Télécharger la sauvegarde complète",
                            file,
                            file_name=fichier_enfant,
                            mime="application/json"
                        )

        # ==============================
        # CONSEILS
        # ==============================
        with tabs[7]:

            st.markdown("""
            <div class='lp-card'>
            <h3>💡 Conseils pour aider l’enfant au quotidien</h3>

            <br>

            <b>Langage et compréhension</b><br><br>
            • parler lentement et clairement<br>
            • faire des phrases courtes<br>
            • donner une consigne à la fois<br>
            • montrer en même temps que l’on parle<br>
            • faire répéter sans mettre l’enfant en échec

            <br><br>

            <b>Pour aider la dysphasie / le langage</b><br><br>
            • jouer avec les syllabes<br>
            • répéter des mots simples puis plus longs<br>
            • utiliser des images<br>
            • encourager les phrases courtes puis plus longues<br>
            • reformuler correctement sans gronder

            <br><br>

            <b>Préparer lecture et écriture</b><br><br>
            • jouer avec les sons des mots<br>
            • reconnaître des syllabes simples<br>
            • écouter des comptines et rimes<br>
            • tracer des lignes, boucles, formes<br>
            • manipuler livres, lettres, images

            <br><br>

            <b>Loisirs utiles</b><br><br>
            • lecture quotidienne avec un adulte<br>
            • comptines et chansons<br>
            • puzzles<br>
            • jeux de société simples<br>
            • dessin et coloriage<br>
            • musique<br>
            • natation ou activités motrices douces

            <br><br>

            <b>Alimentation</b><br><br>
            Une alimentation équilibrée aide le développement général de l’enfant :
            fruits, légumes, œufs, poissons gras, légumineuses, bonnes matières grasses.

            <br><br>

            <b>Important</b><br><br>
            Les vitamines ou compléments ne doivent pas être donnés sans avis d’un professionnel de santé.
            Ce logiciel est un soutien éducatif et ne remplace pas l’orthophoniste, le neuropédiatre
            ou un autre professionnel.

            </div>
            """, unsafe_allow_html=True)

        # ==============================
        # A PROPOS
        # ==============================
        with tabs[8]:

            st.markdown("### ℹ️ Informations")

            st.write("Version du logiciel :", VERSION_LOGICIEL)

            st.markdown("""
            <div class='lp-card'>

            <h3>ℹ️ À propos de Langage Pas à Pas</h3>

            <br>

            <b>Langage Pas à Pas</b> est un programme éducatif conçu pour aider
            les parents à accompagner le développement du langage de leur enfant.

            <br><br>

            Le logiciel permet de :

            <br><br>

            • réaliser une évaluation simple du langage<br>
            • estimer l’âge de langage de l’enfant<br>
            • identifier les domaines à renforcer<br>
            • générer un programme personnalisé sur 24 semaines<br>
            • suivre la progression semaine après semaine<br>
            • obtenir un bilan automatique

            <br><br>

            Les exercices sont courts, progressifs et adaptés
            au niveau de l’enfant.

            <br><br>

            <b>Important :</b><br>
            Ce programme est un outil éducatif destiné aux familles.
            Il ne remplace pas l’évaluation réalisée par un professionnel de santé.

            <br><br>

            © 2026 – Langage Pas à Pas

            </div>
            """, unsafe_allow_html=True)


            st.markdown("""
            <div style="text-align:center;
            font-size:12px;
            color:#777;
            margin-top:30px;">

            Logiciel éducatif – tous droits réservés<br>
            Ce programme ne remplace pas l’évaluation d’un professionnel de santé.

            </div>
            """, unsafe_allow_html=True)


        # =========================
        # 💾 CHARGEMENT DONNÉES
        # =========================

        if "lp_data" not in st.session_state:

            prenom = st.session_state.get("prenom")

            if prenom:
                data = charger(prenom)
            else:
                data = {}

            st.session_state["lp_data"] = data

        data = st.session_state["lp_data"]


        # =========================
        # 📚 LECTURE PAS À PAS
        # =========================

        with tab_lecture:

            # =========================
            # 🔐 NIVEAU LECTURE SYNCHRONISÉ AVEC L'ÉVALUATION
            # =========================

            niveau_source = st.session_state.get("niveau_langage", "retard modéré")
            niveau_source = str(niveau_source).lower().strip()

            if niveau_source in ["retard sévère", "severe", "sévère"]:
                niveau = "severe"
            elif niveau_source in ["retard léger", "leger", "léger"]:
                niveau = "leger"
            else:
                niveau = "modere"

            # =========================
            # 📚 PROGRAMME AUTO
            # =========================

            programme = programme_lecture(niveau)

            # =========================
            # 💾 SAUVEGARDE LECTURE PAR ENFANT
            # =========================

            profil = data.get("profil", {})
            prenom = profil.get("prenom", "enfant")

            if "lecture_progression" not in data:
                data["lecture_progression"] = {}

            if niveau not in data["lecture_progression"]:
                data["lecture_progression"][niveau] = {
                    "lettres": {},
                    "syllabes": {},
                    "mots": {},
                    "phrases": {}
                }

            lecture_data = data["lecture_progression"][niveau]

            # =========================
            # 📊 PROGRESSION GLOBALE
            # =========================

            progression_lecture = 0
            prenom = data.get("profil", {}).get("prenom", "default")

            if data.get("lettres_validees_" + prenom, False):
                progression_lecture += 25

            if data.get("syllabes_valides_" + prenom, False):
                progression_lecture += 25

            if data.get("mots_valides_" + prenom, False):
                progression_lecture += 25

            if data.get("phrases_valides_" + prenom, False):
                progression_lecture += 25

            st.markdown("### 📊 Progression globale")
            st.progress(progression_lecture / 100)
            st.caption(f"{progression_lecture}% du programme complété")

            if st.button("💾 Sauvegarder ma progression"):
                if prenom:
                    sauvegarder(data, prenom)
                    st.success("✅ Progression sauvegardée")

            if progression_lecture == 0:
                st.info("👉 Commencez par les lettres pour démarrer le programme")
            elif progression_lecture < 100:
                st.info("👉 Continuez les exercices pour progresser")
            else:
                st.success("🎉 Programme terminé ! Bravo !")

            # =========================
            # 🧠 INTRO + MÉTHODE
            # =========================

            st.markdown(f"""
            <div class='lp-card lp-ok'>
            <h2>📚 Lecture Pas à Pas</h2>

            Niveau actuel : <b>{niveau.upper()}</b>

            Méthode progressive :
            1️⃣ Lettres → 2️⃣ Syllabes → 3️⃣ Mots → 4️⃣ Phrases

            👉 Programme adapté automatiquement à l’enfant
            </div>
            """, unsafe_allow_html=True)

            # =========================
            # 🎯 ADAPTATION GLOBALE LECTURE
            # =========================

            if niveau == "severe":
                syllabes_affichage = SYLLABES_COMPLETES[:20]
                mots_affichage = MOTS_COMPLETS[:15]
                phrases_affichage = PHRASES_COMPLETES[:5]

            elif niveau == "modere":
                syllabes_affichage = SYLLABES_COMPLETES[:60]
                mots_affichage = MOTS_COMPLETS[:50]
                phrases_affichage = PHRASES_COMPLETES[:20]

            else:
                syllabes_affichage = SYLLABES_COMPLETES
                mots_affichage = MOTS_COMPLETS
                phrases_affichage = PHRASES_COMPLETES


            # =========================
            # 📑 SOUS-ONGLETS
            # =========================

            sous_tabs = st.tabs([
                "🔤 Lettres",
                "🔡 Syllabes",
                "🧩 Mots",
                "🗣 Phrases",
                "💡 Conseils"
            ])

            # =========================
            # 🔤 LETTRES
            # =========================

            with sous_tabs[0]:

                st.markdown("### 🔤 Lettres")

                # 🎯 seuil adapté au niveau
                if niveau == "severe":
                    seuil = 3
                elif niveau == "modere":
                    seuil = 5
                else:
                    seuil = 8

                if niveau == "severe":
                    st.success("👉 Étape principale pour ce niveau")
                else:
                    st.info("👉 Révision importante des bases")

                # 💾 récupération données
                if "lecture_lettres" not in data:
                    data["lecture_lettres"] = {}

                lettres_data = data["lecture_lettres"]

                # 👇 prénom AVANT tout
                prenom = data.get("profil", {}).get("prenom", "default")

                # =========================
                # 🎯 ADAPTATION NOMBRE DE LETTRES
                # =========================

                if niveau == "severe":
                    lettres_affichage = ALPHABET[:8]
                elif niveau == "modere":
                    lettres_affichage = ALPHABET[:15]
                else:
                    lettres_affichage = ALPHABET

                # 👇 AJOUT SIMPLE
                if st.checkbox("🔎 Voir toutes les lettres"):
                    lettres_affichage = ALPHABET

                # =========================
                # ✅ FORMULAIRE (ANTI LAG)
                # =========================

                with st.form("form_lettres"):

                    reussite_lettres = 0

                    for i, lettre in enumerate(lettres_affichage):

                        st.markdown(f"""
                        <div style="background:#fff7f2;padding:10px;margin-bottom:8px;border-radius:10px;border-left:5px solid #ffb38a;">
                        <b style="font-size:22px;">{lettre['lettre']}</b> →

                        <b>Script :</b> {lettre['script']} |
                        <b>Cursive :</b> {lettre['cursive']} |
                        🔊 <b>Son :</b> {lettre['son']}
                        </div>
                        """, unsafe_allow_html=True)

                        key_data = str(i)

                        checked = st.checkbox(
                            f"✔ Lettre {lettre['lettre']} reconnue",
                            value=lettres_data.get(key_data, False),
                            key=f"lettre_{prenom}_{niveau}_{i}"
                        )

                        lettres_data[key_data] = checked

                        if checked:
                            reussite_lettres += 1

                    submit = st.form_submit_button("✅ Valider")

                # =========================
                # 💾 SAUVEGARDE (UNE SEULE FOIS)
                # =========================

                if submit:
                    data["lecture_lettres"] = lettres_data
                    st.session_state["lp_data"] = data

                    with st.spinner("💾 Enregistrement..."):
                        if prenom:
                            sauvegarder(data, prenom)

                    st.success("✅ Progression bien enregistrée !")

                # =========================
                # 🎯 VALIDATION PAR ENFANT
                # =========================

                if reussite_lettres >= seuil and not data.get("lettres_validees_" + prenom, False):

                    st.balloons()

                    st.success("🎉 Bravo !!! Tu progresses super bien 💖")

                    st.markdown("""
                    <div style="
                    background:#eaf7f0;
                    padding:15px;
                    border-radius:12px;
                    text-align:center;
                    font-size:18px;
                    ">
                    🌟 Continue comme ça, tu es incroyable ! 🌟
                    </div>
                    """, unsafe_allow_html=True)

                    data["lettres_validees_" + prenom] = True
                    st.session_state["lp_data"] = data

                    if prenom:
                        sauvegarder(data, prenom)

                # =========================
                # 📊 INFOS
                # =========================

                st.info("👉 Dire le son avec l’enfant et répéter 3 fois")
                st.caption(f"Progression : {reussite_lettres} / {seuil}")

                # =========================
                # 📄 PDF
                # =========================

                pdf_buffer = generer_pdf_lecture(programme, "lettres")

                st.download_button(
                    "📥 Télécharger PDF Lettres",
                    data=pdf_buffer,
                    file_name="lettres.pdf",
                    mime="application/pdf"
                )

            # =========================
            # 🔡 SYLLABES
            # =========================

            with sous_tabs[1]:

                st.markdown("### 🔡 Syllabes")

                # 🎯 seuil adapté au niveau
                if niveau == "severe":
                    seuil = 5
                elif niveau == "modere":
                    seuil = 12
                else:
                    seuil = 20

                if niveau in ["severe", "modere"]:
                    st.success("👉 Étape adaptée à ce niveau")
                else:
                    st.info("👉 Révision utile même en niveau avancé")

                # =========================
                # 🎯 LISTE COMPLÈTE DE SYLLABES
                # =========================

                syllabes_base = SYLLABES_COMPLETES

                # =========================
                # 🎯 ADAPTATION SELON LE NIVEAU
                # =========================

                if niveau == "severe":
                    syllabes_affichage = syllabes_base[:30]
                elif niveau == "modere":
                    syllabes_affichage = syllabes_base[:100]
                else:
                    syllabes_affichage = syllabes_base

                # 💾 récupération données
                if "lecture_syllabes" not in data:
                    data["lecture_syllabes"] = {}

                syllabes_data = data["lecture_syllabes"]

                # 👇 prénom AVANT tout
                prenom = data.get("profil", {}).get("prenom", "default")

                # =========================
                # ✅ FORMULAIRE (ANTI LAG)
                # =========================

                with st.form("form_syllabes"):

                    reussite_syllabes = 0

                    for i, s in enumerate(syllabes_affichage):

                        st.markdown(f"""
                        <div style="background:#f2fbff;padding:10px;margin-bottom:6px;border-radius:10px;border-left:5px solid #8ad4ff;">
                        🔤 <b>{s}</b>
                        <br><small>Lire la syllabe puis la répéter</small>
                        </div>
                        """, unsafe_allow_html=True)

                        key_data = str(i)

                        checked = st.checkbox(
                            f"✔ {s} lu correctement",
                            value=syllabes_data.get(key_data, False),
                            key=f"syllabe_{prenom}_{niveau}_{i}"
                        )

                        syllabes_data[key_data] = checked

                        if checked:
                            reussite_syllabes += 1

                    submit = st.form_submit_button("✅ Valider")

                # =========================
                # 💾 SAUVEGARDE (UNE SEULE FOIS)
                # =========================

                if submit:
                    data["lecture_syllabes"] = syllabes_data
                    st.session_state["lp_data"] = data

                    with st.spinner("💾 Enregistrement..."):
                        if prenom:
                            sauvegarder(data, prenom)

                    st.success("✅ Progression bien enregistrée !")

                # =========================
                # 🎯 VALIDATION PAR ENFANT
                # =========================

                if reussite_syllabes >= seuil and not data.get("syllabes_valides_" + prenom, False):

                    st.balloons()

                    st.success("🎉 Bravo !!! Tu progresses super bien 💖")

                    st.markdown("""
                    <div style="
                    background:#eaf7f0;
                    padding:15px;
                    border-radius:12px;
                    text-align:center;
                    font-size:18px;
                    ">
                    🌟 Continue comme ça, tu es incroyable ! 🌟
                    </div>
                    """, unsafe_allow_html=True)

                    data["syllabes_valides_" + prenom] = True
                    st.session_state["lp_data"] = data

                    if prenom:
                        sauvegarder(data, prenom)

                # =========================
                # 📊 MÉTHODE
                # =========================

                st.info("👉 Dire le son de chaque lettre")
                st.info("👉 Fusionner les sons : b + a = ba")
                st.info("👉 Répéter chaque syllabe 3 fois")
                st.info("👉 Lire lentement puis normalement")
                st.caption(f"Progression : {reussite_syllabes} / {seuil}")

                # =========================
                # 📄 PDF
                # =========================

                pdf_buffer = generer_pdf_lecture(programme, "syllabes")

                st.download_button(
                    "📥 Télécharger PDF Syllabes",
                    data=pdf_buffer,
                    file_name="syllabes.pdf",
                    mime="application/pdf"
                )

            # =========================
            # 🧩 MOTS
            # =========================

            with sous_tabs[2]:

                st.markdown("### 🧩 Mots")

                # 🎯 seuil adapté au niveau
                if niveau == "severe":
                    seuil = 5
                elif niveau == "modere":
                    seuil = 12
                else:
                    seuil = 20

                if niveau in ["modere", "leger"]:
                    st.success("👉 Étape adaptée")
                else:
                    st.info("👉 À introduire progressivement")

                # =========================
                # 🎯 LISTE COMPLÈTE DE MOTS
                # =========================

                mots_base = MOTS_COMPLETS

                # =========================
                # 🎯 ADAPTATION SELON LE NIVEAU
                # =========================

                if niveau == "severe":
                    mots_affichage = mots_base[:20]
                elif niveau == "modere":
                    mots_affichage = mots_base[:80]
                else:
                    mots_affichage = mots_base

                # 💾 récupération données
                if "lecture_mots" not in data:
                    data["lecture_mots"] = {}

                mots_data = data["lecture_mots"]

                # 👇 prénom AVANT tout
                prenom = data.get("profil", {}).get("prenom", "default")

                # =========================
                # ✅ FORMULAIRE (ANTI LAG)
                # =========================

                with st.form("form_mots"):

                    reussite_mots = 0

                    for i, mot in enumerate(mots_affichage):

                        st.markdown(f"""
                        <div style="background:#f7fff2;padding:10px;margin-bottom:6px;border-radius:10px;border-left:5px solid #9cff8a;">
                        📖 <b>{mot}</b>
                        <br><small>Lire puis expliquer</small>
                        </div>
                        """, unsafe_allow_html=True)

                        key_data = str(i)

                        checked = st.checkbox(
                            f"✔ {mot} lu correctement",
                            value=mots_data.get(key_data, False),
                            key=f"mot_{prenom}_{niveau}_{i}"
                        )

                        mots_data[key_data] = checked

                        if checked:
                            reussite_mots += 1

                    submit = st.form_submit_button("✅ Valider")

                # =========================
                # 💾 SAUVEGARDE (UNE SEULE FOIS)
                # =========================

                if submit:
                    data["lecture_mots"] = mots_data
                    st.session_state["lp_data"] = data

                    with st.spinner("💾 Enregistrement..."):
                        if prenom:
                            sauvegarder(data, prenom)

                    st.success("✅ Progression bien enregistrée !")

                # =========================
                # 🎯 VALIDATION PAR ENFANT
                # =========================

                if submit and reussite_mots >= seuil and not data.get("mots_valides_" + prenom, False):

                    st.balloons()

                    st.success("🎉 Bravo !!! Tu progresses super bien 💖")

                    st.markdown("""
                    <div style="
                    background:#eaf7f0;
                    padding:15px;
                    border-radius:12px;
                    text-align:center;
                    font-size:18px;
                    ">
                    🌟 Continue comme ça, tu es incroyable ! 🌟
                    </div>
                    """, unsafe_allow_html=True)

                    data["mots_valides_" + prenom] = True
                    st.session_state["lp_data"] = data

                    if prenom:
                        sauvegarder(data, prenom)

                # =========================
                # 📊 MÉTHODE
                # =========================

                st.info("👉 Découper le mot en syllabes : ex. ma-man")
                st.info("👉 Lire lentement puis normalement")
                st.info("👉 Expliquer ce que veut dire le mot")
                st.info("👉 Utiliser le mot dans une petite phrase")
                st.caption(f"Progression : {reussite_mots} / {seuil}")

                # =========================
                # 📄 PDF
                # =========================

                pdf_buffer = generer_pdf_lecture(programme, "mots")

                st.download_button(
                    "📥 Télécharger PDF Mots",
                    data=pdf_buffer,
                    file_name="mots.pdf",
                    mime="application/pdf"
                )

            # =========================
            # 🗣 PHRASES
            # =========================

            with sous_tabs[3]:

                st.markdown("### 🗣 Phrases")

                # 🎯 seuil adapté au niveau
                if niveau == "severe":
                    seuil = 3
                elif niveau == "modere":
                    seuil = 8
                else:
                    seuil = 15

                if niveau == "leger":
                    st.success("👉 Étape principale")
                else:
                    st.info("👉 Niveau avancé (accessible progressivement)")

                # =========================
                # 🎯 LISTE COMPLÈTE DE PHRASES
                # =========================

                phrases_base = [
                    # phrases très simples
                    "papa mange",
                    "maman lit",
                    "le chat dort",
                    "le chien court",
                    "bébé joue",
                    "léo saute",
                    "lina chante",
                    "le soleil brille",
                    "la pluie tombe",
                    "le bébé dort",

                    # phrases simples
                    "papa mange une pomme",
                    "maman lit un livre",
                    "le chat dort sur le lit",
                    "le chien court dans le jardin",
                    "le bébé joue avec un jouet",
                    "la voiture roule vite",
                    "le lapin mange une carotte",
                    "la fille tient un ballon",
                    "le garçon joue dehors",
                    "le bateau flotte sur l’eau",

                    # compréhension
                    "la petite fille lit calmement",
                    "le grand chien regarde la fenêtre",
                    "maman coupe un bon gâteau",
                    "le petit garçon boit du lait",
                    "le canard nage dans la rivière",
                    "la maîtresse montre un cahier",
                    "la fleur pousse dans le jardin",
                    "la lune brille dans le ciel",
                    "le cheval court dans le champ",
                    "la poule marche dans la cour",

                    # phrases riches
                    "le petit chat gris dort sur le canapé",
                    "la voiture rouge roule sur la route",
                    "les enfants jouent ensemble dans le parc",
                    "le garçon ouvre la porte de la maison",
                    "la maman prépare un gâteau au chocolat",
                    "la maîtresse lit une histoire aux élèves",
                    "le lapin blanc saute dans l’herbe verte",
                    "le vent pousse les nuages dans le ciel",
                    "la fillette range ses jouets dans sa chambre",
                    "le chien noir court après la balle rouge",

                    # phrases longues
                    "la petite fille regarde un papillon dans le jardin",
                    "le garçon écrit son prénom sur un cahier bleu",
                    "la maman prépare le repas dans la cuisine",
                    "le soleil chauffe le sable de la plage",
                    "les oiseaux chantent dans les arbres du parc",
                    "la voiture s’arrête devant la maison jaune",
                    "le petit garçon met son cartable sur la chaise",
                    "le lapin mange tranquillement sa carotte orange",
                    "la maîtresse explique la leçon aux enfants",
                    "le bateau avance doucement sur la rivière"
                ]

                # =========================
                # 🎯 ADAPTATION NIVEAU
                # =========================

                if niveau == "severe":
                    phrases_affichage = phrases_base[:8]
                elif niveau == "modere":
                    phrases_affichage = phrases_base[:25]
                else:
                    phrases_affichage = phrases_base

                # =========================
                # 💾 DATA
                # =========================

                if "lecture_phrases" not in data:
                    data["lecture_phrases"] = {}

                phrases_data = data["lecture_phrases"]

                prenom = data.get("profil", {}).get("prenom", "default")

                # =========================
                # 🎯 PHRASE DU MOMENT
                # =========================

                phrase_focus = next(
                    (phrases_affichage[i] for i in range(len(phrases_affichage))
                    if not phrases_data.get(str(i), False)),
                    phrases_affichage[0] if phrases_affichage else ""
                )

                st.markdown(f"""
                <div style="background:#fff7f2;padding:15px;border-radius:12px;border-left:6px solid #ffb38a;">

                <b>🎯 Phrase du moment :</b><br><br>

                <h3>{phrase_focus}</h3>

                👉 Lire lentement<br>
                👉 Comprendre<br>
                👉 Reformuler

                </div>
                """, unsafe_allow_html=True)

                # =========================
                # ✅ FORMULAIRE
                # =========================

                with st.form("form_phrases"):

                    reussite_phrases = 0

                    for i, p in enumerate(phrases_affichage):

                        mots = p.split()

                        sujet = mots[0] if len(mots) > 0 else ""
                        action = mots[1] if len(mots) > 1 else ""

                        st.markdown(f"""
                        <div style="background:#fff2fb;padding:10px;margin-bottom:6px;border-radius:10px;border-left:5px solid #ff8ad4;">
                        🗣 <b>{p}</b>

                        <br><small>Lire, comprendre, reformuler</small>

                        <div style="font-size:13px; color:#555; margin-top:6px;">
                        👉 Qui ? → {sujet}<br>
                        👉 Action ? → {action}
                        </div>

                        </div>
                        """, unsafe_allow_html=True)

                        key_data = str(i)

                        checked = st.checkbox(
                            f"✔ Phrase comprise",
                            value=phrases_data.get(key_data, False),
                            key=f"phrase_{prenom}_{niveau}_{i}"
                        )

                        phrases_data[key_data] = checked

                        if checked:
                            reussite_phrases += 1

                    submit = st.form_submit_button("✅ Valider")

                # =========================
                # 💾 SAUVEGARDE
                # =========================

                if submit:
                    data["lecture_phrases"] = phrases_data
                    st.session_state["lp_data"] = data

                    with st.spinner("💾 Enregistrement..."):
                        if prenom:
                            sauvegarder(data, prenom)

                    st.success("✅ Progression bien enregistrée !")

                # =========================
                # 🎯 VALIDATION
                # =========================

                if submit and reussite_phrases >= seuil and not data.get("phrases_valides_" + prenom, False):

                    st.balloons()

                    st.success("🎉 Bravo !!! Tu progresses super bien 💖")

                    st.markdown("""
                    <div style="
                    background:#eaf7f0;
                    padding:15px;
                    border-radius:12px;
                    text-align:center;
                    font-size:18px;
                    ">
                    🌟 Continue comme ça, tu es incroyable ! 🌟
                    </div>
                    """, unsafe_allow_html=True)

                    data["phrases_valides_" + prenom] = True
                    st.session_state["lp_data"] = data

                    if prenom:
                        sauvegarder(data, prenom)

                # =========================
                # 📊 MÉTHODE PRO
                # =========================

                st.markdown("""
                <div style="background:#fff7f2;padding:12px;border-radius:10px;border-left:5px solid #ffb38a;">

                <b>📖 Méthode de lecture :</b><br><br>

                ✔ Lire lentement chaque mot<br>
                ✔ Identifier le sujet (qui ?)<br>
                ✔ Comprendre l’action (fait quoi ?)<br>
                ✔ Reformuler avec ses propres mots<br>
                ✔ Relire la phrase normalement<br>

                </div>
                """, unsafe_allow_html=True)

                st.caption(f"Progression : {reussite_phrases} / {seuil}")

                # =========================
                # 📄 PDF
                # =========================

                pdf_buffer = generer_pdf_lecture(programme, "phrases")

                st.download_button(
                    "📥 Télécharger PDF Phrases",
                    data=pdf_buffer,
                    file_name="phrases.pdf",
                    mime="application/pdf"
                )

            # =========================
            # 💡 CONSEILS
            # =========================

            with sous_tabs[4]:

                st.markdown("### 💡 Conseils")

                st.markdown("""
                <div style="background:#fff7f2;padding:15px;border-radius:10px;border-left:6px solid #ffb38a;">

                <b>👶 Pour accompagner votre enfant :</b><br><br>

                ✔ 5 minutes par jour suffisent<br>
                ✔ Répéter souvent les mêmes exercices<br>
                ✔ Encourager chaque réussite<br>
                ✔ Ne pas corriger brutalement<br>
                ✔ Faire des pauses si fatigue<br>
                ✔ Toujours finir sur une réussite<br>

                <br>

                <b>📚 Méthode recommandée :</b><br>

                1️⃣ Lettres → 2️⃣ Syllabes → 3️⃣ Mots → 4️⃣ Phrases<br>
                👉 Ne pas brûler les étapes<br>

                <br>

                <b>❤️ Important :</b><br>
                Chaque enfant progresse à son rythme. La régularité est plus importante que la durée.

                </div>
                """, unsafe_allow_html=True)

                # =========================
                # 📄 PDF CONSEILS
                # =========================

                pdf_buffer = generer_pdf_lecture(programme, "conseils")

                st.download_button(
                    "📥 Télécharger PDF Conseils",
                    data=pdf_buffer,
                    file_name="conseils.pdf",
                    mime="application/pdf"
                )