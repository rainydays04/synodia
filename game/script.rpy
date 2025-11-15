# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Athena")
image Athena = im.Scale("athena.png",1000,1000)
image bg stair = im.Scale("staircase.png",1920,1080)

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

  
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
    show bg stair
label weapons_room:
    show bg stair
    show artemis
label leadership:
    show bg stair
