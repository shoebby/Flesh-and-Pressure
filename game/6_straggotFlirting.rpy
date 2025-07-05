label straggot:
    scene ch6
    play audio "chaptercard.mp3"
    pause

    show bg counter
    show speaker tom sad at portrait
    t "Dating is so hard..."

    show speaker itske confused at portrait
    f "Mh? How so?"

    show speaker tom sad at portrait
    t "Girls are so confusing! It's like they have all these expectations, and they don't say any of them out loud, you kinda just have to guess all he time."

    show speaker itske stressed at portrait
    f_t "Okay, if I don't do something now there's a major chance he will turn into either an incel or a manosphere weirdo."

    show speaker tom sad at portrait
    t "I've been on dating apps, done a bunch of texting, but it never seems to turn into a date..."
    t "Like, you have a girlfriend right?"

    show speaker itske nervous at portrait
    f "Errr..."
    
    f_t "Such horrible timing for a conversation like this, right after yesterday's mess."
    show speaker itske pouting at portrait
    f_t "She didn't block me but with how cold and distant she is now I kinda wish she did."
    show speaker itske bothered at portrait
    f_t "Whatever, fucking chaser."

    nvl clear

    show speaker itske pouting at portrait
    f "No... We broke up, like a week into when I started here."

    show speaker itske thinking at portrait
    f_t "Maybe I should text her again? But that'd be double-texting... People don't like that as far as I've picked up."
    show speaker itske pouting at portrait
    f_t "Comes off as desperate?"
    show speaker itske confused at portrait
    f_t "But what if you have two things to say?"
    show speaker itske annoyed at portrait
    f_t "I hate that this guy is like 10\% right, it -is- complicated."

    show speaker tom neutral at portrait
    t "Oh, weird, I thought I heard you talk about her recently."

    show speaker itske scared at portrait
    f_t "Oh fuck he remembers, I know it's psychotic to pretend like you're still dating your ex but it made things a bit easier while working here."
    show speaker itske stressed at portrait
    f_t "There's no shame in that, right?"

    show speaker itske nervous at portrait
    f "Y-you must've misremembered."

    nvl clear

    show speaker tom neutral at portrait
    t "I guess so. It's crazy to think it's already been like what, 3 months since you started working here?"
    t "Time really flies."

    show speaker itske thinking at portrait
    f_t "I've been working here for that long?"
    show speaker itske pouting at portrait
    f_t "I didn't realize but this is somehow now contending with the strip bar gig for longest held job."
    show speaker itske smug at portrait
    f_t "And I had a sweet gimmick there! I have no gimmick here at all! Except for my trash-compacting I guess."
    show speaker itske pouting at portrait
    f_t "Why haven't they fired me yet?"
    show speaker itske thinking at portrait
    f_t "Has anything happened that would be fireable so far?"
    f_t "No... I guess not, but it's not like that was a requirement in the past."
    show speaker itske disgust at portrait
    f_t "At some places it just took a wrong glance at a customer; I understand my resting bitch face isn't exactly working to my benefit, but it's always felt..."
    show speaker itske heartbroken at portrait
    f_t "Unfair..."

    nvl clear

    show speaker itske nervous at portrait
    f "Yeah... H-hah, it sure does."

    show speaker itske disgust at portrait
    f_t "Change the subject before you start crying, you baby."

    show speaker itske nervous at portrait
    f "H-hey! Maybe you could run your date ideas by me, I'm pretty -experienced- when it comes to women... Hehe..."

    show speaker itske disgust at portrait
    f_t "Oh my god shut up you've had like 2 relationships and they both violently imploded, and hookups do NOT count as relevant dating experience."

    show speaker tom neutral at portrait
    t "Oh! Sure! Alright so I was thinking, for this girl I've been texting with for a while, she -really- likes anime, do you know wha-"

    show speaker itske smug at portrait
    f_t "My sagely nodding cues him into the fact that I am also a disgusting weeb. I even have my arms crossed, it's like the full picture."

    show speaker tom neutral at portrait
    t "Well I figured, why not take her out to karaoke?"

    show speaker itske smiling at portrait
    f_t "This is an incredible idea."

    show speaker tom neutral at portrait
    t "I think I'd like your perspective on this cause she's trans as well-"

    show speaker itske shock at portrait
    f_t "This is a-{nw}"

    f "HORRIBLE idea."

    nvl clear

    show speaker tom sad at portrait
    t "Oh god is it?"

    show speaker itske smug at portrait
    f "99\% chance it is. Even if she went through with it there's a major chance she breaks down crying halfway through her first performance-"

    show speaker itske disgust at portrait
    f_t "Wow, projecting much?"

    show speaker itske smug at portrait
    f "-and at that point it'll just be over."

    show speaker tom sad at portrait
    t "Okay... So what sort of date ideas do you suggest?"

    show speaker itske pouting at portrait
    f "Well it depends y'know? You've gotta know what they like and it mostly hinges on that."
    show speaker itske smiling at portrait
    f "You already applied that really well but it should just be something else in that general direction y'know?"
    show speaker itske forcedsmile at portrait
    f "Depending on the person even minigolf could be a good date idea"

    show speaker tom neutral at portrait
    t "Haha, so I take it you don't like midgetgolf?"

    show speaker itske annoyed at portrait
    f "I hate it. Also don't call it that, it's kinda ableist."

    show speaker tom sad at portrait
    t "O-okay... Then... What should I do? Any ideas?"

    nvl clear
    show speaker itske pouting at portrait

menu (nvl=True):
    f_t "Hmm..."

    "{color=#fff}[[DISGUSTINGLY DEFAULT, TORTUROUSLY TYPICAL]{/color} Go see a Ghibli movie, surely that'd be fine. Girls like Ghibli, be the sensitive boy she dreams about!":
        show speaker itske confused at portrait
        f "Well do you know Studio Ghibli?"

        show speaker tom neutral at portrait
        t "... U-uhm...?"

        show speaker itske disgust at portrait
        f_t "Oh my god he's such a normie."

        show speaker itske smiling at portrait
        f "Okay... It's an animation studio that makes anime movies essentially, but they're like, super whimsical and fantastical."

        show speaker tom neutral at portrait
        t "Oh I'm sure she'd like that! She likes to wear these fluffy, frilly, cutesy dresses 'n stuff, like a Disney princess!"

        show speaker itske forcedsmile at portrait
        f_t "Oh god he fell for a lolita girl."
        f_t "Not just a lolita girl, but from his description probably a sweet lolita girl."
        f_t "She's going to ruin his life and eat him alive."
        show speaker itske thinking at portrait
        f_t "I'm so fucking envious."

        show speaker itske smiling at portrait
        f "A-ah, yeah, nice! But yeah cinemas screen them here pretty often. Could be a good idea..."

    "{color=#fff}[[DESPERATE FAKE MIRRORER]{/color} Binge an extremely niche anime with her, try to match her power level.":
        show speaker itske smug at portrait
        f "Well, you want to impress her right?"

        show speaker tom neutral at portrait
        t "Uhh yeah, I guess so?"

        show speaker itske smug at portrait
        f "Well you could invite her over to watch something like, super niche and super artsy."

        show speaker tom neutral at portrait
        t "You sure that's a good idea? I don't want to come off as pretentious."

        show speaker itske annoyed at portrait
        f_t "Liking peak media is NOT pretentious."

        show speaker tom neutral at portrait
        t "Besides, wouldn't I basically be lying? I don't know anything about anime."

        show speaker itske confused at portrait
        f "You know Pokémon right?"

        show speaker tom neutral at portrait
        t "Isn't that French?"

        show speaker itske bothered at portrait
        f_t "Oh my god this guy is clueless."

        show speaker itske tired at portrait
        f "Hff... Just watch Madoka Magica with her, she will be impressed, it's not too niche, trust me, I know weeb girls."

    "{color=#fff}[[FAUX-THOUGHTFUL EGOCENTRIC]{/color} Offer to take her to do something -you- like to do, whatever that might be. Pull her from her bubble! Let her into yours!":
        show speaker itske smiling at portrait
        f "Well if you don't know much about it, maybe you should bring her along to something you enjoy?"

        show speaker tom neutral at portrait
        t "Hmm... So far she seems quite comfortable in her interests..."

        show speaker itske smiling at portrait
        f "Offer to pull her out of her bubble! Maybe she'll appreciate it. What sorta things do you like to do?"

        show speaker tom neutral at portrait
        t "I see where you're coming from... Maybe I should take her to the gym!"

        show speaker itske stressed at portrait
        f_t "Oh god."

        show speaker tom neutral at portrait
        t "She's quite scrawny, especially in her arms! I think she's a bit ashamed of it cause she wears long sleeves in every picture I've seen."

        show speaker itske scared at portrait
        f_t "Ohhhh no."

        show speaker tom neutral at portrait
        t "And afterwards we could go out for a nice protein-rich meal for some 'sick gains'! She said she skips meals pretty often, lack of money probably so I could treat her."

        show speaker itske terrified at portrait
        f_t "Nonononono."

        show speaker itske sad at portrait
        f "Just..."
        f "Take her midg-... Minigolfing..."
        f "No gym..."
    
label straggot2:

    show speaker tom neutral at portrait
    t "Ah! Okay, I'll keep that in mind. Thanks!"

    nvl clear

    t "I'm wondering though... What do -you- like?"

    show speaker itske pouting at portrait
    f "What I like? Uh, CSI shows I guess, I've been binging CSI: Cyber lately and it's honestly kinda horrible and I know the subgenre as a whole is essentially copaganda but like-"

    show speaker tom shy at portrait
    t "Well... I'm seeing something else I like..."

    show speaker itske confused at portrait
    f "Huh? What was that?"

    show speaker tom shy at portrait
    t "O-oh, I said: I'm seeing something else I like..."

    show speaker itske confused at portrait
    f "..."

    show speaker tom shy at portrait
    t "..."

    show speaker itske disgust at portrait
    f "..."

    show speaker tom shy at portrait
    t "... I'm seei-"

    show speaker itske annoyed at portrait
    f "Are you flirting with me?"

    show speaker tom shy at portrait
    t "... Maybe."

    show speaker itske bothered at portrait
    f_t "Oh god he is, what the fuck man he's not even in his 20s."

    show speaker itske nervous at portrait
    f "You... Should focus on your weeb girl..."

    show speaker tom shy at portrait
    t "Eheh... Yeah, but like, you're so..."

    show speaker itske annoyed at portrait
    f_t "Don't fucking say it."

    show speaker tom shy at portrait
    t "Mature..."

    show speaker itske yelling at portrait
    f "Oh my f-{nw}"

    nvl clear
    scene lock_ch6
    play music lock_lick1 noloop
    scene lock_ch6_txt1 with Dissolve(1.0)
    scene lock_ch6_txt2 with Dissolve(1.0)
    scene lock_ch6_txt3 with Dissolve(1.5)
    scene lock_ch6_txt4 with Dissolve(4.0)
    pause
    stop music
    jump speaking