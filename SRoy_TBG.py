class Game:
    def __init__(self):
        self.board = [0,1,2,3,4,5,6,7,8]
        self.g = input("Would you like to play noughts and crosses(enter n), hangman(enter h) or an adventure game(a)")
        if self.g == "n":
            self.show_board()
            self.x = True
            self.counter = 1
            while self.x:

                
                while self.counter%2 == 1:
                    turn = int(input("Which box would you like to put your mark in?"))
                    if self.board[turn]!="x" and self.board[turn]!="o":                        
                        self.board[turn] = "x"
                        self.show_board()
                        self.counter+=1
                        
                    if self.board[0]=="x" and self.board[1] == "x" and self.board[2] == "x":
                        self.x = False
                        print("x has won")
                        exit()
                        
                    if self.board[3] == "x" and self.board[4] == "x" and self.board[5] == "x":
                        self.x = False
                        print("x has won")
                        exit()
                    if self.board[6]=="x" and self.board[7]=="x" and self.board[8] == "x":
                        self.x = False
                        print("x has won")
                        exit()
                    if self.board[0]=="o" and self.board[1]=="o" and self.board[2] == "o":
                        self.x = False
                        print("o has won")
                        exit()
                    if self.board[3]=="o" and self.board[4]=="o" and self.board[5] == "o":
                        self.x = False
                        print("o has won")
                        exit()
                    if self.board[6]=="o" and self.board[7]=="o" and self.board[8] == "o":
                        self.x = False
                        print("o has won")
                        exit()
                    if self.board[0]=="x" and self.board[4]=="x" and self.board[8] == "x":
                        self.x = False
                        print("x has won")
                        exit()
                    if self.board[2]=="x" and self.board[4]=="x" and self.board[6] == "x":
                        self.x = False
                        print("x has won")
                        exit()
                    if self.board[0]=="o" and self.board[4]=="o" and self.board[8] == "o":
                        self.x = False
                        print("o has won")
                        exit()
                    if self.board[2]=="o" and self.board[4]=="o" and self.board[6] == "o":
                        self.x = False
                        print("o has won")
                        exit()
                    if self.board[0]=="x" and self.board[3]=="x" and self.board[6] == "x":
                        self.x = False
                        print("x has won")
                        exit()
                    if self.board[1]=="x" and self.board[4]=='x' and self.board[7] == "x":
                        self.x = False
                        print("x has won")
                        exit()
                    if self.board[2]=="x" and self.board[5]=="x" and self.board[8] == "x":
                        self.x = False
                        print("x has won")
                        exit()
                    if self.board[0]=="o" and self.board[3]=="o" and self.board[6] == "o":
                        self.x = False
                        print("o has won")
                        exit()
                    if self.board[1]=="o" and self.board[4]=="o" and self.board[7] == "o":
                        self.x = False
                        print("o has won")
                        exit()
                
                    if self.board[2]=="o" and self.board[5]=="o" and self.board[8] == "o":
                        self.x = False
                        print("o has won")
                        exit()
          
                    
            
    
                    
                while self.counter%2 == 0:
                    turn = int(input("Which box would you like to put your mark in?"))
                    if self.board[turn]!="x" and self.board[turn]!="o":                        
                        self.board[turn] = "o"
                        self.show_board()
                        
                    if self.board[0]=="x" and self.board[1] == "x" and self.board[2] == "x":
                        self.x = False
                        print("x has won")
                        exit()
                    if self.board[3] == "x" and self.board[4] == "x" and self.board[5] == "x":
                        self.x = False
                        print("x has won")
                        self.kill()
                        exit()
                    if self.board[6]=="x" and self.board[7]=="x" and self.board[8] == "x":
                        self.x = False
                        print("x has won")
                        exit()
                    if self.board[0]=="o" and self.board[1]=="o" and self.board[2] == "o":
                        self.x = False
                        print("o has won")
                        exit()
                    if self.board[3]=="o" and self.board[4]=="o" and self.board[5] == "o":
                        self.x = False
                        print("o has won")
                        exit()
                    if self.board[6]=="o" and self.board[7]=="o" and self.board[8] == "o":
                        self.x = False
                        print("o has won")
                        exit()
                    if self.board[0]=="x" and self.board[4]=="x" and self.board[8] == "x":
                        self.x = False
                        print("x has won")
                        exit()
                    if self.board[2]=="x" and self.board[4]=="x" and self.board[6] == "x":
                        self.x = False
                        print("x has won")
                        exit()
                    if self.board[0]=="o" and self.board[4]=="o" and self.board[8] == "o":
                        self.x = False
                        print("o has won")
                        exit()
                    if self.board[2]=="o" and self.board[4]=="o" and self.board[6] == "o":
                        self.x = False
                        print("o has won")
                        exit()
                    if self.board[0]=="x" and self.board[3]=="x" and self.board[6] == "x":
                        self.x = False
                        print("x has won")
                        exit()
                    if self.board[1]=="x" and self.board[4]=='x' and self.board[7] == "x":
                        self.x = False
                        print("x has won")
                        exit()
                    if self.board[2]=="x" and self.board[5]=="x" and self.board[8] == "x":
                        self.x = False
                        print("x has won")
                        exit()
                    if self.board[0]=="o" and self.board[3]=="o" and self.board[6] == "o":
                        self.x = False
                        print("o has won")
                        exit()
                    if self.board[1]=="o" and self.board[4]=="o" and self.board[7] == "o":
                        self.x = False
                        print("o has won")
                        exit()
                    if self.board[2]=="o" and self.board[5]=="o" and self.board[8] == "o":
                        self.x = False
                        print("o has won")
                        exit()
                    self.counter+=1
        elif self.g == "h":
            
            self.word = input("What word are we playing with?(ask a friend) ")
            print("""


















































                   """)
            self.word_base = list("_"*len(self.word))
            print(self.word_base)
            self.deaths = 0
            self.goverdeaths = 9
            
            self.answer = list(self.word)

            
            while self.deaths<self.goverdeaths:
                self.guessed_letter = input("What letter are you guessing? ")
                if self.guessed_letter in self.answer:
                    self.index = 0
                    for letter in self.answer:
                        
                        if letter == self.guessed_letter:
                            self.showstring = ""
                            self.word_base[self.index] = self.answer[self.index]
                            for i in self.word_base:
                                
                                self.showstring= self.showstring+i
                        self.index+=1

                    print(self.showstring)
                    self.want_to_guess = input("Would you like to guess the word?(press y to guess or press any key and then ENTER to not guess)")
                    if self.want_to_guess.lower() == "y":
                        self.guessed_word = input("What's your guess?")
                        if self.guessed_word == self.word:
                            print("congrats, you won!")
                            exit()
                        else:
                            print("Sorry, that was wrong!")
                            self.deaths+=1
                            if self.deaths == 1:
                                self.oned()
                            elif self.deaths == 2:
                                self.twod()
                            elif self.deaths == 3:
                                self.threed()
                            elif self.deaths == 4:
                                self.fourd()
                            elif self.deaths == 5:
                                self.fived()
                            elif self.deaths == 6:
                                self.sixd()
                            elif self.deaths == 7:
                                self.sevend()
                            elif self.deaths == 8:
                                self.eightd()
                            elif self.deaths == 9:
                                self.nined()
                                print("Sorry, you lost the game):")
                                exit()
                    
            
                elif self.guessed_letter not in self.answer:
                    print("Sorry, that is not in the word!")
                    self.deaths+=1
                    if self.deaths == 1:
                        self.oned()
                    elif self.deaths == 2:
                        self.twod()
                    elif self.deaths == 3:
                        self.threed()
                    elif self.deaths == 4:
                        self.fourd()
                    elif self.deaths == 5:  
                        self.fived()
                    elif self.deaths == 6:
                        self.sixd()
                    elif self.deaths == 7:
                        self.sevend()
                    elif self.deaths == 8:
                        self.eightd()
                    elif self.deaths == 9:
                        self.nined()
                        print("Sorry, you lost the game):")
        elif self.g == "a":
            self.printtitle()
            print("""You have a task to intercept and retrieve a very important piece of mail which has the nuclear launch codes to destroy your country""")
            self.c1 = int(input("You are just outside the main military fort. You have four other men with you. Will you take 2 with you and leave 2 behind to guard your squad and give warnings(1) or will you take all of them(2)?"))
            if self.c1 == 1:
                self.printfort()
                self.c2 = int(input("Will you enter via the main gate(1) or enter via the plumbing system(2)?"))
                if self.c2 == 1:
                    self.c3  = int(input("You are now inside the military fort, you hear three enemies walking towards you. Will you hide in the cupboard(1) or wait for the enemy to come closer and then melee him(2)?"))
                    if self.c3 == 1:
                        self.printgunshot()
                        self.printcloud()
                        print("A spider in the cupboard crawled on your face and you went bonkers. Your position was discovered")
                    elif self.c3 == 2:
                        print("Good decision, you have knocked out the enemies and have taken their uniforms.")
                        self.c4 = int(input("You only have 15 mins until the enemy launch a nuclear attack, will you scan the area for enemy troops(1) or proceed upstairs to the nuclear command centre(2)"))
                        if self.c4 == 1:
                            self.printcommandc()
                            print("You have knocked out most of the enemies in the area.")
                            self.c5 = int(input("Will you call in your guards from outside(1) or continue with only 2 men(2)?"))
                            if self.c5 == 1:
                                self.printgunshot()
                                print("You shoot all the 5 men in the command centre. The launch codes are somewhere in the room, you have to find them and seize them.")
                                self.c7 = int(input("You think they might be hidden in a safe. Will you try and guess the 4 digit combination(1) or use explosives to open the safe(2)."))
                                if self.c7 == 1:
                                    self.printgunshot()
                                    self.printcloud()
                                    print("Enemy found you and shot you.")
                                    exit()
                                elif self.c7 == 2:
                                    self.c9 = int(input("You have the codes but the explosion set off an alarm. You can either exit via the window(1) or stay, lay explosives and then leave(2)"))
                                    if self.c9 == 1:
                                        self.printtitle()
                                        print("Well done, you have saved your country")
                                        exit()
                                    elif self.c9 == 2:
                                        self.printcloud()
                                        print("So close to saving your country but still so far. You have lost the game!")
                                        exit()
                                    
                            elif self.c5 == 2:
                                self.printgunshot()
                                self.printcloud()
                                print("You enter the nuclear command room and there are 5 men, they outnumber and kill you")
                                exit()
                        elif self.c4 == 2:
                            print("An enemy spotted you going up the stair case. They ask for your id card since they don't recognise you")
                            self.c6 = int(input("Will you shoot him(1) or knock him out(2)?"))
                            if self.c6 == 1:
                                self.printcloud()
                                print("Bad idea")
                                exit()
                            elif self.c6 == 2:
                                print("Good Idea.")
                                self.c8 = int(input("Will you hide the body in the cupboard(1) or in the bathroom(2)"))
                                if self.c8 == 1:
                                    print("Good Idea")
                                    self.c10 = int(input("Will you call in your guards from outside(1) or continue with only 2 men(2)?"))
                                    if self.c10 == 1:
                                        self.printcommandc()
                                        self.printgunshot()
                                        print("You shoot all 5 men in the command centre. The launch codes are in the room you find must find them and seize them")
                                        self.c11 = int(input("You think they might be in a safe, will you try and guess the 4 digit combination(1) or use exposives(2)."))
                                        if self.c11 == 1:
                                            self.printgunshot()
                                            self.printcloud()
                                            print("You took too long and an enemy found you, you and your men are now dead.")
                                        elif self.c11 == 2:
                                            self.printexplosives()
                                            self.c70 = int(input("You have the codes but is has sent off an alarm. Will you leave via the window(1) or stay and lay down explosives(2)?"))
    
                                            if self.c70 == 1:
                                                self.printtitle()
                                                print("Well Done, you've saved your country")
                                                exit()
                                            elif self.c70 == 2:
                                                self.printcloud()
                                                print("So lose but so far, your country is flattened")
                                                exit()
                                    elif self.c10 == 2:
                                        self.printgunshot()
                                        self.printcloud()
                                        print("You enter the nuclear command room and there are 5 men, they outnumber and kill you")
                                        exit()
                                    elif self.c8 == 2:
                                        print("Someone was in the bathroom and they have shot you")
                                        exit()
                        
                elif self.c2 == 2:
                    self.printtetanus()
                    self.printcloud()
                    print("Unfortunately, you and your crew of 2 others cut your hands and get tetanus, you immediately die")
            elif self.c1 == 2:
                self.printgunshot()
                self.printcloud()
                print("An enemy soldier walked behind you, shot you in the head and your country has disappeared")
                exit()
    def show_board(self):
        print(self.board[0],"|",self.board[1],"|",self.board[2])
        print("________")
        print(self.board[3],"|",self.board[4],"|",self.board[5])
        print("________")
        print(self.board[6],"|",self.board[7],"|",self.board[8])
    def oned(self):
        print("_____")
    def twod(self):
        print("     |")
        print("     |")
        print("     |")
        print("     |")
        print("     |")
        print("     |")
        print("     |")
        print("     |")
        print("     |")
        print("_____")
    def threed(self):
        print("_____")
        print("     |")
        print("     |")
        print("     |")
        print("     |")
        print("     |")
        print("     |")
        print("     |")
        print("     |")
        print("     |")
        print("_____")
    def fourd(self):
        print(" _____")
        print("|    |")
        print("|    |")
        print("|    |")
        print("     |")
        print("     |")
        print("     |")
        print("     |")
        print("     |")
        print("     |")
        print("_____")
    def fived(self):
        print(" _____")
        print("|    |")
        print("|    |")
        print("|    |")
        print("()   |")
        print("     |")
        print("     |")
        print("     |")
        print("     |")
        print("     |")
        print("_____")
    def sixd(self):
        print(" _____")
        print("|    |")
        print("|    |")
        print("|    |")
        print("()   |")
        print("\    |")
        print("     |")
        print("     |")
        print("     |")
        print("     |")
        print("_____")
    def sevend(self):
        print(" _____")
        print("|    |")
        print("|    |")
        print("|    |")
        print("()   |")
        print("\/   |")
        print("     |")
        print("     |")
        print("     |")
        print("     |")
        print("_____")
    def eightd(self):
        print(" _____")
        print("|    |")
        print("|    |")
        print("|    |")
        print("()   |")
        print("\/   |")
        print("|    |")
        print("     |")
        print("     |")
        print("     |")
        print("_____")
    def nined(self):
        print(" _____")
        print("|    |")
        print("|    |")
        print("|    |")
        print("()   |")
        print("\/   |")
        print("||   |")
        print("     |")
        print("     |")
        print("     |")
        print("_____")
        
    def __del__(self):
        print("Game Over")
    def printcloud(self):
        print("""   ________________
                          ____/ (  (    )   )  \___
                         /( (  (  )   _    ))  )   )\
                       ((     (   )(    )  )   (   )  )
                     ((/  ( _(   )   (   _) ) (  () )  )
                    ( (  ( (_)   ((    (   )  .((_ ) .  )_
                   ( (  )    (      (  )    )   ) . ) (   )
                  (  (   (  (   ) (  _  ( _) ).  ) . ) ) ( )
                  ( (  (   ) (  )   (  ))     ) _)(   )  )  )
                 ( (  ( \ ) (    (_  ( ) ( )  )   ) )  )) ( )
                  (  (   (  (   (_ ( ) ( _    )  ) (  )  )   )
                 ( (  ( (  (  )     (_  )  ) )  _)   ) _( ( )
                  ((  (   )(    (     _    )   _) _(_ (  (_ )
                   (_((__(_(__(( ( ( |  ) ) ) )_))__))_)___)
                   ((__)        \\||lll|l||///          \_))
                            (   /(/ (  )  ) )\   )
                          (    ( ( ( | | ) ) )\   )
                           (   /(| / ( )) ) ) )) )
                         (     ( ((((_(|)_)))))     )
                          (      ||\(|(|)|/||     )
                        (        |(||(||)||||        )
                          (     //|/l|||)|\\ \     )
                        (/ / //  /|//||||\\  \ \  \ _)
-------------------------------------------------------------------------------""")
    def printtitle(self):
        print("""  _________                    _____.___.                     _________                      __                 
 /   _____/____ ___  __ ____   \__  |   | ____  __ _________  \_   ___ \  ____  __ __  _____/  |________ ___.__.
 \_____  \\__  \\  \/ // __ \   /   |   |/  _ \|  |  \_  __ \ /    \  \/ /  _ \|  |  \/    \   __\_  __ <   |  |
 /        \/ __ \\   /\  ___/   \____   (  <_> )  |  /|  | \/ \     \___(  <_> )  |  /   |  \  |  |  | \/\___  |
/_______  (____  /\_/  \___  >  / ______|\____/|____/ |__|     \______  /\____/|____/|___|  /__|  |__|   / ____|
        \/     \/          \/   \/                                    \/                  \/             \/ """)
    def printcommandc(self):
        print("""__ _____ ____ _____ ______ _______ _____ ______ ______ ______ ___
__]_____]____]_____]______]_______]_____]______]______]______]___]
             _                       _______  |||"||;;|.||##||=|||
  _                           _     |   *  3| |||-|| =|-||==||+|||
  ____________       _              |       | |||_||__|_||__||_|||
|`.   --__     `.        _______    |       | ||================||
|  `._____________`.  .'|.-----.|   _ ======| ||| | -|&|^^|!!|-|||
|   | .-----------.| |  ||     ||  (o))   _ | ||| |**|=|+-|##|=|||
|   | |  .-------.|| |  ||     ||  /||   / \`._|  .-.|_|__|__|_|||
|   | |  |       |||_`..|'_____'| //||___\_/.'\| (( ))==========||
|   | |`.|  ==== ||| | `---------(o)||         \  /-'-=|+|.-|-'|||
|`. | |`.|_______|||/|______________||__.--._ (o)/|=|;:|-|&&|&&|||
|  `|_|===========||_|                 (____)-.'(o)_|__|_|__|__|||
|   | |  .-------.||                           `._\=============||
|   | |  |       |||                             `.     |       ||
|   | |`.|  ==== |||`._____________________________`.  o|o      ||
|`. | |`.|_______||| |._.----------------.__.-------.|__|_______||
|  `|_|===========|| || '----------------'  | .---. ||  __
|   | |  .-------.|| ||               |     |_______||.'\.'.
|   | |  |       ||| || ______________|     | .---. ||'.__.'
|   | |`.|  ==== ||| ||                `.   |_______|||  _ |
 `. | |`.|_______||| ||                  `. | .---. |||_  ||
   `|_|========LGB||`||                    `|_______|||____|
                       `.                    `.
                         `.____________________`.
""")
    def printfort(self):
        print("""                         o
                            .-'"|
                            |-'"|
                                |   _.-'`.
                               _|-"'_.-'|.`.
                              |:^.-'_.-'`.;.`.
                              | `.'.   ,-'_.-'|
                              |   + '-'.-'   J
           __.            .d88|    `.-'      |
      _.--'_..`.    .d88888888|     |       J'b.
   +:" ,--'_.|`.`.d88888888888|-.   |    _-.|888b.
   | \ \-'_.--'_.-+888888888+'  _>F F +:'   `88888bo.
    L \ +'_.--'   |88888+"'  _.' J J J  `.    +8888888b.
    |  `+'        |8+"'  _.-'    | | |    +    `+8888888._-'.
  .d8L  L         J  _.-'        | | |     `.    `+888+^'.-|.`.
 d888|  |         J-'            F F F       `.  _.-"_.-'_.+.`.`.
d88888L  L     _.  L            J J J          `|. +'_.-'    `_+ `;
888888J  |  +-'  \ L         _.-+.|.+.          F `.`.     .-'_.-"J
8888888|  L L\    \|     _.-'     '   `.       J    `.`.,-'.-"    |
8888888PL | | \    `._.-'               `.     |      `..-"      J.b
8888888 |  L L `.    \     _.-+.          `.   L+`.     |        F88b
8888888  L | |   \   _..--'_.-|.`.          >-'    `., J        |8888b
8888888  |  L L   +:" _.--'_.-'.`.`.    _.-'     .-' | |       JY88888b
8888888   L | |   J \ \_.-'     `.`.`.-'     _.-'   J J        F Y88888b
Y888888    \ L L   L \ `.      _.-'_.-+  _.-'       | |       |   Y88888b
`888888b    \| |   |  `. \ _.-'_.-'   |-'          J J       J     Y88888b
 Y888888     +'\   J    \ '_.-'       F    ,-T"\   | |    .-'      )888888
  Y88888b.      \   L    +'          J    /  | J  J J  .-'        .d888888
   Y888888b      \  |    |           |    F  '.|.-'+|-'         .d88888888
    Y888888b      \ J    |           F   J    -.              .od88888888P
     Y888888b      \ L   |          J    | .' ` \d8888888888888888888888P
      Y888888b      \|   |          |  .-'`.  `\ `.88888888888888888888P
       Y888888b.     J   |          F-'     \\ ` \ \88888888888888888P'
        Y8888888b     L  |         J       d8`.`\  \`.8888888888888P'
         Y8888888b    |  |        .+      d8888\  ` .'  `Y888888P'
         `88888888b   J  |     .-'     .od888888\.-'
          Y88888888b   \ |  .-'     d888888888P'
          `888888888b   \|-'       d888888888P
           `Y88888888b            d8888888P'
             Y88888888bo.      .od88888888   hs
             `8888888888888888888888888888
              Y88888888888888888888888888P
               `Y8888888888888888888888P'
                 `Y8888888888888P'
                      `Y88888P'""")
    def printgunshot(self):
        print("""      ^
         | |
       @#####@
     (###   ###)-.
   .(###     ###) \
  /  (###   ###)   )
 (=-  .@#####@|_--"
 /\    \_|l|_/ (\
(=-\     |l|    /
 \  \.___|l|___/
 /\      |_|   /
(=-\._________/\
 \             /
   \._________/
     #  ----  #
     #   __   #
     \########/
                                           """)
	
    def printexplosives(self):
        print(""" 
     ______________________________    . \  | / .
     /                            / \     \ \ / /
    |                            | ==========  - -
     \____________________________\_/     / / \ \
  ______________________________      \  | / | \
 /                            / \     \ \ / /.   .
|                            | ==========  - -
 \____________________________\_/     / / \ \    /
      ______________________________   / |\  | /  .
     /                            / \     \ \ / /
    |                            | ==========  -  - -
     \____________________________\_/     / / \ \
                                        .  / | \  .""")
		
    def printtetanus(self):
        print("""           __    _                                   
                    _wr""        "-q__                             
                 _dP                 9m_     
               _#P                     9#_                         
              d#@                       9#m                        
             d##                         ###                       
            J###                         ###L                      
            {###K                       J###K                      
            ]####K      ___aaa___      J####F                      
        __gmM######_  w#P""   ""9#m  _d#####Mmw__                  
     _g##############mZ_         __g##############m_               
   _d####M@PPPP@@M#######Mmp gm#########@@PPP9@M####m_             
  a###""          ,Z"#####@" '######"\g          ""M##m            
 J#@"             0L  "*##     ##@"  J#              *#K           
 #"               `#    "_gmwgm_~    dF               `#_          
7F                 "#_   ]#####F   _dK                 JE          
]                    *m__ ##### __g@"                   F          
                       "PJ#####LP"                                 
 `                       0######_                      '           
                       _0########_                                   
     .               _d#####^#####m__              ,              
      "*w_________am#####P"   ~9#####mw_________w*"                  
          ""9@#####@M""           ""P@#####@M""                    
""")
		
    
    
ng = Game()
            
