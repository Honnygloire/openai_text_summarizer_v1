# Simulation d'un appel à l'API OpenAI pour résumer un texte

texte = open("data.txt").read()

def faux_openai_summarizer(input_text: str) -> str:
    """Retourne un résumé prédéfinis pour démonstration."""
    return "Ce texte explique que LangChain aide à structurer l'utilisation des modèles de langage."

#Exécution 
reponse = faux_openai_summarizer(texte)

#Affichage du résumé
print("Résumé généré :", reponse)