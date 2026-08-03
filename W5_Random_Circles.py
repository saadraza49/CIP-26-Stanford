from graphics import Canvas
import random

CANVAS_WIDTH = 300
CANVAS_HEIGHT = 300
CIRCLE_SIZE = 20
N_CIRCLES = 20

def main():
    print('Random Circles')
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    # Draw N_circle
    for i in range(N_CIRCLES):
        draw_random_circle(canvas)
# EXTENSIONS FOR YOU GUYS
#     Draw a random number of circles between 1 and 20
#     Draw circles of a random size 
#     Draw the circles such that all parts of the circle are within the canvas 


def draw_random_circle(canvas):
    # write the logic for creating 1 circle
    x1 = random.randint(0, CANVAS_WIDTH + 1) # STARTING x POSITION  
    y1 = random.randint(0, CANVAS_HEIGHT + 1) # starting y POSITION
    # most confusing part

    x2 =  x1 + CIRCLE_SIZE      # x1 + CIRCLE_SIZE
    y2 =  y1 + CIRCLE_SIZE      # y1 + CIRCLE_SIZE
    color = random_color()

    print(x1,y1,x2,y2)
    canvas.create_oval(x1,y1,x2,y2,color)



def random_color():
    """
    This is a function to use to get a random color for each circle. We have
    defined this for you and there is no need to edit code in this function,
    but feel free to read it over if you are interested. 
    """
    colors = ['blue', 'purple', 'salmon', 'lightblue', 'cyan', 'forestgreen','black']
    return random.choice(colors)

if __name__ == '__main__':
    main()

    