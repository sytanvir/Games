
from graphics import Canvas 
import time
import random
    
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 500
SIZE = 20
Velocity=20
# if you make this larger, the game will go slower
DELAY = .1

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    goal,goal_left_x,goal_right_x,goal_left_y,goal_right_y=goal_rectangle(canvas)
    text = canvas.create_text(190, 425,font=' Input', font_size = 30,text=str(0),color='black')
    player=player_rectangle(canvas)
    line(canvas)
    
    x = canvas.get_left_x(player)
    y = canvas.get_top_y(player)
    start_y=0
    start_x=0
    points=0
    
    
   
    while True:
        
        key=canvas.get_last_key_press()
        for i in range(10000):
            
            while key == 'ArrowRight':
                canvas.moveto(player,start_x,start_y)
                start_x+=Velocity
                
                if start_x==goal_left_x and start_y==goal_left_y:
                    
                    
                    canvas.delete(goal)
                    canvas.delete(text)
                    goal,goal_left_x,goal_right_x,goal_left_y,goal_right_y=goal_rectangle(canvas)
                    canvas.get_last_key_press()
                    points+=1
                    text=score(canvas,points)
                    
                if start_x>=x+390:
                    game_over(canvas)
                    break
                time.sleep(DELAY)
                new_direction = canvas.get_last_key_press() # getting the key press once
                if new_direction:
                    key=new_direction   # no need to worry about empty buffers
                    start_x-=20 
                
            while key == 'ArrowDown':
                
                canvas.moveto(player,start_x,start_y)
                start_y+=Velocity
                
                
                if start_x==goal_left_x and start_y==goal_right_y-20:
                    
                    canvas.delete(goal)
                    canvas.delete(text)
                    goal,goal_left_x,goal_right_x,goal_left_y,goal_right_y=goal_rectangle(canvas)
                    canvas.get_last_key_press()
                    points+=1
                    text=score(canvas,points)
                if start_y>=y+390:
                    game_over(canvas)
                    break
                time.sleep(DELAY)
                new_direction = canvas.get_last_key_press() # getting the key press once
                if new_direction:
                    key=new_direction   # no need to worry about empty buffers
                    start_y-=20
                
            
                
            while key == 'ArrowUp':
                
                canvas.moveto(player,start_x,start_y)
                start_y-=Velocity
                if start_x==goal_left_x and start_y==goal_right_y-20:
                    
                    canvas.delete(goal)
                    canvas.delete(text)
                    goal,goal_left_x,goal_right_x,goal_left_y,goal_right_y=goal_rectangle(canvas)
                    canvas.get_last_key_press()
                    points+=1
                    text=score(canvas,points)
                if start_y<=y-20:
                    game_over(canvas)
                    break
                time.sleep(DELAY)
                
                new_direction = canvas.get_last_key_press() # getting the key press once
                if new_direction:
                    key=new_direction   # no need to worry about empty buffers
                    start_y+=20
                
            
            while key == 'ArrowLeft':
                
                canvas.moveto(player,start_x,start_y)
                start_x-=Velocity
                if start_x==goal_right_x-20 and start_y==goal_left_y:
                    
                    canvas.delete(goal)
                    canvas.delete(text)
                    goal,goal_left_x,goal_right_x,goal_left_y,goal_right_y=goal_rectangle(canvas)
                    canvas.get_last_key_press()
                    points+=1
                    text=score(canvas,points)
    
                if start_x<=x-20:
                    game_over(canvas)
                    break
                #time.sleep(DELAY)
                new_direction = canvas.get_last_key_press() # getting the key press once
                if new_direction:
                    key=new_direction   # no need to worry about empty buffers
                    start_x+=20
                
            
       
#### HELPER FUNCTIONS####

#creat player and goal rectangle 
#return player and rectangle
def player_rectangle(canvas):    
    
    #Player cordinates
    pl_x_l=0
    pl_y_t=0
    pl_x_r= pl_x_l + SIZE
    pl_y_b= pl_y_t + SIZE
    player=canvas.create_rectangle(pl_x_l,pl_y_t,pl_x_r,pl_y_b,'black')
    
    return player
    
#creat a goal cordintes and goal object    
def goal_rectangle(canvas):
    
    #goal random cordinates
    goal_left_x=random.randrange(0,380,20)
    goal_left_y=random.randrange(0,380,20)
    
    goal_right_x=goal_left_x+SIZE
    goal_right_y=goal_left_y+SIZE
    
    goal=canvas.create_oval(goal_left_x,goal_left_y,goal_right_x,goal_right_y,'Indigo ')
    return goal,goal_left_x,goal_right_x,goal_left_y,goal_right_y


#create line
def line(canvas):
    line = canvas.create_line(0, 400, 400, 400,'black')
    line = canvas.create_line(0, 402, 400, 402,'black')
    
#create score update
def game_over(canvas):
   
    colors = ['blue', 'purple', 'salmon', 'lightblue', 'cyan', 'forestgreen']
    color=random.choice(colors)
    text = canvas.create_text(120, 200,font=' Input', font_size = 30,text='GAME OVER!',color=color)
    return text
    
#show score
def score(canvas,points):
    colors = ['blue', 'purple', 'salmon', 'lightblue', 'cyan', 'forestgreen']
    color=random.choice(colors)
    text = canvas.create_text(165, 425,font='Input', font_size = 30,text='score!'+str(points),color=color)
    return text
    
    
    
    
if __name__ == '__main__':
    main()