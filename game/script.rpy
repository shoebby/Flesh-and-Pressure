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

image f_nameplate:
    'f_nameplate1'
    0.15
    'f_nameplate2'
    0.15
    choice:
        'f_nameplate3'
        0.15
    choice:
        'f_nameplate2'
        0.15
    choice:
        'f_nameplate1'
        0.15
    choice:
        'f_nameplate4'
        0.15
    'f_nameplate3'
    0.15
    'f_nameplate4'
    0.15
    repeat

image f_body_work:
    'f_body_work1'
    0.15
    'f_body_work2'
    0.15
    'f_body_work3'
    0.15
    repeat

image f_body_tank:
    'f_body_tank1'
    0.15
    'f_body_tank2'
    0.15
    'f_body_tank3'
    0.15
    repeat

image f_exp_neutral:
    'f_exp_neutral1'
    0.15
    'f_exp_neutral2'
    0.15
    'f_exp_neutral3'
    0.15
    repeat
image f_exp_stressed:
    'f_exp_stressed1'
    0.15
    'f_exp_stressed2'
    0.15
    'f_exp_stressed3'
    0.15
    repeat
image f_exp_flustered:
    'f_exp_flustered1'
    0.15
    'f_exp_flustered2'
    0.15
    'f_exp_flustered3'
    0.15
    repeat
image f_exp_exerted:
    'f_exp_exerted1'
    0.15
    'f_exp_exerted2'
    0.15
    'f_exp_exerted3'
    0.15
    repeat
image f_exp_nervous:
    'f_exp_nervous1'
    0.15
    'f_exp_nervous2'
    0.15
    'f_exp_nervous3'
    0.15
    repeat
image f_exp_edge:
    'f_exp_edge1'
    0.15
    'f_exp_edge2'
    0.15
    'f_exp_edge3'
    0.15
    repeat
image f_exp_bust:
    'f_exp_bust1'
    0.15
    'f_exp_bust2'
    0.15
    'f_exp_bust3'
    0.15
    repeat

transform portrait:
    xpos 520
    ypos 70
    xsize 150
    ysize 175

transform scroll_scanlines:
    ypos -1.5
    pause 0.1
    choice:
        ypos -1.01
    choice:
        ypos -1.05
    choice:
        ypos -1.02
    choice:
        ypos -1.98
    pause 0.1
    repeat

transform flicker_left:
    xpos 0.0
    choice:
        0.1
        xpos -0.004
    choice:
        0.2
        xpos -0.002
    choice:
        0.3
        xpos -0.001
    0.1
    choice:
        0.1
        xpos 0.001
    choice:
        0.2
        xpos 0.005
    choice:
        0.3
        xpos 0.02
    0.1
    choice:
        0.05
        xpos 0.001
    choice:
        0.05
        xpos 0.005
    choice:
        0.05
        xpos 0.001
    choice:
        0.05
        xpos 0.005
    choice:
        0.05
        xpos 0.1
    0.1
    choice:
        0.1
    choice:
        0.1
    choice:
        0.05
    repeat

transform flicker_up:
    ypos 0.0
    choice:
        0.4
    choice:
        0.9
    choice:
        1.9
    0.1
    choice:
        linear 6 ypos -0.2
    choice:
        ypos -0.03
    choice:
        ypos 0.05
    0.2
    ypos 0.0
    choice:
        0.4
    choice:
        0.9
    choice:
        1.4
    0.1
    choice:
        ypos -0.1
    choice:
        ypos -0.05
    choice:
        ypos 0.02
    0.1
    choice:
        0.4
    choice:
        0.9
    choice:
        1.4
    repeat

transform flicker_down:
    ypos 0.0
    choice:
        0.1
    choice:
        0.1
    choice:
        0.05
    choice:
        ypos -0.03
        choice:
            0.1
        choice:
            0.1
        choice:
            0.05
    choice:
        ypos -0.005
        choice:
            0.1
        choice:
            0.1
        choice:
            0.05
    choice:
        ypos 0.0
        choice:
            0.1
        choice:
            0.1
        choice:
            0.05
    choice:
        ypos -0.01
        choice:
            0.1
        choice:
            0.1
        choice:
            0.05
    repeat

image backyard_red:
    "backyard_r"
    flicker_left
    
image backyard_green:
    "backyard_g"
    flicker_down
    
image backyard_blue:
    "backyard_b"
    flicker_up

image pulse_scanlines:
    "scanlines"
    
    alpha 1.0
    linear 3 alpha 0.2
    linear 2  alpha 1.0

    linear 0.05 alpha 0.1
    linear 0.05 alpha 1.0

    linear 0.2 alpha 0.1
    linear 0.1 alpha 1.0

    linear 3 alpha 0.2
    linear 2  alpha 1.0

    linear 3 alpha 0.2
    linear 2  alpha 1.0
    repeat

image lift:
    'lift1' with Dissolve(2.5)
    3
    'lift2' with Dissolve(2.5)
    3
    'lift3' with Dissolve(2.5)
    3
    repeat

layeredimage itske:
    group body:
        attribute work default:
            "f_body_work"
        attribute tank:
            "f_body_tank"

    group face:
        attribute neutral default:
            "f_exp_neutral"
        attribute stressed:
            "f_exp_stressed"
        attribute flustered:
            "f_exp_flustered"
        attribute exerted:
            "f_exp_exerted"
        attribute nervous:
            "f_exp_nervous"
        attribute edge:
            "f_exp_edge"
        attribute bust:
            "f_exp_bust"

    group nameplate:
        attribute nameplate default:
            "f_nameplate"

layeredimage bg:
    group image_main:
        attribute backyard default:
            "backyard_main"

    group image_red:
        attribute backyard_r default:
            "backyard_red"
            blend "add"

    group image_green:
        attribute backyard_g default:
            "backyard_green"
            blend "add"

    group image_blue:
        attribute backyard_b default:
            "backyard_blue"
            blend "add"
            
    group scanlines:
        attribute scanlines default:
            at scroll_scanlines
            "pulse_scanlines"
            blend "add"

init python:
    renpy.music.register_channel("sound2")
    preferences.text_cps = 100