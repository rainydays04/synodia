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
image bg gardan = im.Scale("garden.png",1920,1080)
default scholar = 0
default ruler = 0
default soldier = 0
default scholar_path = False
default warrior_path = False
default ruler_path = False



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
    $ scholar_path = True
    hide athena
    narrator "You walk down the hall and you see a sign."
    narrator"{i}In this hall dwell three goddesses, but you may address only one.{i}"
    show bg artmuseum
    menu:
        "Saraswati":
            narrator "You walk towards a graceful and serene women draped in gold and white. You can hear a beautiful hum coming from a face decorated with thick, wavy hair. Goddess of music."
            show saraswati
            s "I can hear the sound, but now I want to hear your voice! Tell me what you seek."
            menu:
                "I have come to hear your experience with music.":
                    $ scholar += 1
                    s "Why do you ask of this?"
                    menu:
                        "I would love to hear your tale.":
                            s "Oh! I'd love for someone to listen to my story like a song."
                            s "I sang the notes that spoke to me, even when no one could hear."
                            s "Take note of that."

                "I ask for help in leading my band troop.":
                    $ ruler += 1
                    s "It is the song that strings people like a melody."
                    s "Even the most alluring tune cannot bring harmony without heart."
                "I play the lyre for the armies. I seek out your advice.":
                    $ soldier += 1
                    s "Play your strings while they play with swords!"
                    s "You both must have pride in your job."
            s "I have given you a lyric. Now build your ballad. Remember my words like a chorus."
            hide saraswati       
            
        "Seshat":
            narrator "When you enter the room, you walk towards and elegant a poised woman, palm scroll in hand. Goddess of writing and record-keeping."
            show seshat
            se "I would like to hear the words I cannot see on paper."
            menu:
                "I have come to learn your story.":
                    $ scholar += 1
                    se "What inspires your question?"
                    menu:
                        "Your anecdote is appealing to my ears.":
                            se "My story is better told in writing than orally."
                            se "Seek my book in the museum. I trust you with its secrets."

                "I would like to build a library.":
                    $ ruler += 1
                    se "Amazing. Your tale starts with the ones of others."
                    se "A keeper of history is a present to the future."

                "I hope to write stories about fallen warriors and friends.":
                    $ soldier += 1
                    se "Bless your narrative. Chronicles are crucial."
                    se "These accounts are necessary. You could write a novella!"

            se "Choose your own story. The plot is yours."
            hide seshat

        "Minerva":
            narrator "The lady you appraoch is armoered with a regal posture and eyes sharp for aesthetics. Goddess of art."
            show minerva
            mi "Paint me the picture of your business!"
            menu:
                "I hope to visualize your story. Speak your story.":
                    $ scholar += 1
                    mi "What a creative statement."
                    menu:
                        "I am drawn towards your story.":
                            mi "And you draw my attention."
                            mi "Look carefully at my work. Your analysis should take as equal work as my art."
                            mi "My story is hidden behind every drop of paint."

                "I will teach young ones to pursue an interest in the arts.":
                    $ ruler += 1
                    mi "Lovely. The future will be brighter than the sun of my drawings."
                    mi "The passion of children will stain you like ink."

                "I capture the horrors of war in my sketches.":
                    $ soldier += 1
                    mi "Pity to your soul."
                    mi "The palette cannot have as much color as the emotions of soldiers."
            mi "I expect my brush to have touched the canvas that is your mind."
            hide minerva
    if not warrior_path and not ruler_path:
        menu:
            "Where do you head of next?"
            "I should learn skills for the battlefield":
                jump weapons_room
            "I'd like to explore how toi become a better leader":
                jump leadership
    elif not warrior_path and ruler_path :
        menu:
            "Where do you head of next?"
            "I should learn skills for the battlefield":
                jump weapons_room
    elif warrior_path and not ruler_path:
        menu:
            "Where do you head of next?"
            "I'd like to explore how toi become a better leader":
                jump leadership
    else:
        jump ending 

label weapons_room:
    $ warrior_path =True
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
            hide artemis      
            
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
            hide kannon
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
            hide bellona
    if not scholar_path and not ruler_path:
        menu:
            "Where do you head of next?"
            "I wants to look more into the arts":
                jump art_room
            "I'd like to explore how toi become a better leader":
                jump leadership
    elif not scholar_path and ruler_path :
        menu:
            "Where do you head of next?"
            "I wants to look more into the arts":
                jump art_room
    elif scholar_path and not ruler_path:
        menu:
            "Where do you head of next?"
            "I'd like to explore how toi become a better leader":
                jump leadership
    else:
        jump ending 


    

label leadership:
    $ ruler_path = True
    hide athena
    narrator "You walk down the hall and you see a sign "
    narrator"{i}In this hall dwell three goddesses, but you may address only one.{i}"
    show bg strategy
    menu:
        "Ma'at":
            narrator "The woman you approach is tall and composed with a single ostriuch feather in her hair. Goddess of truth, balance, and cosmic order."
            show maat
            m "What is it you have come for? I will provide you with the knowledge of which exist as is?"
            menu:
                "How do I write a legacy that lives on after me":
                    m"The truth does not wear overtime, but instead it becomes more poignant"
                "How do I become a fair judge for the people?":
                    m "Weight each as I do with the heart. Without favo nor fear"
                "How do I know I am fighting for a just cause?":
                    m "Think with your heart before you do your blade. Thea heart is always truthful to the host while the blade only obeys"
            m "I send you off to turn these truths into actions"
            hide maat

        "Guanyin":
            narrator "Wrapped in flowing white robes, Guanyn has soft features across her calm face.Goddess of mercy, compassion, and protection."
            show guanyin
            g "I have been informed tou seek understanding, dear one. Let me provide you with a clear view"
            menu:
                "How can I turn the sorrow I experience into art to be shared":
                    g "Understand your sorrow first. If you do not understand it, then how can you share it to others?"
                "When I fight, how do restrain myself from cruelty":
                    g"Keep in mind what you are protecting, not what you are fighting against."
                "In what ways can hope be given to those who have lost it?":
                    g "Be an example, exude hope and light even in the simpliest of ways. Hope grows silently in the darkness of dread"
            hide guanyin
        "Amaterasu":
            narrator "Amaratsu has sunlit hair that glows as if under the dawn light, almost as warm as her eyes. Goddess of the sun, light, and renewal."
            show amaterasu
            am "You shine bright my acolyte. What would you like to know to have people follow it"
            menu:
                "Is there a way to capture warmth and light in my art?":
                    am "Create what inspires you, write the truth so others can bask in the light of your work"
                "Are there ways of which I can create new begginings for when everything around me falls?":
                    am "To rebuild everything you had, build with the future in mind. Not just the things but people too."
                "I will fall in battle, how do I rise again?":
                    am "Do as the sun and bring yourself up slowly until you brighten everything that was once above you"
            hide amaterasu
    if not warrior_path and not scholar_path:
        menu:
            "Where do you head of next?"
            "I wants to look more into the arts":
                jump art_room
            "I'd like to explore how toi become a better leader":
                jump leadership
    elif not warrior_path and ruler_path :
        menu:
            "Where do you head of next?"
            "I should learn skills for the battlefield":
                jump weapons_room
    elif warrior_path and not ruler_path:
        menu:
            "Where do you head of next?"
            "I wants to look more into the arts":
                jump art_room
    else:
        jump ending 

label ending:
    show bg gardan
    narrator "You exit the hall to the garden in the back, seeing Athena waiting in the center of it all"
    show athena
    a "Did quite the questioning didn't you?"
    menu:
        "Is that not what you asked me to do?":
            narrator "She chuckled slightly"
            a "Quite cocky now. I am glad you went through it as thoroughly as you did."
        "Yes, I quite enjoyed it":
            a "Glad you enoyed yourself. The goddesses also enjoyed your questioning"
    menu:
        "I came for guide of what I shall become":
            a "ah indeed you have"
    if scholar>=2:
        a "By wisdom won and discipline proven, I name you Scholar. Stand tall in the light of knowledge."
        a "In your name there shall be a library built in your name with all the knowledge in every known language"
    elif soldier>=2:
        a "Your blade is steady, and your purpose truer still. I name you Warrior."
        a "When you return home there is an army awaiting your command"
    elif ruler>=2:
        a "Your judgment is clear, your voice unwavering. I name you Leader"
        a "We gift you a kingdom in your name for your excellance of rule to be put to use"
    else:
        a "By valor, by intellect, by the fate written in your blood — rise, Demigod."
        a "You may move between your home with mortals and reside amongts the gods"
return