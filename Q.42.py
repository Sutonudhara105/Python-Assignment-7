'''Write a program to input player's name (string) and runs (integer) scored for n number of players where n should be input from the keyboard. Store the player’s details in a dictionary called 'cricket'. After preparing the dictionary, input the player's name and print the runs scored by the player otherwise returns'-1' if the player's name is not found.'''

n =  int(input("Enter the number of players: "))
cricket = {}

for i in range(n):
    name = input("Enter the name of player: ")
    runs = int(input("Enter the runs scored by the player: "))
    cricket[name] = runs

while True:
    name = input("Enter the name of player: ")
    if name in cricket:
        print("The Score of player"+ name + "is",cricket[name])
    else:
        print("-1")
    ch = input("Do you want to continue? (y/n): ")
    if ch == 'n':
        break
