##Exercice Python 05 PARTIE 1 : Fichier utils.py
def convertir_note(texte):
    """Convertit une note textuelle en nombre décimal."""
    try:
        return float(texte.replace(",", "."))
    except (ValueError, AttributeError):
        return None


def moyenne_notes(notes):
    """Calcule la moyenne des notes valides."""
    notes_valides = [
        note for note in notes
        if note is not None
    ]

    if not notes_valides:
        return None

    return sum(notes_valides) / len(notes_valides)


def mention(moyenne):
    """Retourne la mention correspondant à la moyenne."""
    if moyenne is None:
        return "Aucune mention"
    elif moyenne < 10:
        return "Insuffisant"
    elif moyenne < 12:
        return "Passable"
    elif moyenne < 14:
        return "Assez bien"
    elif moyenne < 16:
        return "Bien"
    else:
        return "Très bien"
