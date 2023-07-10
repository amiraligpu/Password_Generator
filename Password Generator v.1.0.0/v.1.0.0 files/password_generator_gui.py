from ast import Lambda
import random
from password_generator_creator import insert_pass
import customtkinter
import tkinter
import webbrowser
from tkinter import messagebox

path_dict = {'lower_english': False, 'cap_english': False, 'signs': False, 'nums': False, 'jpn': False, 'per': False, 'grk': False}

def checkbox_event(option, value):
    global path_dict
    path_dict[option] = value


def open_gui():

    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("blue")

    app = customtkinter.CTk()
    app.title("Password Generator")

    button = customtkinter.CTkButton(master=app, text="Report Issue", command = lambda: webbrowser.open("https://github.com/amiraligpu/Password_Generator/issues"))
    button.grid(row=0, column= 0, sticky = "w")

    label = customtkinter.CTkLabel(app, text="Password Generator", fg_color="transparent", font = ("Calibri", 15))
    label.grid(row=0, column= 1)

    len_entry = customtkinter.CTkEntry(app, placeholder_text="Password Length")
    len_entry.grid(row = 1, column = 1)

    radiobutton_var = customtkinter.IntVar(value=1)


    english_low_letter_check = customtkinter.CTkCheckBox(app, text="English Lowercase Letters", 
                                                     command= lambda: checkbox_event("lower_english",english_low_letter_check.get()), 
                                                     onvalue= True, offvalue= False)
    english_low_letter_check.grid(row = 2, column = 0, sticky="w")

    english_cap_letter_check = customtkinter.CTkCheckBox(app, text="English Capital Letters", 
                                                     command= lambda: checkbox_event("cap_english",english_cap_letter_check.get()), 
                                                     onvalue= True, offvalue= False)
    english_cap_letter_check.grid(row = 3, column = 0, sticky="w")

    signs_check = customtkinter.CTkCheckBox(app, text="Signs", 
                                                     command= lambda: checkbox_event("signs",signs_check.get()), 
                                                     onvalue= True, offvalue= False)
    signs_check.grid(row = 2, column = 1, sticky="w")

    number_check = customtkinter.CTkCheckBox(app, text="Numbers", 
                                                     command= lambda: checkbox_event("nums",number_check.get()), 
                                                     onvalue= True, offvalue= False)
    number_check.grid(row = 2, column = 2, sticky="w")

    persian_check = customtkinter.CTkCheckBox(app, text="Persian Alphabets", 
                                                     command= lambda: checkbox_event("per",persian_check.get()), 
                                                     onvalue= True, offvalue= False)
    persian_check.grid(row = 3, column = 1, sticky="w")

    japanese_check = customtkinter.CTkCheckBox(app, text="Japanese Alphabets", 
                                                     command= lambda: checkbox_event("jpn",japanese_check.get()), 
                                                     onvalue= True, offvalue= False)
    japanese_check.grid(row = 3, column = 2, sticky="w")

    greek_check = customtkinter.CTkCheckBox(app, text="Greek Alphabets", 
                                                     command= lambda: checkbox_event("grk",greek_check.get()), 
                                                     onvalue= True, offvalue= False)
    greek_check.grid(row = 4, column = 0, sticky="w")


    button = customtkinter.CTkButton(master=app, text="click to generate password", command = lambda: insert_pass(app, path_dict, int(len_entry.get())) if len_entry.get().isnumeric() else messagebox.showerror("wrong entry", "Length of password must be a number"))
    button.grid(row = 4, column=1)

    app.mainloop()

open_gui()