# 7.0 Jedi Training (20pts)  Name:________________

'''
1. TEST PICTURE  (10pts)
------------------------
Recreate, exactly the Test Picture from the website. The arcade colors used in this picture in no particular order are:
BLACK, ALMOND, PHLOX, BLUSH, RED, BLUE, WISTERIA, AMBER, BRICK_RED and YELLOW.
The picture is 500px wide and 400px tall. Look up ARC in the documentation to do the PAC-MAN.
Upload your code and a screenshot of your picture.

import arcade

sw=500
sh=400

arcade.open_window(sw,sh,"Test picture")
arcade.set_background_color(arcade.color.ALMOND)

arcade.start_render()

for x in range(20,sw,20): #background
    arcade.draw_line(x,0, x, sh, arcade.color.BLACK, 2)
for y in range(20,sh,20):
    arcade.draw_line(0,y,sw,y,arcade.color.BLACK,2 )

arcade.draw_lrtb_rectangle_filled(20, 80, 380, 360, arcade.color.PHLOX) #rectange


arcade.draw_circle_filled(250,200,40,arcade.color.WISTERIA) #circle

arcade.draw_text("I love you. I know.", 21, 160, arcade.color.BRICK_RED, 20) #text

arcade.draw_line(80, 20, 120, 60, arcade.color.BLUE, 1) #the line

arcade.draw_ellipse_filled(100, 100, 120, 40, arcade.color.AMBER) #ellipse

arcade.draw_rectangle_filled(200,260,40,20,arcade.color.BLUSH,-45) #rotated rectangle

arcade.draw_point(460, 10, arcade.color.RED, 5) #the point

arcade.draw_arc_filled(400,320,120,120,arcade.color.YELLOW, 30, 330)


arcade.finish_render()


arcade.run()

'''


'''
2. FLAG CREATION  (10pts)
---------------
Make your flag 260 pixels tall
Use the scaling image on the website to determine other dimensions
The hexadecimal colors for the official flag are red: #BF0A30 and blue: #002868
Title the window, "The Stars and Stripes"
You can use a draw_text command and used 20 pt. asterisks for the stars.
Can you use <20 lines of code?
CHALLENGE: Can you make the entire flag parametrically? This means if I change the hoist to 520px the flag will resize accordingly.
Upload your code and a screenshot of your flag.


import arcade
arcade.open_window(494,260,"The Stars and Stripes") #naming it
arcade.set_background_color(arcade.color.WHITE) #backlground color
arcade.start_render()

for i in range(0,260,40):
    arcade.draw_rectangle_filled(247, i+10, 494, 20, (191,10,48))

arcade.draw_lrtb_rectangle_filled(0,(0.76*260),260,120,(0,40,104))

down=0
for j in range(0,5):
    for i in range(0,6):
        arcade.draw_text("*",16.38+(i*30.76),(225.96-down),arcade.color.WHITE,20)
    down+=26.08

down=0
for j in range(0,4):
    for i in range(0,5):
        arcade.draw_text("*",32.76+(i*30.76),(211.96-down),arcade.color.WHITE,20)
    down+=26.08

arcade.finish_render()

arcade.run()
'''








