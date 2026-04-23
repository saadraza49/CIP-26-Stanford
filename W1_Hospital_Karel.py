from karel.stanfordkarel import *

def main(): 
    # move the karel
    while front_is_clear(): 
        if beepers_present():
            build_hospital()
        safe_move()

    # build a hospital


def build_hospital():
    turn_left()
    for i in range(2):
        move()
        put_beeper()
    
    turn_right()
    move()
    put_beeper()
    turn_right()
    for i in range(2):
        move()
        put_beeper()
    turn_left()
    


def turn_right():
    # to turn right
    for i in range(3):
        turn_left()

def safe_move():
    if front_is_clear():
        move()


if __name__ == '__main__':
    main()