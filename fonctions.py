from tkinter import *
import gestionnaire

window = Tk()

window.title("Welcome to Student Class Order")

# create a label widget with font size
lbl = Label(window, text = "Welcome to Student Class Order", font = ("Arial Bold",20))
lbl.grid(column = 5, row = 5)



btnajout = Button(window, text = "ajout", bg = "grey", fg = "black", font = ("Arial",20))
btnajout.grid(column = 5, row = 10)

btn_affinom_prenom = Button(window, text = "afficher le prénom", bg = "grey", fg = "black", font = ("Arial",20))
btn_affinom_prenom.grid(column = 5, row = 10)

btn_affiID = Button(window, text = "afficher l'identification de l'élève", bg = "grey", fg = "black", font = ("Arial",20))
btn_affiID.grid(column = 5, row = 10)

btn_affispés = Button(window, text = "afficher les spécialitées des élèves", bg = "grey", fg = "black", command = affispés, font = ("Arial",20))
btn_affispés.grid(column = 5, row = 10)

window.geometry('500x500')



window.mainloop()   