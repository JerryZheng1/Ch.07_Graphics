Point: arcade.draw_point(50, 580, arcade.color.RED, 5)
Line: arcade.draw_line(75, 590, 95, 570, arcade.color.BLACK, 2)
line: start coordinate, end coordinate

arcade.draw_lrtb_rectangle_filled(5, 35, 590, 570, arcade.color.BITTER_LIME)
(590)
(5,35)
(570)

circle: arcade.draw_circle_outline(140, 580, 18, arcade.color.WISTERIA, 3)

for i in range(0,260,40):
    arcade.draw_rectangle_filled(247, i+10, 494, 20, (191,10,48))


down=0
for j in range(0,5):
    for i in range(0,6):
        arcade.draw_text("*",16.38+(i*30.76),(225.96-down),arcade.color.WHITE,20)
    down+=26.08

background lines:
for x in range(20,sw,20): #background
    arcade.draw_line(x,0, x, sh, arcade.color.BLACK, 2)
for y in range(20,sh,20):
    arcade.draw_line(0,y,sw,y,arcade.color.BLACK,2 )

arcade.draw_arc_filled(400,320,120,120,arcade.color.YELLOW, 30, 330)


for i in range(0,260,40):
    arcade.draw_rectangle_filled(247, i+10, 494, 20, (191,10,48))

point_list = ((30, 240),

              (45, 240),

              (60, 255),

              (60, 285),

              (45, 300),

              (30, 300))

arcade.draw_polygon_outline(point_list, arcade.color.SPANISH_VIOLET, 3)


