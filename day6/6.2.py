"""
Reeborg's World hurdle challenge day 4.
"""

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    counter = 0
    turn_left()
    while wall_on_right():
        move()
        counter += 1
    turn_right()
    move()
    turn_right()
    while counter > 0:
        move()
        counter -= 1
    turn_left()

while not at_goal():
    if not front_is_clear():
        jump()
    elif not wall_in_front():
        move()