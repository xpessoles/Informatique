import turtle as t
import tkinter as tk

app = tk.Tk()
cv = t.ScrolledCanvas(app)   
cv.pack()
screen = t.TurtleScreen(cv)
screen.screensize(1500, 1500)   
t1 = t.RawTurtle(screen)


#t.forward(L)
#t.left(45)
#t.forward(L/math.sqrt(2))
#t.right(90)
#t.forward(L/math.sqrt(2))

def dessiner_dragon(n,s,L):
    if n==1:
        t.forward(L)
    else:
        dessiner_dragon(n-1,1,L)
        tourner_plume(s)
        dessiner_dragon(n-1,-1,L)
        
def tourner_plume(s):
    if s==1:
        t.left(90)
    if s==-1:
        t.right(90)
        
def tracer_segment(L):
    t.forward(L)
        
k=7
L=320/(1.414)**(k-1)
t.up()
#t.goto(-100,-100)
t.down()
dessiner_dragon(k,1,L)
#t.getcanvas().postscript(file = "dragon{0}.eps".format(k))
    