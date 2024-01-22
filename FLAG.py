# import arcade
# # y=260
# arcade.open_window(494,260,"The Stars and Stripes") #naming it
# arcade.set_background_color(arcade.color.WHITE) #backlground color
# arcade.start_render()
#
# for i in range(0,260,40):
#     arcade.draw_rectangle_filled(247, i+10, 494, 20, (191,10,48))
#
# arcade.draw_lrtb_rectangle_filled(0,(0.76*260),260,120,(0,40,104))
#
# for i in range(0,6):
#     arcade.draw_text("*",16.38+(i*30.76),(225.96),arcade.color.WHITE,20)
#
# down=0
# for j in range(0,4):
#     for i in range(0,4):
#         arcade.draw_text("*",32.76+(i*30.76),(211.96-down),arcade.color.WHITE,20)
#         down+=26.08
#         down=0
#         arcade.draw_text("*", 16.38 + (i * 30.76), (225.96), arcade.color.WHITE, 20)
#         down+=26.08
#
# arcade.finish_render()
#
# arcade.run()

import arcade
# y=260
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