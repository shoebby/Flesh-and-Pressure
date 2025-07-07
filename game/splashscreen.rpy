label splashscreen:
    scene splash1
    play music pressing
    $ renpy.pause(1.0, hard=True)
    show text "{size=+4}This is a story about loneliness and abandonment{/size}" with dissolve
    $ renpy.pause(2.0, hard=True)
    show text "{size=+4}Which includes potentially triggering material{/size}" with dissolve
    $ renpy.pause(2.0, hard=True)
    show text "{size=+4}Such as gore{/size}" with dissolve
    $ renpy.pause(2.0, hard=True)
    show text "{size=+4}Casual transphobia{/size}" with dissolve
    $ renpy.pause(2.0, hard=True)
    show text "{size=+4}And painful straggot flirting{/size}" with dissolve
    $ renpy.pause(2.0, hard=True)
    show text "{size=+4}It also includes flashing imagery{/size}" with dissolve
    $ renpy.pause(2.0, hard=True)
    hide text with dissolve
    $ renpy.pause(2.0, hard=True)
    show text "{size=+4}I hope this makes you smile, cry, or cum{/size}" with dissolve
    $ renpy.pause(0.5, hard=True)
    hide text
    stop music
    queue sound chaptercard
    scene splash2
    $ renpy.pause(0.5, hard=True)

    return