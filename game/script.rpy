init python:
    renpy.music.register_channel("sound2", "sound")

    def SpeakingBlip(event, speakerID, **kwargs):
        beeps = 0 #at the start of the dialogue set beeps to 0
        while beeps < 999: #absolute maximum amount of beeps per dialogue, can be whatever its just to make the while loop work
            randosound = renpy.random.randint(0,6) #select a random integer
            if event == "show": #pick one of 7 'blip' sound effects, you can make it less but im doing musical scales and modes so its a lot
                if randosound == 0:
                    renpy.sound.queue("speakingBlips/" + speakerID + "blip1.wav", channel="sound", loop=False)  #construct the path of the audio clip using the
                elif randosound == 1:                                                                           #speakerID, for example one of these clips is called
                    renpy.sound.queue("speakingBlips/" + speakerID + "blip2.wav", channel="sound", loop=False)  #f_blip3.wav
                elif randosound == 2:
                    renpy.sound.queue("speakingBlips/" + speakerID + "blip3.wav", channel="sound", loop=False)
                elif randosound == 3:
                    renpy.sound.queue("speakingBlips/" + speakerID + "blip4.wav", channel="sound", loop=False)
                elif randosound == 4:
                    renpy.sound.queue("speakingBlips/" + speakerID + "blip5.wav", channel="sound", loop=False)
                elif randosound == 5:
                    renpy.sound.queue("speakingBlips/" + speakerID + "blip6.wav", channel="sound", loop=False)
                elif randosound == 6:
                    renpy.sound.queue("speakingBlips/" + speakerID + "blip7.wav", channel="sound", loop=False)
                spause = renpy.music.get_duration(channel="sound") #pause the channel for the duration of the audioclip, so they dont overlap a bunch
            elif event == "slow_done" or event == "end":        #if the dialogue box is finished writing
                renpy.sound.stop(channel="sound", fadeout=0.1)  #stop the channel sound, fadeout of 0.1s to make sure it doesn't make an annoying 'click' sound
            beeps += 1 #add 1 to beeps after a clip is called

define j = Character("", kind=nvl, color="#ffffff", what_color="#dfff87", what_prefix="\"", what_suffix="\"", callback=SpeakingBlip, cb_speakerID="j_") #jenn - VO'D
define f = Character("", kind=nvl, color="#ffffff", what_color="#ffb787", what_prefix="\"", what_suffix="\"", callback=SpeakingBlip, cb_speakerID="f_") #Itske - VO'D
define f_t = Character("", kind=nvl, what_italic=True, what_color="#ff781f", callback=SpeakingBlip, cb_speakerID="f_t_") #Itske mind-thoughts
define p = Character("", kind=nvl, color="#ffffff", what_color="#87a7ff", what_prefix="\"", what_suffix="\"", callback=SpeakingBlip, cb_speakerID="p_") #piper - VO'D
define m = Character("", kind=nvl, color="#ffffff", what_color="#ffa7dd", what_prefix="\"", what_suffix="\"", callback=SpeakingBlip, cb_speakerID="m_") #mae
define t = Character("", kind=nvl, color="#ffffff", what_color="#ff8787", what_prefix="\"", what_suffix="\"", callback=SpeakingBlip, cb_speakerID="t_") #tom - VO'D
define c = Character("", kind=nvl, color="#ffffff", what_color="#c587ff", what_prefix="\"", what_suffix="\"", callback=SpeakingBlip, cb_speakerID="c_") #cammy - VO'Dcnn
define d = Character("", kind=nvl, color="#ffffff", what_color="#87fbff", what_prefix="\"", what_suffix="\"", callback=SpeakingBlip, cb_speakerID="d_") #date
define d_t = Character("", kind=nvl, what_italic=True, what_color="#1fc0ff", callback=SpeakingBlip, cb_speakerID="d_t_") #date mind-thoughts
define mt = Character("", kind=nvl, color="#ffffff", what_color="#91ff87", what_prefix="\"", what_suffix="\"", callback=SpeakingBlip, cb_speakerID="mt_") #meat - VO'D
define piss = Character("", kind=nvl, color="#ffffff", what_color="#fff787", what_prefix="\"", what_suffix="\"", callback=SpeakingBlip, cb_speakerID="piss_") #the pee on the floor - VO'D
define chud = Character("", kind=nvl, color="#ffffff", what_color="#afafaf", what_prefix="\"", what_suffix="\"", callback=SpeakingBlip, cb_speakerID="chud_") #chud customer - VO'D

transform Nameplate(frame1, frame2, frame3, frame4):
    frame1
    0.15
    frame2
    0.15
    choice:
        frame3
    choice:
        frame1
    0.15
    choice:
        frame2
    choice:
        frame4
    0.15
    frame3
    0.15
    frame4
    0.15
    repeat

transform Speaker(frame1, frame2, frame3):
    frame1
    0.15
    frame2
    0.15
    frame3
    0.15
    repeat

transform MainMenuSky(frame1, frame2, frame3, frame4, frame5, frame6, frame7, frame8, frame9, frame10, frame11, frame12, alphaValue):
    xpos 0
    ypos -0.25
    
    frame1 with Dissolve(.125), alpha alphaValue
    0.25
    frame2 with Dissolve(.125), alpha alphaValue
    0.25
    frame3 with Dissolve(.125), alpha alphaValue
    0.25
    frame4 with Dissolve(.125), alpha alphaValue
    0.25
    frame5 with Dissolve(.125), alpha alphaValue
    0.25
    frame6 with Dissolve(.125), alpha alphaValue
    0.25
    frame7 with Dissolve(.125), alpha alphaValue
    0.25
    frame8 with Dissolve(.125), alpha alphaValue
    0.25
    frame9 with Dissolve(.125), alpha alphaValue
    0.25
    frame10 with Dissolve(.125), alpha alphaValue
    0.25
    frame11 with Dissolve(.125), alpha alphaValue
    0.25
    frame12 with Dissolve(.125), alpha alphaValue
    0.25
    repeat

transform MainMenuItske():
    "gui/itske_field1.png"
    0.15
    "gui/itske_field2.png"
    0.15
    "gui/itske_field3.png"
    0.15
    repeat

transform MainMenuLogo():
    "gui/logo1.png"
    0.15
    "gui/logo2.png"
    0.15
    "gui/logo3.png"
    0.15
    repeat

transform portrait:
    xpos 520
    ypos 70
    xsize 150
    ysize 175

transform showcase:
    xpos 0.275
    ypos 0.55
    xanchor 0.5
    yanchor 0.5

transform bgpos:
    ypos 1.0

#region Scanline Transforms

transform scanlines_slight:
    ypos 1.0
    choice:
        0.05
    choice:
        0.15
    choice:
        0.2
    pause 0.05
    choice:
        ypos 0.95
    choice:
        ypos 0.96
    choice:
        ypos 0.97
    choice:
        ypos 1.0
    choice:
        ypos 0.8
    choice:
        0.05
    choice:
        0.15
    choice:
        0.2
    pause 0.05
    repeat

transform scanlines_moderate:
    ypos 1.0
    pause 0.1
    choice:
        ypos 0.99
    choice:
        ypos 0.95
    choice:
        ypos 0.98
    choice:
        ypos 0.5
    choice:
        ypos 0.35
    choice:
        ypos 0.6
    pause 0.1
    repeat

transform scanlines_intense:
    ypos 1.0
    choice:
        0.0
    choice:
        0.05
    choice:
        0.1
    pause 0.1
    choice:
        ypos 0.1
    choice:
        ypos 0.2
    choice:
        ypos 0.3
    choice:
        ypos 0.4
    choice:
        ypos 0.5
    choice:
        ypos 0.6
    choice:
        ypos 0.7
    choice:
        ypos 0.8
    choice:
        ypos 0.9
    choice:
        ypos 0.95
    choice:
        ypos 1.0
    pause 0.05
    choice:
        0.0
    choice:
        0.05
    choice:
        0.1
    repeat

image pulse_scanlines:
    "scanlines"
    alpha 0.4
    linear 3 alpha 0.2
    linear 2  alpha 0.4

    linear 0.05 alpha 0.01
    linear 0.05 alpha 0.4

    linear 0.2 alpha 0.1
    linear 0.1 alpha 0.4

    linear 3 alpha 0.2
    linear 2  alpha 0.4

    linear 3 alpha 0.2
    linear 2  alpha 0.4
    repeat

#endregion

#region Flicker Transforms

transform FlickerRight(image):
    ypos 1.0
    image

    choice:
        0.1
        xpos -0.003
    choice:
        0.2
        xpos -0.002
    choice:
        0.3
        xpos -0.001
    0.1
    choice:
        0.1
        xpos -0.001
    choice:
        0.2
        xpos -0.005
    choice:
        0.3
        xpos -0.003
    0.1
    choice:
        0.05
        xpos -0.001
    choice:
        0.05
        xpos -0.005
    choice:
        0.05
        xpos -0.001
    choice:
        0.05
        xpos -0.005
    choice:
        0.05
        xpos 0.002
    0.1
    choice:
        0.1
    choice:
        0.1
    choice:
        0.05

    repeat

transform FlickerLeft(image):
    ypos 1.0
    image

    choice:
        0.1
        xpos 0.003
    choice:
        0.2
        xpos 0.002
    choice:
        0.3
        xpos 0.001
    0.1
    choice:
        0.1
        xpos 0.001
    choice:
        0.2
        xpos 0.005
    choice:
        0.3
        xpos 0.003
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
        xpos 0.002
    0.1
    choice:
        0.1
    choice:
        0.1
    choice:
        0.05

    repeat

transform FlickerUp_slight(image):
    ypos 1.0
    image

    choice:
        0.1
    choice:
        0.1
    choice:
        0.05
    choice:
        ypos 0.997
        choice:
            0.1
        choice:
            0.1
        choice:
            0.05
    choice:
        ypos 0.995
        choice:
            0.1
        choice:
            0.1
        choice:
            0.05
    choice:
        ypos 1.0
        choice:
            0.1
        choice:
            0.1
        choice:
            0.05
    choice:
        ypos 0.99
        choice:
            0.1
        choice:
            0.1
        choice:
            0.05
    repeat

transform FlickerUp_moderate(image):
    ypos 1.0
    image

    choice:
        0.4
    choice:
        0.9
    choice:
        1.9
    0.1
    choice:
        linear 6 ypos 0.8
    choice:
        ypos 0.97
    choice:
        ypos 0.95
    0.2
    ypos 1.0
    choice:
        0.4
    choice:
        0.9
    choice:
        1.4
    0.1
    choice:
        ypos 0.9
    choice:
        ypos 0.95
    choice:
        ypos 0.98
    0.1
    choice:
        0.4
    choice:
        0.9
    choice:
        1.4
    repeat

transform Flashback(image, _prd, _amp, _spd):
    image
    function WaveShader(direction='both', repeat='mirrored', period =_prd, amp=_amp, speed=_spd)

#endregion

#region ITSKE

image itske_showcase:
    "f_exp_neutral1"
    0.15
    "f_exp_neutral2"
    0.15
    "f_exp_neutral3"
    0.15

    "f_exp_stressed1"
    0.15
    "f_exp_stressed2"
    0.15
    "f_exp_stressed3"
    0.15

    "f_exp_flustered1"
    0.15
    "f_exp_flustered2"
    0.15
    "f_exp_flustered3"
    0.15

    "f_exp_exerted1"
    0.15
    "f_exp_exerted2"
    0.15
    "f_exp_exerted3"
    0.15

    "f_exp_nervous1"
    0.15
    "f_exp_nervous2"
    0.15
    "f_exp_nervous3"
    0.15

    "f_exp_edge1"
    0.15
    "f_exp_edge2"
    0.15
    "f_exp_edge3"
    0.15

    "f_exp_bust1"
    0.15
    "f_exp_bust2"
    0.15
    "f_exp_bust3"
    0.15

    "f_exp_angry1"
    0.15
    "f_exp_angry2"
    0.15
    "f_exp_angry3"
    0.15

    "f_exp_enraged1"
    0.15
    "f_exp_enraged2"
    0.15
    "f_exp_enraged3"
    0.15

    "f_exp_yelling1"
    0.15
    "f_exp_yelling2"
    0.15
    "f_exp_yelling3"
    0.15

    "f_exp_annoyed1"
    0.15
    "f_exp_annoyed2"
    0.15
    "f_exp_annoyed3"
    0.15

    "f_exp_blehhh1"
    0.15
    "f_exp_blehhh2"
    0.15
    "f_exp_blehhh3"
    0.15

    "f_exp_heartbroken1"
    0.15
    "f_exp_heartbroken2"
    0.15
    "f_exp_heartbroken3"
    0.15

    "f_exp_sad1"
    0.15
    "f_exp_sad2"
    0.15
    "f_exp_sad3"
    0.15

    "f_exp_crying1"
    0.15
    "f_exp_crying2"
    0.15
    "f_exp_crying3"
    0.15

    "f_exp_bawling1"
    0.15
    "f_exp_bawling2"
    0.15
    "f_exp_bawling3"
    0.15

    "f_exp_disgust1"
    0.15
    "f_exp_disgust2"
    0.15
    "f_exp_disgust3"
    0.15

    "f_exp_tired1"
    0.15
    "f_exp_tired2"
    0.15
    "f_exp_tired3"
    0.15

    "f_exp_smug1"
    0.15
    "f_exp_smug2"
    0.15
    "f_exp_smug3"
    0.15

    "f_exp_smiling1"
    0.15
    "f_exp_smiling2"
    0.15
    "f_exp_smiling3"
    0.15

    "f_exp_forcedsmile1"
    0.15
    "f_exp_forcedsmile2"
    0.15
    "f_exp_forcedsmile3"
    0.15

    "f_exp_pouting1"
    0.15
    "f_exp_pouting2"
    0.15
    "f_exp_pouting3"
    0.15

    "f_exp_thinking1"
    0.15
    "f_exp_thinking2"
    0.15
    "f_exp_thinking3"
    0.15

    "f_exp_shock1"
    0.15
    "f_exp_shock2"
    0.15
    "f_exp_shock3"
    0.15

    "f_exp_scared1"
    0.15
    "f_exp_scared2"
    0.15
    "f_exp_scared3"
    0.15

    "f_exp_terrified1"
    0.15
    "f_exp_terrified2"
    0.15
    "f_exp_terrified3"
    0.15
    repeat

image itske_showcase_crush:
    "f_exp_crush1_1"
    0.15
    "f_exp_crush1_2"
    0.15
    "f_exp_crush1_3"
    0.15

    "f_exp_crush2_1"
    0.15
    "f_exp_crush2_2"
    0.15
    "f_exp_crush2_3"
    0.15

    "f_exp_crush3_1"
    0.15
    "f_exp_crush3_2"
    0.15
    "f_exp_crush3_3"
    0.15

    "f_exp_crush4_1"
    0.15
    "f_exp_crush4_2"
    0.15
    "f_exp_crush4_3"
    0.15

    "f_exp_crush5_1"
    0.15
    "f_exp_crush5_2"
    0.15
    "f_exp_crush5_3"
    0.15

    "f_exp_crush6_1"
    0.15
    "f_exp_crush6_2"
    0.15
    "f_exp_crush6_3"
    0.15
    repeat

layeredimage speaker itske:
    group body:
        attribute work default:
            Speaker("f_body_work1", "f_body_work2", "f_body_work3")
        attribute tank:
            Speaker("f_body_tank1", "f_body_tank2", "f_body_tank3")
        attribute naked:
            Speaker("f_body_naked1", "f_body_naked2", "f_body_naked3")
        attribute drawn:
            Speaker("f_body_drawn1", "f_body_drawn2", "f_body_drawn3")
        attribute disheveled:
            Speaker("f_body_disheveled1", "f_body_disheveled2", "f_body_disheveled3")

    group face:
        attribute neutral default:
            Speaker("f_exp_neutral1", "f_exp_neutral2", "f_exp_neutral3")
        attribute stressed:
            Speaker("f_exp_stressed1", "f_exp_stressed2", "f_exp_stressed3")
        attribute flustered:
            Speaker("f_exp_flustered1", "f_exp_flustered2", "f_exp_flustered3")
        attribute exerted:
            Speaker("f_exp_exerted1", "f_exp_exerted2", "f_exp_exerted3")
        attribute nervous:
            Speaker("f_exp_nervous1", "f_exp_nervous2", "f_exp_nervous3")
        attribute edge:
            Speaker("f_exp_edge1", "f_exp_edge2", "f_exp_edge3")
        attribute bust:
            Speaker("f_exp_bust1", "f_exp_bust2", "f_exp_bust3")
        attribute angry:
            Speaker("f_exp_angry1", "f_exp_angry2", "f_exp_angry3")
        attribute enraged:
            Speaker("f_exp_enraged1", "f_exp_enraged2", "f_exp_enraged3")
        attribute yelling:
            Speaker("f_exp_yelling1", "f_exp_yelling2", "f_exp_yelling3")
        attribute annoyed:
            Speaker("f_exp_annoyed1", "f_exp_annoyed2", "f_exp_annoyed3")
        attribute blehhh:
            Speaker("f_exp_blehhh1", "f_exp_blehhh2", "f_exp_blehhh3")
        attribute heartbroken:
            Speaker("f_exp_heartbroken1", "f_exp_heartbroken2", "f_exp_heartbroken3")
        attribute sad:
            Speaker("f_exp_sad1", "f_exp_sad2", "f_exp_sad3")
        attribute crying:
            Speaker("f_exp_crying1", "f_exp_crying2", "f_exp_crying3")
        attribute bawling:
            Speaker("f_exp_bawling1", "f_exp_bawling2", "f_exp_bawling3")
        attribute disgust:
            Speaker("f_exp_disgust1", "f_exp_disgust2", "f_exp_disgust3")
        attribute tired:
            Speaker("f_exp_tired1", "f_exp_tired2", "f_exp_tired3")
        attribute smug:
            Speaker("f_exp_smug1", "f_exp_smug2", "f_exp_smug3")
        attribute smiling:
            Speaker("f_exp_smiling1", "f_exp_smiling2", "f_exp_smiling3")
        attribute forcedsmile:
            Speaker("f_exp_forcedsmile1", "f_exp_forcedsmile2", "f_exp_forcedsmile3")
        attribute pouting:
            Speaker("f_exp_pouting1", "f_exp_pouting2", "f_exp_pouting3")
        attribute thinking:
            Speaker("f_exp_thinking1", "f_exp_thinking2", "f_exp_thinking3")
        attribute shock:
            Speaker("f_exp_shock1", "f_exp_shock2", "f_exp_shock3")
        attribute scared:
            Speaker("f_exp_scared1", "f_exp_scared2", "f_exp_scared3")
        attribute terrified:
            Speaker("f_exp_terrified1", "f_exp_terrified2", "f_exp_terrified3")
        attribute confused:
            Speaker("f_exp_confused1","f_exp_confused2","f_exp_confused3")
        attribute bothered:
            Speaker("f_exp_bothered1","f_exp_bothered2","f_exp_bothered3")
        attribute upset:
            Speaker("f_exp_upset1","f_exp_upset2","f_exp_upset3")
        attribute focused:
            Speaker("f_exp_focused1","f_exp_focused2","f_exp_focused3")
        #crushing
        attribute crush1:
            Speaker("f_exp_crush1_1","f_exp_crush1_2","f_exp_crush1_3")
        attribute crush2:
            Speaker("f_exp_crush2_1","f_exp_crush2_2","f_exp_crush2_3")
        attribute crush3:
            Speaker("f_exp_crush3_1","f_exp_crush3_2","f_exp_crush3_3")
        attribute crush4:
            Speaker("f_exp_crush4_1","f_exp_crush4_2","f_exp_crush4_3")
        attribute crush5:
            Speaker("f_exp_crush5_1","f_exp_crush5_2","f_exp_crush5_3")
        attribute crush6:
            Speaker("f_exp_crush6_1","f_exp_crush6_2","f_exp_crush6_3")
        #showcase sequences
        attribute showcase:
            "itske_showcase"
        attribute showcase_crush:
            "itske_showcase_crush"

    group nameplate:
        attribute name default:
            Nameplate("f_nameplate1","f_nameplate2","f_nameplate3","f_nameplate4")
        attribute trash:
            Nameplate("f_nameplate_trash1","f_nameplate_trash2","f_nameplate_trash3","f_nameplate_trash4")

#endregion

#region JENN

layeredimage speaker jenn:
    group body:
        attribute body default:
            Speaker("j_body1", "j_body2", "j_body3")

    group face:
        attribute neutral default:
            Speaker("j_exp_neutral1", "j_exp_neutral2", "j_exp_neutral3")
        attribute worried:
            Speaker("j_exp_worried1", "j_exp_worried2", "j_exp_worried3")
        attribute enraged:
            Speaker("j_exp_enraged1", "j_exp_enraged2", "j_exp_enraged3")
        attribute cringe:
            Speaker("j_exp_cringe1", "j_exp_cringe2", "j_exp_cringe3")

    group nameplate:
        attribute name default:
            Nameplate("j_nameplate1","j_nameplate2","j_nameplate3","j_nameplate4")
        attribute manager:
            Nameplate("j_nameplate_mgr1","j_nameplate_mgr2","j_nameplate_mgr3","j_nameplate_mgr4")

#endregion

#region TOM

layeredimage speaker tom:
    group body:
        attribute body default:
            Speaker("t_body1", "t_body2", "t_body3")

    group face:
        attribute neutral default:
            Speaker("t_exp_neutral1", "t_exp_neutral2", "t_exp_neutral3")
        attribute sad:
            Speaker("t_exp_sad1", "t_exp_sad2", "t_exp_sad3")
        attribute shy:
            Speaker("t_exp_shy1", "t_exp_shy2", "t_exp_shy3")

    group nameplate:
        attribute name default:
            Nameplate("t_nameplate1","t_nameplate2","t_nameplate3","t_nameplate4")

#endregion

#region MAE

layeredimage speaker mae:
    group body:
        attribute body default:
            Speaker("m_body1", "m_body2", "m_body3")

    group face:
        attribute neutral default:
            Speaker("m_exp_neutral1", "m_exp_neutral2", "m_exp_neutral3")
        attribute happy:
            Speaker("m_exp_happy1", "m_exp_happy2", "m_exp_happy3")
        attribute stressed:
            Speaker("m_exp_stressed1", "m_exp_stressed2", "m_exp_stressed3")

    group nameplate:
        attribute name default:
            Nameplate("m_nameplate1","m_nameplate2","m_nameplate3","m_nameplate4")

#endregion

#region MEAT

layeredimage speaker meat:
    group body:
        attribute unjacketed default:
            Speaker("mt_body_unjacketed1", "mt_body_unjacketed2", "mt_body_unjacketed3")
        attribute jacketed:
            Speaker("mt_body_jacketed1", "mt_body_jacketed2", "mt_body_jacketed3")

    group face:
        attribute neutral default:
            Speaker("mt_exp_neutral1", "mt_exp_neutral2", "mt_exp_neutral3")
        attribute aroused:
            Speaker("mt_exp_aroused1", "mt_exp_aroused2", "mt_exp_aroused3")
        attribute smug:
            Speaker("mt_exp_smug1", "mt_exp_smug2", "mt_exp_smug3")
        attribute shock:
            Speaker("mt_exp_shock1", "mt_exp_shock2", "mt_exp_shock3")
        attribute embarrassed:
            Speaker("mt_exp_embarrassed1", "mt_exp_embarrassed2", "mt_exp_embarrassed3")

    group nameplate:
        attribute name default:
            Nameplate("mt_nameplate1","mt_nameplate2","mt_nameplate3","mt_nameplate4")

#endregion

#region CAMMY

layeredimage speaker cammy:
    group body:
        attribute body default:
            Speaker("c_body1", "c_body2", "c_body3")

    group face:
        attribute neutral default:
            Speaker("c_exp_neutral1","c_exp_neutral2","c_exp_neutral3")
        attribute aroused:
            Speaker("c_exp_aroused1","c_exp_aroused2","c_exp_aroused3")
        attribute focused:
            Speaker("c_exp_focused1","c_exp_focused2","c_exp_focused3")
        attribute happy:
            Speaker("c_exp_happy1","c_exp_happy2","c_exp_happy3")
        attribute smiling:
            Speaker("c_exp_smiling1","c_exp_smiling2","c_exp_smiling3")
        attribute worried:
            Speaker("c_exp_worried1","c_exp_worried2","c_exp_worried3")

    group nameplate:
        attribute name default:
            Nameplate("c_nameplate1","c_nameplate2","c_nameplate3","c_nameplate4")

#endregion

#region PIPER

layeredimage speaker piper:
    group body:
        attribute human default:
            Speaker("p_body_human1", "p_body_human2", "p_body_human3")
        attribute body_warped1:
            Speaker("p_body_warped1_1", "p_body_warped1_2", "p_body_warped1_3")
        attribute body_warped2:
            Speaker("p_body_warped2_1", "p_body_warped2_2", "p_body_warped2_3")
        attribute body_warped3:
            Speaker("p_body_warped3_1", "p_body_warped3_2", "p_body_warped3_3")

    group face:
        attribute neutral default:
            Speaker("p_exp_neutral1", "p_exp_neutral2", "p_exp_neutral3")
        attribute grin:
            Speaker("p_exp_grin1", "p_exp_grin2", "p_exp_grin3")
        attribute itske:
            Speaker("f_exp_smug1","f_exp_smug2","f_exp_smug3")
        attribute exp_warped1:
            Speaker("p_exp_warped1_1", "p_exp_warped1_2", "p_exp_warped1_3")
        attribute exp_warped2:
            Speaker("p_exp_warped2_1", "p_exp_warped2_2", "p_exp_warped2_3")
        attribute exp_warped3:
            Speaker("p_exp_warped3_1", "p_exp_warped3_2", "p_exp_warped3_3")

    group nameplate:
        attribute name default:
            Nameplate("p_nameplate1","p_nameplate2","p_nameplate3","p_nameplate4")
        attribute que:
            Nameplate("p_nameplate_que1","p_nameplate_que2","p_nameplate_que3","p_nameplate_que4")

#endregion

#region CHUD

layeredimage speaker chud:
    group body:
        attribute body default:
            Speaker("chud_body1", "chud_body2", "chud_body3")

    group face:
        attribute neutral default:
            Speaker("chud_exp_neutral1", "chud_exp_neutral2", "chud_exp_neutral3")

    group nameplate:
        attribute name default:
            Nameplate("chud_nameplate1","chud_nameplate2","chud_nameplate3","chud_nameplate4")

#endregion

#region PISS

layeredimage speaker piss:
    group body:
        attribute body default:
            Speaker("piss_body1", "piss_body2", "piss_body3")

    group face:
        attribute neutral default:
            Speaker("piss_exp1", "piss_exp2", "piss_exp3")

    group nameplate:
        attribute name default:
            Nameplate("piss_nameplate1","piss_nameplate2","piss_nameplate3","piss_nameplate4")

#endregion

#region DATE

layeredimage speaker date:
    group body:
        attribute body default:
            Speaker("d_body1", "d_body2", "d_body3")

    group face:
        attribute neutral default:
            Speaker("d_exp_neutral1", "d_exp_neutral2", "d_exp_neutral3")
        attribute smiling:
            Speaker("d_exp_smiling1","d_exp_smiling2","d_exp_smiling3")
        attribute worried:
            Speaker("d_exp_worried1","d_exp_worried2","d_exp_worried3")
        attribute awkward:
            Speaker("d_exp_awkward1","d_exp_awkward2","d_exp_awkward3")
        attribute yikes:
            Speaker("d_exp_yikes1","d_exp_yikes2","d_exp_yikes3")

    group nameplate:
        attribute name default:
            Nameplate("d_nameplate1","d_nameplate2","d_nameplate3","d_nameplate4")

#endregion

#region BACKGROUNDS

layeredimage bg backyard:
    group main:
        attribute backyard default:
            at bgpos
            "backyard"

    group red:
        attribute backyard_r default:
            FlickerRight("backyard_r")
            blend "add"

    group green:
        attribute backyard_g default:
            FlickerUp_slight("backyard_g")
            blend "add"

    group blue:
        attribute backyard_b default:
            FlickerLeft("backyard_b")
            blend "add"
            
    group scanlines:
        attribute slight default:
            at scanlines_slight
            "pulse_scanlines"
        attribute moderate:
            at scanlines_moderate
            "pulse_scanlines"
        attribute intense:
            at scanlines_intense
            "pulse_scanlines"

layeredimage bg loveshot1:
    group main:
        attribute loveshot1 default:
            at bgpos
            "piper_loveshot1"

    group red:
        attribute loveshot1_r default:
            FlickerRight("piper_loveshot1_r")
            blend "add"

    group green:
        attribute loveshot1_g default:
            FlickerUp_slight("piper_loveshot1_g")
            blend "add"

    group blue:
        attribute loveshot1_b default:
            FlickerLeft("piper_loveshot1_b")
            blend "add"
            
    group scanlines:
        attribute slight default:
            at scanlines_slight
            "pulse_scanlines"
        attribute moderate:
            at scanlines_moderate
            "pulse_scanlines"
        attribute intense:
            at scanlines_intense
            "pulse_scanlines"

layeredimage bg loveshot2:
    group main:
        attribute loveshot2 default:
            at bgpos
            "piper_loveshot2"

    group red:
        attribute loveshot2_r default:
            FlickerRight("piper_loveshot2_r")
            blend "add"

    group green:
        attribute loveshot2_g default:
            FlickerUp_slight("piper_loveshot2_g")
            blend "add"

    group blue:
        attribute loveshot2_b default:
            FlickerLeft("piper_loveshot2_b")
            blend "add"
            
    group scanlines:
        attribute slight default:
            at scanlines_slight
            "pulse_scanlines"
        attribute moderate:
            at scanlines_moderate
            "pulse_scanlines"
        attribute intense:
            at scanlines_intense
            "pulse_scanlines"

layeredimage bg office:
    group main:
        attribute office default:
            at bgpos
            "office"

    group red:
        attribute office_r default:
            FlickerRight("office_r")
            blend "add"
    
    group green:
        attribute office_g default:
            FlickerUp_slight("office_g")
            blend "add"
    
    group blue:
        attribute office_b default:
            FlickerLeft("office_b")
            blend "add"

    group scanlines:
        attribute slight default:
            at scanlines_slight
            "pulse_scanlines"
        attribute moderate:
            at scanlines_moderate
            "pulse_scanlines"
        attribute intense:
            at scanlines_intense
            "pulse_scanlines"

layeredimage bg bathroom:
    group main:
        attribute bathroom default:
            at bgpos
            "bathroom"

    group red:
        attribute bathroom_r default:
            FlickerRight("bathroom_r")
            blend "add"

    group green:
        attribute bathroom_g default:
            FlickerUp_slight("bathroom_g")
            blend "add"

    group blue:
        attribute bathroom_b default:
            FlickerLeft("bathroom_b")
            blend "add"
            
    group scanlines:
        attribute slight default:
            at scanlines_slight
            "pulse_scanlines"
        attribute moderate:
            at scanlines_moderate
            "pulse_scanlines"
        attribute intense:
            at scanlines_intense
            "pulse_scanlines"

layeredimage bg bedroom:
    group main:
        attribute bedroom default:
            at bgpos
            "bedroom"

    group red:
        attribute bedroom_r default:
            FlickerRight("bedroom_r")
            blend "add"

    group green:
        attribute bedroom_g default:
            FlickerUp_slight("bedroom_g")
            blend "add"

    group blue:
        attribute bedroom_b default:
            FlickerLeft("bedroom_b")
            blend "add"
            
    group scanlines:
        attribute slight default:
            at scanlines_slight
            "pulse_scanlines"
        attribute moderate:
            at scanlines_moderate
            "pulse_scanlines"
        attribute intense:
            at scanlines_intense
            "pulse_scanlines"

layeredimage bg bedroom_fb:
    group red:
        attribute flashback_r default:
            Flashback("bedroom_r", (2.5, 1.1), (-2.0, 1.4), (0.3, -1.2))
            blend "add"

    group green:
        attribute flashback_g default:
            Flashback("bedroom_g", (1.0, 0.3), (4.0, -1.2), (0.6, 1.5))
            blend "add"

    group blue:
        attribute flashback_b default:
            Flashback("bedroom_b", (0.6, 2.1), (1.0, 2.1), (1.5, 2.0))
            blend "add"

layeredimage bg counter:
    group main:
        attribute counter default:
            at bgpos
            "counter"

    group red:
        attribute counter_r default:
            FlickerRight("counter_r")
            blend "add"

    group green:
        attribute counter_g default:
            FlickerUp_slight("counter_g")
            blend "add"

    group blue:
        attribute counter_b default:
            FlickerLeft("counter_b")
            blend "add"
            
    group scanlines:
        attribute slight default:
            at scanlines_slight
            "pulse_scanlines"
        attribute moderate:
            at scanlines_moderate
            "pulse_scanlines"
        attribute intense:
            at scanlines_intense
            "pulse_scanlines"

layeredimage bg desk:
    group main:
        attribute desk default:
            at bgpos
            "desk"

    group red:
        attribute desk_r default:
            FlickerRight("desk_r")
            blend "add"

    group green:
        attribute desk_g default:
            FlickerUp_slight("desk_g")
            blend "add"

    group blue:
        attribute desk_b default:
            FlickerLeft("desk_b")
            blend "add"
            
    group scanlines:
        attribute slight default:
            at scanlines_slight
            "pulse_scanlines"
        attribute moderate:
            at scanlines_moderate
            "pulse_scanlines"
        attribute intense:
            at scanlines_intense
            "pulse_scanlines"

layeredimage bg frontdoor:
    group main:
        attribute frontdoor default:
            at bgpos
            "frontdoor"

    group red:
        attribute frontdoor_r default:
            FlickerRight("frontdoor_r")
            blend "add"

    group green:
        attribute frontdoor_g default:
            FlickerUp_slight("frontdoor_g")
            blend "add"

    group blue:
        attribute frontdoor_b default:
            FlickerLeft("frontdoor_b")
            blend "add"
            
    group scanlines:
        attribute slight default:
            at scanlines_slight
            "pulse_scanlines"
        attribute moderate:
            at scanlines_moderate
            "pulse_scanlines"
        attribute intense:
            at scanlines_intense
            "pulse_scanlines"

layeredimage bg hallway:
    group main:
        attribute hallway default:
            at bgpos
            "hallway"

    group red:
        attribute hallway_r default:
            FlickerRight("hallway_r")
            blend "add"

    group green:
        attribute hallway_g default:
            FlickerUp_slight("hallway_g")
            blend "add"

    group blue:
        attribute hallway_b default:
            FlickerLeft("hallway_b")
            blend "add"
            
    group scanlines:
        attribute slight default:
            at scanlines_slight
            "pulse_scanlines"
        attribute moderate:
            at scanlines_moderate
            "pulse_scanlines"
        attribute intense:
            at scanlines_intense
            "pulse_scanlines"

layeredimage bg hobby:
    group main:
        attribute hobby default:
            at bgpos
            "hobby"

    group red:
        attribute hobby_r default:
            FlickerRight("hobby_r")
            blend "add"

    group green:
        attribute hobby_g default:
            FlickerUp_slight("hobby_g")
            blend "add"

    group blue:
        attribute hobby_b default:
            FlickerLeft("hobby_b")
            blend "add"
            
    group scanlines:
        attribute slight default:
            at scanlines_slight
            "pulse_scanlines"
        attribute moderate:
            at scanlines_moderate
            "pulse_scanlines"
        attribute intense:
            at scanlines_intense
            "pulse_scanlines"

layeredimage bg kitchen:
    group main:
        attribute kitchen default:
            at bgpos
            "kitchen"

    group red:
        attribute kitchen_r default:
            FlickerRight("kitchen_r")
            blend "add"

    group green:
        attribute kitchen_g default:
            FlickerUp_slight("kitchen_g")
            blend "add"

    group blue:
        attribute kitchen_b default:
            FlickerLeft("kitchen_b")
            blend "add"
            
    group scanlines:
        attribute slight default:
            at scanlines_slight
            "pulse_scanlines"
        attribute moderate:
            at scanlines_moderate
            "pulse_scanlines"
        attribute intense:
            at scanlines_intense
            "pulse_scanlines"

layeredimage bg livingroom:
    group main:
        attribute livingroom default:
            at bgpos
            "livingroom"

    group red:
        attribute livingroom_r default:
            FlickerRight("livingroom_r")
            blend "add"

    group green:
        attribute livingroom_g default:
            FlickerUp_slight("livingroom_g")
            blend "add"

    group blue:
        attribute livingroom_b default:
            FlickerLeft("livingroom_b")
            blend "add"
            
    group scanlines:
        attribute slight default:
            at scanlines_slight
            "pulse_scanlines"
        attribute moderate:
            at scanlines_moderate
            "pulse_scanlines"
        attribute intense:
            at scanlines_intense
            "pulse_scanlines"

layeredimage bg machinery:
    group main:
        attribute machinery default:
            at bgpos
            "machinery"

    group red:
        attribute machinery_r default:
            FlickerRight("machinery_r")
            blend "add"

    group green:
        attribute machinery_g default:
            FlickerUp_slight("machinery_g")
            blend "add"

    group blue:
        attribute machinery_b default:
            FlickerLeft("machinery_b")
            blend "add"
            
    group scanlines:
        attribute slight default:
            at scanlines_slight
            "pulse_scanlines"
        attribute moderate:
            at scanlines_moderate
            "pulse_scanlines"
        attribute intense:
            at scanlines_intense
            "pulse_scanlines"

layeredimage bg walkway:
    group main:
        attribute walkway default:
            at bgpos
            "walkway"

    group red:
        attribute walkway_r default:
            FlickerRight("walkway_r")
            blend "add"

    group green:
        attribute walkway_g default:
            FlickerUp_slight("walkway_g")
            blend "add"

    group blue:
        attribute walkway_b default:
            FlickerLeft("walkway_b")
            blend "add"
            
    group scanlines:
        attribute slight default:
            at scanlines_slight
            "pulse_scanlines"
        attribute moderate:
            at scanlines_moderate
            "pulse_scanlines"
        attribute intense:
            at scanlines_intense
            "pulse_scanlines"

#endregion