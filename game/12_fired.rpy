label fired:
    scene ch12
    play audio "chaptercard.mp3"
    pause

    show bg office
    show speaker jenn enraged at portrait
    j "..."

    show speaker itske pouting at portrait
    f "..."

    show speaker jenn enraged at portrait
    j "You broke his nose, Itske."

    show speaker itske crying at portrait
    f "I-I'm sorry-"

    show speaker jenn enraged at portrait
    j "I know, save it for when... -If- you ever see him again."

    show speaker itske pouting at portrait
    f_t "Jenn seems to be deep in thought, she pinches the bridge of her nose and buries her face in her hands."
    show speaker itske disgust at portrait
    f_t "I've never seen her this upset, I fucked up bad."

    nvl clear
    show speaker itske thinking at portrait

    menu (nvl=True):
        f_t "Is there something I can say to get out of this...?"

        "{color=#fff}[[WHORE]{/color} Bribe her... Somehow, with something. Do I even have any savings left? Maybe she's into trannies?":
            show speaker itske nervous at portrait
            f "W-would you like-{nw}"

            show speaker jenn enraged at portrait
            j "Don't."

            show speaker itske pouting at portrait
            jump A1

        "{color=#fff}[[VICTIM]{/color} It... Wasn't my fault? Could try to go with that? He took a swing at me, for sure.":
            show speaker itske heartbroken at portrait
            f "Well he did-{nw}"

            show speaker jenn enraged at portrait
            j "No, let me think."

            show speaker itske pouting at portrait
            jump A2

        "{color=#fff}[[PUPPY]{/color} Begging might work. As pathetic as possible, preferably.":
            show speaker itske crying at portrait
            f "Jenn please I-{nw}"

            show speaker jenn enraged at portrait
            j "Stop."

            show speaker itske pouting at portrait
            jump A3

label A1:
    menu (nvl=True):
        f "..."
        "{color=#fff}[[VICTIM]{/color} It... Wasn't my fault? Could try to go with that? He took a swing at me, for sure.":
            show speaker itske heartbroken at portrait
            f "Well he did-{nw}"

            show speaker jenn enraged at portrait
            j "No, let me think."

            show speaker itske pouting at portrait
            jump B3

        "{color=#fff}[[PUPPY]{/color} Begging might work. As pathetic as possible, preferably.":
            show speaker itske crying at portrait
            f "Jenn please I-{nw}"

            show speaker jenn enraged at portrait
            j "Stop."

            show speaker itske pouting at portrait
            jump B2

label A2:
    menu (nvl=True):
        f "..."
        "{color=#fff}[[WHORE]{/color} Bribe her... Somehow, with something. Do I even have any savings left? Maybe she's into trannies?":
            show speaker itske nervous at portrait
            f "W-would you like-{nw}"

            show speaker jenn enraged at portrait
            j "Don't."

            show speaker itske pouting at portrait
            jump B3
        "{color=#fff}[[PUPPY]{/color} Begging might work. As pathetic as possible, preferably.":
            show speaker itske crying at portrait
            f "Jenn please I-{nw}"

            show speaker jenn enraged at portrait
            j "Stop."

            show speaker itske pouting at portrait
            jump B1

label A3:
    menu (nvl=True):
        f "..."
        "{color=#fff}[[WHORE]{/color} Bribe her... Somehow, with something. Do I even have any savings left? Maybe she's into trannies?":
            show speaker itske nervous at portrait
            f "W-would you like-{nw}"

            show speaker jenn enraged at portrait
            j "Don't."

            show speaker itske pouting at portrait
            jump B2
        "{color=#fff}[[VICTIM]{/color} It... Wasn't my fault? Could try to go with that? He took a swing at me, for sure.":
            show speaker itske heartbroken at portrait
            f "Well he did-{nw}"

            show speaker jenn enraged at portrait
            j "No, let me think."

            show speaker itske pouting at portrait
            jump B1

label B1:
    menu (nvl=True):
        f "..."
        "{color=#fff}[[WHORE]{/color} Bribe her... Somehow, with something. Do I even have any savings left? Maybe she's into trannies?":
            show speaker itske nervous at portrait
            f "W-would you like-{nw}"

            show speaker jenn enraged at portrait
            j "Don't."

            jump fired_end

label B2:
    menu (nvl=True):
        f "..."
        "{color=#fff}[[VICTIM]{/color} It... Wasn't my fault? Could try to go with that? He took a swing at me, for sure.":
            show speaker itske heartbroken at portrait
            f "Well he did-{nw}"

            show speaker jenn enraged at portrait
            j "No, let me think."

            jump fired_end

label B3:
    menu (nvl=True):
        f "..."
        "{color=#fff}[[PUPPY]{/color} Begging might work. As pathetic as possible, preferably.":
            show speaker itske crying at portrait
            f "Jenn please I-{nw}"

            show speaker jenn enraged at portrait
            j "Stop."

            jump fired_end

label fired_end:
    show speaker itske terrified at portrait
    f "... Is there anything-{nw}"

    show speaker jenn cringe at portrait
    j "Can you -please- shut up!"

    nvl clear

    show speaker itske scared at portrait
    f "..."

    show speaker jenn enraged at portrait
    j "God..."
    j "..."
    show speaker jenn worried at portrait
    j "I'm sorry."

    nvl clear

    show speaker itske crying at portrait
    f_t "After a moment of vulnerability her demeanor turns back to stone, she gets up to print a document."

    show speaker jenn enraged at portrait
    j "... You have 2 weeks left on your contract, after that you won't be working here anymore."
    j "I... Suggest you start looking for another job."

    nvl clear

    show speaker itske crying at portrait
    f_t "She hands me a freshly printed document."
    f_t "It's warm."
    f_t "The words are too blurry to make out."
    f_t "I hurriedly stuff it in one of my cargo pockets as her gaze bores into me."

    show speaker jenn enraged at portrait
    j "You won't need to finish your shift today, go home."
    j "I'll see you tomorrow."

    nvl clear
    scene lock_ch12
    play music lock_lick1 noloop
    scene lock_ch12_txt1 with Dissolve(1.0)
    scene lock_ch12_txt2 with Dissolve(1.0)
    scene lock_ch12_txt3 with Dissolve(1.5)
    scene lock_ch12_txt4 with Dissolve(4.0)
    pause
    stop music
    jump crushed