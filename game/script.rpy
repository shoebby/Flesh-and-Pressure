define j = Character("", kind=nvl, color="#ffffff", what_prefix="\"", what_suffix="\"") #jenn
define f = Character("", kind=nvl, color="#ffffff", what_color="#ffb787", what_prefix="\"", what_suffix="\"") #Itske
define f_t = Character("", kind=nvl, what_italic=True, what_color="#ff781f") #Itske mind-thoughts
define p = Character("", kind=nvl, color="#ffffff", what_color="#1f88ff", what_prefix="\"", what_suffix="\"") #piper
define m = Character("", kind=nvl, color="#ffffff", what_prefix="\"", what_suffix="\"") #mae
define t = Character("", kind=nvl, color="#ffffff", what_prefix="\"", what_suffix="\"") #tom
define c = Character("", kind=nvl, color="#ffffff", what_prefix="\"", what_suffix="\"") #cammy
define d = Character("", kind=nvl, color="#ffffff", what_prefix="\"", what_suffix="\"") #date
define d_t = Character("", kind=nvl, what_italic=True, what_color="#1fff97") #date mind-thoughts
define mt = Character("", kind=nvl, color="#ffffff", what_prefix="\"", what_suffix="\"") #meat
define piss = Character("", kind=nvl, color="#ffffff", what_prefix="\"", what_suffix="\"") #the pee on the floor
define chud = Character("", kind=nvl, color="#ffffff", what_prefix="\"", what_suffix="\"") #chud customer
define trash = Character("", kind=nvl, color="#ffffff", what_prefix="\"", what_suffix="\"") #trash


transform portrait:
    xpos 520
    ypos 70
    xsize 150
    ysize 175

image speaker girl std = "girl/girl_standard.png"
image speaker girl smile = "girl/girl_smile.png"
image speaker girl listening = "girl/girl_listening.png"
image speaker girl thinking = "girl/girl_thinking.png"
image speaker girl horny1 = "girl/girl_flustered.png"
image speaker girl horny2 = "girl/girl_excited.png"
image speaker girl horny3 = "girl/girl_hotnbothered.png"
image speaker girl horny4 = "girl/girl_edge.png"
image speaker girl horny5 = "girl/girl_busted.png"

image speaker manager = "others/manager.png"

image lift:
    'scenes/lift1.png' with Dissolve(4.0)
    pause 4.0
    'scenes/lift2.png' with Dissolve(4.0)
    pause 4.0
    'scenes/lift3.png' with Dissolve(4.0)
    pause 4.0
    repeat

init python:
    renpy.music.register_channel("sound2")
    preferences.text_cps = 100