print('''                   .-==========
                         .-' O    =====
                        /___       ===
                           \_      |
_____________________________)    (_____________________________
\___________               .'      `,              ____________/
  \__________`.     |||<   `.      .'   >|||     .'__________/
     \_________`._  |||  <   `-..-'   >  |||  _.'_________/
        \_________`-..|_  _ <      > _  _|..-'_________/
           \_________   |_|  //  \\  |_|   _________/
                      .-\   //    \\   /-.
      ,  .         _.'.- `._        _.' -.`._         .  ,
    <<<<>>>>     .' .'  /  '``----''`  \  `. `.     <<<<>>>>
      '/\`         /  .' .'.'/|..|\`.`. `.  \         '/\`
      (())        `  /  / .'| |||| |`. \  \  '        (())
       /\          ::_.' .' /| || |\ `. `._::          /\
      //\\           '``.' | | || | | `.''`           //\\
      //\\             .` .` | || | '. '.             //\\
      //\\                `  | `' |  '                //\\
      \\//                                            \\//
       \/                                             \/''')


print("Welcome to treasure Island.")
print("Your mission is to find the treasure.")

first_junction = input("You're ar a cross road. Where do you want to go? Type 'left' or 'right' : ")
if first_junction == "left":
    second_junction = input("You come to a lake. there is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across. : ")
    if second_junction == "wait":
        third_juction = input("You arrive at island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you chooose? :")
        if third_juction == "yellow":
            print("You win")
        elif third_juction == "blue":
            print("You enter a room of beasts. Game over")
        else:
            print("You enter a room of vapire. Game over")
    else:
        print(" game over killed by the sharks")
else:
    print("Game over")