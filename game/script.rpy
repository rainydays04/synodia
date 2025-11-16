# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Athena")
define am = Character("Amaterasu")
define ar = Character("Artemis")
define b = Character("Bellona")
define g = Character("Guanyin")
define k = Character("Kannon")
define m = Character("Ma'at")
define mi = Character("Minerva")
define s = Character("Saraswati")
define se = Character("Seshat")
image athena = im.Scale("athena.png",1000,1000)
image amaterasu = im.Scale("amaterasu.png",1000,1000)
image artemis = im.Scale("artemis.png",1000,1000)
image bellona = im.Scale("bellona.png",1000,1000)
image guanyin = im.Scale("guanyin.png",1000,1000)
image kannon = im.Scale("kannon.png",1000,1000)
image maat = im.Scale("ma'at.png",1000,1000)
image minerva = im.Scale("minerva.png",1000,1000)
image saraswati = im.Scale("saraswati.png",1000,1000)
image seshat = im.Scale("seshat.png",1000,1000)
image bg stair = im.Scale("staircase.png",1920,1080)
image bg artmuseum = im.Scale("artmuseum.png",1920,1080)
image bg strategy = im.Scale("strategy.png",1920,1080)
image bg weapons = im.Scale("weapons.png",1920,1080)
default scholar = 0
default ruler = 0
default soldier = 0



label start:


  
    show bg stair

    narrator "After weeks of travel, you finally make it to the steps of the ancient temple"
    narrator "The temple that is said to have several vessels of knowledge for who you want to become"
    narrator "But {w}what do you want to become?"
    narrator "Before you comeplete your though, a tall woman approaches you, (other important decriptors for athena)"
    show athena
    a "What brings you here?"
    menu:
        "I come here to learn of the arts":
            a "The arts you say? I know a group of ladies who can assist you in that.Down the hall to the left and you will find the knowledge you seek"
            jump art_room
        "I come to learn the ways of a warrior":
            a "A warrior is a noble job, but that means you need noble teachers. Down the hall to the right and you will find the knowledge you seek  "
            jump weapons_room
        "To become a leader for the people":
            a "A leader must know what its like to be led to have an idea of what people want. If you go straight down the hall you will find some of the best leaders"
            jump leadership
    return   

label art_room:
    hide athena
    narrator "You walk down the hall and you see a sign."
    narrator"{i}In this hall dwell three goddesses, but you may address only one.{i}"
    show bg artmuseum
    menu:
        "Saraswati":
            narrator "You walk towards a graceful and serene women draped in gold and white. You can hear a beautiful hum coming from a face decorated with thick, wavy hair. Goddess of music."
            show saraswati
            ar "I can hear the sound, but now I want to hear your voice! Tell me what you seek."
            menu:
                "I have come to hear your experience with music.":
                    $ scholar += 1
                    ar "Why do you ask of this?"
                    menu:
                        "I would love to hear your tale.":
                            ar "Oh! I'd love for someone to listen to my story like a song."
                            ar "I sang the notes that spoke to me, even when no one could hear."
                            ar "Take note of that."

                "I ask for help in leading my band troop.":
                    $ ruler += 1
                    ar "It is the song that strings people like a melody."
                    ar "Even the most alluring tune cannot bring harmony without heart."
                "I play the lyre for the armies. I seek out your advice.":
                    $ soldier += 1
                    ar "Play your strings while they play with swords!"
                    ar "You both must have pride in your job."
            ar "I have given you a lyric. Now build your ballad. Remember my words like a chorus."
                    
            
        "Seshat":
            narrator "When you enter the room, you walk towards and elegant a poised woman, palm scroll in hand. Goddess of writing and record-keeping."
            show seshat
            ar "I would like to hear the words I cannot see on paper."
            menu:
                "I have come to learn your story.":
                    $ scholar += 1
                    ar "Why do you ask of this?"
                    menu:
                        "I would love to hear your tale.":
                            ar "My story is better told in writing than orally."
                            ar "I sang the notes that spoke to me, even when no one could hear."
                            ar "Take note of that."

                "I ask for help in leading my band troop.":
                    $ ruler += 1
                    ar "It is the song that strings people like a melody."
                    ar "Even the most alluring tune cannot bring harmony without heart."
                "I play the lyre for the armies. I seek out your advice.":
                    $ soldier += 1
                    ar "Play your strings while they play with swords!"
                    ar "You both must have pride in your job."
            ar "I have given you a lyric. Now build your ballad. Remember my words like a chorus."

        "Minerva":
            narrator "The lady you appraoch is armoered with a regalnposture and sharp eyes. "
            show minerva
            ar "I can hear the sound, but now I want to hear your voice! Tell me what you seek."
            menu:
                "I have come to hear your experience with music.":
                    $ scholar += 1
                    ar "Why do you ask of this?"
                    menu:
                        "I would love to hear your tale.":
                            ar "Oh! I'd love for someone to listen to my story like a song."
                            ar "I sang the notes that spoke to me, even when no one could hear."
                            ar "Take note of that."

                "I ask for help in leading my band troop.":
                    $ ruler += 1
                    ar "It is the song that strings people like a melody."
                    ar "Even the most alluring tune cannot bring harmony without heart."
                "I play the lyre for the armies. I seek out your advice.":
                    $ soldier += 1
                    ar "Play your strings while they play with swords!"
                    ar "You both must have pride in your job."
            ar "I have given you a lyric. Now build your ballad. Remember my words like a chorus."

label weapons_room:
    hide athena
    narrator "You walk down the hall and you see a sign "
    narrator"{i}In this hall dwell three goddesses, but you may address only one.{i}"
    show bg weapons
    menu:
        "Artemis":
            narrator "You approach a tall woman. Sharp-eyed with moon-pale skin and a hunter’s stance. Goddess of the hunt, wilderness, and the night sky."
            show artemis
            ar "You have travled quite far to this temple. The moon has led you to talk to me{w} tell me why"
            menu:
                "I have come to hear your tales on being a warrior":
                    $ scholar += 1
                    ar "My tales? That is asking of much."
                    menu:
                        "Any length of knowledge from you is appreciated":
                            ar "Then I'll leave you with this"
                            ar "A girl followed a deer into the dark and found herself braver than the path."
                            ar "Remember this on your travels, young one"

                "I ask for your leadership to better my skills of a warrior":
                    $ ruler += 1
                    ar "You cannot take power. It is owned by those who protect their people"
                    ar "I look forward in seeing what you do"
                "I seek out your knowledge one tactical strategies of a warrior":
                    $ soldier += 1
                    ar "Move with the forest, not against it"
                    ar "You would make your advantage a burden if you do"
            ar "Go forth with what I share. I wish you luck dear warrior. No matter what fight you choose"
                    
            
        "Kannon":
            narrator "The goddess you appraoch is gentle-faced, calm, often shown in flowing robes with a peaceful aura. Goddess of mercy, compassion, and listening to the suffering. "
            show kannon
            k "Hello dear acolyte. I hear you traveled far? Please take a seat."
            k "You are in pursuit of knowledge, don't you? What would you like to ask?"
            menu:
                "When sharing the truth, is there beauty in softening it?":
                    $ scholar +=1
                    k"The beauty in sharing the truth is having the courage to share it"
                "Will I ever save enough lives to makeup for the ones lost?":
                    $ soldier +=1
                    k "Lives, attained and lost, are not to tally. Having any impact on one is a blessing on this earth"
                "How do I lead without losing myself to power?":
                    $ leader +=1
                    k "The one who loses themselves to power cannot truly lead by name nor action. So rest assured, have the ability to be lost, there is not use in being found"
            k "I truly admire your willingness to learn, dear. I look forward to see how you use this knowledge"
        "Bellona":
            narrator "Bellona is armored with eyes like burning coals. Goddess of war, discipline, and strategic victory."
            show bellona
            b "You are strong for traveling here in solitude and I respect that. So tell me, what do ask from me?"
            menu:
                "Why is it that conflict inspire creation?":
                    b"Because it is what survives from it"
                "Can strength exist without violence":
                    b "Strength exist first and can exist alone, but power lies in having restraint"
                "When is war justified?":
                    b"It is justified when peace has been given every chance possible, not simple as an excuse to avoid conflict"
            b"Please depart with this knowledge and I look forward to wha you do"
return

    

label leadership:
    hide athena
    narrator "You walk down the hall and you see a sign "
    narrator"{i}In this hall dwell three goddesses, but you may address only one.{i}"
    show bg strategy
    menu:
        "Ma'at":
            narrator "You approach a tall woman. Sharp-eyed with moon-pale skin and a hunter’s stance. Goddess of the hunt, wilderness, and the night sky."
            show maat
            ar "You have travled quite far to this temple. The moon has led you to talk to me{w} tell me why"
            menu:
                "I have come to hear your tales on being a warrior":
                    $ scholar += 1
                    ar "My tales? That is asking of much."
                    menu:
                        "Any length of knowledge from you is appreciated":
                            ar "Then I'll leave you with this"
                            ar "A girl followed a deer into the dark and found herself braver than the path."
                            ar "Remember this on your travels, young one"

                "I ask for your leadership to better my skills of a warrior":
                    $ ruler += 1
                    ar "You cannot take power. It is owned by those who protect their people"
                    ar "I look forward in seeing what you do"
                "I seek out your knowledge one tactical strategies of a warrior":
                    $ soldier += 1
                    ar "Move with the forest, not against it"
                    ar "You would make your advantage a burden if you do"
            ar "Go forth with what I share. I wish you luck dear warrior. No matter what fight you choose"
                    
            
        "Guanyin":
            narrator "The goddess you appraoch is gentle-faced, calm, often shown in flowing robes with a peaceful aura. Goddess of mercy, compassion, and listening to the suffering. "
            show guanyin

        "Amaterasu":
            narrator "Bellona is armored with eyes like burning coals. Goddess of war, discipline, and strategic victory."
            show amaterasu
