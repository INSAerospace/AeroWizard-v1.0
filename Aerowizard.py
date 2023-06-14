
#********************************************************************
# -*- coding: UTF-8 -*-
#
# Projet : AeroWizard
#
# Auteur: Lucas KOWASLKI
#
#********************************************************************

import tkinter as tk
import tkinter
from tkinter import*
from tkinter import filedialog
from tkinter import ttk
from math import pi
from PIL import Image,ImageTk

aire = 0.0
def about():
    about_tk= Tk()
    about_tk.title("About")
    about_tk.configure(bg="white")
    about_tk.geometry("300x350+100+100")
    about_tk.resizable(False,False)
    

    menu_barre=tkinter.Menu(about_tk)

    menu_barre.add_command(label="  A propos    ")

    About= Canvas(about_tk,width=300,height=350,relief=GROOVE)
    About.place(x=0,y=0)

    label_produit=Label(About,text="Product :",font=('helvetica',10,"bold"))
    label_produit.place(x=20,y=20)

    souslab_produit=Label(About,text="Logiciel de Dimensionnement",font=('helvetica',10))
    souslab_produit.place(x=50,y=60)

    label_version=Label(About,text="Version :",font=('helvetica',10,"bold"))
    label_version.place(x=20,y=100)

    souslab_version=Label(About,text="1.0",font=('helvetica',10))
    souslab_version.place(x=50,y=135)

    label_commentaire=Label(About,text="Description :",font=('helvetica',10,"bold"))
    label_commentaire.place(x=20,y=170)

    souslab_commentaire=Label(About,text="Logiciel de dimensionnement",font=('helvetica',10))
    souslab_commentaire.place(x=50,y=210)
    souslab_commentaire2=Label(About,text="de Parachute.",font=('helvetica',10))
    souslab_commentaire2.place(x=50,y=230)

    label_Auteur=Label(About,text="Autor :",font=('helvetica',10,"bold"))
    label_Auteur.place(x=20,y=270)

    souslab_auteur=Label(About,text="KOWALSKI Lucas",font=('helvetica',10))
    souslab_auteur.place(x=50,y=300)

    about_tk.mainloop()

def effacer_labels_caracteristiques():
    label_rayon_ext.config(text="Rayon extérieur :")
    label_rayon_int.config(text="Rayon intérieur :")
    label_longueur.config(text="Longueur :")
    label_largeur.config(text="Largeur :")

def sauvegarder():
    vitesse = round(float(entree_vitesse.get()),3)
    masse = round(float(entree_masse.get()),3)
    type_parachute = ""
    if var_type_parachute.get() == 1:
        type_parachute = "Circulaire"
    elif var_type_parachute.get() == 2:
        type_parachute = "Carré"
    elif var_type_parachute.get() == 3:
        type_parachute = "Croix"
    
    fichier = open("Parachute.txt", "w")
    fichier.write(f"Vitesse de descente : {vitesse}\n")
    fichier.write(f"Masse : {masse}\n")
    fichier.write(f"Aire du parachute nécessaire : {aire} m²\n")
    fichier.write(f"Type de parachute : {type_parachute}\n")
    if var_type_parachute.get() == 1:
        if var_trou_stabilisateur.get() == 1:
            coefficient = entree_coefficient.get()
            fichier.write(f"Rayon extérieur : {(2 * aire) / pi}\n")
            fichier.write(f"Rayon intérieur : {((2 * aire) / pi) * float(coefficient)}\n")
        else:
            fichier.write(f"Rayon : {(aire / pi) ** 0.5}\n")
    elif var_type_parachute.get() == 2:
        fichier.write(f"Longueur : {aire ** 0.5}\n")
    elif var_type_parachute.get() == 3:
        longueur = (aire / 2) ** 0.5
        largeur = longueur / 2
        fichier.write(f"Longueur : {longueur}\n")
        fichier.write(f"Largeur : {largeur}\n")
    
    fichier.close()

def calculer_aire():
    
    vitesse = float(entree_vitesse.get())
    masse = float(entree_masse.get())
    global aire
    aire = round((2 * masse * 9.81) / ((vitesse**2)* 1.292),3)
    label_aire.config(text=f"Aire du parachute : {aire} m²")
    
def afficher_caracteristiques():
    calculer_aire()
    global aire
    canvas.delete("all")  # Effacer les schémas précédents
    effacer_labels_caracteristiques()  # Réinitialiser les labels des caractéristiques
    if var_type_parachute.get() == 1:  # Parachute circulaire
        if var_trou_stabilisateur.get() == 1:
            coefficient = entree_coefficient.get()
            if coefficient:
                coefficient = float(coefficient)
                rayon_ext = (2 * aire) / pi
                rayon_int = rayon_ext * coefficient
                # Dessiner le schéma d'une section de parachute circulaire avec trou de stabilisation
                canvas.create_oval(50, 50, 250, 250, outline="black", width=2)  # Cercle extérieur
                canvas.create_oval(100, 100, 200, 200, outline="black", width=2)  # Cercle intérieur
                # Afficher les variables caractéristiques
                label_rayon_ext.config(text=f"Rayon extérieur : {round(rayon_ext,3)}")
                label_rayon_int.config( text=f"Rayon intérieur : {round(rayon_int,3)}")

                label_rayon.config( text=f"Rayon : N/A")
                label_longueur.config( text=f"Longueur : N/A")
                label_largeur.config( text=f"Largeur : N/A")
                
            else:
                erreur_coefficient.config(text="Veuillez entrer le Ratio.",bg="red")
        else:
            rayon = (aire / pi) ** 0.5
            # Dessiner le schéma d'une section de parachute circulaire simple
            canvas.create_oval(50, 50, 250, 250, outline="black", width=2)  # Cercle extérieur
            # Afficher la variable caractéristique
            label_rayon.config( text=f"Rayon : {round(rayon,3)}")

            label_largeur.config( text=f"Largeur : N/A")
            label_longueur.config( text=f"Longueur : N/A")
            label_rayon_ext.config(text=f"Rayon extérieur : N/A")
            label_rayon_int.config( text=f"Rayon intérieur : N/A")
            
    elif var_type_parachute.get() == 2:  # Parachute carré
        longueur = (aire) ** 0.5
        # Dessiner le schéma d'une section de parachute carré
        canvas.create_rectangle(50, 50, 250, 250, outline="black", width=2)
        # Afficher la variable caractéristique
        label_longueur.config( text=f"Longueur : {round(longueur,3)}")

        label_rayon.config( text=f"Rayon : N/A")
        label_largeur.config( text=f"Largeur : N/A")
        label_rayon_ext.config(text=f"Rayon extérieur : N/A")
        label_rayon_int.config( text=f"Rayon intérieur : N/A")
        
        
    elif var_type_parachute.get() == 3:  # Parachute croix
        longueur = (aire / 2) ** 0.5
        largeur = longueur / 2
        # Dessiner le schéma de la croix
        # Rectangle vertical
        canvas.create_rectangle(150 - largeur, 50, 150 + largeur, 250, outline="black", width=80)
        # Rectangle horizontal
        canvas.create_rectangle(50, 150 - largeur, 250, 150 + largeur, outline="black", width=80)
        # Afficher les variables caractéristiques
        label_longueur.config( text=f"Longueur : {round(longueur,3)}")
        label_largeur.config( text=f"Largeur : {round(largeur,3)}")

        label_rayon.config( text=f"Rayon : N/A")
        label_rayon_ext.config(text=f"Rayon extérieur : N/A")
        label_rayon_int.config( text=f"Rayon intérieur : N/A")
        
def temp_text(e):
   entree_vitesse.delete(0,"end")

def temp_text2(e):
   entree_masse.delete(0,"end")

def quitter():
    fenetre.quit()
    fenetre.destroy()
    

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("AeroWizard")
fenetre.geometry("800x450")
fenetre.configure(bg='white')
fenetre.resizable(False,False)
fenetre.iconphoto(False, tk.PhotoImage(file="./assets/icone.png"))


menu_barre=tkinter.Menu(fenetre)

file_menu=tkinter.Menu(menu_barre,tearoff=0)

file_menu.add_separator()
file_menu.add_command(label="Save",command=sauvegarder)
file_menu.add_separator()
file_menu.add_command(label="Quit",command=quitter)

about_menu=tkinter.Menu(menu_barre,tearoff=0)

menu_barre.add_cascade(label="  File    ",menu=file_menu)
menu_barre.add_command(label="  About    ",command=about)

# Label et entrée pour la vitesse de descente
label_vitesse = tk.Label(fenetre, text="V.Landing :",bg='white')

entree_vitesse = tk.Entry(fenetre,bg="white", width=10, borderwidth=2)
entree_vitesse.insert(0, "m/s")
entree_vitesse.bind("<FocusIn>", temp_text)


# Label et entrée pour la masse
label_masse = tk.Label(fenetre, text="Masse :",bg='white')

entree_masse = tk.Entry(fenetre,bg="white", width=10, borderwidth=2)
entree_masse.insert(0, "kg")
entree_masse.bind("<FocusIn>", temp_text2)

# Bouton pour calculer l'aire du parachute
bouton_calculer_aire = tk.Button(fenetre, text="Calculer l'aire", command=calculer_aire)


# Label pour afficher l'aire du parachute
label_aire = tk.Label(fenetre, text="Aire :",bg='white')


# Labels pour les caractéristiques dimensionnelles du parachute
label_type_parachute = tk.Label(fenetre, text="Type de parachute :",bg='white')
var_type_parachute = tk.IntVar()
check_circulaire = tk.Checkbutton(fenetre, text="Circulaire",bg='white', variable=var_type_parachute, onvalue=1)
check_carre = tk.Checkbutton(fenetre, text="Carré",bg='white', variable=var_type_parachute, onvalue=2)
check_croix = tk.Checkbutton(fenetre, text="Croix",bg='white', variable=var_type_parachute, onvalue=3)

# Entrée pour le coefficient multiplicateur du rayon intérieur du parachute circulaire avec trou de stabilisation
label_coefficient = tk.Label(fenetre, text="Ratio :",bg='white')

entree_coefficient = tk.Entry(fenetre,bg="white", width=10, borderwidth=2)

var_trou_stabilisateur = tk.IntVar()
check_trou_stabilisateur = tk.Checkbutton(fenetre, text="Trou stabilisateur",bg='white', variable=var_trou_stabilisateur)

# Label pour afficher l'erreur de coefficient
erreur_coefficient = tk.Label(fenetre, text="",bg="white")

# Bouton pour afficher les caractéristiques du parachute
bouton_caracteristiques = tk.Button(fenetre, text="Recherche",width=20, command=afficher_caracteristiques)

# Canvas pour afficher les schémas des parachutes
canvas = tk.Canvas(fenetre, width=300, height=300, bg="white")

# Bouton pour sauvegarder les valeurs
bouton_save = tk.Button(fenetre, text="Save", command=sauvegarder,width=20)

# Labels pour les caractéristiques dimensionnelles du parachute
label_rayon_ext = tk.Label(fenetre, text="Rayon extérieur :",bg='white')
label_rayon_int = tk.Label(fenetre, text="Rayon intérieur :",bg='white')
label_rayon = tk.Label(fenetre, text="Rayon :",bg='white')
label_longueur = tk.Label(fenetre, text="Longueur :",bg='white')
label_largeur = tk.Label(fenetre, text="Largeur :",bg='white')

#Placement des widgets


param = tk.Label(fenetre,text = "Paramètres :", font=("Helvetica bold", 18),bg='white')
param.place(x= 50,y= 10)
label_vitesse.place(x=30,y=50)
entree_vitesse.place(x=100,y=50)

label_masse.place(x=30,y=80)
entree_masse.place(x=100,y=80)

label_type_parachute.place(x=30,y=120)


check_circulaire.place(x=50,y=150)
check_carre.place(x=50,y=180)
check_croix.place(x=50,y=210)

check_trou_stabilisateur.place(x=30,y=240)

label_coefficient.place(x=50,y=270)
entree_coefficient.place(x=100,y=270)

erreur_coefficient.place(x=50,y=300)

bouton_caracteristiques.place(x=50,y=340)

#Load an image in the script
img= (Image.open("./assets/logo.png"))

#Resize the Image using resize method
resized_image= img.resize((50,50), Image.ANTIALIAS)
photo= ImageTk.PhotoImage(resized_image)

# display an image label
#photo = tk.PhotoImage(file='./assets/logo.png')
image_label = ttk.Label(
    fenetre,
    image=photo,
    borderwidth=0
)
image_label.place(x = 280,y=340)
insa = tk.Label(fenetre,text = "INSA", font=("Helvetica bold", 18),bg='white',fg="red")
insa.place(x = 340,y=350)
erospace = tk.Label(fenetre,text = "erospace", font=("Helvetica bold", 18),bg='white',fg="black")
erospace.place(x = 395,y=350)

canvas.place(x=250,y=30)

bouton_save.place(x=600,y=340)

resultat = tk.Label(fenetre,text = "Résultats :", font=("Helvetica bold", 18),bg='white')
resultat.place(x = 600,y=10)

label_aire.place(x=580,y=100)

label_rayon_ext.place(x=580,y=150)
label_rayon_int.place(x=580,y=180)
label_rayon.place(x=580,y=210)
label_longueur.place(x=580,y=240)
label_largeur.place(x=580,y=270)

fenetre.config(menu=menu_barre)

fenetre.mainloop()



