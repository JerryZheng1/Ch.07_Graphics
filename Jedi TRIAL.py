import arcade
arcade.open_window(600,600,"219119") #tittle
arcade.set_background_color(arcade.color.AMAZON)
arcade.start_render()
for i in range(200,600,200): #background w/lines 3x3 grid
    arcade.draw_line(i,0, i, 600, arcade.color.BLACK, 2)
    arcade.draw_line(0, i, 600, i, arcade.color.BLACK, 2)
arcade.draw_rectangle_filled(100, 500, 50, 50, arcade.color.NEON_CARROT) #1
arcade.draw_rectangle_outline(100, 500, 50, 50, arcade.color.BLACK,2)
arcade.draw_circle_filled(300,500,50,arcade.color.BRIGHT_TURQUOISE) #2
arcade.draw_arc_filled(500,500,40,40,arcade.color.YELLOW,30,330,180) #3 backward pacman
point_list = ((100,200),(0, 300),(100,400),(200, 300)) #4
arcade.draw_polygon_filled(point_list, arcade.color.BARBIE_PINK)
for i in range(200,420,20): #5
    arcade.draw_line(200,0+i,0+i, 200, arcade.color.BLACK, 2)
    arcade.draw_line(0+i,400,400,0+i,arcade.color.BLACK,2)
arcade.draw_rectangle_filled(500,300,200,200,arcade.color.WHITE) #6
for i in range(220,400,40):
    arcade.draw_rectangle_filled(500,10+i, 200, 20, arcade.color.RED)
arcade.draw_rectangle_filled(450,350,100,100,arcade.color.NAVY_BLUE)
for x in range(0,200,40):#7
    arcade.draw_circle_filled(x+20,100,20,arcade.color.BLUEBERRY)
for j in range(0,19):#8
    for i in range(0,19):
        arcade.draw_point(210+(10*i),190-(j*10),arcade.color.NEON_GREEN,2)
arcade.draw_text("Jerry Zheng",450,100,arcade.color.BLACK,12) #9
arcade.finish_render()
arcade.run()