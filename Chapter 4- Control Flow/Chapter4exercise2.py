#if-else chain
print("\tfirst_round\n")

#if alien_color is green, print a statement that the player just earned 5 points for shooting the alien
alien_color = 'green'
alien_color = (input("DON'T SHOOT THE GREEN ALIEN!"))

if alien_color == 'green':
    print("You only earned 5 points!")
else:
    print("SCORE! You just earned 10 points!")


print("\tsecond_round\n")
#if the alien_color isn’t green, print a statement that the player just earned 10 points
alien_color = 'yellow'
alien_color = (input("HIT THE GREEN ALIEN!"))

if alien_color == 'red' + 'yellow' :
    print("You only earned 5 points!")
    if alien_color == 'yellow' :
        print("You only earned 5 points!")
else:
    print("SCORE! You just earned 10 points!")

    alien_color = 'green'


#if block/ else block
#if block
coin = 'heads'

coin = (input("heads or tails? "))
if coin == 'tails':
    print("Yikes! try again!")
else:
    print("Heads!!! We got a winner!")

    coin = 'heads'

#else block
if coin == 'tails':
    print("Try again!")
else: 
    print("You got lucky!")
    
