import arcade
arcade.open_window(1000,700,"Jerry Zheng")
arcade.set_background_color((79,102,74,255))
arcade.start_render()



#ROAD BETWEEN STADIUM AND BUILDING
arcade.draw_lrtb_rectangle_filled(550,620,550,200,(178,180,188,255))


#GRASS UNDER SCHOOL
arcade.draw_rectangle_filled(250,375,600,700,(79,102,74,255))

#parking LOT
arcade.draw_point(200,300,arcade.color.YELLOW,5)
arcade.draw_rectangle_filled(220,300,240,200,(180,185,192,255))

arcade.draw_circle_outline(220,300,25,arcade.color.BLACK)
arcade.draw_text("P",210,287,arcade.color.BLACK,25)



#sidewalks
arcade.draw_lrtb_rectangle_filled(340,365,480,200,(201,191,185,255))
# arcade.draw_point(340,410,arcade.color.WHITE,5)
# arcade.draw_point(100,395,arcade.color.WHITE,5)
# arcade.draw_point(80,560,arcade.color.WHITE,5)
# arcade.draw_point(500,540,arcade.color.WHITE,5)
arcade.draw_lrtb_rectangle_filled(100,340,200,190,(201,191,185,255))
arcade.draw_lrtb_rectangle_filled(80,100,395,190,(201,191,185,255))

# arcade.draw_point(300,400,arcade.color.WHITE,5)
#bottom sidewalk
arcade.draw_lrtb_rectangle_filled(100,340,410,395,(201,191,185,255))
arcade.draw_lrtb_rectangle_filled(80,100,560,395,(201,191,185,255))
arcade.draw_lrtb_rectangle_filled(80,900,560,540,(201,191,185,255))
arcade.draw_lrtb_rectangle_filled(126,136,440,400,(201,191,185,255))
arcade.draw_lrtb_rectangle_filled(160,168,480,400,(201,191,185,255))
arcade.draw_lrtb_rectangle_filled(240,248,480,400,(201,191,185,255))
arcade.draw_lrtb_rectangle_filled(185,225,480,400,(201,191,185,255))
arcade.draw_lrtb_rectangle_filled(270,280,480,400,(201,191,185,255))
arcade.draw_lrtb_rectangle_filled(300,310,480,400,(201,191,185,255))
arcade.draw_lrtb_rectangle_filled(360,400,370,350,(201,191,185,255))


#top sidewalk
arcade.draw_lrtb_rectangle_filled(165,172,550,500,(201,191,185,255))
arcade.draw_lrtb_rectangle_filled(240,247,550,500,(201,191,185,255))


#sidewalk by weight room
arcade.draw_lrtb_rectangle_filled(340,560,200,190,(201,191,185,255))
arcade.draw_lrtb_rectangle_filled(385,395,220,200,(201,191,185,255))
arcade.draw_lrtb_rectangle_filled(490,505,380,190,(201,191,185,255))


#exit gym side walks
arcade.draw_rectangle_filled(480,270,20,10,(201,191,185,255))
arcade.draw_rectangle_filled(480,315,20,10,(201,191,185,255))
arcade.draw_rectangle_filled(495,360,120,10,(201,191,185,255))

#sidewalk from music side
arcade.draw_lrtb_rectangle_filled(545,555,455,360,(201,191,185,255))
arcade.draw_rectangle_filled(531,455,49,10,(201,191,185,255))
arcade.draw_rectangle_filled(531,420,49,5,(201,191,185,255))
arcade.draw_rectangle_filled(531,375,49,5,(201,191,185,255))

#lunch door exit
arcade.draw_rectangle_filled(480,460,60,9,(201,191,185,255))
arcade.draw_lrtb_rectangle_filled(500,510,540,520,(201,191,185,255))

#parking lot by gym
arcade.draw_point(555,280,arcade.color.YELLOW,5)
arcade.draw_rectangle_filled(555,277,100,157,(180,185,192,255))
arcade.draw_circle_outline(555,280,25,arcade.color.BLACK)
arcade.draw_text("P",545,267,arcade.color.BLACK,25)

#bus parking
arcade.draw_point(565,500,arcade.color.YELLOW,5)
arcade.draw_rectangle_filled(565,500,110,80,(180,185,192,255))
arcade.draw_circle_outline(565,500,25,arcade.color.BLACK)
arcade.draw_text("P",555,487,arcade.color.BLACK,25)

#parking lot to exit by baseball
arcade.draw_lrtb_rectangle_filled(20,100,395,375,(180,185,192,255))
arcade.draw_lrtb_rectangle_filled(80,100,395,180,(180,185,192,255))
arcade.draw_lrtb_rectangle_filled(20,80,580,395,(180,185,192,255))
arcade.draw_lrtb_rectangle_filled(80,160,580,560,(180,185,192,255))
arcade.draw_lrtb_rectangle_filled(140,160,650,560,(180,185,192,255))
arcade.draw_lrtb_rectangle_filled(80,100,150,0,(180,185,192,255))

#pool parking lot
arcade.draw_lrtb_rectangle_filled(0,80,240,180,(205,201,193,255))
arcade.draw_circle_outline(40,210,25,arcade.color.BLACK)
arcade.draw_text("P",30,197,arcade.color.BLACK,25)

#neighborhood road
arcade.draw_lrtb_rectangle_filled(0,875,670,640,(158,163,174,255))

#bottom road
arcade.draw_lrtb_rectangle_filled(0,875,180,150,(158,163,174,255))
# arcade.draw_point(0,166,arcade.color.RED,5)
# arcade.draw_point(0,164,arcade.color.RED,5)

arcade.draw_line(0,166,80,166,arcade.color.YELLOW)
arcade.draw_line(0,164,80,164,arcade.color.YELLOW)
arcade.draw_line(115,166,875,164,arcade.color.YELLOW)
arcade.draw_line(115,164,875,164,arcade.color.YELLOW)



#traffic stop
# arcade.draw_point(96,188,arcade.color.RED,5)
for i in range(8):
    arcade.draw_rectangle_filled(110,178-(4*i),5,2,arcade.color.WHITE)
arcade.draw_rectangle_filled(116,173,2,13,arcade.color.WHITE)
arcade.draw_rectangle_filled(79,157,2,14,arcade.color.WHITE)

for i in range(5):
    arcade.draw_rectangle_filled(99-(4*i),185,2,5,arcade.color.WHITE)

#field sidewalk bottom
arcade.draw_lrtb_rectangle_filled(600,875,200,190,(201,191,185,255))

#main parking lot to exit from weight room
arcade.draw_lrtb_rectangle_filled(320,339,200,180,(180,185,192,255))

#gym to exit road
arcade.draw_lrtb_rectangle_filled(560,610,200,180,(180,185,192,255))


#field ticket area
point_list=(
    (635,255),
    (645,260),
    (665,240),
    (655,235))
arcade.draw_polygon_filled(point_list,(134,135,151,255))
arcade.draw_polygon_outline(point_list,arcade.color.BLACK)

point_list=(
    (665,240),
    (655,235),
    (655,230),
    (665,230))
arcade.draw_polygon_filled(point_list,(146,76,67,255))
arcade.draw_polygon_outline(point_list,arcade.color.BLACK)

point_list=(
    (635,255),
    (635,250),
    (655,230),
    (655,235))
arcade.draw_polygon_filled(point_list,(146,76,67,255))
arcade.draw_polygon_outline(point_list,arcade.color.BLACK)


#football field

#grass
arcade.draw_rectangle_filled(750,400,215,220,(85,102,33,255))
#outer track
arcade.draw_rectangle_filled(750,400,175,185,(22,41,58,255))



arcade.draw_ellipse_filled(750, 400, 150, 200, (22,41,58,255))

for i in range(1,5):
    arcade.draw_ellipse_outline(750, 400, (150-(i*5)), (200-(i*5)), arcade.color.WHITE)

arcade.draw_rectangle_filled(750, 400, 95, 115, (68,128,80,255))

arcade.draw_rectangle_outline(750, 400, 80, 100, arcade.color.WHITE)

for y in range(350,450,10):
    arcade.draw_line(710,y,790,y,arcade.color.WHITE,1 )


#top goal post
arcade.draw_line(750,450,750,465,arcade.color.YELLOW)
arcade.draw_line(740,465,760,465,arcade.color.YELLOW)
arcade.draw_line(740,465,740,485,arcade.color.YELLOW)
arcade.draw_line(760,465,760,485,arcade.color.YELLOW)


#bottom goal post
arcade.draw_line(750,350,750,365,arcade.color.YELLOW)
arcade.draw_line(740,365,760,365,arcade.color.YELLOW)
arcade.draw_line(740,365,740,385,arcade.color.YELLOW)
arcade.draw_line(760,365,760,385,arcade.color.YELLOW)


arcade.draw_rectangle_filled(707, 400, 5, 33, arcade.color.WHITE)
arcade.draw_rectangle_filled(793, 400, 5, 33, arcade.color.WHITE)

#LEFT U
arcade.draw_rectangle_filled(755, 415, 16, 6, (197,76,86,255))
arcade.draw_rectangle_filled(745, 413, 6, 10, (197,76,86,255))

#RIGHT U
arcade.draw_rectangle_filled(745, 403, 6, 14, (32,67,100,255))
arcade.draw_rectangle_filled(752, 396, 20, 7, (32,67,100,255))

#LEFT STANDS
for i in range(7):
    arcade.draw_rectangle_outline((650+(i*3)),(435-(i*3)),3,50,arcade.color.BLACK)
    arcade.draw_rectangle_filled((650+(i*3)),(435-(i*3)),3,50,arcade.color.GRAY)

for i in range(7):
    arcade.draw_rectangle_outline((650 + (i * 3)), (390 - (i * 3)), 3, 50, arcade.color.BLACK)
    arcade.draw_rectangle_filled((650 + (i * 3)), (390 - (i * 3)), 3, 50, arcade.color.GRAY)

arcade.draw_rectangle_filled(673,392,6,95,(64,84,109,255))

arcade.draw_triangle_filled(
    648,367,648,344,677,344,arcade.color.BLACK
)

#RIGHT STANDS
for i in range(7):
    arcade.draw_rectangle_outline((835+(i*3)),(415+(i*3)),3,50,arcade.color.BLACK)
    arcade.draw_rectangle_filled((835+(i*3)),(415+(i*3)),3,50,arcade.color.GRAY)

for i in range(7):
    arcade.draw_rectangle_outline((835 + (i * 3)), (370+(i * 3)), 3, 50, arcade.color.BLACK)
    arcade.draw_rectangle_filled((835 + (i * 3)), (370 + (i * 3)), 3, 50, arcade.color.GRAY)

arcade.draw_rectangle_filled(830,392,6,95,(64,84,109,255))

arcade.draw_triangle_filled(
    827,344,855,344,855,365,arcade.color.BLACK
)

#SCOREBOARD


arcade.draw_rectangle_filled(750,290,40,20,arcade.color.NAVY_BLUE)
arcade.draw_rectangle_outline(750,290,40,20,arcade.color.WHITE)
arcade.draw_rectangle_outline(750,295,20,5,arcade.color.WHITE)
arcade.draw_rectangle_outline(735,295,5,5,arcade.color.WHITE)
arcade.draw_rectangle_outline(765,295,5,5,arcade.color.WHITE)
arcade.draw_rectangle_filled(750,283,25,5,arcade.color.BLACK)

#legs of scoreboard
arcade.draw_rectangle_filled(738,270,5,20,(148,137,112))
arcade.draw_rectangle_filled(760,270,5,20,(148,137,112))



#Urbandale on the right side



arcade.draw_lrtb_rectangle_filled(875,1000,700,0,arcade.color.WHITE)
arcade.draw_text("U",915,625,arcade.color.NAVY_BLUE,50)
arcade.draw_text("R",915,555,arcade.color.NAVY_BLUE,50)
arcade.draw_text("B",915,485,arcade.color.NAVY_BLUE,50)
arcade.draw_text("A",915,415,arcade.color.NAVY_BLUE,50)
arcade.draw_text("N",915,345,arcade.color.NAVY_BLUE,50)
arcade.draw_text("D",915,275,arcade.color.NAVY_BLUE,50)
arcade.draw_text("A",915,205,arcade.color.NAVY_BLUE,50)
arcade.draw_text("L",915,135,arcade.color.NAVY_BLUE,50)
arcade.draw_text("E",915,65,arcade.color.NAVY_BLUE,50)


#bottom of football field


#bottom of football field buildings
# arcade.draw_point(700,260,arcade.color.RED,5)
# arcade.draw_point(800,260,arcade.color.RED,5)
# arcade.draw_point(800,250,arcade.color.RED,5)
# arcade.draw_point(780,250,arcade.color.RED,5)
# arcade.draw_point(780,240,arcade.color.RED,5)
# arcade.draw_point(720,240,arcade.color.RED,5)
# arcade.draw_point(720,250,arcade.color.RED,5)
#
# arcade.draw_point(700,250,arcade.color.RED,5)
# # arcade.draw_point(720,235,arcade.color.RED,5)

arcade.draw_lrtb_rectangle_filled(700,720,250,235,(146,76,67,255))
arcade.draw_lrtb_rectangle_outline(700,720,250,235,arcade.color.BLACK)

arcade.draw_lrtb_rectangle_filled(707,713,244,238,(180,153,156,255))
arcade.draw_lrtb_rectangle_outline(707,713,244,238,arcade.color.BLACK)


arcade.draw_lrtb_rectangle_filled(780,800,250,235,(146,76,67,255))
arcade.draw_lrtb_rectangle_outline(780,800,250,235,arcade.color.BLACK)

arcade.draw_lrtb_rectangle_filled(787,793,244,238,(180,153,156,255))
arcade.draw_lrtb_rectangle_outline(787,793,244,238,arcade.color.BLACK)

point_list=(
    (700,260),
    (800,260),
    (800,250),
    (780,250),
    (780,240),
    (720,240),
    (720,250),
    (700,250))
arcade.draw_polygon_filled(point_list,(197,200,206,255))
arcade.draw_polygon_outline(point_list,arcade.color.BLACK)

arcade.draw_lrtb_rectangle_filled(720,780,240,230,(182,163,170,255))
arcade.draw_lrtb_rectangle_outline(720,780,240,230,arcade.color.BLACK)

# arcade.draw_point(740,240,arcade.color.RED,5)
# arcade.draw_point(760,230,arcade.color.RED,5)

arcade.draw_lrtb_rectangle_filled(735,765,240,230,(168,137,149,255))
arcade.draw_lrtb_rectangle_outline(735,765,240,230,arcade.color.BLACK)

arcade.draw_lrtb_rectangle_outline(736,746,235,230,arcade.color.BLACK)
arcade.draw_lrtb_rectangle_outline(747,753,235,230,arcade.color.BLACK)
arcade.draw_lrtb_rectangle_outline(754,764,235,230,arcade.color.BLACK)

arcade.draw_lrtb_rectangle_filled(728,730,235,230,arcade.color.WHITE)
arcade.draw_lrtb_rectangle_filled(770,772,235,230,arcade.color.WHITE)

#roof of building

arcade.draw_lrtb_rectangle_filled(714,740,264,238,(160,164,179,255))
arcade.draw_lrtb_rectangle_outline(714,740,264,238,arcade.color.BLACK)
# arcade.draw_point(727,258,arcade.color.RED,5)
# arcade.draw_point(727,248,arcade.color.RED,5)

arcade.draw_line(727,258,727,248,arcade.color.BLACK)
arcade.draw_line(714,264,727,258,arcade.color.BLACK)
arcade.draw_line(740,264,727,258,arcade.color.BLACK)
arcade.draw_line(714,238,727,248,arcade.color.BLACK)
arcade.draw_line(740,238,727,248,arcade.color.BLACK)

arcade.draw_lrtb_rectangle_filled(760,786,264,238,(160,164,179,255))
arcade.draw_lrtb_rectangle_outline(760,786,264,238,arcade.color.BLACK)

arcade.draw_line(773,258,773,248,arcade.color.BLACK)
arcade.draw_line(760,264,773,258,arcade.color.BLACK)
arcade.draw_line(786,264,773,258,arcade.color.BLACK)
arcade.draw_line(760,238,773,248,arcade.color.BLACK)
arcade.draw_line(786,238,773,248,arcade.color.BLACK)

#bottom left building
# arcade.draw_rectangle_filled(700,250,50,30,(143, 112, 78))
# arcade.draw_rectangle_outline(700,250,50,30,arcade.color.BLACK)
# arcade.draw_rectangle_filled(710,245,10,20,arcade.color.WHITE)
# arcade.draw_rectangle_outline(710,245,10,20,arcade.color.BLACK)
#
# point_list=(
#     (675,265),
#     (690,275),
#     (710,275),
#     (725,265))
#
# arcade.draw_polygon_filled(point_list,arcade.color.WHITE)
# arcade.draw_polygon_outline(point_list,arcade.color.BLACK)
#
#
# #bottom middle building
# arcade.draw_rectangle_filled(750,245,50,20,(196, 131, 96))
# arcade.draw_rectangle_outline(750,245,50,20,arcade.color.BLACK)
#
# arcade.draw_rectangle_outline(735,240,15,10,arcade.color.BLACK)
# arcade.draw_rectangle_outline(750,240,10,10,arcade.color.BLACK)
# arcade.draw_rectangle_outline(765,240,15,10,arcade.color.BLACK)
#
#
# #bottom right building
# arcade.draw_rectangle_filled(800,250,50,30,(143, 112, 78))
# arcade.draw_rectangle_outline(800,250,50,30,arcade.color.BLACK)
#
# arcade.draw_rectangle_filled(795,245,10,20,arcade.color.WHITE)
# arcade.draw_rectangle_outline(795,245,10,20,arcade.color.BLACK)
#
# point_list=(
#     (775,265),
#     (790,275),
#     (810,275),
#     (825,265))
#
# arcade.draw_polygon_filled(point_list,arcade.color.WHITE)
# arcade.draw_polygon_outline(point_list,arcade.color.BLACK)
#
#
#
# #right right building
# arcade.draw_rectangle_filled(835,245,20,20,(143, 112, 78))
# arcade.draw_rectangle_outline(835,245,20,20,arcade.color.BLACK)

#lunch room ish
point_list=(
    (407,545),
    (470,545),
    (470,500),
    (407,500))
arcade.draw_polygon_filled(point_list,(197,200,206,255))
arcade.draw_polygon_outline(point_list,arcade.color.BLACK)


point_list=(
    (397,460),
    (460,460),
    (460,480),
    (510,480),
    (510,520),
    (460,520),
    (460,515),
    (397,515),
    (397,460))
arcade.draw_polygon_filled(point_list,(197,200,206,255))
arcade.draw_polygon_outline(point_list,arcade.color.BLACK)

point_list=(
    (460,480),
    (510,480),
    (510,465),
    (460,465))
arcade.draw_polygon_filled(point_list,(146,76,67,255))
arcade.draw_polygon_outline(point_list,arcade.color.BLACK)

arcade.draw_rectangle_filled(487,470,10,10,(199,193,195,255))
arcade.draw_rectangle_outline(487,470,10,10,(199,193,195,255))


arcade.draw_rectangle_filled(463,470,5,5,(77,60,66,255))
arcade.draw_rectangle_outline(463,470,5,5,(77,60,66,255))

arcade.draw_rectangle_filled(470,470,3,5,(182,167,183,255))
arcade.draw_rectangle_outline(470,470,3,5,(182,167,183,255))

arcade.draw_rectangle_filled(477,470,5,5,(77,60,66,255))
arcade.draw_rectangle_outline(477,470,5,5,(77,60,66,255))

arcade.draw_rectangle_filled(498,470,5,5,(77,60,66,255))
arcade.draw_rectangle_outline(498,470,5,5,(77,60,66,255))

arcade.draw_rectangle_filled(502,470,3,5,(182,167,183,255))
arcade.draw_rectangle_outline(502,470,3,5,(182,167,183,255))

arcade.draw_rectangle_filled(506,470,5,5,(77,60,66,255))
arcade.draw_rectangle_outline(506,470,5,5,(77,60,66,255))


point_list=(
    (397,460),
    (386,460),
    (386,540),
    (397,540),
    (397,560),
    (407,560),
    (407,460),
    (397,460))
arcade.draw_polygon_filled(point_list,(197,200,206,255))
arcade.draw_polygon_outline(point_list,arcade.color.BLACK)

point_list=(
    (386,460),
    (407,460),
    (407,430),
    (386,430))
arcade.draw_polygon_filled(point_list,(146,76,67,255))
arcade.draw_polygon_outline(point_list,arcade.color.BLACK)
arcade.draw_line(460,515,460,480,arcade.color.BLACK)


#lunchroom roof
arcade.draw_rectangle_filled(434,510,56,20,(154,159,168,255))
arcade.draw_rectangle_outline(434,510,56,20,arcade.color.BLACK)
# arcade.draw_point(406,510,arcade.color.WHITE,5)
# arcade.draw_point(440,510,arcade.color.WHITE,5)
arcade.draw_line(406,510,440,510,arcade.color.BLACK)
arcade.draw_line(440,510,462,520,arcade.color.BLACK)
arcade.draw_line(440,510,462,500,arcade.color.BLACK)



#MAIN ENTRANCE

# arcade.draw_point(387,540,arcade.color.WHITE,5)
# arcade.draw_point(387,540,arcade.color.WHITE,5)
# arcade.draw_point(315,540,arcade.color.WHITE,5)
# arcade.draw_point(315,510,arcade.color.WHITE,5)
# arcade.draw_point(325,510,arcade.color.WHITE,5)
# arcade.draw_point(325,515,arcade.color.WHITE,5)
# arcade.draw_point(325,490,arcade.color.WHITE,5)
# arcade.draw_point(380,490,arcade.color.WHITE,5)
# arcade.draw_point(380,470,arcade.color.WHITE,5)
# arcade.draw_point(325,470,arcade.color.WHITE,5)
# arcade.draw_point(370,490,arcade.color.WHITE,5)
# arcade.draw_point(370,460,arcade.color.WHITE,5)
# arcade.draw_point(385,460,arcade.color.WHITE,5)
# arcade.draw_point(385,515,arcade.color.WHITE,5)
# arcade.draw_point(387,515,arcade.color.WHITE,5)

point_list=(
    (387,540),
    (315,540),
    (315,510),
    (325,510),
    (325,515),
    (387,515))
arcade.draw_polygon_filled(point_list,(197,200,206,255))
arcade.draw_polygon_outline(point_list,arcade.color.BLACK)

point_list=(
    (325,515),
    (325,490),
    (380,490),
    (380,470),
    (386,470),
    (386,515))
arcade.draw_polygon_filled(point_list,(197,200,206,255))
arcade.draw_polygon_outline(point_list,arcade.color.BLACK)

arcade.draw_lrtb_rectangle_filled(380,386,470,460,(146,76,67,255))
arcade.draw_lrtb_rectangle_outline(380,386,470,460,arcade.color.BLACK)

point_list=(
    (325,490),
    (380,490),
    (380,470),
    (325,470))
arcade.draw_polygon_filled(point_list,(146,76,67,255))
arcade.draw_polygon_outline(point_list,arcade.color.BLACK)


for i in range(5):
    arcade.draw_rectangle_filled(333+(10*i),480,5,6,(57,43,56,255))
for i in range(4):
    arcade.draw_rectangle_filled(338+(10*i),480,2,6,(164,146,157,255))

# arcade.draw_point(340,515,arcade.color.WHITE,5)
# arcade.draw_point(365,515,arcade.color.WHITE,5)
# arcade.draw_point(365,460,arcade.color.WHITE,5)
# arcade.draw_point(340,460,arcade.color.WHITE,5)
# arcade.draw_point(342,440,arcade.color.WHITE,5)

point_list=(
    (340,515),
    (365,515),
    (365,460),
    (340,460))
arcade.draw_polygon_filled(point_list,(151,157,178,255))
arcade.draw_polygon_outline(point_list,arcade.color.BLACK)

arcade.draw_lrtb_rectangle_filled(340,342,460,445,(150,122,128,255))
arcade.draw_lrtb_rectangle_outline(340,342,460,445,arcade.color.BLACK)

arcade.draw_lrtb_rectangle_filled(363,365,460,445,(150,122,128,255))
arcade.draw_lrtb_rectangle_outline(363,365,460,445,arcade.color.BLACK)


arcade.draw_rectangle_filled(353,505,30,20,(159,162,176,255))
arcade.draw_rectangle_outline(353,505,30,20,arcade.color.BLACK)

# # arcade.draw_point(352,510,arcade.color.WHITE,5)
# arcade.draw_point(352,500,arcade.color.WHITE,5)
arcade.draw_line(352,510,352,500,arcade.color.BLACK)

arcade.draw_line(338,495,352,500,arcade.color.BLACK)
arcade.draw_line(368,495,352,500,arcade.color.BLACK)

arcade.draw_line(338,515,352,510,arcade.color.BLACK)
arcade.draw_line(368,515,352,510,arcade.color.BLACK)






#urbandale high school SIGN


arcade.draw_lrtb_rectangle_filled(340,365,440,435,(199,199,204,255))
arcade.draw_lrtb_rectangle_outline(340,365,440,435,arcade.color.BLACK)

arcade.draw_lrtb_rectangle_filled(340,342,435,420,(150,122,128,255))
arcade.draw_lrtb_rectangle_outline(340,342,435,420,arcade.color.BLACK)


arcade.draw_lrtb_rectangle_filled(363,365,435,420,(150,122,128,255))
arcade.draw_lrtb_rectangle_outline(363,365,435,420,arcade.color.BLACK)

arcade.draw_lrtb_rectangle_filled(370,397,555,540,(197,200,206,255))
arcade.draw_lrtb_rectangle_outline(370,397,555,540,arcade.color.BLACK)


#main entrance right
arcade.draw_lrtb_rectangle_filled(315,325,510,485,(146,76,67,255))
arcade.draw_lrtb_rectangle_outline(315,325,510,485,arcade.color.BLACK)

#3RD BUILDING

# arcade.draw_point(250,530,arcade.color.WHITE,5)
# arcade.draw_point(315,530,arcade.color.WHITE,5)
arcade.draw_lrtb_rectangle_filled(250,315,530,510,(197,200,206,255))
arcade.draw_lrtb_rectangle_outline(250,315,530,510,arcade.color.BLACK)
#
# arcade.draw_point(315,510,arcade.color.WHITE,5)
# arcade.draw_point(250,510,arcade.color.WHITE,5)
# arcade.draw_point(250,470,arcade.color.WHITE,5)
# arcade.draw_point(265,470,arcade.color.WHITE,5)
# arcade.draw_point(265,465,arcade.color.WHITE,5)
# arcade.draw_point(285,465,arcade.color.WHITE,5)
# arcade.draw_point(285,470,arcade.color.WHITE,5)
# arcade.draw_point(285,470,arcade.color.WHITE,5)
# arcade.draw_point(300,510,arcade.color.WHITE,5)
point_list=(
    (250,510),
    (250,470),
    (265,470),
    (265,465),
    (285,465),
    (285,470),
    (300,470),
    (300,510))
arcade.draw_polygon_filled(point_list,(197,200,206,255))
arcade.draw_polygon_outline(point_list,arcade.color.BLACK)


# arcade.draw_point(250,525,arcade.color.WHITE,5)
# arcade.draw_point(250,555,arcade.color.WHITE,5)
# arcade.draw_point(267,545,arcade.color.WHITE,5)
# arcade.draw_point(280,545,arcade.color.WHITE,5)
# arcade.draw_point(290,545,arcade.color.WHITE,5)
# arcade.draw_point(290,555,arcade.color.WHITE,5)
# arcade.draw_point(310,555,arcade.color.WHITE,5)
# arcade.draw_point(310,525,arcade.color.WHITE,5)

point_list=(
    (250,525),
    (250,555),
    (267,555),
    (267,545),
    (293,545),
    (293,555),
    (310,555),
    (310,525))
arcade.draw_polygon_filled(point_list,(197,200,206,255))
arcade.draw_polygon_outline(point_list,arcade.color.BLACK)

arcade.draw_rectangle_filled(280,545,20,26,(169,174,185,255))
arcade.draw_rectangle_outline(280,545,20,26,arcade.color.BLACK)

# arcade.draw_point(270,558,arcade.color.WHITE,5)
# arcade.draw_point(290,558,arcade.color.WHITE,5)
# arcade.draw_point(280,550,arcade.color.WHITE,5)
# arcade.draw_point(280,540,arcade.color.WHITE,5)

arcade.draw_line(280,550,280,540,arcade.color.BLACK)
arcade.draw_line(270,558,280,550,arcade.color.BLACK)
arcade.draw_line(290,558,280,550,arcade.color.BLACK)
arcade.draw_line(270,532,280,540,arcade.color.BLACK)
arcade.draw_line(290,532,280,540,arcade.color.BLACK)

#libary face of 3rd building
# arcade.draw_point(285,460,arcade.color.WHITE,5)
# arcade.draw_point(292,450,arcade.color.WHITE,5)
# arcade.draw_point(292,440,arcade.color.WHITE,5)
# arcade.draw_point(300,440,arcade.color.WHITE,5)
arcade.draw_lrtb_rectangle_filled(285,300,470,442,(146,76,67,255))
arcade.draw_lrtb_rectangle_outline(285,300,470,442,arcade.color.BLACK)

arcade.draw_lrtb_rectangle_filled(285,292,470,442,(186,187,200,255))
arcade.draw_lrtb_rectangle_outline(285,292,470,442,arcade.color.BLACK)


#STRIPES On 3rd building
# arcade.draw_point(285,460,arcade.color.WHITE,5)
# arcade.draw_point(292,440,arcade.color.WHITE,5)
# arcade.draw_point(285,445,arcade.color.WHITE,5)

arcade.draw_lrtb_rectangle_filled(285,292,460,455,(70,66,73,255))
arcade.draw_lrtb_rectangle_outline(285,292,460,455,arcade.color.BLACK)

arcade.draw_lrtb_rectangle_filled(285,292,455,450,(177,156,164,255))
arcade.draw_lrtb_rectangle_outline(285,292,455,450,arcade.color.BLACK)

arcade.draw_lrtb_rectangle_filled(285,292,450,445,(70,66,73,255))
arcade.draw_lrtb_rectangle_outline(285,292,450,445,arcade.color.BLACK)

arcade.draw_lrtb_rectangle_filled(285,292,445,442,(177,156,164,255))
arcade.draw_lrtb_rectangle_outline(285,292,445,442,arcade.color.BLACK)


#mid of 3rd building
arcade.draw_lrtb_rectangle_filled(265,285,465,440,(146,76,67,255))
arcade.draw_lrtb_rectangle_outline(265,285,465,440,arcade.color.BLACK)

arcade.draw_lrtb_rectangle_filled(272,278,465,440,(195,191,202,255))
arcade.draw_lrtb_rectangle_outline(272,278,465,440,arcade.color.BLACK)

arcade.draw_rectangle_filled(275,445,10,10,arcade.color.BLACK)
for i in range(2):
    arcade.draw_rectangle_filled(267+(2*i),450,1,10,(177,156,164,255))

for i in range(2):
    arcade.draw_rectangle_filled(281+(2*i),450,1,10,(177,156,164,255))

#left of 3rd building



arcade.draw_lrtb_rectangle_filled(250,265,470,442,(146,76,67,255))
arcade.draw_lrtb_rectangle_outline(250,265,470,442,arcade.color.BLACK)

arcade.draw_lrtb_rectangle_filled(258,265,470,442,(186,187,200,255))
arcade.draw_lrtb_rectangle_outline(258,265,470,442,arcade.color.BLACK)

arcade.draw_lrtb_rectangle_filled(258,265,460,455,(70,66,73,255))
arcade.draw_lrtb_rectangle_outline(258,265,460,455,arcade.color.BLACK)

arcade.draw_lrtb_rectangle_filled(258,265,455,450,(177,156,164,255))
arcade.draw_lrtb_rectangle_outline(258,265,455,450,arcade.color.BLACK)

arcade.draw_lrtb_rectangle_filled(258,265,450,445,(70,66,73,255))
arcade.draw_lrtb_rectangle_outline(258,265,450,445,arcade.color.BLACK)

arcade.draw_lrtb_rectangle_filled(258,265,445,442,(177,156,164,255))
arcade.draw_lrtb_rectangle_outline(258,265,445,442,arcade.color.BLACK)


# #2nd building


# arcade.draw_point(250,525,arcade.color.WHITE,5)
# arcade.draw_point(225,525,arcade.color.WHITE,5)
# arcade.draw_point(225,540,arcade.color.WHITE,5)
# arcade.draw_point(180,540,arcade.color.WHITE,5)
# arcade.draw_point(180,525,arcade.color.WHITE,5)
# arcade.draw_point(160,525,arcade.color.WHITE,5)
# arcade.draw_point(250,510,arcade.color.WHITE,5)

point_list=(
    (250,525),
    (230,525),
    (230,540),
    (180,540),
    (180,525),
    (160,525),
    (160,510),
    (250,510))
arcade.draw_polygon_filled(point_list,(197,200,206,255))
arcade.draw_polygon_outline(point_list,arcade.color.BLACK)


# arcade.draw_point(170,510,arcade.color.WHITE,5)
# arcade.draw_point(240,510,arcade.color.WHITE,5)
# arcade.draw_point(240,480,arcade.color.WHITE,5)
# arcade.draw_point(230,480,arcade.color.WHITE,5)
# arcade.draw_point(240,440,arcade.color.WHITE,5)
# arcade.draw_point(230,490,arcade.color.WHITE,5)
# arcade.draw_point(180,490,arcade.color.WHITE,5)
# arcade.draw_point(180,480,arcade.color.WHITE,5)
# arcade.draw_point(170,480,arcade.color.WHITE,5)




point_list=(
    (170,510),
    (240,510),
    (240,480),
    (230,480),
    (230,490),
    (180,490),
    (180,480),
    (170,480))
arcade.draw_polygon_filled(point_list,(197,200,206,255))
arcade.draw_polygon_outline(point_list,arcade.color.BLACK)

#
# arcade.draw_point(170,480,arcade.color.WHITE,5)
# arcade.draw_point(180,440,arcade.color.WHITE,5)

arcade.draw_lrtb_rectangle_filled(230,240,480,440,(146,76,67,255))
arcade.draw_lrtb_rectangle_outline(230,240,480,440,arcade.color.BLACK)

arcade.draw_rectangle_filled(235,470,5,5,arcade.color.BLACK)

arcade.draw_lrtb_rectangle_filled(170,180,480,440,(146,76,67,255))
arcade.draw_lrtb_rectangle_outline(170,180,480,440,arcade.color.BLACK)

arcade.draw_rectangle_filled(175,470,5,5,arcade.color.BLACK)


#
# arcade.draw_point(240,510,arcade.color.WHITE,5)
# arcade.draw_point(250,490,arcade.color.WHITE,5)


arcade.draw_lrtb_rectangle_filled(240,250,510,490,(146,76,67,255))
arcade.draw_lrtb_rectangle_outline(240,250,510,490,arcade.color.BLACK)
arcade.draw_rectangle_filled(245,503,5,5,arcade.color.BLACK)
arcade.draw_rectangle_filled(245,495,5,5,arcade.color.BLACK)

# arcade.draw_point(160,510,arcade.color.WHITE,5)
# arcade.draw_point(170,490,arcade.color.WHITE,5)

arcade.draw_lrtb_rectangle_filled(160,170,510,490,(146,76,67,255))
arcade.draw_lrtb_rectangle_outline(160,170,510,490,arcade.color.BLACK)
arcade.draw_rectangle_filled(165,503,5,5,arcade.color.BLACK)
arcade.draw_rectangle_filled(165,495,5,5,arcade.color.BLACK)

#1st building
# arcade.draw_point(160,510,arcade.color.WHITE,5)
# arcade.draw_point(160,550,arcade.color.WHITE,5)
# arcade.draw_point(140,550,arcade.color.WHITE,5)
# arcade.draw_point(160,525,arcade.color.WHITE,5)
# arcade.draw_point(80,525,arcade.color.WHITE,5)

arcade.draw_lrtb_rectangle_filled(90,160,525,510,(197,200,206,255))
arcade.draw_lrtb_rectangle_outline(90,160,525,510,arcade.color.BLACK)



#
# arcade.draw_point(160,525,arcade.color.WHITE,5)
# arcade.draw_point(160,555,arcade.color.WHITE,5)
# arcade.draw_point(143,555,arcade.color.WHITE,5)
# arcade.draw_point(143,545,arcade.color.WHITE,5)
# arcade.draw_point(127,545,arcade.color.WHITE,5)
# arcade.draw_point(127,555,arcade.color.WHITE,5)
# arcade.draw_point(110,555,arcade.color.WHITE,5)
# arcade.draw_point(110,525,arcade.color.WHITE,5)



point_list=(
    (160,525),
    (160,555),
    (143,555),
    (143,545),
    (117,545),
    (117,555),
    (100,555),
    (100,525))
arcade.draw_polygon_filled(point_list,(197,200,206,255))
arcade.draw_polygon_outline(point_list,arcade.color.BLACK)


# arcade.draw_point(270,558,arcade.color.WHITE,5)
# arcade.draw_point(290,558,arcade.color.WHITE,5)
# arcade.draw_point(280,550,arcade.color.WHITE,5)
# arcade.draw_point(280,540,arcade.color.WHITE,5)

# arcade.draw_point(170,558,arcade.color.WHITE,5)

arcade.draw_rectangle_filled(130,545,20,26,(169,174,185,255))
arcade.draw_rectangle_outline(130,545,20,26,arcade.color.BLACK)

# arcade.draw_point(120,558,arcade.color.WHITE,5)
# arcade.draw_point(140,558,arcade.color.WHITE,5)
# arcade.draw_point(130,550,arcade.color.WHITE,5)
# arcade.draw_point(130,540,arcade.color.WHITE,5)

arcade.draw_line(120,558,130,550,arcade.color.BLACK)
arcade.draw_line(140,558,130,550,arcade.color.BLACK)
arcade.draw_line(130,550,130,540,arcade.color.BLACK)
arcade.draw_line(120,532,130,540,arcade.color.BLACK)
arcade.draw_line(140,532,130,540,arcade.color.BLACK)

#bottom of 1st building

# arcade.draw_point(160,510,arcade.color.WHITE,5)
# arcade.draw_point(160,470,arcade.color.WHITE,5)
# arcade.draw_point(140,470,arcade.color.WHITE,5)
# arcade.draw_point(140,465,arcade.color.WHITE,5)
# arcade.draw_point(120,465,arcade.color.WHITE,5)
# arcade.draw_point(120,470,arcade.color.WHITE,5)
# arcade.draw_point(100,470,arcade.color.WHITE,5)
# arcade.draw_point(100,510,arcade.color.WHITE,5)

point_list=(
    (160,510),
    (160,470),
    (140,470),
    (140,465),
    (120,465),
    (120,470),
    (100,470),
    (100,510))
arcade.draw_polygon_filled(point_list,(197,200,206,255))
arcade.draw_polygon_outline(point_list,arcade.color.BLACK)

arcade.draw_lrtb_rectangle_filled(120,140,465,440,(146,76,67,255))
arcade.draw_lrtb_rectangle_outline(120,140,465,440,arcade.color.BLACK)

arcade.draw_lrtb_rectangle_filled(127,133,465,440,(195,191,202,255))
arcade.draw_lrtb_rectangle_outline(127,133,465,440,arcade.color.BLACK)

arcade.draw_rectangle_filled(130,445,10,10,arcade.color.BLACK)

for i in range(2):
    arcade.draw_rectangle_filled(122+(2*i),450,1,10,(177,156,164,255))

for i in range(2):
    arcade.draw_rectangle_filled(136+(2*i),450,1,10,(177,156,164,255))


#stripes on  right 3rd building

arcade.draw_lrtb_rectangle_filled(140,160,470,442,(146,76,67,255))
arcade.draw_lrtb_rectangle_outline(140,160,470,442,arcade.color.BLACK)

arcade.draw_lrtb_rectangle_filled(140,147,470,442,(186,187,200,255))
arcade.draw_lrtb_rectangle_outline(140,147,470,442,arcade.color.BLACK)

arcade.draw_lrtb_rectangle_filled(140,147,460,455,(70,66,73,255))
arcade.draw_lrtb_rectangle_outline(140,147,460,455,arcade.color.BLACK)

arcade.draw_lrtb_rectangle_filled(140,147,455,450,(177,156,164,255))
arcade.draw_lrtb_rectangle_outline(140,147,455,450,arcade.color.BLACK)

arcade.draw_lrtb_rectangle_filled(140,147,450,445,(70,66,73,255))
arcade.draw_lrtb_rectangle_outline(140,147,450,445,arcade.color.BLACK)

arcade.draw_lrtb_rectangle_filled(140,147,445,442,(177,156,164,255))
arcade.draw_lrtb_rectangle_outline(140,147,445,442,arcade.color.BLACK)



#stripes on left 3rd building

arcade.draw_lrtb_rectangle_filled(100,120,470,442,(146,76,67,255))
arcade.draw_lrtb_rectangle_outline(100,120,470,442,arcade.color.BLACK)

arcade.draw_lrtb_rectangle_filled(113,120,470,442,(186,187,200,255))
arcade.draw_lrtb_rectangle_outline(113,120,470,442,arcade.color.BLACK)

arcade.draw_lrtb_rectangle_filled(113,120,460,455,(70,66,73,255))
arcade.draw_lrtb_rectangle_outline(113,120,460,455,arcade.color.BLACK)

arcade.draw_lrtb_rectangle_filled(113,120,455,450,(177,156,164,255))
arcade.draw_lrtb_rectangle_outline(113,120,455,450,arcade.color.BLACK)

arcade.draw_lrtb_rectangle_filled(113,120,450,445,(70,66,73,255))
arcade.draw_lrtb_rectangle_outline(113,120,450,445,arcade.color.BLACK)

arcade.draw_lrtb_rectangle_filled(113,120,445,442,(177,156,164,255))
arcade.draw_lrtb_rectangle_outline(113,120,445,442,arcade.color.BLACK)



#stairs at freshman hallway
arcade.draw_lrtb_rectangle_filled(90,100,510,490,(197,200,206,255))
arcade.draw_lrtb_rectangle_outline(90,100,510,490,arcade.color.BLACK)


arcade.draw_lrtb_rectangle_filled(90,100,490,475,(188,197,210,255))
arcade.draw_lrtb_rectangle_outline(90,100,490,475,arcade.color.BLACK)
arcade.draw_rectangle_filled(95,482,10,7,(50,52,79,255))


#baseball doors
# arcade.draw_point(90,525,arcade.color.WHITE,5)
# arcade.draw_point(80,525,arcade.color.WHITE,5)
arcade.draw_rectangle_filled(83,518,14,14,(162,167,177,255))
arcade.draw_rectangle_outline(83,518,14,14,arcade.color.BLACK)
arcade.draw_line(76,525,83,518,arcade.color.BLACK)
arcade.draw_line(76,511,83,518,arcade.color.BLACK)
arcade.draw_line(83,518,90,518,arcade.color.BLACK)

# arcade.draw_point(76,511,arcade.color.WHITE,5)
# arcade.draw_point(90,500,arcade.color.WHITE,5)
arcade.draw_lrtb_rectangle_filled(76,90,511,500,(55,64,94,255))
arcade.draw_lrtb_rectangle_outline(76,90,511,500,arcade.color.BLACK)


#libary entrance
# arcade.draw_point(180,490,arcade.color.WHITE,5)
# arcade.draw_point(180,450,arcade.color.WHITE,5)
# arcade.draw_point(180,420,arcade.color.WHITE,5)
# arcade.draw_point(230,420,arcade.color.WHITE,5)
# arcade.draw_point(230,450,arcade.color.WHITE,5)


arcade.draw_lrtb_rectangle_filled(180,230,450,420,(146,76,67,255))
arcade.draw_lrtb_rectangle_outline(180,230,450,420,arcade.color.BLACK)


for i in range(3):
    arcade.draw_rectangle_filled(184+(4*i),435,2,15,(167,149,154,255))


arcade.draw_rectangle_filled(205,430,20,8,(55,48,68,255))
arcade.draw_rectangle_outline(205,430,20,8,arcade.color.BLACK)

for i in range(3):
    arcade.draw_rectangle_filled(218+(4*i),435,2,15,(167,149,154,255))

for i in range(3):
    arcade.draw_rectangle_filled(199+(6*i),430,3,27,(146,76,67,255))
    arcade.draw_rectangle_outline(199+(6*i),430,3,26,arcade.color.BLACK)

# arcade.draw_point(230,450,arcade.color.WHITE,5)
# arcade.draw_point(230,490,arcade.color.WHITE,5)

arcade.draw_lrtb_rectangle_filled(180,230,490,450,(197,200,206,255))
arcade.draw_lrtb_rectangle_outline(180,230,490,450,arcade.color.BLACK)

arcade.draw_rectangle_filled(205,460,30,30,(152,161,172,255))
arcade.draw_rectangle_outline(205,460,30,30,arcade.color.BLACK)

# arcade.draw_point(205,465,arcade.color.RED,5)
# arcade.draw_point(205,455,arcade.color.RED,5)
# arcade.draw_point(190,475,arcade.color.RED,5)
# arcade.draw_point(220,475,arcade.color.RED,5)
# arcade.draw_point(190,445,arcade.color.RED,5)
# arcade.draw_point(220,445,arcade.color.RED,5)

arcade.draw_line(205,465,205,455,arcade.color.BLACK)
arcade.draw_line(190,475,205,465,arcade.color.BLACK)
arcade.draw_line(220,475,205,465,arcade.color.BLACK)
arcade.draw_line(190,445,205,455,arcade.color.BLACK)
arcade.draw_line(220,445,205,455,arcade.color.BLACK)





#stairs up by change the world U
# arcade.draw_point(300,510,arcade.color.WHITE,5)
# arcade.draw_point(315,510,arcade.color.WHITE,5)
# arcade.draw_point(315,490,arcade.color.WHITE,5)
# arcade.draw_point(310,490,arcade.color.WHITE,5)

arcade.draw_lrtb_rectangle_filled(300,315,510,490,(197,200,206,255))
arcade.draw_lrtb_rectangle_outline(300,315,510,490,arcade.color.BLACK)

# arcade.draw_point(307,490,arcade.color.WHITE,5)
# arcade.draw_point(315,475,arcade.color.WHITE,5)

arcade.draw_lrtb_rectangle_filled(300,315,490,475,(188,197,210,255))
arcade.draw_lrtb_rectangle_outline(300,315,490,475,arcade.color.BLACK)
arcade.draw_rectangle_filled(307,482,15,7,(50,52,79,255))



#above PAC entrance
point_list=(
    (406,390),
    (381,390),
    (381,410),
    (368,410),
    (368,425),
    (381,425),
    (381,445),
    (381,445),
    (406,445))
arcade.draw_polygon_filled(point_list,(197,200,206,255))
arcade.draw_polygon_outline(point_list,arcade.color.BLACK)


point_list=(
    (368,410),
    (381,410),
    (381,368),
    (368,368))
arcade.draw_polygon_filled(point_list,(146,76,67,255))
arcade.draw_polygon_outline(point_list,arcade.color.BLACK)



point_list=(
    (406,390),
    (381,390),
    (381,365),
    (406,365))
arcade.draw_polygon_filled(point_list,(146,76,67,255))
arcade.draw_polygon_outline(point_list,arcade.color.BLACK)

#right of above
point_list=(
    (436,405),
    (436,368),
    (523,368),
    (523,405))

arcade.draw_polygon_filled(point_list,(146,76,67,255))
arcade.draw_polygon_outline(point_list,arcade.color.BLACK)



for i in range(7):
    arcade.draw_rectangle_filled(440+(6*i),379,3,20,(160,131,136,255))

arcade.draw_rectangle_filled(450,425,87,69,(197,200,206,255))
arcade.draw_rectangle_outline(450,425,87,69,arcade.color.BLACK)

point_list=(
    (493,390),
    (523,390),
    (523, 405),
    (533, 405),
    (533, 425),
    (523, 425),
    (523, 435),
    (513, 435),
    (513, 460),
    (493, 460))
arcade.draw_polygon_filled(point_list,(197,200,206,255))
arcade.draw_polygon_outline(point_list,arcade.color.BLACK)

arcade.draw_rectangle_filled(498,373,15,10,arcade.color.BLACK)

point_list=(
    (523,405),
    (523,380),
    (533,380),
    (533,405))

arcade.draw_polygon_filled(point_list,(146,76,67,255))
arcade.draw_polygon_outline(point_list,arcade.color.BLACK)


arcade.draw_point(406,307,arcade.color.WHITE,5)


#GYM/BOTTOM BUILDING

#filling in gaps between weight room
arcade.draw_point(400,300,arcade.color.YELLOW,5)
arcade.draw_rectangle_filled(400,300,40,105,(197,200,206,255))
arcade.draw_rectangle_outline(400,300,40,105,arcade.color.BLACK)


#MAIN GYM
point_list=(
    (395,237),
    (475,237),
    (475,297),
    (395,297))
arcade.draw_polygon_filled(point_list,(197,200,206,255))
arcade.draw_polygon_outline(point_list,arcade.color.BLACK)


point_list=(
    (395,237),
    (395,212),
    (455,215),
    (455,237))
arcade.draw_polygon_filled(point_list,(151,76,67,255))
arcade.draw_polygon_outline(point_list,arcade.color.BLACK)



# arcade.draw_point(470,297,arcade.color.YELLOW,5)


arcade.draw_lrtb_rectangle_filled(455,475,237,215,(146,76,67,255))
arcade.draw_lrtb_rectangle_outline(455,475,237,215,arcade.color.BLACK)
arcade.draw_line(455,237,455,215,(146,76,67,255))


#bottom triangle
point_list=(
    (410,235),
    (410,225),
    (455,230),
    (455,235))

arcade.draw_polygon_filled(point_list,(197,200,206,255))
arcade.draw_polygon_outline(point_list,arcade.color.BLACK)


point_list=(
    (410,225),
    (410,210),
    (455,215),
    (455,230))
arcade.draw_polygon_filled(point_list,(146,76,67,255))
arcade.draw_polygon_outline(point_list,arcade.color.BLACK)


#weight room

arcade.draw_lrtb_rectangle_filled(350,380,350,250,(197,200,206,255))
arcade.draw_lrtb_rectangle_outline(350,380,350,250,arcade.color.BLACK)

point_list=(
    (380,250),
    (380,280),
    (395,280),
    (395,250))
arcade.draw_polygon_filled(point_list,(197,200,206,255))
arcade.draw_polygon_outline(point_list,arcade.color.BLACK)
arcade.draw_line(380,251,380,280,(197,200,206,255))

point_list=(
    (350,250),
    (395,250),
    (395,220),
    (350,220))

arcade.draw_polygon_filled(point_list,(140,115,122,255))
arcade.draw_polygon_outline(point_list,arcade.color.BLACK)

arcade.draw_rectangle_filled(362,230,20,15,(27,48,82,255))

for i in range(4):
    arcade.draw_rectangle_filled(375+(2*i),235,1,29,(169,146,154,255))

arcade.draw_rectangle_filled(390,230,10,20,(27,45,73,255))


#AUX GYM

point_list=(
    (395,310),
    (395,350),
    (475,350),
    (475,310))
arcade.draw_polygon_filled(point_list,(197,200,206,255))
arcade.draw_polygon_outline(point_list,arcade.color.BLACK)

arcade.draw_line(475,355,470,310,(148,157,168,255))

point_list=(
    (460,310),
    (460,365),
    (475,365),
    (475,310))
arcade.draw_polygon_filled(point_list,(197,200,206,255))
arcade.draw_polygon_outline(point_list,arcade.color.BLACK)


point_list=(
    (465,297),
    (395,297),
    (395,310),
    (465,315))
arcade.draw_polygon_filled(point_list,(197,200,206,255))
arcade.draw_polygon_outline(point_list,arcade.color.BLACK)

arcade.draw_triangle_filled(465,315,465,297,470,297,arcade.color.BLACK)

#
arcade.draw_rectangle_filled(480,320,10,20,(121,149,136,255))
arcade.draw_rectangle_outline(480,320,10,20,arcade.color.BLACK)


point_list=(
    (475,310),
    (485,310),
    (485,313),
    (475,313))
arcade.draw_polygon_filled(point_list,(210,214,225,255))
arcade.draw_polygon_outline(point_list,arcade.color.BLACK)


point_list=(
    (475,320),
    (485,320),
    (485,323),
    (475,323))
arcade.draw_polygon_filled(point_list,(210,214,225,255))
arcade.draw_polygon_outline(point_list,arcade.color.BLACK)


point_list=(
    (475,328),
    (485,328),
    (485,331),
    (475,331))
arcade.draw_polygon_filled(point_list,(210,214,225,255))
arcade.draw_polygon_outline(point_list,arcade.color.BLACK)

#PAC ENTRANCE

point_list=(
    (395,350),
    (395,370),
    (406,370),
    (406,390),
    (436,390),
    (436,370),
    (436,350))
arcade.draw_polygon_filled(point_list,(197,200,206,255))
arcade.draw_polygon_outline(point_list,arcade.color.BLACK)







#above PAC ROOF

arcade.draw_rectangle_filled(445,425,30,60,(150,155,164,255))
arcade.draw_rectangle_outline(445,425,30,60,arcade.color.BLACK)
# arcade.draw_point(445,425,arcade.color.WHITE,5)
# arcade.draw_point(445,440,arcade.color.WHITE,5)
# arcade.draw_point(445,410,arcade.color.WHITE,5)
arcade.draw_line(445,440,445,410,arcade.color.BLACK)
arcade.draw_line(430,455,445,440,arcade.color.BLACK)
arcade.draw_line(460,455,445,440,arcade.color.BLACK)
arcade.draw_line(430,395,445,410,arcade.color.BLACK)
arcade.draw_line(460,395,445,410,arcade.color.BLACK)





# arcade.draw_rectangle_outline(200,300,200,200,arcade.color.BLACK)
# arcade.draw_rectangle_filled(200,300,10,150,(159,152,136,255))
# arcade.draw_rectangle_outline(200,300,10,150,arcade.color.BLACK)
# arcade.draw_rectangle_filled(200,300-75,40,5,(159,152,136,255))
# arcade.draw_rectangle_outline(200,300-75,40,5,arcade.color.BLACK)
# arcade.draw_rectangle_filled(200,300+75,40,5,(159,152,136,255))
# arcade.draw_rectangle_outline(200,300+75,40,5,arcade.color.BLACK)
#
# #4th line
# arcade.draw_line(240,375,240,225,arcade.color.YELLOW,1)
# arcade.draw_rectangle_filled(240,375,20,5,(159,152,136,255))
# arcade.draw_rectangle_outline(240,375,20,5,arcade.color.BLACK)
#
#
# arcade.draw_rectangle_filled(240,225,20,5,(159,152,136,255))
# arcade.draw_rectangle_outline(240,225,20,5,arcade.color.BLACK)
#
#
# #5th line
# arcade.draw_line(270,375,270,225,arcade.color.YELLOW,1)
# arcade.draw_rectangle_filled(270,375,20,5,(159,152,136,255))
# arcade.draw_rectangle_outline(270,375,20,5,arcade.color.BLACK)
#
# arcade.draw_rectangle_filled(270,225,20,5,(159,152,136,255))
# arcade.draw_rectangle_outline(270,225,20,5,arcade.color.BLACK)

# arcade.draw_lrtb_rectangle_filled(160,167,500,400,(201,191,185,255))


# arcade.draw_point(500,520,arcade.color.WHITE,5)
# arcade.draw_point(510,540,arcade.color.WHITE,5)

# arcade.draw_point(555,550,arcade.color.WHITE,5)
# arcade.draw_point(100,395,arcade.color.WHITE,5)
# arcade.draw_point(0,180,arcade.color.WHITE,5)
# arcade.draw_point(875,150,arcade.color.RED,5)

# arcade.draw_point(20,100,arcade.color.WHITE,5)
# arcade.draw_point(600,200,arcade.color.WHITE,5)
# # arcade.draw_point(875,190,arcade.color.RED,5)
# arcade.draw_point(870,515,arcade.color.RED,5)
# arcade.draw_point(630,515,arcade.color.RED,5)
# arcade.draw_point(635,255,arcade.color.RED,5)
# arcade.draw_point(640,260,arcade.color.RED,5)
# arcade.draw_point(660,240,arcade.color.RED,5)
# arcade.draw_point(655,235,arcade.color.RED,5)

# arcade.draw_line(630,510,630,270,arcade.color.BLACK,1)
# arcade.draw_point(340,180,arcade.color.RED,5)


# arcade.draw_lrtb_rectangle_filled(320,340,200,180,(201,191,185,255))

# arcade.draw_lrtb_rectangle_filled(80,160,580,560,(201,191,185,255))

# arcade.draw_lrtb_rectangle_filled(555,640,550,200,(201,191,185,255))
# arcade.draw_lrtb_rectangle_filled(80,100,395,190,(201,191,185,255))

#
# (201,191,185,255)
# arcade.draw_lrtb_rectangle_filled(385,395,220,200,(201,191,185,255))


arcade.finish_render()
arcade.run()