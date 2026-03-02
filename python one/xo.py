cells = ["1", "2", "3", '4', '5', '6', '7', '8', '9']

print(f"  {cells[0]}  |  {cells[1]}  |  {cells[2]}  ")
print("_____|_____|_____")
print("     |     |     ")
print(f"  {cells[3]}  |  {cells[4]}  |  {cells[5]}  ")
print("_____|_____|_____")
print("     |     |     ")
print(f"  {cells[6]}  |  {cells[7]}  |  {cells[8]}  ")
print("     |     |     ")


i = 0
player_input= input("Please Enter a Number from 1-9: ")
if int(player_input)>9 or int(player_input)<0:
    print("please retry")
while i<9:
    if cells[i]==player_input:
        cells[i]="X"

    i += 1


print(f"  {cells[0]}  |  {cells[1]}  |  {cells[2]}  ")
print("_____|_____|_____")
print("     |     |     ")
print(f"  {cells[3]}  |  {cells[4]}  |  {cells[5]}  ")
print("_____|_____|_____")
print("     |     |     ")
print(f"  {cells[6]}  |  {cells[7]}  |  {cells[8]}  ")
print("     |     |     ")