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

    a "welcome"

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.



    # These display lines of dialogue.



    # This ends the game.

    return
