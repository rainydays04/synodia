# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Athena")
define ar = Character("Artemis")
define s = Character("Saraswati")
image Athena = im.Scale("athena.png",1000,1000)
image artemis = im.Scale("artemis.png",1000,1000)
image kannon = im.Scale("kannon.png",1000,1000)
image saraswati = im.Scale("saraswati.png",1000,1000)
image bg stair = im.Scale("staircase.png",1920,1080)
image bg weapons = im.Scale("weapons.png",1920,1080)



label start:


  
    show bg stair

    narrator "After weeks of travel, you finally make it to the steps of the ancient temple"
    narrator "The temple that is said to have several vessels of knowledge for who you want to become"
    narrator "But {w}what do you want to become?"
    narrator "Before you comeplete your though, a tall woman approaches you, (other important decriptors for athena)"
    show Athena
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
    show bg weapons
label weapons_room:
    show bg weapons
    show artemis
    show kannon
label leadership:
    show bg weapons
