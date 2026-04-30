from karel.stanfordkarel import *


def main():
    move()
    spread()
    return_to_base()


def spread():
    while beepers_present():
        pick_beeper()
        if beepers_present():
            go_to_empty_pile()
            put_beeper()
            return_to_the_pile()
    put_beeper()


def return_to_the_pile():
    turn_around()
    while beepers_present():
        move()
    turn_around()
    move()

def go_to_empty_pile():
    while beepers_present():
        move()


def turn_around():
    turn_left()
    turn_left()

def return_to_base():
    turn_around()
    move()
    turn_around()



if __name__ == '__main__':
    main()