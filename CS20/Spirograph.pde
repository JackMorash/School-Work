def setup():
    global centerX, centerY
    fullScreen()
    colorMode(HSB, 360)
    centerX, centerY = width/2, height/2
 
 
def draw():
    background(0)
    a, b, h = mouseX, 60, mouseY
    for i in range(1, 361):
        t, ot = radians(i), radians(i-1)
        d, od = a*t, a*ot
        oxpos = (a-b)*cos(ot)+h*cos(od)
        oypos = (a-b)*sin(ot)+h*sin(od)
        xpos = (a-b)*cos(t)+h*cos(d)
        ypos = (a-b)*sin(t)+h*sin(d)
        stroke(i-1, 360, 360)
        line(centerX+oxpos, centerY+oypos, centerX+xpos, centerY+ypos)
