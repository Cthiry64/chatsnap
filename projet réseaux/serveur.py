inport socket
hote=""
port=12800
connexion_ principale = socket.socket (socket.AF_INET, socket.socK_STREAM)
connexion principale.bind((hote, port))
connexion principale .1isten(5)
print("Le serveur écoute à présent sur le port {)".fornat (port))
connexion_avec_client, infos_Connexion - connexion_principale.accept ()
msg_recu= b""
while msg_recu != b"fin":
    msg recu = connexion_avec_client. reV(1024)
    #L'instruction ci-dessous peut lever une exception si le message
    # Receptionne comporte des accents
    print (msg_recu.decode ())
    connexion_avec_client. send (b"5/ 5")
print ("Fermeture de la connexion ")
connexion_avec_client.close ()
connexion_principale.close ()