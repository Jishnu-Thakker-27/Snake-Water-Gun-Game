# Snake Water Gun Game
import random
print("=================================================================================")
print("                             GAME STARTS                                         ")
print("=================================================================================")


def game_comp_rule(Move,Computer,U_move,C_move):
    if(Move==Computer):
        print(f"You chose {U_move} and Computer chose {C_move}\n")
        print("It's a draw!\n")
        print("Type '0' to play again! \n")
    elif(Move==1 and Computer==2):
        print(f"You chose {U_move} and Computer chose {C_move}\n")
        print("Congratulations.You Won!!!\n")
        print("Type '0' to play again!\n ")
    elif(Move==2 and Computer==3):
        print(f"You chose {U_move} and Computer chose {C_move}\n")
        print("Congratulations.You Won!!!\n")
        print("Type '0' to play again!\n ")
    elif(Move==3 and Computer==1):
        print(f"You chose {U_move} and Computer chose {C_move}\n")
        print("Congratulations.You Won!!!\n")
        print("Type '0' to play again!\n ")
    elif(Move==2 and Computer==1):
        print(f"You chose {U_move} and Computer chose {C_move}\n")
        print("You Lost!!\n")
        print("Type '0' to play again! \n")
    elif(Move==3 and Computer==2):
        print(f"You chose {U_move} and Computer chose {C_move}\n")
        print("You Lost!!")
        print("Type '0' to play again! \n")
    elif(Move==1 and Computer==3):
        print(f"You chose {U_move} and Computer chose {C_move}\n")
        print("You Lost!!\n")
        print("Type '0' to play again!\n ")
    elif(Move!=1 or Move!=2 or Move!=3):
        print("Invalid Input.\n")
        print("Make Your Move\n")
    

print("Welcome To The Game.\n")
print("Enter 1 to play with Computer!")
print("OR")
print("Enter 2 to play with a Friend!.\n")
Type=int(input("Enter The Type You Want To Play"))


print("Snake Water Gun!")
print("Type 'S' for Snake")
print("Type 'W' for Water")
print("Type 'G' for Gun\n")

def computer_game():
    Computer=random.choice([1,2,3])
    User=(input("Enter Your Move: \n")).lower()
    game_dict={
    "s":1,
    "w":2,
    "g":3
}
    U_dict={
    "s":"Snake",
    "w":"Water",
    "g":"Gun"
}
    C_dict={
    1:"Snake",
    2:"Water",
    3:"Gun"
}
    Move=game_dict[User]
    U_move=U_dict[User]
    C_move=C_dict[Computer]
    game_comp_rule(Move,Computer,U_move,C_move)

def friend_game():
    User1=(input("Player 1, Enter Your Move: \n")).lower()
    User2=(input("Player 2, Enter Your Move: \n")).lower()


if(Type==1):
    computer_game()
elif(Type==2):
    friend_game()
print("=================================================================================")
print("                              GAME ENDS                                          ")
print("=================================================================================")