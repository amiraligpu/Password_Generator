from os import path
import random
import customtkinter
from tkinter import messagebox
import pyperclip

character_string="ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩپچجحخهعغفقثصضگکمنتالبیسشئدذرزطظوあぁかさたなはまやゃらわがざだばぱぴびぢじぎゐりみひにちしきぃいうぅくすつぬふむゆゅるぐずづぶぷぺべでぜげゑれめへねてせけぇえおぉこそとのほもよょろをごぞどぼぽゔっんーゝゞ、。ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
english_string = "abcdefghijklmnopqrstuvwxyz"
english_cap_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
signs_string = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
numbers_string = "0123456789"
persian_string = "پچجحخهعغفقثصضگکمنتالبیسشئدذرزطظو"
japanese_string = "あぁかさたなはまやゃらわがざだばぱぴびぢじぎゐりみひにちしきぃいうぅくすつぬふむゆゅるぐずづぶぷぺべでぜげゑれめへねてせけぇえおぉこそとのほもよょろをごぞどぼぽゔっんーゝゞ、。"
greek_string = "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"
def pass_crt(passlen, path_dict):
    target_string = ""
    if path_dict["lower_english"] == True:
        target_string = target_string + english_string
    if path_dict["cap_english"] == True:
        target_string = target_string + english_cap_string
    if path_dict["signs"] == True:
        target_string = target_string + signs_string
    if path_dict["nums"] == True:
        target_string = target_string + numbers_string
    if path_dict["jpn"] == True:
        target_string = target_string + japanese_string
    if path_dict["per"] == True:
        target_string = target_string + persian_string
    if path_dict["grk"] == True:
        target_string = target_string + greek_string
    user_password = "".join(random.choices(target_string,k = passlen))
    return user_password


def insert_pass(window, path_dict, passlen):
    path_check = list()
    for i in path_dict.values():
        path_check.append(i)
    if path_check.count(False) == len(path_check):
        messagebox.showerror("No Choosen CheckBox", "Please check atleast one box from provided boxes.")
        path_check = list()
        return
    
    
    label_2 = customtkinter.CTkLabel(window, text="Your password is:", fg_color="transparent", font = ("Calibri", 15))
    label_2.grid(row=5, column= 1, sticky="n")
    
    
    results = pass_crt(passlen, path_dict)
    window.textbox = customtkinter.CTkTextbox(master=window)
    window.textbox.grid(row=6, column=1, sticky = "nsew")
    window.textbox.insert("0.0", f"{results}")
    button = customtkinter.CTkButton(master=window, text="Copy", command = lambda: pass_copy(results))
    button.grid(row=7, column= 1, sticky = "nsew")


def pass_copy(results):
    pyperclip.copy(results)
    messagebox.showinfo("Copy", "Your password has been copied successfully to the clipboard.")