label start:
    show bg backyard
    play music "introthump.mp3" loop
   
    f_t "I hate my job."
    f_t "It's boring, pays horribly, but at least my coworkers are sweet."
    f_t "They don't misgender me... intentionally... and usually get it right aside from a few unfortunate moments."
    f_t "It's probably the first job I've ever worked where I feel like I am 'part of the team'."
    f_t "Regardless of their kindness, however, I still feel out of place."
    f_t "I am miles away from the people I talk to right in front of me."
    f_t "Their happiness, their joy; thin plasticy film wrapped tight over my skin, isolating me from all of it."
    f_t "Thankfully, besides them, there's her, and she is beautiful."
    nvl clear
    f_t "Her lightly beveled edges wink at me when the sun hits them just right..."
    f_t "Her coat is a textured cobalt blue..."
    f_t "She's snappy, tactile, inviting..."
    f_t "Even her hazard sticker is fully intact..."
    show bg loveshot1 with Dissolve(2.0)
    pause
    queue sound "pressing.mp3" loop volume 0.1
    f_t "She accommodates a bulky wheelie bin without issue, and I help her deal with it."
    f_t "I turn her switch with a satisfying click..."
    f_t "I press and hold down her button..."
    f_t "I push her lever..."
    f_t "With a slow groan her piston pushes downwards towards the trash, compacting it as if it were air."
    f_t "She works effortlessly at first, but with density building even she starts to struggle."
    f_t "Her mechanical whine creeps up an octave, her piston slows to a crawl, and right before she buckles..."
    f_t "I yank her lever towards me, relieving her tension, allowing her piston back up, granting her a breath."
    f_t "This dance repeats itself, usually around 8pm, before people start to complain about noise, and until all of the day's trash has been dealt with."
    nvl clear
    show bg loveshot2 with Dissolve(2.0)
    f_t "Press. Pull. Compress. Whine. Push. Release."
    f_t "The crunching, cracking, and popping trash bags..."
    show speaker itske flustered at portrait with dissolve
    f "..."
    nvl clear
    f_t "Press. Pull. Compress. Whine. Push. Release."
    f_t "Familiar sounds, nights spent with heavy-handed people."
    show speaker itske nervous at portrait
    f "W-what if..."
    nvl clear
    f_t "Press. Pull. Compress. Whine. Push. Release."
    f_t "I get close to her body and push my groin up against her, feeling her machinal purr resonate through me."
    show speaker itske exerted at portrait
    f "So warm..."
    nvl clear
    f_t "Press. Pull. Compress. Whine. Push. Release."
    f_t "It's a good task, my coworkers are thankful for my effort, I can never tell them how much she makes me feel."
    show speaker itske flustered at portrait
    f "I n-need this..."
    nvl clear
    f_t "Press. Pull. Compress. Whine. Push. Release."
    f_t "I imagine myself inside of this trash bin. Her disc looming over me, stuck, helpless, morbidly curious."
    show speaker itske exerted at portrait
    f "P-please..."
    nvl clear
    f_t "Press. Pull. Compress. Whine. Push. Release."
    f_t "An unknown pair of hands would take hold of her, and she'd start moving towards me; horror and lust sloshing around in my mind."
    show speaker itske edge at portrait
    f "Hgnn..."
    nvl clear
    f_t "Press. Pull. Compress. Whine. Push. Release."
    f_t "I would feel her cold metal touch press down on my spine, slowly taking away my breath."
    show speaker itske exerted at portrait
    f "Haahh... F-fuck..."
    nvl clear
    f_t "Press. Pull. Compress. Whine. Push. Release."
    f_t "My bones would strain, bend, creak, but inevitably prove unable to resist her."
    show speaker itske nervous at portrait
    f "Goddd... Why is this so hot..."
    nvl clear
    f_t "Press. Pull. Compress. Whine. Push. Release."
    play audio "bones_ribscrush.mp3" volume 0.5
    show speaker itske edge at portrait
    f_t "They would crack and splinter, driving themselves into my lungs, my heart, perforating my skin from the inside."
    nvl clear
    f_t "Press. Pull. Compress. Whine. Push. Release."
    f_t "I feel warm and cold, so much is happening while she just keeps moving. The pain would be unbearable if it wasn't for the adrenaline."
    show speaker itske flustered at portrait
    f "I haven't felt this good in so long..."
    nvl clear
    f_t "Press. Pull. Compress. Whine. Push. Release."
    show speaker itske exerted at portrait
    f_t "My body is broken, blood gushes from my mouth and nose, the pressure on my skull is rising."
    nvl clear
    f_t "Press. Pull. Compress. Whine. Push. Release."
    show speaker itske edge at portrait
    f_t "It hurts so much and feels so good, all she needs is a small extra push until..."
    play audio "bones_skullcrush.mp3" volume 0.5
    hide piper
    nvl clear
    stop sound
    stop music
    show speaker itske bust at portrait
    pause
    f_t "Press. Pull. Compress. Whine. Push. Release."
    f_t "I want her to crush me."
    stop sound2
    show speaker itske exerted at portrait
    f "Oh god my fucking pants-{nw}"

    nvl clear
    hide speaker
    play music "titletrack.mp3"

label titlescreen:
    scene _titlescreen
    $ renpy.pause(11.0, hard=True)
    stop music
    jump interview1