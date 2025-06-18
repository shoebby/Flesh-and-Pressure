label interview1:
    scene ch1
    play audio "chaptercard.mp3"
    pause
    play music "hydrangeaBreath.mp3"
    scene office
    
    show itske tank at portrait

    f_t "Her office is nice, albeit a bit cramped, and full of -stuff-."
    f_t "Pictures from work parties, toys, little trinkets..."
    f_t "A Groot Funko Pop? Yeugh..."

    nvl clear

    f_t "I'm not sure if it's specifically her office or an office shared by multiple managers, but it definitely -feels- hers with how comfortable she is, reclining in her office chair like that..."
    show itske stressed at portrait
    f_t "This rickety folding chair she pulled out for me makes me so small compared to herself, I have to look up at her."
    f_t "Thankfully she has a nice mole above her eyebrow for me to focus on instead of her eyes, otherwise my nerves would be through the roof."

    nvl clear

    f_t "It's sweltering, she's wearing this nice baby blue blouse that suits her perfectly."
    show itske nervous at portrait  
    f_t "I notice It fits her a bit too well..."
    f_t "Why did she have to unbutton the three top buttons..."
    show itske edge at portrait
    f_t "Guhhh, stop drooling, I need to keep my mind straight."

    nvl clear
    show itske -edge at portrait
    f_t "This is business."

    nvl clear

    f_t "Engaging Itske business mode."

    nvl clear
    
    f_t "I might be insanely stressed, and I might want to get the hell out of here as soon as possible, but oh my god if I don't get this job..."

    nvl clear
    show itske stressed at portrait
    f_t "Don't do something embarrassing, don't blow your chances, else I'm going to miss rent and I'll get kicked out and then I'll be homeless and someone will k-{nw}"

    nvl clear

    show speaker manager at portrait
    j "So! tell me [[EXPLETIVE], why did you choose to apply here?"
    hide speaker
    show itske stressed at portrait
    f "A-ah! Yeah, well..."
    
    show speaker girl listening at portrait
    f_t "Okay, ignore the deadnaming, just DON'T say 'money'. It didn't work yesterday and this job pays too little for that to be a believable reason anyways."
    
    f_t "Remember your onlyfans arc, remember the slaughterhouse gig, do NOT fuck this up."

    show speaker girl thinking at portrait

    menu (nvl=True):
        
        f_t "So... what should I tell her?"

        "{b}{color=#fff}[[MARXIST LABOUR MACHINE]{/b}{/color} I am a machine, designed and constructed to generate as much surplus value as possible for my lord. I will do ANYTHING she asks of me.":
            nvl clear
            show speaker girl std at portrait
            f "W-well, I've loved coffee for a long time, and making it with the proper hardware is a lot of fun to me and-"
            show speaker manager at portrait
            j "Ah, yeah, okay. I'm sorry to inform you that we don't really have anything like that though... We're not like those luxury cinemas that have espresso machines."
            show speaker girl std at portrait
            f_t "Oh my god you IDIOT! the barista job interview is tomorrow, not today!"
            f_t "Didn't you notice the big movie posters?"
            f_t "The popcorn warmers?"
            f_t "The logo on her... chest-... Eheheh..."
            f "A-ah but... well... I like to make popcorn at ho-"
            show speaker manager at portrait
            j "That's... we... get our popcorn pre-popped from the manufacturer..."
            show speaker girl std at portrait
            f_t "Do they do ANYTHING here themselves???"
            f_t "Has the art of cinema been lost???"
            f "Mmmhhhh-I'm really good at cleaning!! And I enjoy it!"
            show speaker manager at portrait
            j "O-okay there we go! We -do- do that here!"
            j "Good job, I know nerves can be bad but you're doing fine."
            show speaker girl std at portrait
            f_t "Why did a cool mature woman like her have to say good job to me why why why why I'm not blushing am I-"
        
        "{b}{color=#fff}[[COMMON-SENSE LIAR]{/b}{/color} I'm uh, a 'people person'? Is that something they want at places like this? Fuck if I know, think of something that sounds good.":
            nvl clear
            show speaker girl std at portrait
            f "I -totally- like being around and interacting with people."
            f_t "Why did I say 'totally' like that."
            show speaker manager at portrait
            j "...Why did you say 'totally' like that?"
            show speaker girl std at portrait
            f_t "Inside voice is NOT outside voice, you stupid mongrel."
            f "N-no reason, something was... stuck... in my throat... Frog..."
            f "But... I do really like people! And movies! Especially movie-going people!"
            show speaker manager at portrait
            j "Ah! Any favourites from this year?"
            show speaker girl std at portrait
            f_t "Normal."
            f_t "Answer."
            f_t "This is an interv-{nw}"

            nvl clear

            f "Well there's this indie comedy parody movie called The People's Joker and I guess it's technically not from this year but I did watch it this year I actually pre-ordered the Blu-ray and it was a story I really resonated with you see-{nw}"

            nvl clear

            f_t "Stop talking."
            f_t "Wrap it up."
            f_t "WRAP IT UP."
            f_t "ABORT."
            f "-So yeah that really felt analogous to my relationship with my mother."
            show speaker manager at portrait
            j "Mhm..."

        "{b}{color=#fff}[[RECOVERING EXNEET]{/b}{/color} I'm a pathetic jobless loser, it's quite visible so I might as well be honest about it. Maybe I can score some pity points.":
            nvl clear
            show speaker girl std at portrait
            f "Can I... Be fully honest with you?"
            show speaker manager at portrait
            j "Well yeah of course, preferably!"
            show speaker girl std at portrait
            f "I've been looking for a job for months now, no one's hiring me and rent is gonna be due soon."
            f "I've worked just about every job a high-school dropout can get hired for, and then some."
            f "Warehouses, retail, bars, clubs, restaurants, call centers, offices..."
            f_t "Okay now look really sad and downtrodden."
            f "A brothel..."
            show speaker manager at portrait
            j "..."
            show speaker girl std at portrait
            f_t "It -was- a brothel but I was technically just a waitress so..."
            f_t "Sorry Madame Jeannette for dragging you like this."
            f "I'm not looking for pity-"
            f_t "I am."
            f "-and I'll work my butt off if you do hire me-"
            f_t "I probably won't."
            f "I'm just asking for a chance."
            show speaker manager at portrait
            j "...Thank you for your honesty."

    nvl clear
    show speaker girl std at portrait
    f_t "Oh god she's scribbling in her notepad, do NOT let her scribble in her notepad, she'll realize I'm being a total freak midwit weirdo."
    f_t "Say something, say ANYTHING."
    f_t "STOP STARING AT HER CLEAVAGE."

    f "B-beautiful weather toda-"

    show speaker manager at portrait
    j "Hey, it's okay. You're hired."

    show speaker girl std at portrait
    f_t "What?"

    f "What?"

    show speaker manager at portrait
    j "You're hired!"
    j "You seem like a good fit in the team, and besides that you look like you could catch a break."

    show speaker girl std at portrait
    f "Wh-whuh?"

    nvl clear
    show speaker manager at portrait
    j "Mismatching socks..."

    show speaker girl std at portrait
    f_t "Hey what-"

    show speaker manager at portrait
    j "Half-applied mascara..."

    show speaker girl std at portrait
    f_t "Oh god damnit-"

    show speaker manager at portrait
    j "Food stuck in your teeth..."

    show speaker girl std at portrait
    f_t "Jeez I get it stop-"

    show speaker manager at portrait
    j "Nugget-shaped grease stains on your clothes..."

    show speaker girl std at portrait
    f_t "I GET IT."

    show speaker manager at portrait
    j "We run a pretty tight ship here so you'll need to keep up, but I want to at the very least give you a shot [[EXPLETIVE]."

    show speaker girl std at portrait
    f "T-thank you miss... And, uhm, if you don't mind..."
    f "I prefer Itske, rather than... that name."

    show speaker manager at portrait
    j "Ah! Noted, thanks. Any pronouns I need to keep in mind?"

    show speaker girl std at portrait
    f_t "Don't push it with the it/its."

    f "Just she and her is fine... Thanks."

    show speaker manager at portrait
    j "Done! See you tomorrow."

    show speaker girl std at portrait
    f_t "Fuuuuck."
    f_t "I need her."

    nvl clear
    jump alone