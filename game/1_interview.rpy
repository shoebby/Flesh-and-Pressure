label interview1:
    scene ch1
    play audio "chaptercard.mp3"
    pause
    play music "music/hydrangeaBreath.mp3"
    scene bg office
    
    show speaker itske tank awkward at portrait
    f_t "Her office is nice, albeit a bit cramped, and full of -stuff-."
    show speaker itske tank pouting at portrait
    f_t "Pictures from work parties, toys, little trinkets..."
    show speaker itske tank disgust at portrait
    f_t "A Groot Funko Pop? Yeugh..."

    nvl clear

    show speaker itske pouting at portrait
    f_t "I'm not sure if it's specifically her office or an office shared by multiple managers, but it definitely -feels- hers with how comfortable she is, reclining in her office chair like that..."
    show speaker itske stressed at portrait
    f_t "This rickety folding chair she pulled out for me makes me so small compared to herself, I have to look up at her."
    f_t "Thankfully she has a nice mole above her eyebrow for me to focus on instead of her eyes, otherwise my nerves would be through the roof."

    nvl clear

    f_t "It's sweltering, she's wearing this nice baby blue blouse that suits her perfectly."
    show speaker itske nervous at portrait  
    f_t "I notice It fits her a bit too well..."
    f_t "Why did she have to unbutton the three top buttons..."
    show speaker itske edge at portrait
    f_t "Guhhh, stop drooling, I need to keep my mind straight."

    nvl clear
    show speaker itske -edge at portrait
    f_t "This is business."

    nvl clear

    f_t "Engaging Itske business mode."

    nvl clear
    
    f_t "I might be insanely stressed, and I might want to get the hell out of here as soon as possible, but oh my god if I don't get this job..."

    nvl clear
    show speaker itske stressed at portrait
    f_t "Don't do something embarrassing, don't blow your chances, else I'm going to miss rent and I'll get kicked out and then I'll be homeless and someone will k-{nw}"

    nvl clear

    show speaker jenn manager at portrait
    j "So! tell me [[EXPLETIVE], why did you choose to apply here?"
    hide speaker
    show speaker itske tank stressed at portrait
    f "A-ah! Yeah, well..."
    
    show speaker itske tank pouting at portrait
    f_t "Okay, ignore the deadnaming, just DON'T say 'money'. It didn't work yesterday and this job pays too little for that to be a believable reason anyways."
    
    f_t "Remember your onlyfans arc, remember the slaughterhouse gig, do NOT fuck this up."

    nvl clear

    show speaker itske tank thinking at portrait

    menu (nvl=True):
        
        f_t "So... what should I tell her?"

        "{color=#fff}[[MARXIST LABOUR MACHINE]{/color} I am a machine, designed and constructed to generate as much surplus value as possible for my lord. I will do ANYTHING she asks of me.":
            nvl clear
            show speaker itske tank smiling at portrait
            f "W-well, I've loved coffee for a long time, and making it with the proper hardware is a lot of fun to me and-"
            show speaker jenn manager worried at portrait
            j "Ah, yeah, okay. I'm sorry to inform you that we don't really have anything like that though... We're not like those luxury cinemas that have espresso machines."

            nvl clear

            show speaker itske tank scared at portrait
            f_t "Oh my god you IDIOT!"
            f_t "The barista interview is tomorrow, not today!"
            f_t "Didn't you notice the big movie posters?"
            f_t "The popcorn warmers?"
            show speaker itske tank nervous at portrait
            f_t "The logo on her... chest-... Eheheh..."
            show speaker itske tank smiling at portrait
            f "A-ah but... well... I like to make popcorn at ho-"
            show speaker jenn manager cringe at portrait
            j "That's... we... get our popcorn pre-popped from the manufacturer..."

            nvl clear

            show speaker itske tank shock at portrait
            f_t "AUUUUGH."
            show speaker itske tank annoyed at portrait
            f_t "Do they do ANYTHING here themselves???"
            f_t "Has the art of cinema been lost???"
            show speaker itske tank upset at portrait
            f "M{w=.1}m{w=.1}h{w=.1}h{w=.1}h{w=.1}h-{nw}"
            show speaker itske tank smiling at portrait
            f "I'm really good at cleaning!! And I enjoy it!"
            show speaker jenn manager worried at portrait
            j "O-okay there we go! We -do- do that here!"
            show speaker jenn manager -worried at portrait
            j "Good job, I know nerves can be bad but you're doing fine."
            show speaker itske tank nervous at portrait
            f_t "Why did a cool mature woman like her have to say good job to me why why why why I'm not blushing am I-"
        
        "{color=#fff}[[COMMON-SENSE LIAR]{/color} I'm uh, a 'people person'? Is that something they want at places like this? Fuck if I know, think of something that sounds good.":
            nvl clear
            show speaker itske tank smug at portrait
            f "I -totally- like being around and interacting with people."
            f_t "Why did I say 'totally' like that."
            show speaker jenn manager worried at portrait
            j "...Why did you say 'totally' like that?"
            show speaker itske tank disgust at portrait
            f_t "Inside voice is NOT outside voice, you stupid mongrel."

            nvl clear

            show speaker itske tank nervous at portrait
            f "N-no reason, something was... stuck... in my throat... Frog..."
            show speaker itske tank smiling at portrait
            f "But... I do really like people! And movies! Especially movie-going people!"
            show speaker jenn manager at portrait
            j "Ah! Any favourites from this year?"
            show speaker itske tank stressed at portrait
            f_t "Normal."
            f_t "Answer."
            f_t "This is an interv-{nw}"

            nvl clear
            show speaker itske tank smiling at portrait
            f "Well there's this indie comedy parody movie called The People's Joker and I guess it's technically not from this year but I did watch it this year I actually pre-ordered the Blu-ray and it was a story I really resonated with because well like the main character I'm also trans and I also had a lot of difficulties coming to terms with-{nw}"

            nvl clear
            show speaker itske tank shock at portrait
            f_t "Stop talking."
            f_t "Wrap it up."
            f_t "WRAP IT UP."
            f_t "ABORT."
            show speaker itske forcedsmile at portrait
            f "-So yeah that really felt analogous to my relationship with my mother and made me cry a bunch."
            show speaker jenn manager cringe at portrait
            j "Mhm..."

        "{color=#fff}[[RECOVERING EXNEET]{/color} I'm a pathetic jobless loser, it's quite visible so I might as well be honest about it. Maybe I can score some pity points.":
            nvl clear
            show speaker itske tank pouting at portrait
            f "Can I... Be fully honest with you?"
            show speaker jenn manager at portrait
            j "Well yeah of course, preferably!"
            show speaker itske tank pouting at portrait
            f "I've been looking for a job for months now, no one's hiring me and rent is gonna be due soon."
            f "I've worked just about every job a high-school dropout can get hired for, and then some."
            f "Warehouses, retail, bars, clubs, restaurants, call centers, offices..."
            f_t "Okay now look really sad and downtrodden."
            show speaker itske tank heartbroken at portrait
            f "A brothel..."
            show speaker jenn manager worried at portrait
            j "..."
            show speaker itske tank disgust at portrait
            f_t "It -was- a brothel but I was technically just a waitress so..."
            f_t "Sorry Madame Jeannette for dragging you like this."

            nvl clear

            show speaker itske tank pouting at portrait
            f "I'm not looking for pity-"
            show speaker itske tank smug at portrait
            f_t "I am."

            nvl clear

            show speaker itske tank pouting at portrait
            f "-and I'll work my butt off if you do hire me-"
            show speaker itske tank smug at portrait
            f_t "I probably won't."

            nvl clear

            show speaker itske tank pouting at portrait
            f "I'm just asking for a chance."
            show speaker jenn manager worried at portrait
            j "...Thank you for your honesty."

    nvl clear
    show speaker itske tank terrified at portrait
    f_t "Oh god she's scribbling in her notepad."
    f_t "Do NOT let her scribble in her notepad, notepads are NEVER a good sign."
    f_t "She'll realize I'm being a total freak midwit weirdo."
    f_t "Say something, say ANYTHING."
    show speaker itske tank exerted at portrait
    f_t "STOP STARING AT HER CLEAVAGE."

    nvl clear

    show speaker itske tank nervous at portrait
    f "B-beautiful weather toda-{nw}"

    show speaker jenn manager at portrait
    j "Hey, it's okay. You're hired."

    nvl clear

    show speaker itske tank confused at portrait
    f_t "What?"

    f "What?"

    show speaker jenn manager at portrait
    j "You're hired!"
    j "You seem like a good fit in the team, and besides that you look like you could catch a break."

    show speaker itske tank scared at portrait
    f "Wh-whuh?"

    nvl clear

    show speaker jenn manager at portrait
    j "Mismatching socks..."

    show speaker itske tank sad at portrait
    f_t "Hey what-"

    show speaker jenn manager at portrait
    j "Half-applied mascara..."

    show speaker itske tank tired at portrait
    f_t "Oh god damnit-"

    show speaker jenn manager at portrait
    j "Food stuck in your teeth..."

    show speaker itske tank disgust at portrait
    f_t "Jeez I get it stop-"

    show speaker jenn manager at portrait
    j "Nugget-shaped grease stains on your clothes..."

    show speaker itske tank yelling at portrait
    f_t "I GET IT."

    show speaker jenn manager at portrait
    j "We run a pretty tight ship here so you'll need to keep up, but I want to at the very least give you a shot [[EXPLETIVE]."

    nvl clear

    show speaker itske tank pouting at portrait
    f "T-thank you miss... And, uhm, if you don't mind..."
    show speaker itske tank nervous at portrait
    f "I prefer Itske, rather than... that name."

    show speaker jenn manager at portrait
    j "Ah! Noted, thanks. Any pronouns I need to keep in mind?"

    show speaker itske tank neutral at portrait
    f_t "Don't push it with the it/its."
    show speaker itske tank forcedsmile at portrait
    f "Just she and her is fine... Thanks."

    show speaker jenn manager at portrait
    j "Done! See you tomorrow."

    show speaker itske tank flustered at portrait
    f_t "Fuuuuck."
    show speaker itske tank nervous at portrait
    f_t "I need her."
    
    nvl clear
    scene lock_ch1
    play music lock_lick1 noloop
    scene lock_ch1_txt1 with Dissolve(1.0)
    scene lock_ch1_txt2 with Dissolve(1.0)
    scene lock_ch1_txt3 with Dissolve(1.5)
    scene lock_ch1_txt4 with Dissolve(4.0)
    pause
    stop music
    jump alone