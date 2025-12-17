# OpenAI – Text Summarizer (V1)

Mini-projet de découverte de l’API **OpenAI**.

---

## Objectif

Ce projet illustre la mécanique d’un appel à l’API OpenAI à travers un exemple simple :  
envoyer un texte à un modèle de langage et obtenir un résumé automatique en quelques phrases.

Pour éviter les contraintes liées aux API externes (clé OpenAI, quotas, facturation), j’ai choisi d’utiliser un **faux résumeur simulé**.  
Cela permet de démontrer la structure et le fonctionnement d’un appel API sans dépendances externes.

---

## Structure du projet

```bash
openai-text-summarizer/
├── data.txt #Document texte à résumer
├── main.py #Script principal avec la logique de OpenAi
└── README.md #Documentation du projet
```

---

## ⚙️ Installation

1. **Cloner le repo**
   ```bash
   git clone https://github.com/Honnygloire/openai_text_summarizer_v1.git
   cd openai-text-summarizer-v1
2. **Installer les dépedances**
   ```bash
   pip install -r requirements.txt
   ```

## Explication des choix

Faux résumeur (faux_openai_summarizer) : J’ai choisi de simuler un appel à l’API OpenAI pour éviter les problèmes de clé API ou de quota. Cela permet de se concentrer sur la mécanique d’un appel API.

Lecture du fichier (data.txt) : Le texte source est lu directement depuis un fichier pour simuler un cas réel d’entrée utilisateur.

Pipeline simple : Texte → fonction de résumé → affichage du résultat. Ce choix illustre la logique d’un appel API sans complexité supplémentaire.

Affichage du résultat (print) : Permet de montrer directement la sortie du “résumeur” dans le terminal.

## Exécution

Lancer le script :
```bash 
python3 main.py
```
Exemple de sortie :
```bash 
Ce texte explique que LangChain aide à structurer l'utilisation des modèles de langage.
```