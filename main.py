#git add .
#git commit -m ""
#git push origin main


#with open('file_name.txt') as reader:
    # Further file processing goes here




from asyncio import FIRST_COMPLETED
import random
import time

menu=str("in")
fn_menu=str("in")
global p_1_score
p_1_score=0
#game_menu_choice=str("")

#from here to next # is string variables for each team
Team_1_main=str("Team 1 UK: Steve, John, Dave, Barry, Stuart, Katy")
Team_1_Steve=str("Steve - ATK:4 DEF:5")
Team_1_John=str("John - ATK:7 DEF:1")
Team_1_Dave=str("Dave - ATK:5 DEF:3")
Team_1_Barry=str("Barry - ATK:8 DEF:2")
Team_1_Stuart=str("Stuart - ATK:6 DEF:4")
Team_1_Katy_GK=str("Katy GK - ATK:2 DEF:6")
Team_1_Steve_ATK=int(4)
Team_1_John_ATK=int(7)
Team_1_Dave_ATK=int(5)
Team_1_Barry_ATK=int(8)
Team_1_Stuart_ATK=int(6)
Team_1_Katy_ATK=int(2)
Team_1_Steve_DEF=int(5)
Team_1_John_DEF=int(1)
Team_1_Dave_DEF=int(3)
Team_1_Barry_DEF=int(2)
Team_1_Stuart_DEF=int(4)
Team_1_Katy_DEF=int(6)




Team_2_main=str("Team 2 Spain: Mateo, Sofia, Isabella, Hugo, Lucas, Matias")
Team_2_Mateo=str("Mateo - ATK:5 DEF:2")
Team_2_Sofia=str("Sofia - ATK:6 DEF:3")
Team_2_Isabella=str("Isabella - ATK:3 DEF:3")
Team_2_Hugo=str("Hugo - ATK:7 DEF:2")
Team_2_Lucas=str("Lucas - ATK:8 DEF:4")
Team_2_Matias_GK=str("Matias GK - ATK:3 DEF:6")


Team_3_main=str("Team 3 Canada: Jakson, Noah, Benjamin, Emma, Amelia, Chloe")
Team_3_Jakson=str("Jakson - ATK:4 DEF:3")
Team_3_Noah=str("Noah - ATK:5 DEF:3")
Team_3_Benjamin=str("Benjamin - ATK:7 DEF:4")
Team_3_Emma=str("Emma - ATK:6 DEF:5")
Team_3_Amelia=str("Amelia - ATK:7 DEF:2")
Team_3_Chloe_GK=str("Chloe GK - ATK:2 DEF:7")


Team_4_main=str("Team 4 Russia: Adrik, Aleksi, Borya, Dimitri, Vladimir, Evgenii")
Team_4_Adrik=str("Adrik - ATK:4 DEF:4")
Team_4_Aleksi=str("Aleksi - ATK:6 DEF:3")
Team_4_Borya=str("Borya - ATK:8 DEF:2")
Team_4_Dimitri=str("Dimitri - ATK:7 DEF:5")
Team_4_Vladimir=str("Vladimir - ATK:6 DEF:6")
Team_4_Evgenii_GK=str("Evgenii GK - ATK:3 DEF:7")


Team_5_main=str("Team 5 France: Abella, Alice, Ailie, Barrie, Caitlin, Farand")
Team_5_Abella=str("Abella - ATK:4 DEF:2")
Team_5_Alice=str("Alice - ATK:5 DEF:1")
Team_5_Ailie=str("Ailie - ATK:7 DEF:4")
Team_5_Barrie=str("Barrie - ATK:6 DEF:3")
Team_5_Caitlin=str("Caitlin - ATK:4 DEF:2")
Team_5_Farand_GK=str("Farand - ATK:1 DEF:5")


Team_6_main=str("Team 6 Italy: Alberto, Beatrice, Calynda, Dani, Elena, Fabian")
Team_6_Alberto=str("Alberto - ATK:4 DEF:3")
Team_6_Beatrice=str("Beatrice - ATK:5 DEF:3")
Team_6_Calynda=str("Calynda - ATK:5 DEF:2")
Team_6_Dani=str("Dani - ATK:6 DEF:1")
Team_6_Elena=str("Elena - ATK:8 DEF:3")
Team_6_Fabian_GK=str("Fabian GK - ATK:2 DEF:6")


Team_7_main=str("Team 7 India: Aja, Akhil, Bhavya, Anusha, Arlet, Chanda")
Team_7_Aja=str("Aja - ATK:5 DEF:2")
Team_7_Akhil=str("Akhil - ATK:4 DEF:3")
Team_7_Bhavya=str("Bhavya - ATK:7 DEF:3")
Team_7_Anusha=str("Anusha - ATK:6 DEF:2")
Team_7_Arlet=str("Arlet - ATK:6 DEF:3")
Team_7_Chanda_GK=str("Chanda GK - ATK:1 DEF:6")
#end of player string variables

#from here to next # is the printing statements for each team
def team_1_menu():
    print(Team_1_main)
    time.sleep(4)
    print(Team_1_Steve)
    time.sleep(2)
    print(Team_1_John)
    time.sleep(2)
    print(Team_1_Dave)
    time.sleep(2)
    print(Team_1_Barry)
    time.sleep(2)
    print(Team_1_Stuart)
    time.sleep(2)
    print(Team_1_Katy_GK)

def team_2_menu():
    print(Team_2_main)
    time.sleep(4)
    print(Team_2_Mateo)
    time.sleep(2)
    print(Team_2_Sofia)
    time.sleep(2)
    print(Team_2_Isabella)
    time.sleep(2)
    print(Team_2_Hugo)
    time.sleep(2)
    print(Team_2_Lucas)
    time.sleep(2)
    print(Team_2_Matias_GK)

def team_3_menu():
    print(Team_3_main)
    time.sleep(4)
    print(Team_3_Jakson)
    time.sleep(2)
    print(Team_3_Noah)
    time.sleep(2)
    print(Team_3_Benjamin)
    time.sleep(2)
    print(Team_3_Emma)
    time.sleep(2)
    print(Team_3_Amelia)
    time.sleep(2)
    print(Team_3_Chloe_GK)

def team_4_menu():
    print(Team_4_main)
    time.sleep(4)
    print(Team_4_Adrik)
    time.sleep(2)
    print(Team_4_Aleksi)
    time.sleep(2)
    print(Team_4_Borya)
    time.sleep(2)
    print(Team_4_Dimitri)
    time.sleep(2)
    print(Team_4_Vladimir)
    time.sleep(2)
    print(Team_4_Evgenii_GK)

def team_5_menu():
    print(Team_5_main)
    time.sleep(4)
    print(Team_5_Abella)
    time.sleep(2)
    print(Team_5_Alice)
    time.sleep(2)
    print(Team_5_Ailie)
    time.sleep(2)
    print(Team_5_Barrie)
    time.sleep(2)
    print(Team_5_Caitlin)
    time.sleep(2)
    print(Team_5_Farand_GK)

def team_6_menu():
    print(Team_6_main)
    time.sleep(4)
    print(Team_6_Alberto)
    time.sleep(2)
    print(Team_6_Beatrice)
    time.sleep(2)
    print(Team_6_Calynda)
    time.sleep(2)
    print(Team_6_Dani)
    time.sleep(2)
    print(Team_6_Elena)
    time.sleep(2)
    print(Team_6_Fabian_GK)

def team_7_menu():
    print(Team_7_main)
    time.sleep(4)
    print(Team_7_Aja)
    time.sleep(2)
    print(Team_7_Akhil)
    time.sleep(2)
    print(Team_7_Bhavya)
    time.sleep(2)
    print(Team_7_Anusha)
    time.sleep(2)
    print(Team_7_Arlet)
    time.sleep(2)
    print(Team_7_Chanda_GK)
#end of team printing statements

#from here to next # is player team selection
def game_menu_p1():
    global player_1_team
    if game_menu_t_choice=="1":
            team_1_menu()
            player_1_team=str(input("choose this team? y/n: "))
            if player_1_team=="y":
                player_1_team=str("1")
            else:
                game_menu_p1()
    elif game_menu_t_choice=="2":
            team_2_menu()
            player_1_team=str(input("choose this team? y/n: "))
            if player_1_team=="y":
                player_1_team=str("2")
            else:
                game_menu_p1()
    elif game_menu_t_choice=="3":
            team_3_menu()
            player_1_team=str(input("choose this team? y/n: "))
            if player_1_team=="y":
                player_1_team=str("3")
            else:
                game_menu_p1()
    elif game_menu_t_choice=="4":
            team_4_menu()
            player_1_team=str(input("choose this team? y/n: "))
            if player_1_team=="y":
                player_1_team=str("4")
            else:
                game_menu_p1()
    elif game_menu_t_choice=="5":
            team_5_menu()
            player_1_team=str(input("choose this team? y/n: "))
            if player_1_team=="y":
                player_1_team=str("5")
            else:
                game_menu_p1()
    elif game_menu_t_choice=="6":
            team_6_menu()
            player_1_team=str(input("choose this team? y/n: "))
            if player_1_team=="y":
                player_1_team=str("6")
            else:
                game_menu_p1()
    elif game_menu_t_choice=="7":
            team_7_menu()
            player_1_team=str(input("choose this team? y/n: "))
            if player_1_team=="y":
                player_1_team=str("7")
            else:
                game_menu_p1()
    print("Your team is "+player_1_team)
    main_menu()

def game_menu_p2():
    global player_2_team
    if game_menu_t_choice=="1":
            team_1_menu()
            player_2_team=str(input("choose this team? y/n: "))
            if player_2_team=="y":
                player_2_team=str("1")
            else:
                game_menu_p2()
    elif game_menu_t_choice=="2":
            team_2_menu()
            player_2_team=str(input("choose this team? y/n: "))
            if player_2_team=="y":
                player_2_team=str("2")
            else:
                game_menu_p1()
    elif game_menu_t_choice=="3":
            team_3_menu()
            player_2_team=str(input("choose this team? y/n: "))
            if player_2_team=="y":
                player_2_team=str("3")
            else:
                game_menu_p1()
    elif game_menu_t_choice=="4":
            team_4_menu()
            player_2_team=str(input("choose this team? y/n: "))
            if player_2_team=="y":
                player_2_team=str("4")
            else:
                game_menu_p1()
    elif game_menu_t_choice=="5":
            team_5_menu()
            player_2_team=str(input("choose this team? y/n: "))
            if player_2_team=="y":
                player_2_team=str("5")
            else:
                game_menu_p1()
    elif game_menu_t_choice=="6":
            team_6_menu()
            player_2_team=str(input("choose this team? y/n: "))
            if player_2_team=="y":
                player_2_team=str("6")
            else:
                game_menu_p1()
    elif game_menu_t_choice=="7":
            team_7_menu()
            player_2_team=str(input("choose this team? y/n: "))
            if player_2_team=="y":
                player_2_team=str("7")
            else:
                game_menu_p1()
    print("Your team is "+player_2_team)
    main_menu()
#end of player team selection

#from here to next # is the actual game
def main_menu_play():
    global p_1_player
    global p_2_player
    global p_1_GK
    global p_2_GK
    if player_2_team=="1":
        p_2_GK=Team_1_Katy_DEF
    elif player_2_team=="2":
        print("not done yet")
    elif player_2_team=="3":
        print("not done yet")
    elif player_2_team=="4":
        print("not done yet")
    elif player_2_team=="5":
        print("not done yet")
    elif player_2_team=="6":
        print("not done yet")
    elif player_2_team=="7":
        print("not done yet")
    
    if player_1_team=="1":
        team_1_menu()
    elif player_1_team=="2":
        team_2_menu()
    elif player_1_team=="3":
        team_3_menu()
    elif player_1_team=="4":
        team_4_menu()
    elif player_1_team=="5":
        team_5_menu()
    elif player_1_team=="6":
        team_6_menu()
    elif player_1_team=="7":
        team_7_menu()
    p_1_player=str(input("select player 1-7: "))
    if p_1_player=="1":
        score=p_2_GK-Team_1_Steve_ATK
    elif p_1_player=="2":
        print("not done yet")
    elif p_1_player=="3":
        print("not done yet")
    elif p_1_player=="4":
        print("not done yet")
    elif p_1_player=="5":
        print("not done yet")
    elif p_1_player=="6":
        print("not done yet")
    elif p_1_player=="7":
        print("not done yet")
    
    if score>=0:
        global p_1_score
        p_1_score=p_1_score+1
        p_1_score_str=str(p_1_score)
        print("Score! Player 1 is on "+p_1_score_str)
        main_menu_play()
        
    

#end of game




#from here to next # is player team selection menu
def main_menu_player():
    global game_menu_t_choice
    game_menu_p_choice=str(input("Choose a player 1/2: "))
    if game_menu_p_choice=="1":
        game_menu_t_choice=str(input("Choose a team to view: 1,2,3,4,5,6,7: "))
        game_menu_p1()
    elif game_menu_p_choice=="2":
        game_menu_t_choice=str(input("Choose a team to view: 1,2,3,4,5,6,7: "))
        game_menu_p2()
#end of player team selection menu






#from here to next # is main menu
def main_menu():
    global game_menu_choice
    game_menu_choice=str(input("Choose player or game? player/game: "))
    if game_menu_choice=="player":
        main_menu_player()
    elif game_menu_choice=="game":
        main_menu_play()
#end of main menu





#this is a very special line of code, it is how this whole proces starts and ends, my entire prodject depends of these 11 characters.
main_menu()