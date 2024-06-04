# Imports
import customtkinter
import pickle
import sys
import os
import time
import threading
import random
import osascript
from pygame import mixer
from PIL import Image
import audio_module as audio

# Variables (Classifying)
global bps, amount_of_blocks, click_amount, overworld_cost, netherworld_cost, endworld_cost, endworld_amount, netherworld_amount, overworld_amount, achievement1_completed, achievement2_completed, achievement3_completed, achievement4_completed, achievement5_completed, achievement6_completed, achievement7_completed, overworld_click, netherworld_click_per_second, netherworld_cost_multiplyer, endworld_click_per_second, endworld_cost_multiplyer, overworld_cost_multiplyer, change_picture, number_count, steve_click, current_question
bps = 1
click_amount = 1
amount_of_blocks = 0
overworld_cost = 50
overworld_cost_multiplyer = 1
overworld_amount = 0
overworld_click = 1.2
netherworld_cost = 500
netherworld_cost_multiplyer = 1
netherworld_amount = 0
netherworld_click_per_second = 10.4
endworld_cost = 45000
endworld_cost_multiplyer = 1
endworld_click_per_second = 78.3
endworld_amount = 0
steve_click = 0
achievement1_completed = False
achievement2_completed = False
achievement3_completed = False
achievement4_completed = False
achievement5_completed = False
achievement6_completed = False
achievement7_completed = False
current_question = 1


# Textures & Color Values
dirt_block_color = "#ba855c"
grass_block_color = "#19d432"
stone_block_color = "#7f7f7f"
iron_block_color = "#e6e6e6"
gold_block_color = "#fee046"
diamond_block_color = "#63f0e0"
netherite_block_color = "#424043"

dirt_block = customtkinter.CTkImage(
    dark_image=Image.open("dirt_block.png"), size=(230, 230))
grass_block = customtkinter.CTkImage(
    dark_image=Image.open("grass_block.png"), size=(230, 230))
stone_block = customtkinter.CTkImage(
    dark_image=Image.open("stone_block.png"), size=(230, 230))
iron_block = customtkinter.CTkImage(
    dark_image=Image.open("iron_block.png"), size=(230, 230))
gold_block = customtkinter.CTkImage(
    dark_image=Image.open("gold_block.png"), size=(230, 230))
diamond_block = customtkinter.CTkImage(
    dark_image=Image.open("diamond_block.png"), size=(230, 230))
netherite_block = customtkinter.CTkImage(
    dark_image=Image.open("netherite_block.png"), size=(230, 230))
bg_black = customtkinter.CTkImage(
    dark_image=Image.open("bg_black.png"), size=(406, 600))
bg_blue = customtkinter.CTkImage(
    dark_image=Image.open("bg_blue.png"), size=(606, 400))
overworld_bg = customtkinter.CTkImage(
    dark_image=Image.open("overworld_bg.png"), size=(600, 150))
netherworld_bg = customtkinter.CTkImage(
    dark_image=Image.open("netherworld_bg.png"), size=(600, 150))
theend_bg = customtkinter.CTkImage(
    dark_image=Image.open("theend_bg.png"), size=(600, 150))
sign_bg = customtkinter.CTkImage(
    dark_image=Image.open("bg_sign.png"), size=(245, 145))
price_bg = customtkinter.CTkImage(
    dark_image=Image.open("price_bg.png"), size=(105, 60))
creeper_bg = customtkinter.CTkImage(
    dark_image=Image.open("creeper_bg.png"), size=(70, 70))
overworld_button = customtkinter.CTkImage(
    dark_image=Image.open("overworld_button.png"), size=(100, 60))
nether_button = customtkinter.CTkImage(
    dark_image=Image.open("nether_button.png"), size=(100, 60))
theend_button = customtkinter.CTkImage(
    dark_image=Image.open("theend_button.png"), size=(100, 60))
overworld_placement = customtkinter.CTkImage(
    dark_image=Image.open("overworld_placement.png"), size=(20, 20))
overworld_placement2 = customtkinter.CTkImage(
    dark_image=Image.open("overworld_placement2.png"), size=(20, 20))
netherworld_placement = customtkinter.CTkImage(
    dark_image=Image.open("netherworld_placement.png"), size=(20, 20))
netherworld_placement2 = customtkinter.CTkImage(
    dark_image=Image.open("netherworld_placement2.png"), size=(20, 20))
endworld_placement = customtkinter.CTkImage(
    dark_image=Image.open("endworld_placement.png"), size=(20, 20))
endworld_placement2 = customtkinter.CTkImage(
    dark_image=Image.open("endworld_placement2.png"), size=(20, 20))
placement_bg = customtkinter.CTkImage(
    dark_image=Image.open("bg_sign.png"), size=(100, 40))
save_bg = customtkinter.CTkImage(
    dark_image=Image.open("save_bg.png"), size=(100, 40))
load_bg = customtkinter.CTkImage(
    dark_image=Image.open("load_bg.png"), size=(100, 40))
back_right_bg = customtkinter.CTkImage(
    dark_image=Image.open("back_right_bg.png"), size=(40, 40))
info_bg = customtkinter.CTkImage(
    dark_image=Image.open("info_bg.png"), size=(40, 40))
settings_bg = customtkinter.CTkImage(
    dark_image=Image.open("settings_bg.png"), size=(40, 40))
back_left_bg = customtkinter.CTkImage(
    dark_image=Image.open("back_left_bg.png"), size=(40, 40))
panelSeperator_up = customtkinter.CTkImage(
    dark_image=Image.open("panelSeperator_up.png"), size=(20, 600))
panelSeperator_side = customtkinter.CTkImage(
    dark_image=Image.open("panelSeperator_side.png"), size=(600, 20))
achievement1_locked = customtkinter.CTkImage(
    dark_image=Image.open("achievement1_locked.png"), size=(48, 76))
achievement1_unlocked = customtkinter.CTkImage(
    dark_image=Image.open("achievement1_unlocked.png"), size=(48, 76))
achievement2_locked = customtkinter.CTkImage(
    dark_image=Image.open("achievement2_locked.png"), size=(48, 76))
achievement2_unlocked = customtkinter.CTkImage(
    dark_image=Image.open("achievement2_unlocked.png"), size=(48, 76))
achievement3_locked = customtkinter.CTkImage(
    dark_image=Image.open("achievement3_locked.png"), size=(48, 76))
achievement3_unlocked = customtkinter.CTkImage(
    dark_image=Image.open("achievement3_unlocked.png"), size=(48, 76))
achievement4_locked = customtkinter.CTkImage(
    dark_image=Image.open("achievement4_locked.png"), size=(48, 76))
achievement4_unlocked = customtkinter.CTkImage(
    dark_image=Image.open("achievement4_unlocked.png"), size=(48, 76))
achievement5_locked = customtkinter.CTkImage(
    dark_image=Image.open("achievement5_locked.png"), size=(48, 76))
achievement5_unlocked = customtkinter.CTkImage(
    dark_image=Image.open("achievement5_unlocked.png"), size=(48, 76))
achievement6_locked = customtkinter.CTkImage(
    dark_image=Image.open("achievement6_locked.png"), size=(48, 76))
achievement6_unlocked = customtkinter.CTkImage(
    dark_image=Image.open("achievement6_unlocked.png"), size=(48, 76))
achievement7_locked = customtkinter.CTkImage(
    dark_image=Image.open("achievement7_locked.png"), size=(48, 76))
achievement7_unlocked = customtkinter.CTkImage(
    dark_image=Image.open("achievement7_unlocked.png"), size=(48, 76))
achievementList_bg = customtkinter.CTkImage(
    dark_image=Image.open("achievementList_bg.png"), size=(179, 69))
wood_bg = customtkinter.CTkImage(
    dark_image=Image.open("wooden_sword_bg.png"), size=(45, 45))
stone_bg = customtkinter.CTkImage(
    dark_image=Image.open("stone_sword_bg.png"), size=(45, 45))
iron_bg = customtkinter.CTkImage(
    dark_image=Image.open("iron_sword_bg.png"), size=(45, 45))
gold_bg = customtkinter.CTkImage(
    dark_image=Image.open("gold_sword_bg.png"), size=(45, 45))
diamond_bg = customtkinter.CTkImage(
    dark_image=Image.open("diamond_sword_bg.png"), size=(45, 45))
netherite_bg = customtkinter.CTkImage(
    dark_image=Image.open("netherite_sword_bg.png"), size=(45, 45))
elytra_bg = customtkinter.CTkImage(
    dark_image=Image.open("elytra_bg.png"), size=(45, 45))
checkmark_bg = customtkinter.CTkImage(
    dark_image=Image.open("checkmark_bg.png"), size=(25, 25))
end_ball_bg = customtkinter.CTkImage(
    dark_image=Image.open("end_ball_bg.png"), size=(300, 300))
question1 = customtkinter.CTkImage(
    dark_image=Image.open("question1.png"), size=(300, 300))
question2 = customtkinter.CTkImage(
    dark_image=Image.open("question2.png"), size=(300, 300))
question3 = customtkinter.CTkImage(
    dark_image=Image.open("question3.png"), size=(300, 300))
question4 = customtkinter.CTkImage(
    dark_image=Image.open("question4.png"), size=(300, 300))
question5 = customtkinter.CTkImage(
    dark_image=Image.open("question5.png"), size=(300, 300))
question6 = customtkinter.CTkImage(
    dark_image=Image.open("question6.png"), size=(300, 300))
question7 = customtkinter.CTkImage(
    dark_image=Image.open("question7.png"), size=(300, 300))
question8 = customtkinter.CTkImage(
    dark_image=Image.open("question8.png"), size=(300, 300))
question9 = customtkinter.CTkImage(
    dark_image=Image.open("question9.png"), size=(300, 300))
background = customtkinter.CTkImage(
    dark_image=Image.open("background.png"), size=(1200, 800))
background2 = customtkinter.CTkImage(
    dark_image=Image.open("background2.png"), size=(342, 100))

# Info Button Callback (Info Window)
def info_button_callback2():
    info_window = customtkinter.CTkToplevel()

    w = 300
    h = 96
    ws = info_window.winfo_screenwidth()
    hs = info_window.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    info_window.geometry('%dx%d+%d+%d' % (w, h, x, y))
    info_window.resizable(False, False)
    info_window.title("About MC Clicker")

    creeper_label = customtkinter.CTkLabel(
        info_window, width=70, height=70, image=creeper_bg, text="", corner_radius=0, fg_color="transparent", bg_color="transparent")
    creeper_label.place(x=13, y=48, anchor="w")

    copyright_label = customtkinter.CTkLabel(
        info_window, text="Copyright © 2024 Aiden Sorabji", fg_color="transparent", bg_color="transparent", font=customtkinter.CTkFont("SF Pro thinitalic", 10))
    copyright_label.place(x=98, y=56, anchor="w")

    name_label = customtkinter.CTkLabel(
        info_window, text="Aiden Sorabji", fg_color="transparent", bg_color="transparent", font=customtkinter.CTkFont("SF Pro Semibold", 15))
    name_label.place(x=98, y=34, anchor="w")

    info_window.mainloop()

# Secret Menu (Questionnaire)
def secret_menu():
    global codes_entry, question_label, question1_answer, question2_answer, question3_answer, question4_answer, question5_answer, question6_answer, question7_answer, question8_answer, question9_answer, current_question, secret_menu
    secret_menu = customtkinter.CTkToplevel()
    w = 318
    h = 297
    ws = secret_menu.winfo_screenwidth()
    hs = secret_menu.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    secret_menu.geometry('%dx%d+%d+%d' % (w, h, x, y))
    secret_menu.resizable(False, False)
    secret_menu.title("Ender Questions")

    def question1_():
        global question_label
        question_label.configure(image=question1) 
    def question2_():
        global question_label
        question_label.configure(image=question2)  
    def question3_():
        global question_label
        question_label.configure(image=question3)  
    def question4_():
        global question_label
        question_label.configure(image=question4)
    def question5_():
        global question_label
        question_label.configure(image=question5)
    def question6_():
        global question_label
        question_label.configure(image=question6)
    def question7_():
        global question_label
        question_label.configure(image=question7)
    def question8_():
        global question_label
        question_label.configure(image=question8)
    def question9_():
        global question_label
        question_label.configure(image=question9)

    def after():
        global secret_menu
        end = customtkinter.CTkToplevel()
        w = 1200
        h = 800
        ws = end.winfo_screenwidth()
        hs = end.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        end.geometry('%dx%d+%d+%d' % (w, h, x, y))
        end.resizable(False, False)
        end.title("The End")

        secret_menu.destroy()

        background1 = customtkinter.CTkLabel(
            end, image=background, text="", corner_radius=0, fg_color="transparent", bg_color="transparent")
        background1.place(x=0, y=0)

        background21 = customtkinter.CTkButton(end, image=background2, text="", corner_radius=0, bg_color="#868686",
                                               fg_color="#868686", border_width=0, border_spacing=0, hover_color="#868686", command=info_button_callback2)
        background21.place(x=610, y=297)

        end.mainloop()

    def question_check():
        global codes_entry, current_question

        # Get and strip any leading/trailing spaces
        user_input = codes_entry.get()

        question1_answer = ["stronghold", "Stronghold",
                            "strong hold", "Strong Hold", "Strong hold"]
        question2_answer = ["Map", "map"]
        question3_answer = ["Obsidian", "obsidian"]
        question4_answer = ["Sea Lantern",
                            "Sea lantern", "sea Lantern", "sea lantern"]
        question5_answer = ["Phantom", "phantom"]
        question6_answer = ["Chorus Plant",
                            "Chorus plant", "chorus Plant", "chorus plant", "Chorus Fruit", "Chorus fruit", "chorus Fruit", "chorus fruit"]
        question7_answer = ["End Portal Frame", "End portal frame", "End Portal frame",
                            "end portal frame", "End portal Frame", "end Portal Frame", "end portal Frame"]
        question8_answer = ["Looting", "looting"]
        question9_answer = ["Snowy Tundra",
                            "Snowy tundra", "snowy Tundra", "snowy tundra", "Snow Tundra", "Snow tundra", "snow Tundra", "snow tundra"]

        if current_question == 1:
            if user_input in question1_answer:
                codes_entry.destroy()
                codes_entry = customtkinter.CTkEntry(
                    secret_menu, width=241, height=27, placeholder_text="Answer Here", text_color="#d25ad6")
                codes_entry.place(x=9, y=225)
                current_question = 2
                question2_()
            else:
                codes_entry.destroy()
                codes_entry = customtkinter.CTkEntry(
                    secret_menu, width=241, height=27, placeholder_text="Wrong Answer", text_color="#d25ad6", placeholder_text_color="#d92929")
                codes_entry.place(x=9, y=225)

        elif current_question == 2:
            if user_input in question2_answer:
                codes_entry.destroy()
                codes_entry = customtkinter.CTkEntry(
                    secret_menu, width=241, height=27, placeholder_text="Answer Here", text_color="#d25ad6")
                codes_entry.place(x=9, y=225)
                current_question = 3
                question3_()
            else:
                codes_entry.destroy()
                codes_entry = customtkinter.CTkEntry(
                    secret_menu, width=241, height=27, placeholder_text="Wrong Answer", text_color="#d25ad6", placeholder_text_color="#d92929")
                codes_entry.place(x=9, y=225)

        elif current_question == 3:
            if user_input in question3_answer:
                codes_entry.destroy()
                codes_entry = customtkinter.CTkEntry(
                    secret_menu, width=241, height=27, placeholder_text="Answer Here", text_color="#d25ad6")
                codes_entry.place(x=9, y=225)
                current_question = 4
                question4_()
            else:
                codes_entry.destroy()
                codes_entry = customtkinter.CTkEntry(
                    secret_menu, width=241, height=27, placeholder_text="Wrong Answer", text_color="#d25ad6", placeholder_text_color="#d92929")
                codes_entry.place(x=9, y=225)

        elif current_question == 4:
            if user_input in question4_answer:
                codes_entry.destroy()
                codes_entry = customtkinter.CTkEntry(
                    secret_menu, width=241, height=27, placeholder_text="Answer Here", text_color="#d25ad6")
                codes_entry.place(x=9, y=225)
                current_question = 5
                question5_()
            else:
                codes_entry.destroy()
                codes_entry = customtkinter.CTkEntry(
                    secret_menu, width=241, height=27, placeholder_text="Wrong Answer", text_color="#d25ad6", placeholder_text_color="#d92929")
                codes_entry.place(x=9, y=225)

        elif current_question == 5:
            if user_input in question5_answer:
                codes_entry.destroy()
                codes_entry = customtkinter.CTkEntry(
                    secret_menu, width=241, height=27, placeholder_text="Answer Here", text_color="#d25ad6")
                codes_entry.place(x=9, y=225)
                current_question = 6
                question6_()
            else:
                codes_entry.destroy()
                codes_entry = customtkinter.CTkEntry(
                    secret_menu, width=241, height=27, placeholder_text="Wrong Answer", text_color="#d25ad6", placeholder_text_color="#d92929")
                codes_entry.place(x=9, y=225)

        elif current_question == 6:
            if user_input in question6_answer:
                codes_entry.destroy()
                codes_entry = customtkinter.CTkEntry(
                    secret_menu, width=241, height=27, placeholder_text="Answer Here", text_color="#d25ad6")
                codes_entry.place(x=9, y=225)
                current_question = 7
                question7_()
            else:
                codes_entry.destroy()
                codes_entry = customtkinter.CTkEntry(
                    secret_menu, width=241, height=27, placeholder_text="Wrong Answer", text_color="#d25ad6", placeholder_text_color="#d92929")
                codes_entry.place(x=9, y=225)

        elif current_question == 7:
            if user_input in question7_answer:
                codes_entry.destroy()
                codes_entry = customtkinter.CTkEntry(
                    secret_menu, width=241, height=27, placeholder_text="Answer Here", text_color="#d25ad6")
                codes_entry.place(x=9, y=225)
                current_question = 8
                question8_()
            else:
                codes_entry.destroy()
                codes_entry = customtkinter.CTkEntry(
                    secret_menu, width=241, height=27, placeholder_text="Wrong Answer", text_color="#d25ad6", placeholder_text_color="#d92929")
                codes_entry.place(x=9, y=225)

        elif current_question == 8:
            if user_input in question8_answer:
                codes_entry.destroy()
                codes_entry = customtkinter.CTkEntry(
                    secret_menu, width=241, height=27, placeholder_text="Answer Here", text_color="#d25ad6")
                codes_entry.place(x=9, y=225)
                current_question = 9
                question9_()
            else:
                codes_entry.destroy()
                codes_entry = customtkinter.CTkEntry(
                    secret_menu, width=241, height=27, placeholder_text="Wrong Answer", text_color="#d25ad6", placeholder_text_color="#d92929")
                codes_entry.place(x=9, y=225)

        elif current_question == 9:
            if user_input in question9_answer:
                codes_entry.destroy()
                codes_entry = customtkinter.CTkEntry(
                    secret_menu, width=241, height=27, placeholder_text="Answer Here", text_color="#d25ad6")
                codes_entry.place(x=9, y=225)
                current_question = 10
                after()

            else:
                codes_entry.destroy()
                codes_entry = customtkinter.CTkEntry(
                    secret_menu, width=241, height=27, placeholder_text="Wrong Answer", text_color="#d25ad6", placeholder_text_color="#d92929")
                codes_entry.place(x=9, y=225)

        elif current_question == 10:
            after()

    question_label = customtkinter.CTkLabel(
        secret_menu, image=end_ball_bg, text="", width=300, height=300, bg_color="transparent", fg_color="transparent")
    question_label.place(x=9, y=-40)

    codes_entry = customtkinter.CTkEntry(
        secret_menu, width=241, height=27, placeholder_text="Answer Here", text_color="#d25ad6")
    codes_entry.place(x=9, y=225)
    codes_entry.bind(sequence='<Return>', command=question_check)

    enter_button = customtkinter.CTkButton(
        secret_menu, width=52, height=27, text="Enter", fg_color="#a940a9", command=question_check, hover_color="#872f87")
    enter_button.place(x=257, y=225)

    if current_question == 1:
        question1_()
    elif current_question == 2:
        question2_()
    elif current_question == 3:
        question3_()
    elif current_question == 4:
        question4_()
    elif current_question == 5:
        question5_()
    elif current_question == 6:
        question6_()
    elif current_question == 7:
        question7_()
    elif current_question == 8:
        question8_()
    elif current_question == 9:
        question9_()
    elif current_question == 10:
        after()

    def restart_questionnaire_callback():
        current_question = 1
        question1_()

    restart_questionnaire_button = customtkinter.CTkButton(
        secret_menu, text="Restart Questionnaire", height=29, width=300, fg_color="#913691", hover_color="#7d2e7c", command=restart_questionnaire_callback)
    restart_questionnaire_button.place(x=9, y=260)

    secret_menu.mainloop()

# Save Button (Saving Game to .pkl File)
def save_button_callback2():  # sdkl;jfkl;sdajf;kladsjfas;lkdfja;lsdkjfa;lskdjfa;lsdkjf;laskdfja;lskdfja;lskjfdasl;kjdfasl;kfjasldkjf
    global bps, amount_of_blocks, click_amount, overworld_cost, netherworld_cost, endworld_cost, endworld_amount, netherworld_amount, overworld_amount, achievement1_completed, achievement2_completed, achievement3_completed, achievement4_completed, achievement5_completed, achievement6_completed, achievement7_completed, overworld_click, netherworld_click_per_second, netherworld_cost_multiplyer, endworld_click_per_second, endworld_cost_multiplyer, overworld_cost_multiplyer, current_question

    # Define the filename
    filename = 'save.pkl'

    if os.path.exists(filename):
        # Load the data from the pickle file
        with open(filename, 'wb') as file:
            pickle.dump(bps, file)
            pickle.dump(amount_of_blocks, file)
            pickle.dump(click_amount, file)
            pickle.dump(overworld_cost, file)
            pickle.dump(netherworld_cost, file)
            pickle.dump(endworld_cost, file)
            pickle.dump(endworld_amount, file)
            pickle.dump(netherworld_amount, file)
            pickle.dump(overworld_amount, file)
            pickle.dump(achievement1_completed, file)
            pickle.dump(achievement2_completed, file)
            pickle.dump(achievement3_completed, file)
            pickle.dump(achievement4_completed, file)
            pickle.dump(achievement5_completed, file)
            pickle.dump(achievement6_completed, file)
            pickle.dump(achievement7_completed, file)
            pickle.dump(overworld_click, file)
            pickle.dump(netherworld_click_per_second, file)
            pickle.dump(netherworld_cost_multiplyer, file)
            pickle.dump(endworld_click_per_second, file)
            pickle.dump(endworld_cost_multiplyer, file)
            pickle.dump(overworld_cost_multiplyer, file)
            pickle.dump(current_question, file)
            title = "Saved"
            message = "File Saved to Existing Save: " + filename

            command = f'''
osascript -e 'display notification "{message}" with title "{title}"'
'''
            os.system(command)

    else:
        # Save the new data to the pickle file
        with open(filename, 'wb') as file:
            pickle.dump(bps, file)
            pickle.dump(amount_of_blocks, file)
            pickle.dump(click_amount, file)
            pickle.dump(overworld_cost, file)
            pickle.dump(netherworld_cost, file)
            pickle.dump(endworld_cost, file)
            pickle.dump(endworld_amount, file)
            pickle.dump(netherworld_amount, file)
            pickle.dump(overworld_amount, file)
            pickle.dump(achievement1_completed, file)
            pickle.dump(achievement2_completed, file)
            pickle.dump(achievement3_completed, file)
            pickle.dump(achievement4_completed, file)
            pickle.dump(achievement5_completed, file)
            pickle.dump(achievement6_completed, file)
            pickle.dump(achievement7_completed, file)
            pickle.dump(overworld_click, file)
            pickle.dump(netherworld_click_per_second, file)
            pickle.dump(netherworld_cost_multiplyer, file)
            pickle.dump(endworld_click_per_second, file)
            pickle.dump(endworld_cost_multiplyer, file)
            pickle.dump(overworld_cost_multiplyer, file)
            title = "Saved"
            message = "File Saved to New Save: " + filename

            command = f'''
osascript -e 'display notification "{message}" with title "{title}"'
'''
            os.system(command)

# Load Button (Load Game From .pkl File)
def load_button_callback2():
    global bps, amount_of_blocks, click_amount, overworld_cost, netherworld_cost, endworld_cost, endworld_amount, netherworld_amount, overworld_amount, achievement1_completed, achievement2_completed, achievement3_completed, achievement4_completed, achievement5_completed, achievement6_completed, achievement7_completed, overworld_click, netherworld_click_per_second, netherworld_cost_multiplyer, endworld_click_per_second, endworld_cost_multiplyer, overworld_cost_multiplyer
    global amount_of_blocks_label, blocks_per_second_label, blocks_per_second_label, price_text1, price_text2, price_text3, big_block_button, achievement1, achievement2, achievement3, achievement4, achievement5, achievement6, achievement7, back_right_button, overworld_amount_label, netherworld_amount_label, endworld_amount_label, number_count, change_picture, current_question

    # Define the filename
    filename = 'save.pkl'

    if os.path.exists(filename):
        # Load the data from the pickle file
        with open(filename, 'rb') as file:
            bps = pickle.load(file)
            amount_of_blocks = pickle.load(file)
            click_amount = pickle.load(file)
            overworld_cost = pickle.load(file)
            netherworld_cost = pickle.load(file)
            endworld_cost = pickle.load(file)
            endworld_amount = pickle.load(file)
            netherworld_amount = pickle.load(file)
            overworld_amount = pickle.load(file)
            achievement1_completed = pickle.load(file)
            achievement2_completed = pickle.load(file)
            achievement3_completed = pickle.load(file)
            achievement4_completed = pickle.load(file)
            achievement5_completed = pickle.load(file)
            achievement6_completed = pickle.load(file)
            achievement7_completed = pickle.load(file)
            overworld_click = pickle.load(file)
            netherworld_click_per_second = pickle.load(file)
            netherworld_cost_multiplyer = pickle.load(file)
            endworld_click_per_second = pickle.load(file)
            endworld_cost_multiplyer = pickle.load(file)
            overworld_cost_multiplyer = pickle.load(file)
            current_question = pickle.load(file)

            print(current_question)
            labelish = str(bps) + " per second"
            blocks_per_second_label.configure(text=labelish)
            overworld_amount_entry = (str(overworld_amount)) + "x"
            overworld_amount_label.configure(text=overworld_amount_entry)
            netherworld_amount_entry = (str(netherworld_amount)) + "x"
            netherworld_amount_label.configure(text=netherworld_amount_entry)
            endworld_amount_entry = (str(endworld_amount)) + "x"
            endworld_amount_label.configure(text=endworld_amount_entry)

            price_text1.configure(text=overworld_cost)
            price_text2.configure(text=netherworld_cost)
            price_text3.configure(text=endworld_cost)

            amount_of_blocks_label.configure(text=amount_of_blocks)
            number_count()
            change_picture()

            if achievement1_completed == False:
                achievement1.configure(image=achievement1_locked)
            elif achievement1_completed == True:
                achievement1.configure(image=achievement1_unlocked)
            if achievement2_completed == False:
                achievement2.configure(image=achievement2_locked)
            elif achievement2_completed == True:
                achievement2.configure(image=achievement2_unlocked)
            if achievement3_completed == False:
                achievement3.configure(image=achievement3_locked)
            elif achievement3_completed == True:
                achievement3.configure(image=achievement3_unlocked)
            if achievement4_completed == False:
                achievement4.configure(image=achievement4_locked)
            elif achievement4_completed == True:
                achievement4.configure(image=achievement4_unlocked)
            if achievement5_completed == False:
                achievement5.configure(image=achievement5_locked)
            elif achievement5_completed == True:
                achievement5.configure(image=achievement5_unlocked)
            if achievement6_completed == False:
                achievement6.configure(image=achievement6_locked)
            elif achievement6_completed == True:
                achievement6.configure(image=achievement6_unlocked)
            if achievement7_completed == False:
                achievement7.configure(image=achievement7_locked)
            elif achievement7_completed == True:
                achievement7.configure(image=achievement7_unlocked)

            title = "Loaded"
            message = "Loaded Save "

            command = f'''
osascript -e 'display notification "{message}" with title "{title}"'
    '''
            os.system(command)

    else:
        title = "Error"
        message = "No Save Detected "

        command = f'''
osascript -e 'display notification "{message}" with title "{title}"'
    '''
        os.system(command)

# Achievement List Callback (Achievement Window)
def achievement_list_callback2():
    global achievement1_completed, achievement2_completed, achievement3_completed, achievement4_completed, achievement5_completed, achievement6_completed, achievement7_completed
    achievement_window = customtkinter.CTkToplevel()
    w = 400
    h = 575
    ws = achievement_window.winfo_screenwidth()
    hs = achievement_window.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    achievement_window.geometry('%dx%d+%d+%d' % (w, h, x, y))
    achievement_window.resizable(False, False)
    achievement_window.title("Achievement List")

    wooden_image = customtkinter.CTkLabel(achievement_window, image=wood_bg, text="",
                                          width=45, height=45, corner_radius=0, bg_color="transparent", fg_color="transparent")
    wooden_image.place(x=25, y=25)

    stone_image = customtkinter.CTkLabel(achievement_window, image=stone_bg, text="",
                                         width=45, height=45, corner_radius=0, bg_color="transparent", fg_color="transparent")
    stone_image.place(x=25, y=105)

    iron_image = customtkinter.CTkLabel(achievement_window, image=iron_bg, text="",
                                        width=45, height=45, corner_radius=0, bg_color="transparent", fg_color="transparent")
    iron_image.place(x=25, y=185)

    gold_image = customtkinter.CTkLabel(achievement_window, image=gold_bg, text="",
                                        width=45, height=45, corner_radius=0, bg_color="transparent", fg_color="transparent")
    gold_image.place(x=25, y=265)

    diamond_image = customtkinter.CTkLabel(achievement_window, image=diamond_bg, text="",
                                           width=45, height=45, corner_radius=0, bg_color="transparent", fg_color="transparent")
    diamond_image.place(x=25, y=345)

    netherite_image = customtkinter.CTkLabel(achievement_window, image=netherite_bg, text="",
                                             width=45, height=45, corner_radius=0, bg_color="transparent", fg_color="transparent")
    netherite_image.place(x=25, y=425)

    elytra_image = customtkinter.CTkLabel(achievement_window, image=elytra_bg, text="",
                                          width=45, height=45, corner_radius=0, bg_color="transparent", fg_color="transparent")
    elytra_image.place(x=25, y=505)

    # 80 16

    title1 = customtkinter.CTkLabel(
        achievement_window, text="The Start", bg_color="transparent", font=customtkinter.CTkFont("SF Pro Bold", 13))
    title1.place(x=85, y=38, anchor="w")

    paragraph1 = customtkinter.CTkLabel(
        achievement_window, text="Mine 100 blocks", bg_color="transparent", font=customtkinter.CTkFont("SF Pro Thin", 12), height=7)
    paragraph1.place(x=85, y=54, anchor="w")

    title2 = customtkinter.CTkLabel(
        achievement_window, text="Getting There", bg_color="transparent", font=customtkinter.CTkFont("SF Pro Bold", 13))
    title2.place(x=85, y=118, anchor="w")

    paragraph2 = customtkinter.CTkLabel(
        achievement_window, text="Mine 1,000 blocks", bg_color="transparent", font=customtkinter.CTkFont("SF Pro Thin", 12), height=7)
    paragraph2.place(x=85, y=134, anchor="w")

    title3 = customtkinter.CTkLabel(
        achievement_window, text="Upgraded", bg_color="transparent", font=customtkinter.CTkFont("SF Pro Bold", 13))
    title3.place(x=85, y=198, anchor="w")

    paragraph3 = customtkinter.CTkLabel(
        achievement_window, text="Mine 10,000 blocks", bg_color="transparent", font=customtkinter.CTkFont("SF Pro Thin", 12), height=7)
    paragraph3.place(x=85, y=214, anchor="w")

    title4 = customtkinter.CTkLabel(
        achievement_window, text="Can't Get Better...", bg_color="transparent", font=customtkinter.CTkFont("SF Pro Bold", 13))
    title4.place(x=85, y=278, anchor="w")

    paragraph4 = customtkinter.CTkLabel(
        achievement_window, text="Mine 100,000 blocks", bg_color="transparent", font=customtkinter.CTkFont("SF Pro Thin", 12), height=7)
    paragraph4.place(x=85, y=294, anchor="w")

    title5 = customtkinter.CTkLabel(
        achievement_window, text="Will Get Better!", bg_color="transparent", font=customtkinter.CTkFont("SF Pro Bold", 13))
    title5.place(x=85, y=358, anchor="w")

    paragraph5 = customtkinter.CTkLabel(
        achievement_window, text="Mine 1,000,000 blocks", bg_color="transparent", font=customtkinter.CTkFont("SF Pro Thin", 12), height=7)
    paragraph5.place(x=85, y=374, anchor="w")

    title6 = customtkinter.CTkLabel(
        achievement_window, text="The End?", bg_color="transparent", font=customtkinter.CTkFont("SF Pro Bold", 13))
    title6.place(x=85, y=438, anchor="w")

    paragraph6 = customtkinter.CTkLabel(
        achievement_window, text="Mine 1,000,000,000 blocks", bg_color="transparent", font=customtkinter.CTkFont("SF Pro Thin", 12), height=7)
    paragraph6.place(x=85, y=454, anchor="w")

    title7 = customtkinter.CTkLabel(
        achievement_window, text="The End", bg_color="transparent", font=customtkinter.CTkFont("SF Pro Bold", 13))
    title7.place(x=85, y=518, anchor="w")

    paragraph7 = customtkinter.CTkLabel(
        achievement_window, text="Mine 1 Trillion blocks & 100,000 BPS", bg_color="transparent", font=customtkinter.CTkFont("SF Pro Thin", 12), height=7)
    paragraph7.place(x=85, y=534, anchor="w")

    if achievement1_completed == True:
        checkmark1 = customtkinter.CTkLabel(achievement_window, image=checkmark_bg, text="",
                                            width=25, height=25, corner_radius=0, bg_color="transparent", fg_color="transparent")
        checkmark1.place(x=355, y=35)

    if achievement2_completed == True:
        checkmark2 = customtkinter.CTkLabel(achievement_window, image=checkmark_bg, text="",
                                            width=25, height=25, corner_radius=0, bg_color="transparent", fg_color="transparent")
        checkmark2.place(x=355, y=115)

    if achievement3_completed == True:
        checkmark3 = customtkinter.CTkLabel(achievement_window, image=checkmark_bg, text="",
                                            width=25, height=25, corner_radius=0, bg_color="transparent", fg_color="transparent")
        checkmark3.place(x=355, y=195)

    if achievement4_completed == True:
        checkmark4 = customtkinter.CTkLabel(achievement_window, image=checkmark_bg, text="",
                                            width=25, height=25, corner_radius=0, bg_color="transparent", fg_color="transparent")
        checkmark4.place(x=355, y=275)

    if achievement5_completed == True:
        checkmark5 = customtkinter.CTkLabel(achievement_window, image=checkmark_bg, text="",
                                            width=25, height=25, corner_radius=0, bg_color="transparent", fg_color="transparent")
        checkmark5.place(x=355, y=355)

    if achievement6_completed == True:
        checkmark6 = customtkinter.CTkLabel(achievement_window, image=checkmark_bg, text="",
                                            width=25, height=25, corner_radius=0, bg_color="transparent", fg_color="transparent")
        checkmark6.place(x=355, y=435)

    if achievement7_completed == True:
        checkmark7 = customtkinter.CTkLabel(achievement_window, image=checkmark_bg, text="",
                                            width=25, height=25, corner_radius=0, bg_color="transparent", fg_color="transparent")
        checkmark7.place(x=355, y=515)

    achievement_window.mainloop()

# Main Loop (Main Game)
def main_loop():
    global amount_of_blocks_label, blocks_per_second_label, blocks_per_second_label, price_text1, price_text2, price_text3, big_block_button, achievement1, achievement2, achievement3, achievement4, achievement5, achievement6, achievement7, back_right_button, overworld_amount_label, netherworld_amount_label, endworld_amount_label

    # Main Window Options (Config)
    main = customtkinter.CTk()
    w = 1000
    h = 600
    ws = main.winfo_screenwidth()
    hs = main.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    main.geometry('%dx%d+%d+%d' % (w, h, x, y))
    main.resizable(False, False)
    main.title("Minecraft Clicker | 3.12.2 64-Bit")

    # Left Side (Clicking Side)
    bg_left = customtkinter.CTkLabel(main, image=bg_black, text="", width=406,
                                     height=600, corner_radius=0, fg_color="transparent", bg_color="transparent")
    bg_left.place(x=-5, y=300, anchor="w") # Background Left

    bg_sign_label = customtkinter.CTkLabel(
        main, image=sign_bg, text="", width=245, height=145, corner_radius=0)
    bg_sign_label.place(x=70, y=90, anchor="w") # Stone Sign Bg Left

    amount_of_blocks_label = customtkinter.CTkLabel(main, text=str(
        amount_of_blocks), font=customtkinter.CTkFont("Ubuntu", 39), bg_color="#868586")
    amount_of_blocks_label.place(x=195, y=55, anchor="c") # Number Of Blocks (Continually Updating)

    labelish = str(bps) + " per second"
    blocks_per_second_label = customtkinter.CTkLabel(
        main, text=labelish, font=customtkinter.CTkFont("Ubuntu", 20), bg_color="#868586")
    blocks_per_second_label.place(x=195, y=115, anchor="center") # Blocks Per Second (Continually Updating)

    big_block_icon = customtkinter.CTkLabel(main, image=dirt_block, text="", width=230,
                                            height=230, corner_radius=0, bg_color="transparent", fg_color="transparent")
    big_block_icon.place(x=75, y=350, anchor="w") # Main Button (Icon)

    def big_block_pressed(): # Main Button Callback (big_block_button)
        global amount_of_blocks
        amount_of_blocks += click_amount
        amount_of_blocks = round(amount_of_blocks, 1)
        number_number = len(str(amount_of_blocks))
        if number_number < 9:
            number_count()
        number_count()
        change_picture()
        if amount_of_blocks > 999:
            audio.clicked_hard_blocks()
        elif amount_of_blocks < 1000:
            audio.clicked_dirty_blocks()

    big_block_button = customtkinter.CTkButton(main, image=dirt_block, text="", width=230, height=230, corner_radius=0, bg_color="transparent",
                                               fg_color="transparent", border_width=0, border_spacing=0, hover=True, hover_color=dirt_block_color, command=big_block_pressed)
    big_block_button.place(x=75, y=350, anchor="w") # Main Button (Button)

    bg_right = customtkinter.CTkButton(main, image=bg_blue, text="", width=400,
                                       height=606, corner_radius=0, fg_color="transparent", bg_color="transparent")
    bg_right.place(x=400, y=416, anchor="w") # Lower Right Bg

    overworld_bg_label = customtkinter.CTkButton(main, image=overworld_bg, text="", width=600,
                                                 height=150, corner_radius=0, fg_color="transparent", bg_color="transparent", state="disabled")
    overworld_bg_label.place(x=400, y=76, anchor="w") # Upper Right Bg

    price_bg1 = customtkinter.CTkLabel(
        main, image=price_bg, text="", width=100, height=56, corner_radius=0, fg_color="transparent", bg_color="transparent")
    price_bg1.place(x=412, y=114, anchor="w") # Price Bg

    price_text1 = customtkinter.CTkLabel(
        main, text=overworld_cost, bg_color="#868586", font=customtkinter.CTkFont("Ubuntu", 20))
    price_text1.place(x=464, y=111, anchor="c") # Cost Of Overworld Upgrade (Continually Updating)

    def overworld_button_callback(): # Overworld Button Callback (overworld_button_button)
        global click_amount, overworld_cost_multiplyer, overworld_cost, overworld_click, amount_of_blocks, price_text1, overworld_amount, overworld_amount_label
        audio.click()
        if amount_of_blocks >= overworld_cost:
            amount_of_blocks = amount_of_blocks - overworld_cost
            amount_of_blocks = round(amount_of_blocks, 1)
            number_count()
            click_amount = click_amount + \
                (overworld_click * overworld_cost_multiplyer)
            if overworld_cost_multiplyer >= 1.4:
                pass
            elif overworld_cost_multiplyer == 1:
                overworld_cost_multiplyer += 0.4
            overworld_cost = overworld_cost * overworld_cost_multiplyer
            overworld_cost = round(overworld_cost, 1)
            price_text1.configure(text=overworld_cost)
            change_picture()
            overworld_amount += 1
            overworld_amount_entry = (str(overworld_amount)) + "x"
            overworld_amount_label.configure(text=overworld_amount_entry)
        elif amount_of_blocks < overworld_cost:
            pass

    overworld_button_button = customtkinter.CTkButton(
        main, image=overworld_button, text="", width=80, height=60, corner_radius=0, fg_color="transparent", bg_color="transparent", border_width=0, border_spacing=0, hover=True, hover_color="#7dbb1d", command=overworld_button_callback)
    overworld_button_button.place(x=412, y=40, anchor="w") # Overworld Button (Button)

    placement_bg1 = customtkinter.CTkLabel(main, image=placement_bg, width=10, height=40, text="",
                                           corner_radius=0, fg_color="transparent", bg_color="transparent")
    placement_bg1.place(x=893, y=125, anchor="w") # Steve Face (Icon)

    def overworld_callback(): # Steve Click Callback (overworld_placement_button)
        global overworld_button, overworld_cost, overworld_cost_multiplyer, steve_click
        if steve_click == 0:
            audio.click_overworld()
            overworld_placement_button.configure(image=overworld_placement2)
            steve_click += 1
        elif steve_click > 0:
            audio.click_overworld()
            secret_menu()

    overworld_placement_button = customtkinter.CTkButton(
        main, image=overworld_placement, text="", width=20, height=20, corner_radius=0, bg_color="#858685", fg_color="#858685", hover_color="#858685", command=overworld_callback)
    overworld_placement_button.place(x=897, y=125, anchor="w")  # Steve Face (Button)

    overworld_amount_entry = (str(overworld_amount)) + "x"
    overworld_amount_label = customtkinter.CTkLabel(
        main, text=overworld_amount_entry, corner_radius=0, fg_color="transparent", bg_color="#868686", font=customtkinter.CTkFont("ubuntu", 17))
    overworld_amount_label.place(x=951, y=123, anchor="c") # Amount Of Overworld Upgrades

    netherworld_bg_label = customtkinter.CTkButton(main, image=netherworld_bg, text="", width=600,
                                                   height=150, corner_radius=0, fg_color="transparent", bg_color="transparent", state="disabled")
    netherworld_bg_label.place(x=400, y=246, anchor="w") # Middle Right Bg

    price_bg2 = customtkinter.CTkLabel(
        main, image=price_bg, text="", width=100, height=56, corner_radius=0, fg_color="transparent", bg_color="transparent")
    price_bg2.place(x=412, y=282, anchor="w") # Price Bg

    price_text2 = customtkinter.CTkLabel(
        main, text=netherworld_cost, bg_color="#868586", font=customtkinter.CTkFont("Ubuntu", 20))
    price_text2.place(x=464, y=279, anchor="c") # Cost Of Netherworld Upgrade (Continually Updating)

    def nether_button_callback(): # Netherworld Button Callback (netherworld_button_button)
        global netherworld_cost_multiplyer, netherworld_cost, amount_of_blocks, bps, netherworld_click_per_second, blocks_per_second_label, price_text2, netherworld_amount, netherworld_amount_label
        audio.click()
        if amount_of_blocks >= netherworld_cost:
            amount_of_blocks = amount_of_blocks - netherworld_cost
            amount_of_blocks = round(amount_of_blocks, 1)
            number_count()
            bps = bps + (netherworld_click_per_second *
                         netherworld_cost_multiplyer)
            bps = round(bps, 1)
            labelish = str(bps) + " per second"
            blocks_per_second_label.configure(text=labelish)
            if netherworld_cost_multiplyer >= 1.4:
                pass
            elif netherworld_cost_multiplyer == 1:
                netherworld_cost_multiplyer += 0.4
            netherworld_cost = netherworld_cost * netherworld_cost_multiplyer
            netherworld_cost = round(netherworld_cost, 1)
            price_text2.configure(text=netherworld_cost)
            change_picture()
            netherworld_amount += 1
            netherworld_amount_entry = (str(netherworld_amount)) + "x"
            netherworld_amount_label.configure(text=netherworld_amount_entry)
        elif amount_of_blocks < netherworld_cost:
            pass

    nether_button_button = customtkinter.CTkButton(
        main, image=nether_button, text="", width=80, height=60, corner_radius=0, fg_color="transparent", bg_color="transparent", border_width=0, border_spacing=0, hover=True, hover_color="#83140b", command=nether_button_callback)
    nether_button_button.place(x=412, y=212, anchor="w") # Netherworld Button (Button)

    placement_bg2 = customtkinter.CTkLabel(main, image=placement_bg, width=10, height=40, text="",
                                           corner_radius=0, fg_color="transparent", bg_color="transparent")
    placement_bg2.place(x=893, y=295, anchor="w")  # Pigman Face (Icon)

    def netherworld_callback():  # Pigman Click Callback (netherworld_placement_button)
        audio.click_nether()
        netherworld_placement_button.configure(image=netherworld_placement2)

    netherworld_placement_button = customtkinter.CTkButton(
        main, image=netherworld_placement, text="", width=20, height=20, corner_radius=0, bg_color="#858685", fg_color="#858685", hover_color="#858685", command=netherworld_callback)
    netherworld_placement_button.place(x=897, y=295, anchor="w") # Pigman Face (Button)

    netherworld_amount_entry = (str(netherworld_amount)) + "x"
    netherworld_amount_label = customtkinter.CTkLabel(
        main, text=netherworld_amount_entry, corner_radius=0, fg_color="transparent", bg_color="#868686", font=customtkinter.CTkFont("ubuntu", 17))
    netherworld_amount_label.place(x=951, y=293, anchor="c") # Amount Of Netherworld Upgrades

    theend_bg_label = customtkinter.CTkButton(main, image=theend_bg, text="", width=600, height=150,
                                              corner_radius=0, fg_color="transparent", bg_color="transparent", state="disabled")
    theend_bg_label.place(x=400, y=416, anchor="w") # Lower Right Bg

    price_bg3 = customtkinter.CTkLabel(
        main, image=price_bg, text="", width=100, height=56, corner_radius=0, fg_color="transparent", bg_color="transparent")
    price_bg3.place(x=412, y=452, anchor="w")  # Price Bg

    price_text3 = customtkinter.CTkLabel(
        main, text=endworld_cost, bg_color="#868586", font=customtkinter.CTkFont("Ubuntu", 20))
    price_text3.place(x=464, y=449, anchor="c") # Cost Of Endworld Upgrade (Continually Updating)

    def theend_button_callback():  # Endworld Button Callback (endworld_button_button)
        global endworld_cost_multiplyer, endworld_cost, amount_of_blocks, bps, endworld_click_per_second, blocks_per_second_label, price_text3, endworld_amount, endworld_amount_label
        audio.click()
        if amount_of_blocks >= endworld_cost:
            amount_of_blocks = amount_of_blocks - endworld_cost
            amount_of_blocks = round(amount_of_blocks, 1)
            number_count()
            bps = bps + (bps *
                         0.3)
            bps = round(bps, 1)
            labelish = str(bps) + " per second"
            blocks_per_second_label.configure(text=labelish)
            if endworld_cost_multiplyer >= 1.4:
                pass
            elif endworld_cost_multiplyer == 1:
                endworld_cost_multiplyer += 0.4
            endworld_cost = endworld_cost * endworld_cost_multiplyer
            endworld_cost = round(endworld_cost, 1)
            price_text3.configure(text=endworld_cost)
            change_picture()
            endworld_amount += 1
            endworld_amount_entry = (str(endworld_amount)) + "x"
            endworld_amount_label.configure(text=endworld_amount_entry)
        elif amount_of_blocks < endworld_cost:
            pass

    theend_button_button = customtkinter.CTkButton(
        main, image=theend_button, text="", width=80, height=60, corner_radius=0, fg_color="transparent", bg_color="transparent", border_width=0, border_spacing=0, hover=True, hover_color="#c37de7", command=theend_button_callback)
    theend_button_button.place(x=412, y=381, anchor="w") # Endworld Button (Button)

    placement_bg3 = customtkinter.CTkLabel(main, image=placement_bg, width=10, height=40, text="",
                                           corner_radius=0, fg_color="transparent", bg_color="transparent")
    placement_bg3.place(x=893, y=465, anchor="w")  # Enderman Face (Icon)

    def endworld_callback():  # Enderman Click Callback (endworld_placement_button)
        audio.click_ender()
        endworld_placement_button.configure(image=endworld_placement2)

    endworld_placement_button = customtkinter.CTkButton(
        main, image=endworld_placement, text="", width=20, height=20, corner_radius=0, bg_color="#858685", fg_color="#858685", hover_color="#858685", command=endworld_callback)
    endworld_placement_button.place(x=897, y=465, anchor="w") # Enderman Face (Button)

    endworld_amount_entry = (str(endworld_amount)) + "x"
    endworld_amount_label = customtkinter.CTkLabel(
        main, text=endworld_amount_entry, corner_radius=0, fg_color="transparent", bg_color="#868686", font=customtkinter.CTkFont("ubuntu", 17))
    endworld_amount_label.place(x=951, y=463, anchor="c") # Amount Of Endworld Upgrades

    # Achievement Icons
    achievement1 = customtkinter.CTkLabel(
        main, image=achievement1_locked, text="", width=48, height=76, fg_color="transparent", bg_color="transparent")
    achievement1.place(x=412, y=556, anchor="w") 

    achievement2 = customtkinter.CTkLabel(
        main, image=achievement2_locked, text="", width=48, height=76, fg_color="transparent", bg_color="transparent")
    achievement2.place(x=469, y=556, anchor="w")

    achievement3 = customtkinter.CTkLabel(
        main, image=achievement3_locked, text="", width=48, height=76, fg_color="transparent", bg_color="transparent")
    achievement3.place(x=526, y=556, anchor="w")

    achievement4 = customtkinter.CTkLabel(
        main, image=achievement4_locked, text="", width=48, height=76, fg_color="transparent", bg_color="transparent")
    achievement4.place(x=583, y=556, anchor="w")

    achievement5 = customtkinter.CTkLabel(
        main, image=achievement5_locked, text="", width=48, height=76, fg_color="transparent", bg_color="transparent")
    achievement5.place(x=640, y=556, anchor="w")

    achievement6 = customtkinter.CTkLabel(
        main, image=achievement6_locked, text="", width=48, height=76, fg_color="transparent", bg_color="transparent")
    achievement6.place(x=697, y=556, anchor="w")

    achievement7 = customtkinter.CTkLabel(
        main, image=achievement7_locked, text="", width=48, height=76, fg_color="transparent", bg_color="transparent")
    achievement7.place(x=754, y=556, anchor="w")

    def achievement_list_callback(): # Achievement Window Callback (achievementList_button)
        achievement_list_callback2()

    achievementList_button = customtkinter.CTkButton(
        main, image=achievementList_bg, text="", width=179, height=69, fg_color="transparent", bg_color="transparent", corner_radius=0, border_width=0, border_spacing=0, hover=True, hover_color="#868686", command=achievement_list_callback)
    achievementList_button.place(x=811, y=556, anchor="w") # Achievement Button Window

    # Window Seperators
    panelSeperate1 = customtkinter.CTkLabel(main, image=panelSeperator_side, text="",
                                            width=600, height=18, corner_radius=0, fg_color="transparent", bg_color="transparent")
    panelSeperate1.place(x=400, y=161, anchor="w")

    panelSeperate2 = customtkinter.CTkLabel(main, image=panelSeperator_side, text="",
                                            width=600, height=18, corner_radius=0, fg_color="transparent", bg_color="transparent")
    panelSeperate2.place(x=400, y=331, anchor="w")

    panelSeperate3 = customtkinter.CTkLabel(main, image=panelSeperator_side, text="",
                                            width=600, height=18, corner_radius=0, fg_color="transparent", bg_color="transparent")
    panelSeperate3.place(x=400, y=501, anchor="w")

    panelSeperate4 = customtkinter.CTkLabel(main, image=panelSeperator_up, text="", width=18,
                                            height=600, corner_radius=0, fg_color="transparent", bg_color="transparent")
    panelSeperate4.place(x=385, y=300, anchor="w")

    # Config
    def back_right_button_callback(): # Config Button Callback (back_right_button)
        global settings_button, info_button, back_left_button
        audio.click()
        back_right_button.destroy()

        def settings_button_callback():
            global settings_button, info_button, back_left_button, save_button, load_button, back_left_button2
            audio.click()
            settings_button.destroy()
            info_button.destroy()
            back_left_button.destroy()

            def save_button_callback():
                audio.click()
                save_button_callback2()

            def load_button_callback():
                audio.click()
                load_button_callback2()

            save_button = customtkinter.CTkButton(main, image=save_bg, text="", width=100, height=40, fg_color="transparent",
                                                  bg_color="transparent", corner_radius=0, border_width=0, border_spacing=0, hover=True, hover_color="#868686", command=save_button_callback)
            save_button.place(x=0, y=576, anchor="w")

            load_button = customtkinter.CTkButton(main, image=load_bg, text="", width=100, height=40, fg_color="transparent",
                                                  bg_color="transparent", corner_radius=0, border_width=0, border_spacing=0, hover=True, hover_color="#868686", command=load_button_callback)
            load_button.place(x=106, y=576, anchor="w")

            def back_left_button2_callback():
                global settings_button, info_button, back_left_button, save_button, load_button, back_left_button2
                audio.click()
                save_button.destroy()
                load_button.destroy()
                back_left_button2.destroy()

                settings_button = customtkinter.CTkButton(main, image=settings_bg, text="", width=40, height=40, fg_color="transparent",
                                                          bg_color="transparent", corner_radius=0, border_width=0, border_spacing=0, hover=True, hover_color="#868686", command=settings_button_callback)
                settings_button.place(x=0, y=576, anchor="w")

                info_button = customtkinter.CTkButton(main, image=info_bg, text="", width=40, height=40, fg_color="transparent",
                                                      bg_color="transparent", corner_radius=0, border_width=0, border_spacing=0, hover=True, hover_color="#868686", command=info_button_callback)
                info_button.place(x=46, y=576, anchor="w")

                back_left_button = customtkinter.CTkButton(main, image=back_left_bg, text="", width=40, height=40, fg_color="transparent",
                                                           bg_color="transparent", corner_radius=0, border_width=0, border_spacing=0, hover=True, hover_color="#868686", command=back_left_button_callback)
                back_left_button.place(x=92, y=576, anchor="w")

            back_left_button2 = customtkinter.CTkButton(main, image=back_left_bg, text="", width=40, height=40, fg_color="transparent",
                                                        bg_color="transparent", corner_radius=0, border_width=0, border_spacing=0, hover=True, hover_color="#868686", command=back_left_button2_callback)
            back_left_button2.place(x=212, y=576, anchor="w")

        settings_button = customtkinter.CTkButton(main, image=settings_bg, text="", width=40, height=40, fg_color="transparent",
                                                  bg_color="transparent", corner_radius=0, border_width=0, border_spacing=0, hover=True, hover_color="#868686", command=settings_button_callback)
        settings_button.place(x=0, y=576, anchor="w")

        def info_button_callback():
            audio.click()
            info_button_callback2()

        info_button = customtkinter.CTkButton(main, image=info_bg, text="", width=40, height=40, fg_color="transparent",
                                              bg_color="transparent", corner_radius=0, border_width=0, border_spacing=0, hover=True, hover_color="#868686", command=info_button_callback)
        info_button.place(x=46, y=576, anchor="w")

        def back_left_button_callback():
            audio.click()
            settings_button.destroy()
            info_button.destroy()
            back_right_button = customtkinter.CTkButton(main, image=back_right_bg, text="", width=40, height=40, fg_color="transparent",
                                                        bg_color="transparent", corner_radius=0, border_width=0, border_spacing=0, hover=True, hover_color="#868686", command=back_right_button_callback)
            back_right_button.place(x=0, y=576, anchor="w")

            back_left_button.destroy()

        back_left_button = customtkinter.CTkButton(main, image=back_left_bg, text="", width=40, height=40, fg_color="transparent",
                                                   bg_color="transparent", corner_radius=0, border_width=0, border_spacing=0, hover=True, hover_color="#868686", command=back_left_button_callback)
        back_left_button.place(x=92, y=576, anchor="w")

    back_right_button = customtkinter.CTkButton(main, image=back_right_bg, text="", width=40, height=40, fg_color="transparent",
                                                bg_color="transparent", corner_radius=0, border_width=0, border_spacing=0, hover=True, hover_color="#868686", command=back_right_button_callback)
    back_right_button.place(x=0, y=576, anchor="w")

    # Start Multi-Thread
    increment_thread = threading.Thread(target=increment_blocks)
    increment_thread.daemon = True
    increment_thread.start()

    main.mainloop()

# Properly Format Numbers in amount_of_blocks
def number_count():
    global amount_of_blocks, amount_of_blocks_label
    characters_amount_of_blocks = len(str(amount_of_blocks))
    if (characters_amount_of_blocks > 8) and (characters_amount_of_blocks < 12):
        amount_of_blocks_str = str(amount_of_blocks)
        if characters_amount_of_blocks == 9:
            first_digit = amount_of_blocks_str[:1]   # Get the first digit
            next_three_digits = amount_of_blocks_str[1:4]
            result = f"{first_digit}.{next_three_digits} Million"
            amount_of_blocks_label.configure(text=str(result))
        elif characters_amount_of_blocks == 10:
            first_digit = amount_of_blocks_str[:2]   # Get the first digit
            next_three_digits = amount_of_blocks_str[2:4]
            result = f"{first_digit}.{next_three_digits} Million"
            amount_of_blocks_label.configure(text=str(result))
        elif characters_amount_of_blocks == 11:
            first_digit = amount_of_blocks_str[:3]   # Get the first digit
            # Get the next three digits
            next_three_digits = amount_of_blocks_str[3:4]
            result = f"{first_digit}.{next_three_digits} Million"
            amount_of_blocks_label.configure(text=str(result))
    elif (characters_amount_of_blocks > 11) and (characters_amount_of_blocks < 15):
        amount_of_blocks_str = str(amount_of_blocks)
        if characters_amount_of_blocks == 12:

            first_digit = amount_of_blocks_str[:1]   # Get the first digit
            # Get the next three digits
            next_three_digits = amount_of_blocks_str[1:4]
            result = f"{first_digit}.{next_three_digits} Billion"
            amount_of_blocks_label.configure(text=str(result))
        elif characters_amount_of_blocks == 13:

            first_digit = amount_of_blocks_str[:2]   # Get the first digit
            # Get the next three digits
            next_three_digits = amount_of_blocks_str[2:4]
            result = f"{first_digit}.{next_three_digits} Billion"
            amount_of_blocks_label.configure(text=str(result))
        elif characters_amount_of_blocks == 14:

            first_digit = amount_of_blocks_str[:3]   # Get the first digit
            # Get the next three digits
            next_three_digits = amount_of_blocks_str[3:4]
            result = f"{first_digit}.{next_three_digits} Billion"
            amount_of_blocks_label.configure(text=str(result))
    elif (characters_amount_of_blocks > 14) and (characters_amount_of_blocks < 18):
        amount_of_blocks_str = str(amount_of_blocks)
        if characters_amount_of_blocks == 15:

            first_digit = amount_of_blocks_str[:1]   # Get the first digit
            # Get the next three digits
            next_three_digits = amount_of_blocks_str[1:4]
            result = f"{first_digit}.{next_three_digits} Trillion"
            amount_of_blocks_label.configure(text=str(result))
        elif characters_amount_of_blocks == 16:

            first_digit = amount_of_blocks_str[:2]   # Get the first digit
            # Get the next three digits
            next_three_digits = amount_of_blocks_str[2:4]
            result = f"{first_digit}.{next_three_digits} Trillion"
            amount_of_blocks_label.configure(text=str(result))
        elif characters_amount_of_blocks == 17:

            first_digit = amount_of_blocks_str[:3]   # Get the first digit
            # Get the next three digits
            next_three_digits = amount_of_blocks_str[3:4]
            result = f"{first_digit}.{next_three_digits} Trillion"
            amount_of_blocks_label.configure(text=str(result))
    elif (characters_amount_of_blocks > 17) and (characters_amount_of_blocks < 21):
        amount_of_blocks_str = str(amount_of_blocks)
        if characters_amount_of_blocks == 18:

            first_digit = amount_of_blocks_str[:1]   # Get the first digit
            # Get the next three digits
            next_three_digits = amount_of_blocks_str[1:4]
            result = f"{first_digit}.{next_three_digits} Quadrillion"
            amount_of_blocks_label.configure(text=str(result))
        elif characters_amount_of_blocks == 19:

            first_digit = amount_of_blocks_str[:2]   # Get the first digit
            # Get the next three digits
            next_three_digits = amount_of_blocks_str[2:4]
            result = f"{first_digit}.{next_three_digits} Quadrillion"
            amount_of_blocks_label.configure(text=str(result))
        elif characters_amount_of_blocks == 20:

            first_digit = amount_of_blocks_str[:3]   # Get the first digit
            # Get the next three digits
            next_three_digits = amount_of_blocks_str[3:4]
            result = f"{first_digit}.{next_three_digits} Quadrillion"
            amount_of_blocks_label.configure(text=str(result))
    elif (characters_amount_of_blocks > 20) and (characters_amount_of_blocks < 24):
        amount_of_blocks_str = str(amount_of_blocks)
        if characters_amount_of_blocks == 21:

            first_digit = amount_of_blocks_str[:1]   # Get the first digit
            # Get the next three digits
            next_three_digits = amount_of_blocks_str[1:4]
            result = f"{first_digit}.{next_three_digits} Quintillion"
            amount_of_blocks_label.configure(text=str(result))
        elif characters_amount_of_blocks == 22:

            first_digit = amount_of_blocks_str[:2]   # Get the first digit
            # Get the next three digits
            next_three_digits = amount_of_blocks_str[2:4]
            result = f"{first_digit}.{next_three_digits} Quintillion"
            amount_of_blocks_label.configure(text=str(result))
        elif characters_amount_of_blocks == 23:

            first_digit = amount_of_blocks_str[:3]   # Get the first digit
            # Get the next three digits
            next_three_digits = amount_of_blocks_str[3:4]
            result = f"{first_digit}.{next_three_digits} Quintillion"
            amount_of_blocks_label.configure(text=str(result))
    elif (characters_amount_of_blocks > 23) and (characters_amount_of_blocks < 27):
        amount_of_blocks_str = str(amount_of_blocks)
        if characters_amount_of_blocks == 24:

            first_digit = amount_of_blocks_str[:1]   # Get the first digit
            # Get the next three digits
            next_three_digits = amount_of_blocks_str[1:4]
            result = f"{first_digit}.{next_three_digits} Sextillion"
            amount_of_blocks_label.configure(text=str(result))
        elif characters_amount_of_blocks == 25:

            first_digit = amount_of_blocks_str[:2]   # Get the first digit
            # Get the next three digits
            next_three_digits = amount_of_blocks_str[2:4]
            result = f"{first_digit}.{next_three_digits} Sextillion"
            amount_of_blocks_label.configure(text=str(result))
        elif characters_amount_of_blocks == 26:

            first_digit = amount_of_blocks_str[:3]   # Get the first digit
            # Get the next three digits
            next_three_digits = amount_of_blocks_str[3:4]
            result = f"{first_digit}.{next_three_digits} Sextillion"
            amount_of_blocks_label.configure(text=str(result))
    elif characters_amount_of_blocks < 9:
        amount_of_blocks_label.configure(text=str(amount_of_blocks))

# Change big_block icon/button
def change_picture():
    global amount_of_blocks, big_block_button, achievement1, achievement2, achievement3, achievement4, achievement5, achievement6, achievement7, bps, achievement1_completed, achievement2_completed, achievement3_completed, achievement4_completed, achievement5_completed, achievement6_completed, achievement7_completed
    if (amount_of_blocks > -1) and (amount_of_blocks < 100):
        big_block_button.configure(
            image=dirt_block, hover_color=dirt_block_color)
    elif (amount_of_blocks > 99) and (amount_of_blocks < 1000):
        achievement1.configure(image=achievement1_unlocked)
        big_block_button.configure(
            image=grass_block, hover_color=grass_block_color)
        achievement1_completed = True
    elif (amount_of_blocks > 999) and (amount_of_blocks < 10000):
        achievement2.configure(image=achievement2_unlocked)
        big_block_button.configure(
            image=stone_block, hover_color=stone_block_color)
        achievement2_completed = True
    elif (amount_of_blocks > 9999) and (amount_of_blocks < 100000):
        achievement3.configure(image=achievement3_unlocked)
        big_block_button.configure(
            image=iron_block, hover_color=iron_block_color)
        achievement3_completed = True
    elif (amount_of_blocks > 99999) and (amount_of_blocks < 1000000):
        achievement4.configure(image=achievement4_unlocked)
        big_block_button.configure(
            image=gold_block, hover_color=gold_block_color)
        achievement4_completed = True
    elif (amount_of_blocks > 999999) and (amount_of_blocks < 1000000000):
        achievement5.configure(image=achievement5_unlocked)
        big_block_button.configure(
            image=diamond_block, hover_color=diamond_block_color)
        achievement5_completed = True
    elif (amount_of_blocks > 999999999):
        achievement6.configure(image=achievement6_unlocked)
        big_block_button.configure(
            image=netherite_block, hover_color=netherite_block_color)
        achievement6_completed = True
    elif (amount_of_blocks > 999999999) and (bps > 99999):
        achievement7.configure(image=achievement7_unlocked)
        achievement7_completed = True

# Blocks Per Second Routine
def increment_blocks():
    global amount_of_blocks, amount_of_blocks_label
    while True:
        amount_of_blocks += bps
        amount_of_blocks = round(amount_of_blocks, 1)
        number_number = len(str(amount_of_blocks))
        if number_number > 8:
            number_count()
        number_count()
        change_picture()
        time.sleep(1)

# Run Main
main_loop()