label credits:
    play music "music/credits.ogg" noloop
    scene black
    $ renpy.pause(2.0, hard=True)
    scene credits_1 with dissolve
    $ renpy.pause(15.0, hard=True)
    scene credits_2 with dissolve
    $ renpy.pause(15.0, hard=True)
    scene credits_3 with dissolve
    $ renpy.pause(15.0, hard=True)
    scene credits_4 with dissolve
    $ renpy.pause(15.0, hard=True)
    scene credits_5 with dissolve
    $ renpy.pause(11.5, hard=True)
    scene credits_6 with dissolve
    $ renpy.pause(15.0, hard=True)
    scene black with dissolve
    $ renpy.pause(2.0, hard=True)
    play audio quack
    scene credits_7
    $ renpy.pause(0.1, hard=True)