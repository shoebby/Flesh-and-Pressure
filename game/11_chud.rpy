label chud:
    scene ch11
    play audio "chaptercard.mp3"
    pause

    play music "music/hydrangeaBreath.mp3"
    scene black
    show bg counter
    show speaker itske tired at portrait
    f_t "Heading back inside I feel like a bit of the weight has fallen off my shoulders."
    f_t "I managed to do a task."
    f_t "I'm good."
    f_t "Today will be fine, just like all the others."
    show speaker itske stressed at portrait
    f_t "Woah, that's... A lot of people."

    nvl clear

    show speaker mae stressed at portrait
    m "Ah! Itske! Where were you? I tried to call you over on the porto but you weren't responding?"

    show speaker itske pouting at portrait
    f "A-ah sorry, maybe I forgot to turn it on? Lemme check..."

    show speaker itske disgust at portrait
    f_t "It has been turned on all this time."

    show speaker itske nervous at portrait
    f "Y-yeah seems like it was turned off, sorry, where should I go?"

    show speaker mae stressed at portrait
    m "Hey no worry, you've been out of work for a while! I'm sure you need to get used to things a bit."
    m "If you could start serving people at the food court that'd be perfect."

    show speaker itske sad at portrait
    f_t "I really don't deserve her kindness."

    nvl clear

    show speaker itske focused at portrait
    f_t "I make my way to the food court to start ringing people up."

    nvl clear

    show speaker itske pouting at portrait
    f_t "First order... One medium salty popcorn and two beers..."
    show speaker itske forcedsmile at portrait
    f "That'll be €13,12 please..."

    nvl clear
    show speaker itske pouting at portrait
    f_t "Next one... Roll of mentos and a coke..."
    show speaker itske annoyed at portrait
    f_t "I swear to god if I catch you making a mess..."
    show speaker itske smug at portrait
    f "That'll be €4,69 (nice) please..."

    nvl clear
    show speaker itske pouting at portrait
    f_t "Next one-{nw}"
    stop music
    show speaker chud at portrait
    chud "Hey, -sir-."

    show bg counter resentment with Dissolve(2.0)
    show speaker itske disgust at portrait
    f "Good... Evening... What can I get you?{nw}"
    play music bpd_noise fadein 15.0
    show speaker chud at portrait
    chud "Let's see... How about a coke and a popcorn? -Sir-."

    show speaker itske annoyed at portrait
    f "W-what size and flavour? We have salty and sweet, but we can also mix-{nw}"
    show speaker chud at portrait
    chud "A normal one, -sir-."

    show speaker itske angry at portrait
    f "W-what do you consider normal? It t-tends to vary from person to person...{nw}"
    show speaker chud at portrait
    chud "Salty of course! Sweet isn't normal, -sir-."

    show bg counter hatred with Dissolve(2.0)
    show speaker itske enraged at portrait
    f "B-but what size-{nw}"
    show speaker chud at portrait
    chud "I said normal! So a normal, medium sized, salty popcorn, si-{nw}"

    show speaker itske upset at portrait
    show bg black
    stop music
    play sound "glasscrack.mp3" volume 10.0
    f_t "His nose meets the counter's glass top with a dull crack."

    show speaker itske smug at portrait
    f "A-ahh..."
    show speaker itske pouting at portrait
    f "..."
    show speaker itske disgust at portrait
    f "Fuck."

    nvl clear
    scene lock_ch11
    play music lock_lick1 noloop
    scene lock_ch11_txt1 with Dissolve(1.0)
    scene lock_ch11_txt2 with Dissolve(1.0)
    scene lock_ch11_txt3 with Dissolve(1.5)
    scene lock_ch11_txt4 with Dissolve(4.0)
    pause
    stop music
    jump fired