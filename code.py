import simplegui

# set frame width and height
frame_width = 500  
frame_height = frame_width  

# define canvas size
canvas_width = frame_width
canvas_height = frame_height

# defining emoji face function
def draw_mad_face(canvas, x, y):
    # face
    canvas.draw_circle([x, y], 100, 2, "red", "red")
    # eyes
    canvas.draw_circle([x-30, y-25], 15, 2, "black", "black")
    canvas.draw_circle([x+30, y-25], 15, 2, "black", "black")
    # brows
    canvas.draw_line([x-50, y-50], [x-20, y-40], 8, "black")  # left
    canvas.draw_line([x+50, y-50], [x+20, y-40], 8, "black")  # right 
    # mout
    canvas.draw_line([x-40, y+30], [x-20, y+10], 6, "black")  # left 
    canvas.draw_line([x+40, y+30], [x+20, y+10], 6, "black")  # right 
    canvas.draw_line([x-20, y+10], [x+20, y+10], 6, "black")  # bottom

def draw_happy_face(canvas, x, y):
    # face
    canvas.draw_circle([x, y], 100, 2, "yellow", "yellow")
    # eyes
    canvas.draw_circle([x-30, y-25], 15, 2, "black", "black")
    canvas.draw_circle([x+30, y-25], 15, 2, "black", "black")
    # mouth
    canvas.draw_line([x-40, y+40], [x-20, y+60], 6, "black")  #left
    canvas.draw_line([x+40, y+40], [x+20, y+60], 6, "black")  # right 
    canvas.draw_line([x-20, y+60], [x+20, y+60], 6, "black")  # bottom 

def draw_sad_face(canvas, x, y):
    # face
    canvas.draw_circle([x, y], 100, 2, "blue", "blue") 
    # eyes 
    canvas.draw_circle([x-30, y-25], 15, 2, "black", "black")
    canvas.draw_circle([x+30, y-25], 15, 2, "black", "black")
    # mouth
    canvas.draw_line([x-40, y+30], [x-20, y+10], 6, "black")  # left 
    canvas.draw_line([x+40, y+30], [x+20, y+10], 6, "black")  # right
    canvas.draw_line([x-20, y+10], [x+20, y+10], 6, "black")  # bottom 

def draw_bored_face(canvas, x, y):
    # face 
    canvas.draw_circle([x, y], 100, 2, "yellow", "yellow")
    # eyes 
    canvas.draw_circle([x-30, y-25], 15, 2, "black", "black")
    canvas.draw_circle([x+30, y-25], 15, 2, "black", "black")
    # mouth 
    canvas.draw_line([x-40, y+40], [x+40, y+40], 6, "black")

# draw function 
def draw(canvas): 
    draw_mad_face(canvas, 150, 150)      # top left corner
    draw_happy_face(canvas, 350, 150)   # top right corner
    draw_sad_face(canvas, 150, 350)     # bottom left corner
    draw_bored_face(canvas, 350, 350)  # bottom right corner


frame = simplegui.create_frame("Emoji Faces", canvas_width, canvas_height)
frame.set_draw_handler(draw)
frame.start()
