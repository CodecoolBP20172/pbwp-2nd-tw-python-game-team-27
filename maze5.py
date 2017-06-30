import sys
import readchar
import pygame
import random
import time
moves = ""

def load_map(filename):
    mi = []
    with open(filename) as map:
        for row in map:
            mi.append(list(row.strip()))
    return mi

def high_score(filename):
    list_highscore = []
    with open(filename) as hs:
        for num in hs:
            list_highscore.append(int(num.strip()))
    list_highscore.sort()
    return list_highscore


def level(filename):
    levels = []
    with open(filename) as lvls:
        for level in lvls:
            levels.append(level.strip("\n"))
    return levels


def player_move(i_change, j_change, map_i, position_i, position_j, score, view_dist, map_level):
    if map_i[position_i + i_change][position_j + j_change] == " ":
        position_i = position_i + i_change
        position_j = position_j + j_change
        score = score + view_dist
    if map_i[position_i + i_change][position_j + j_change] == "O":
        map_level = map_level + 1
        score = score + view_dist
    return position_i, position_j, score, map_level


def landmine(map, level):
    mines = []
    for rownum, row in enumerate(map):
        for colnum, col in enumerate(row):
            if col == " ":
                mines.append((rownum, colnum))
    random.shuffle(mines)
    if level < 1:
        number_of_mines = 1
    if level == 1:
        number_of_mines = 3
    mine = mines[0:number_of_mines]
    return mine


def main():
    lvl = level("levels.txt")
    sys.stdout.write("\033c")
    score = 0
    l = 0
    view_distance = 1
    cheat = False
    while l <= len(lvl) - 1:
        if l == len(lvl) - 1:
            sys.stdout.write("\033c")
            play_sound("completed.wav")
            print("Congratulations! You have escaped the maze. \n"
            "Press 'r' to go back to the menu or any other key to quit the game\n")
            if cheat == False:
                with open("hs.txt", "a") as hs:
                    hs.write(str(score) + "\n")
                    high = high_score("hs.txt")
                    if int(score) < high[0]:
                        print("")
                        print("NEW HIGH SCORE")
            else:
                print(
                    "You have used cheats...shame on You...this won't be added to the highscores")
            while True:
                re = readchar.readchar()
                if re == "r":
                    menu()
                else:
                    sys.exit()

        else:
            moves = ""
            map_index = load_map(lvl[l])
            mine_pos = landmine(map_index, l)
            i = 1
            j = 1
            next_map = l
            position = [i, j]
            while next_map == l:
                next_map = l
                map_index = load_map(lvl[l])
                draw(map_index, position, view_distance, score)
                if cheat==True:
                    print(mine_pos)
                ch = readchar.readchar().lower()
                moves += ch

                if ch == "s":
                    i, j, score, l = player_move(1, 0, map_index,  i, j, score, view_distance, l)
                elif ch == "w":
                    i, j, score, l = player_move(-1, 0, map_index, i, j, score, view_distance, l)
                elif ch == "a" :
                    i,j,score,l=player_move(0,-1,map_index,i,j,score,view_distance,l)
                elif ch == "d" :
                    i,j,score,l=player_move(0,1,map_index,i,j,score,view_distance,l)
                elif ch == "x" :
                    while True:
                        print("Would you like to quit? Y/N  ")
                        ch = readchar.readchar().lower()
                        if ch == "n" :
                            break
                        elif ch == "y" :
                            sys.exit()

                elif ch == "j":
                    if view_distance > 1:
                        if view_distance>5:
                            pass
                        else:
                            view_distance = view_distance - 1
                            score=score+view_distance
                elif ch == "k":
                    if view_distance <= 3:
                        view_distance = view_distance + 1
                        score=score+view_distance

                if tuple(position) in mine_pos:
                    print("You just stepped on a landmine. \n That's +50 score point. \n Avoid stepping here again !")
                    play_sound("landmine.wav")
                    score=score+50  
                    time.sleep(2) 
                if cheat_check(moves) ==True:
                    play_sound("cheat.wav")
                    print("Cheat activated. Have fun !")
                    view_distance=10
                    score=0
                    cheat=True
                position=[i,j]
                draw(map_index, position, view_distance, score)
                    
                
def cheat_check(latest_moves):
    cheats=["codecool","lol","kzrg45"]
    for cheat in cheats:
        try:
            if latest_moves[-(len(cheat)):]==cheat:
                time.sleep(1)
                return True
        except IndexError:
            continue

def draw(map,player,range,score):
    sys.stdout.write("\033c")
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
    sys.stdout.write("\033c")
    print("MENU")
    print("1. New Game")
    print("2. High Score")
    print("3. Help")
    print("4. Exit")
    while True:
        ch=readchar.readchar()
        if ch=="1":
            play_sound("meow.wav")
            main()
            break
        elif ch=="2":
            sys.stdout.write("\033c")
            hs=high_score("hs.txt")
            play_sound("meow.wav")
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
            play_sound("meow.wav")
            sys.exit()
        elif ch=="3":
            sys.stdout.write("\033c")
            play_sound("meow.wav")
            print("Reach 'O' to escape the maze. \n"
                  "You can inscrease or decrease your view distance with 'j' and 'k'.\n"
                  "Score is increased at every step by the value of your view distance.\n"
                  "The lower is your score,the higher you can get in the ladder.\n"
                  "Move the character using 'w' 'a' 's' 'd' or press 'x' to exit.\n")
            print("\n Update :\n-Player's now encounter landmines in the labyrinth(at random locations in each game/map). Stepping on a landmine increases our score by 50. \n"
                  "-Added amazing sound effects.. \n"
                  "-Cheats are now avaible. Use them on your own risk. \n"
                  "-Improved performance (clean code) \n ")
            print("Press 'x' to go back to the menu!")
            while True:
                back = readchar.readchar().lower()
                if back == "x" :
                    menu()
                    play_sound("meow.wav")

def play_sound(filename):
    pygame.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

menu()
