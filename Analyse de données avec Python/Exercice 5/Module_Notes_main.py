##Exercice Python 05 PARTIE 2 : Fichier main.py
from Module_Notes_utils import convertir_note, moyenne_notes, mention

notes_brutes = ["12,5", "15", "abc", "9", "18,25"]

notes = [convertir_note(note) for note in notes_brutes]

notes_valides = [note for note in notes if note is not None]

moyenne = moyenne_notes(notes)
resultat_mention = mention(moyenne)

print(f"Notes ignorées : {len(notes) - len(notes_valides)}")
print(f"Moyenne : {moyenne:.2f}")
print(f"Mention : {resultat_mention}")