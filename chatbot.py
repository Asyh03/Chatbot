import random
import customtkinter as ctk


# Dictionnaires des réponses et des liens
responses = {
    "bonjour": ["Salut !", "Bonjour !", "Hey ! Comment ça va ?"],
    "salut" : ["Salut !", "Bonjour !", "Hey ! Comment ça va ?"],
    "comment ça va": ["Je vais bien, merci ! Et toi ?", "Super ! Et toi ?"],
    "quel est ton nom": ["Je suis un chatbot !", "Appelle-moi ChatBotPy."],
    "au revoir": ["À bientôt !", "Au revoir ! Passe une bonne journée."],
    "merci": ["De rien !", "Avec plaisir !"],
}

links = {
    "maths" : 'https://www.bibmath.net/',
    "maths_youtube" : "https://www.youtube.com/@MathsAdultes",
    "python": "https://www.python.org",
    "site officiel de python": "https://www.python.org",
    "wikipedia": "https://www.wikipedia.org",
    "openai": "https://www.openai.com",
    "chatgpt": "https://chat.openai.com",
    "github": "https://github.com",
}

# Fonction pour démarrer le chatbot avec CustomTkinter
def chatbot():
    # Fenêtre principale
    app = ctk.CTk()
    app.title("Chatbot avec CustomTkinter")
    app.geometry("400x400")

# Zone de texte pour afficher les messages
    text_area = ctk.CTkTextbox(app, height=200, width=2000)
    text_area.pack(padx=20, pady=20)

# Entrée pour la saisie de l'utilisateur
    user_input = ctk.CTkEntry(app, width=400, placeholder_text="Tapez votre question...")
    user_input.pack(padx=20, pady=10)

# Fonction pour afficher la réponse du chatbot
    def get_response():
        user_message = user_input.get().lower()
        text_area.insert("end", f"👤 Vous : {user_message}\n")
        
        if user_message == "quit":
            text_area.insert("end", "🤖 Chatbot : Au revoir !\n")
            app.quit()
            return

# Recherche d'une réponse générale
        found = False
        for question, answers in responses.items():
            if question in user_message:
                text_area.insert("end", f"🤖 Chatbot : {random.choice(answers)}\n")
                found = True
                break

# Recherche d'un lien correspondant à la question
        if not found:
            for question, link in links.items():
                if question in user_message:
                    text_area.insert("end", f"🤖 Chatbot : Voici un lien qui peut t'aider : {link}\n")
                    found = True
                    break
        
        if not found:
            text_area.insert("end", "🤖 Chatbot : Désolé, je n'ai pas trouvé de lien ou de réponse pour ta question. 😕\n")
        
# Effacer la saisie utilisateur après avoir affiché la réponse
        user_input.delete(0, "end")
        text_area.see("end")

# Bouton pour envoyer le message
    send_button = ctk.CTkButton(app, text="Envoyer", command=get_response)
    send_button.pack(pady=10)

    app.mainloop()

# Lancer le chatbot
chatbot()
