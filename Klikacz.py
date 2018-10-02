import tkinter as tk
import random
from tkinter import *
from tkinter import messagebox

'''Funkcje'''
def klik(arg):
    global licznik, lista_liczby
    # X przyjmuje wartość wyświetlaną przez kliknięty przycisk
    x = arg["text"]

    # Funkcja do "else'a" poniżej. Symuluje mrygnięcie innym kolorem w przypadku wcisnięcia złego przycisku
    def kolor():
        arg["background"] = "lightgray"
    if x == lista_liczby[licznik]:
        licznik +=1
        arg.flash()
        arg["state"] = DISABLED
        arg["background"] = "green"
        arg["disabledforeground"] = "yellow"
        if licznik == 25:
            tk.messagebox.showinfo("Gratulacje!", "Udało Ci się wygrać! \nZasłużyłeś na pieszczotkę!")
    # Else jest ozdobą, żeby ładniej wyglądała animacja
    else:
        arg["background"] = "red"
        arg.after(200, kolor)


'''Budowa okna i widżetów'''
main_window = tk.Tk()
main_window.title("Klikacz")

# Guziki
guzik1 = tk.Button(main_window, text=random.randint(1, 999), background="lightgray",
                   width=10, command=lambda: klik(guzik1))
guzik2 = tk.Button(main_window, text=random.randint(1, 999), background="lightgray",
                   width=10, command=lambda: klik(guzik2))
guzik3 = tk.Button(main_window, text=random.randint(1, 999), background="lightgray",
                   width=10, command=lambda: klik(guzik3))
guzik4 = tk.Button(main_window, text=random.randint(1, 999), background="lightgray",
                   width=10, command=lambda: klik(guzik4))
guzik5 = tk.Button(main_window, text=random.randint(1, 999), background="lightgray",
                   width=10, command=lambda: klik(guzik5))
guzik6 = tk.Button(main_window, text=random.randint(1, 999), background="lightgray",
                   width=10, command=lambda: klik(guzik6))
guzik7 = tk.Button(main_window, text=random.randint(1, 999), background="lightgray",
                   width=10, command=lambda: klik(guzik7))
guzik8 = tk.Button(main_window, text=random.randint(1, 999), background="lightgray",
                   width=10, command=lambda: klik(guzik8))
guzik9 = tk.Button(main_window, text=random.randint(1, 999), background="lightgray",
                   width=10, command=lambda: klik(guzik9))
guzik10 = tk.Button(main_window, text=random.randint(1, 999), background="lightgray",
                    width=10, command=lambda: klik(guzik10))
guzik11 = tk.Button(main_window, text=random.randint(1, 999), background="lightgray",
                    width=10, command=lambda: klik(guzik11))
guzik12 = tk.Button(main_window, text=random.randint(1, 999), background="lightgray",
                    width=10, command=lambda: klik(guzik12))
guzik13 = tk.Button(main_window, text=random.randint(1, 999), background="lightgray",
                    width=10, command=lambda: klik(guzik13))
guzik14 = tk.Button(main_window, text=random.randint(1, 999), background="lightgray",
                    width=10, command=lambda: klik(guzik14))
guzik15 = tk.Button(main_window, text=random.randint(1, 999), background="lightgray",
                    width=10, command=lambda: klik(guzik15))
guzik16 = tk.Button(main_window, text=random.randint(1, 999), background="lightgray",
                    width=10, command=lambda: klik(guzik16))
guzik17 = tk.Button(main_window, text=random.randint(1, 999), background="lightgray",
                    width=10, command=lambda: klik(guzik17))
guzik18 = tk.Button(main_window, text=random.randint(1, 999), background="lightgray",
                    width=10, command=lambda: klik(guzik18))
guzik19 = tk.Button(main_window, text=random.randint(1, 999), background="lightgray",
                    width=10, command=lambda: klik(guzik19))
guzik20 = tk.Button(main_window, text=random.randint(1, 999), background="lightgray",
                    width=10, command=lambda: klik(guzik20))
guzik21 = tk.Button(main_window, text=random.randint(1, 999), background="lightgray",
                    width=10, command=lambda: klik(guzik21))
guzik22 = tk.Button(main_window, text=random.randint(1, 999), background="lightgray",
                    width=10, command=lambda: klik(guzik22))
guzik23 = tk.Button(main_window, text=random.randint(1, 999), background="lightgray",
                    width=10, command=lambda: klik(guzik23))
guzik24 = tk.Button(main_window, text=random.randint(1, 999), background="lightgray",
                    width=10, command=lambda: klik(guzik24))
guzik25 = tk.Button(main_window, text=random.randint(1, 999), background="lightgray",
                    width=10, command=lambda: klik(guzik25))

# Umieszczenie guzików
guzik1.grid(column=0, row=0)
guzik2.grid(column=0, row=1)
guzik3.grid(column=0, row=2)
guzik4.grid(column=0, row=3)
guzik5.grid(column=0, row=4)
guzik6.grid(column=1, row=0)
guzik7.grid(column=1, row=1)
guzik8.grid(column=1, row=2)
guzik9.grid(column=1, row=3)
guzik10.grid(column=1, row=4)
guzik11.grid(column=2, row=0)
guzik12.grid(column=2, row=1)
guzik13.grid(column=2, row=2)
guzik14.grid(column=2, row=3)
guzik15.grid(column=2, row=4)
guzik16.grid(column=3, row=0)
guzik17.grid(column=3, row=1)
guzik18.grid(column=3, row=2)
guzik19.grid(column=3, row=3)
guzik20.grid(column=3, row=4)
guzik21.grid(column=4, row=0)
guzik22.grid(column=4, row=1)
guzik23.grid(column=4, row=2)
guzik24.grid(column=4, row=3)
guzik25.grid(column=4, row=4)

# Tworzę listę przycisków, nastepnie ich wartości liczbowe dodaję do nowej listy, a tą porządkuję rosnąco.
lista_guzik = [guzik1, guzik2, guzik3, guzik4, guzik5, guzik6, guzik7, guzik8, guzik9, guzik10,
               guzik11, guzik12, guzik13, guzik14, guzik15, guzik16, guzik17, guzik18, guzik19, guzik20,
               guzik21, guzik22, guzik23, guzik24, guzik25]
lista_liczby = []
for i in lista_guzik:
    lista_liczby.append(int(i["text"]))
lista_liczby.sort()

# Tworzę licznik wyznaczający ilość trafień
licznik = 0

main_window.mainloop()



'''Pytania i wątpliwości'''

#  Zdarza się że losują się dwie identyczne liczby (program mimo tego wykonuje się prawidłowo),
# czy trzeba wporwadzać zabezpieczenie przed taką sytuacją?

# Jakie jest oznaczenie naturalnego koloru przycisku - albo jak po zmianie koloru widżetu
# przywrócić jego pierwotny kolor? Bez tej wiedzy musiałem przyciskom narzucić kolor z góry
# (funkcja zmienia je na czerwony, po czym wraca do koloru narzuconego,
# a chciałbym żeby przycisk odzyskał "naturalny" kolor sprzed kliknięcia)
