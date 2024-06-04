from pygame import mixer
import random

mixer.init()
mixer.set_num_channels(100000)


def clicked_hard_blocks():
    random_sound = random.randint(1, 2)
    if random_sound == 1:
        clicked = mixer.Sound("break1.mp3")
        clicked.set_volume(0.5)
        clicked1 = mixer.find_channel()
        clicked1.play(clicked)
    elif random_sound == 2:
        clicked = mixer.Sound("break4.mp3")
        clicked.set_volume(0.5)
        clicked1 = mixer.find_channel()
        clicked1.play(clicked)

def clicked_dirty_blocks():
    random_sound = random.randint(1, 3)
    if random_sound == 1:
        clicked = mixer.Sound("break3.mp3")
        clicked.set_volume(0.5)
        clicked1 = mixer.find_channel()
        clicked1.play(clicked)
    elif random_sound == 2:
        clicked = mixer.Sound("break2.mp3")
        clicked.set_volume(1)
        clicked1 = mixer.find_channel()
        clicked1.play(clicked)
    elif random_sound == 3:
        clicked = mixer.Sound("break5.mp3")
        clicked.set_volume(1)
        clicked1 = mixer.find_channel()
        clicked1.play(clicked)

def click():
    clicked = mixer.Sound("click.mp3")
    clicked.set_volume(0.5)
    clicked1 = mixer.find_channel()
    clicked1.play(clicked)

def achievement_sound():
    clicked = mixer.Sound("achievement_sound.mp3")
    clicked.set_volume(0.5)
    clicked1 = mixer.find_channel()
    clicked1.play(clicked)


def click_overworld():
    clicked = mixer.Sound("oof_sf.mp3")
    clicked.set_volume(0.5)
    clicked1 = mixer.find_channel()
    clicked1.play(clicked)


def click_nether():
    clicked = mixer.Sound("zombie_sf.mp3")
    clicked.set_volume(0.5)
    clicked1 = mixer.find_channel()
    clicked1.play(clicked)


def click_ender():
    clicked = mixer.Sound("enderman_sf.mp3")
    clicked.set_volume(0.5)
    clicked1 = mixer.find_channel()
    clicked1.play(clicked)








