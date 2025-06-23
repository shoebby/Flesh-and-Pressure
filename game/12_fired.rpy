label fired:
    scene ch12
    play audio "chaptercard.mp3"
    pause

    j "..."

    f "..."

    j "You broke his nose, Itske."

    f "I-I'm sorry-"

    j "I know, save it for when... -If- you ever see him again."

    f_t "Jenn seems to be deep in thought, she pinches the bridge of her nose and buries her face in her hands."
    f_t "I've never seen her this upset, I fucked up bad."

    nvl clear

    menu (nvl=True):
        f_t "Is there something I can say to get out of this...?"

        "{color=#fff}[[WHORE]{/color} Bribe her... Somehow, with something. Do I even have any savings left? Maybe she's into trannies?":
            f "W-would you like-{nw}"

            j "Don't."

            jump A1

        "{color=#fff}[[VICTIM]{/color} It... Wasn't my fault? Could try to go with that? He took a swing at me, for sure.":
            f "Well he did-{nw}"

            j "No, let me think."

            jump A2

        "{color=#fff}[[PUPPY]{/color} Begging might work. As pathetic as possible, preferably.":
            f "Jenn please I-{nw}"

            j "Stop."

            jump A3

label A1:
    menu (nvl=True):
        f "..."
        "{color=#fff}[[VICTIM]{/color} It... Wasn't my fault? Could try to go with that? He took a swing at me, for sure.":
            f "Well he did-{nw}"

            j "No, let me think."

            jump B3

        "{color=#fff}[[PUPPY]{/color} Begging might work. As pathetic as possible, preferably.":
            f "Jenn please I-{nw}"

            j "Stop."

            jump B2

label A2:
    menu (nvl=True):
        f "..."
        "{color=#fff}[[WHORE]{/color} Bribe her... Somehow, with something. Do I even have any savings left? Maybe she's into trannies?":
            f "W-would you like-{nw}"

            j "Don't."

            jump B3
        "{color=#fff}[[PUPPY]{/color} Begging might work. As pathetic as possible, preferably.":
            f "Jenn please I-{nw}"

            j "Stop."

            jump B1

label A3:
    menu (nvl=True):
        f "..."
        "{color=#fff}[[WHORE]{/color} Bribe her... Somehow, with something. Do I even have any savings left? Maybe she's into trannies?":
            f "W-would you like-{nw}"

            j "Don't."

            jump B2
        "{color=#fff}[[VICTIM]{/color} It... Wasn't my fault? Could try to go with that? He took a swing at me, for sure.":
            f "Well he did-{nw}"

            j "No, let me think."

            jump B1

label B1:
    menu (nvl=True):
        f "..."
        "{color=#fff}[[WHORE]{/color} Bribe her... Somehow, with something. Do I even have any savings left? Maybe she's into trannies?":
            f "W-would you like-{nw}"

            j "Don't."

            jump fired_end

label B2:
    menu (nvl=True):
        f "..."
        "{color=#fff}[[VICTIM]{/color} It... Wasn't my fault? Could try to go with that? He took a swing at me, for sure.":
            f "Well he did-{nw}"

            j "No, let me think."

            jump fired_end

label B3:
    menu (nvl=True):
        f "..."
        "{color=#fff}[[PUPPY]{/color} Begging might work. As pathetic as possible, preferably.":
            f "Jenn please I-{nw}"

            j "Stop."

            jump fired_end

label fired_end:
    f "... Is there anything-{nw}"

    j "Can you -please- shut up!"

    nvl clear

    f "..."

    j "God..."
    j "..."
    j "I'm sorry."

    nvl clear

    f_t "After a moment of vulnerability her demeanor turns back to stone, she gets up to print a document."

    j "... You have 2 weeks left on your contract, after that you won't be working here anymore."
    j "I... Suggest you start looking for another job."

    nvl clear

    f_t "She hands me a freshly printed document."
    f_t "It's warm."
    f_t "The words are too blurry to make out."
    f_t "I hurriedly stuff it in one of my cargo pockets as her gaze bores into me."

    j "You won't need to finish your shift today, go home."
    j "I'll see you tomorrow."

    nvl clear
    jump crushed