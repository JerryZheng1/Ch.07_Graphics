# import arcade
# arcade.open_window(700,700,"Thats Crazy")
# arcade.set_background_color((255,255,0))
# arcade.start_render()
#
# #fence posts
#
# for x_offset in range(0,610,20):
#
#      arcade.draw_rectangle_filled(0+x_offset,700,10,30,arcade.color.WHITE)
#
#
# #rails
#
# arcade.draw_rectangle_filled(300, 67, 600, 5, arcade.color.WHITE)
#
# arcade.draw_rectangle_filled(300, 52, 600, 5, arcade.color.WHITE)
#
# arcade.finish_render()
#
#
# arcade.run()
#


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
