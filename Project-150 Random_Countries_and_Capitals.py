from tkinter import *
import random

root=Tk()
root.title("Countries and Capitals")
root.geometry("500x500")

enter_country = Entry(root)
enter_country.place(relx= 0.5, rely= 0.2, anchor = CENTER)

enter_capital = Entry(root)
enter_capital.place(relx= 0.5, rely= 0.3, anchor = CENTER)

country_list = Label(root)
capital_list = Label(root)

random_country = Label(root)
random_capital = Label(root)

Country_list = []
Capital_list = []

def Country_list():
    country = enter_country.get()
    Country_list.append(country)
    country_list["text"] = "Country  Name: " + str(Country_list)
    
    capital = enter_capital.get()
    Capital_list.append(capital)
    capital_list["text"] = "Capital  Name: " + str(Capital_list)
    
def random_number():
    length1 = len(Country_list)
    length2 = len(Capital_list)
    
    random_country = random.randint(0, length1-1)
    random_capital = random.randint(0, length2-1)
    
    generated_random_country = Country_list[random_country]
    generated_random_capital = Capital_list[random_capital]
    
    random_country["text"] = str(generated_random_country)
    random_capital["text"] = str(generated_random_capital)
    
btn = Button(root, text= "Add to the Country List", command = random_number)
btn.place(relx = 0.5, rely = 0.3, anchor = CENTER)

country_list.place(relx = 0.5, rely = 0.4, anchor = CENTER)
capital_list.place(relx = 0.5, rely = 0.5, anchor = CENTER)

btn1 = Button(root, text= "What is your random Country ", command = random_number)
btn1.place(relx = 0.5, rely = 0.6, anchor = CENTER)

random_country.place(relx = 0.5, rely = 0.8, anchor = CENTER)
random_capital.place(relx = 0.5, rely = 0.9, anchor = CENTER)

root.mainloop()