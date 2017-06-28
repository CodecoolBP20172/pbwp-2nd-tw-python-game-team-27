import sys
import readchar
import pygame
import random
l=0

i=1
j=1
#position = [i, j]
global_score=0
def load_map(filename):
    mi = []
    with open(filename) as map:
        for row in map:
            mi.append(list(row.strip()))
    return mi

def high_score(filename):
    highScore = []
    with open(filename) as hs:
        for num in hs:
            highScore.append(int(num.strip()))
    highScore.sort()
    return highScore

def level(filename):
    levels=[]
    with open (filename) as lvls:
        for level in lvls:
            levels.append(level.strip("\n"))
    return levels

def finish(mapIndex,i,j,l,score,viewDistance):
    if mapIndex[i + 1][j] == "O" or mapIndex[i - 1][j] == "O" or mapIndex[i][j - 1] == "O" or mapIndex[i][j + 1] == "O":
        sys.stdout.write("\033c")
        l = l + 1
        score=score+viewDistance
   
def score_draw(scoree,viewDistanceee,map,pos): #score_draw(score,viewDistance,mapIndex,position):
    scoree=scoree+viewDistanceee
    sys.stdout.write("\033c")
    draw(map,pos,viewDistanceee,scoree)

def player_move(iChange,jChange,map,posIndex,pos,iPos,jPos):
    #global position
    if map[iPos+iChange][jPos+jChange]==" ":
       # position[posIndex]=pos
        iPos=iPos+iChange
        jPos=jPos+jChange
    return iPos,jPos


def landmine(map):
    mines=[]
    for rownum,row in enumerate(map):
        for colnum,col in enumerate(row):
            if col==" ":
                mines.append((rownum,colnum))
    mine=random.choice(mines)
    return mine

def main():
    pause=False
    move_right=True
    lvl=level("levels.txt")
    #print(high_score("hs.txt"))
    sys.stdout.write("\033c")
    l=0
    i=1
    j=1
    viewDistance=1
    score=global_score
    #position=[i,j]
    
    
    while l<=len(lvl)-1:
        
        i = 1
        j = 1
        if l == len(lvl)-1:
            sys.stdout.write("\033c")
            print("Congratulations! You have escaped the maze. Press 'r' to go back to the menu or any other key to quit the game")
            with open("hs.txt","a") as hs :
                hs.write(str(score)+"\n")
                high=high_score("hs.txt")
                if int(score)<high[0]:
                    print("")
                    print("NEW HiGH SCORE")
            while True:
                re = readchar.readchar()
                if re == "r":
                    menu()
                else:
                    sys.exit()
        else:
            mapindex = load_map(lvl[l])
            mine_pos=landmine(mapindex)
            position = [i, j]
            draw(mapindex, position, viewDistance, score)
            while True:
                ch = readchar.readchar()
                if ch == "s" or ch == "S":
                    if mapindex[i + 1][j] == "O":
                        sys.stdout.write("\033c")
                        l = l + 1
                        score = score + viewDistance
                        break
                    if mapindex[i + 1][j] == " ":
                        position[0] = i + 1
                        i = i + 1
                        score = score + viewDistance
                        sys.stdout.write("\033c")
                        draw(mapindex, position, viewDistance, score)
                elif ch == "w" or ch == "W":
                    if mapindex[i - 1][j] == "O":
                        sys.stdout.write("\033c")
                        l = l + 1
                        score = score + viewDistance
                        break
                    if mapindex[i - 1][j] == " ":
                        position[0] = i - 1
                        i = i - 1
                        sys.stdout.write("\033c")
                        score = score + viewDistance
                        draw(mapindex, position, viewDistance, score)
                elif ch == "a" or ch == "A":
                    if mapindex[i][j - 1] == "O":
                        sys.stdout.write("\033c")
                        l = l + 1
                        score = score + viewDistance
                        break
                    if mapindex[i][j - 1] == " ":
                        position[1] = j - 1
                        j = j - 1
                        sys.stdout.write("\033c")
                        score = score + viewDistance
                        draw(mapindex, position, viewDistance, score)
                elif ch == "d" or ch == "D":
                    if mapindex[i][j + 1] == "O":
                        sys.stdout.write("\033c")
                        l = l + 1
                        score = score + viewDistance
                        break
                    if mapindex[i][j + 1] == " ":
                        position[1] = j + 1
                        j = j + 1
                        sys.stdout.write("\033c")
                        score = score + viewDistance
                        draw(mapindex, position, viewDistance, score)
                elif ch == "x" or ch == "X":
                    sys.stdout.write("\033c")        
                    draw(mapindex, position, viewDistance, score)
                    while True:
                        print("Would you like to quit? Y/N  ")
                        ch = input()
                        if ch == "n" or ch == "N":
                            sys.stdout.write("\033c")
                            draw(mapindex, position, viewDistance, score)
                            break
                        elif ch == "Y" or ch == "y":
                            sys.exit()
                elif ch == "j" or ch == "J":
                    if viewDistance > 1:
                        viewDistance = viewDistance - 1
                        sys.stdout.write("\033c")
                        score = score + viewDistance
                        draw(mapindex, position, viewDistance, score)
                elif ch == "k"or ch == "K":
                    if viewDistance <= 3:
                        viewDistance = viewDistance + 1
                        sys.stdout.write("\033c")
                        score=score+viewDistance
                        draw(mapindex,position,viewDistance,score)
                if position[0]==mine_pos[0] and position[1]==mine_pos[1]:
                    print("MINES FOUNDDDD")
                    score=score+200
            
"""def main():
    lvl=level("levels.txt")
    #print(high_score("hs.txt"))
    sys.stdout.write("\033c")
    score=0
    global i ,j
    viewDistance=1

    position=[i,j]
    while l<=len(lvl)-1:
        
        if l == len(lvl)-1:
            sys.stdout.write("\033c")
            print("Congratulations! You have escaped the maze. Press 'r' to go back to the menu or any other key to quit the game")
            with open("hs.txt","a") as hs :
                hs.write(str(score)+"\n")
                high=high_score("hs.txt")
                if int(score)<high[0]:
                    print("")
                    print("NEW HIGH SCORE")
            while True:
                re = readchar.readchar()
                if re == "r":
                    menu()
                else:
                    sys.exit()
        else:
            mapIndex = load_map(lvl[l])        
            draw(mapIndex, position, viewDistance, score)
            print (player_move(1,0,mapIndex,0,i+1,i,j))
            while True:
                ch = readchar.readchar()
                if ch == "s" or ch == "S":
                    print("S")
                    #finish(mapIndex, i, j, l, score, viewDistance)
                    #player_move(1,0,mapIndex,0,i+1,i,j)
                    
                    i=player_move(1,0,mapIndex,0,i+1,i,j)[0]
                    j=player_move(1,0,mapIndex,0,i+1,i,j)[1]
                   # j=player_move(1,0,mapIndex,0,i+1,i,j)[1]
                    print (player_move(1,0,mapIndex,0,i+1,i,j))
                    
                        
                elif ch == "w" or ch == "W":
                    #finish(mapIndex, i, j, l, score, viewDistance)
                    player_move(-1,0,mapIndex,0,i-1,i,j)
                    #i=player_move(-1,0,mapIndex,0,i-1,i,j)[0]
                    #j=player_move(-1,0,mapIndex,0,i-1,i,j)[1]
                    

                elif ch == "a" or ch == "A":
                   # finish(mapIndex, i, j, l, score, viewDistance)
                    player_move(0,-1,mapIndex,1,j-1,i,j)
                   # i=player_move(0,-1,mapIndex,1,j-1,i,j)[0]
                   # j=player_move(0,-1,mapIndex,1,j-1,i,j)[1]
                    
                elif ch == "d" or ch == "D":
                    #finish(mapIndex, i, j, l, score, viewDistance)
                    player_move(0,1,mapIndex,1,j+1,i,j)
                  #  i=player_move(0,1,mapIndex,1,j+1,i,j)[0]
                   # j=player_move(0,1,mapIndex,1,j+1,i,j)[1]
                    
                elif ch == "x" or ch == "X":
                    sys.stdout.write("\033c")
                    draw(mapIndex, position, viewDistance, score)
                    while True:
                        print("Would you like to quit? Y/N  ")
                        ch = readchar.readchar()
                        if ch == "n" or ch == "N":
                            sys.stdout.write("\033c")
                            draw(mapIndex, position, viewDistance, score)
                            break
                        elif ch == "Y" or ch == "y":
                            sys.exit()
                elif ch == "j" or ch == "J":
                    if viewDistance > 1:
                        viewDistance = viewDistance - 1
                elif ch == "k"or ch == "K":
                    if viewDistance <= 3:
                        viewDistance = viewDistance + 1
               # score_draw(score, viewDistance, mapIndex, position)
                score = score + viewDistance
                sys.stdout.write("\033c")
                draw(mapIndex, position, viewDistance, score) - merge sys.stdout here!!
                print(ch)"""

def draw(map,player,range,score):
    print("w,a,s,d = movement \n"
          "j/k = view distance - / + \n"
          "x = exit")
    print("Score : " + str(score) +" View distance : "+str(range))
    print("")
    for rownum,row in enumerate(map):
        for colnum,col in enumerate(row):
           if rownum==player[0] and colnum==player[1]:
                 sys.stdout.write("s")
           elif (rownum <= player[0] + range and rownum >= player[0] - range) and (colnum <= player[1] + range and colnum >= player[1] - range):
               sys.stdout.write(col)

           else:
               sys.stdout.write(" ")

        sys.stdout.write("\n")
        

def menu():
    play_sound('sms-alert-2-daniel_simon.wav')
    sys.stdout.write("\033c")
    print("MENU")
    print("1. New Game")
    print("2. High Score")
    print("3. Help")
    print("4. Exit")
    while True:
        ch=readchar.readchar()
        if ch=="1":
            main()
            break
        elif ch=="2":
            sys.stdout.write("\033c")
            hs=high_score("hs.txt")
            i=len(hs)
            print("High score ranking: ")
            print("First : "+str(hs[0]))
            print("Second : " + str(hs[1]))
            print("Third : " + str(hs[2]))
            print("Press 'x' to go back to the menu!")
            while True:
                back=readchar.readchar()
                if back =="x" or back=="X":
                    menu()
        elif ch=="4":
            sys.exit()
        elif ch=="3":
            sys.stdout.write("\033c")
            print("Reach 'O' to escape the maze. \n"
                  "You can inscrease or decrease your view distance with 'j' and 'k'.\n"
                  "Score is increased at every step by the value of your view distance.\n"
                  "The lower is your score,the higher you can get in the ladder.\n"
                  "Move the character using 'w' 'a' 's' 'd' or press 'x' to exit.\n")
            print("Press 'x' to go back to the menu!")
            while True:
                back = readchar.readchar()
                if back == "x" or back=="X":
                    menu()

def play_sound(filename):
    pygame.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

menu()
