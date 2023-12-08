firstcolumn = [1, 6, 11, 16, 21]
secondcolumn = [2, 7, 12, 17, 22]
thirdcolumn = [3, 8, 13, 18, 23]
fourthcolumn = [4, 9, 14, 19, 24]
fifthcolumn = [5, 10, 15, 20, 25]

firstrow = [1, 2, 3, 4, 5]
secondrow = [6, 7, 8, 9, 10]
thirdrow = [11, 12, 13, 14, 15]
fourthrow = [16, 17, 18, 19, 20]
fifthrow = [21, 22, 23, 24, 25]

mapclosed = False

print("to use the map, click on it, than use W, A, S, D to move the highlighter to ther room you want to highlight. this will leave the highlighter on a certain room, and will be helpful as a reminder to come back to that room later. when youre done using the map, press C to close the map, and then press B to go back to exploring the Mansion.")



def getcoords(currentroom):
  if currentroom in firstcolumn:
    c = 52
  elif currentroom in secondcolumn:
    c = 132
  elif currentroom in thirdcolumn:
    c = 212
  elif currentroom in fourthcolumn:
    c = 292
  elif currentroom in fifthcolumn:
    c = 372
  else:
    c = 212


  if currentroom in firstrow:
    r = 70
  elif currentroom in secondrow:
    r = 150
  elif currentroom in thirdrow:
    r = 230
  elif currentroom in fourthrow:
    r = 310
  elif currentroom in fifthrow:
    r = 390
  else:
    r = 230
  return(c, r)

def map(allrooms, currentroom, movpla):
  mapclosed = False
  readonce = "read"
  moverplace = movpla
  import pygame
  import time
  onlyonce = 0
  counter = 0

  pygame.init()

  screen_width = 800
  screen_height = 600

  x = 0
  y = 0


  shortrooms = ['zero', 'entrance', 'art', 'pool', 'dungeon', 'trophy', 'gym', 'bricks', 'rug', 'dark', 'living', 'M. bed', 'S. bed', 'collect', 'library', 'computer', 'draw', 'guitar', 'up-down', 'strange', 'basement', 'casino', 'stairwell', 'kitchen', 'closet', 'clowns']







  coords = getcoords(currentroom)
  c = coords[0]
  r = coords[1]



  screen = pygame.display.set_mode((screen_height, screen_width))

  text_font = pygame.font.SysFont("arial", 12)

  def draw_text(text, font, text_col, x, y):

    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

  bigmap = pygame.Rect((25, 25, 400, 400))
  movx = getcoords(moverplace)[0] - 29
  movy = getcoords(moverplace)[1] - 47


  mover = pygame.Rect((movx, movy, 84, 84))

  roomone = pygame.Rect((27, 27, 76, 76))
  roomtwo = pygame.Rect((107, 27, 76, 76))
  roomthree = pygame.Rect((187, 27, 76, 76))
  roomfour = pygame.Rect((267, 27, 76, 76))
  roomfive = pygame.Rect((347, 27, 76, 76))

  roomsix = pygame.Rect((27, 107, 76, 76))
  roomseven = pygame.Rect((107, 107, 76, 76))
  roomeight = pygame.Rect((187, 107, 76, 76))
  roomnine = pygame.Rect((267, 107, 76, 76))
  roomten = pygame.Rect((347, 107, 76, 76))

  roomeleven = pygame.Rect((27, 187, 76, 76))
  roomtwelve = pygame.Rect((107, 187, 76, 76))
  roomthirteen = pygame.Rect((187, 187, 76, 76))
  roomfourteen = pygame.Rect((267, 187, 76, 76))
  roomfifteen = pygame.Rect((347, 187, 76, 76))

  roomsixteen = pygame.Rect((27, 267, 76, 76))
  roomseventeen = pygame.Rect((107, 267, 76, 76))
  roomeighteen = pygame.Rect((187, 267, 76, 76))
  roomnineteen = pygame.Rect((267, 267, 76, 76))
  roomtwenty = pygame.Rect((347, 267, 76, 76))

  roomtwentyone = pygame.Rect((27, 347, 76, 76))
  roomtwentytwo = pygame.Rect((107, 347, 76, 76))
  roomtwentythree = pygame.Rect((187, 347, 76, 76))
  roomtwentyfour = pygame.Rect((267, 347, 76, 76))
  roomtwentyfive = pygame.Rect((347, 347, 76, 76))
  cover = pygame.Rect((520, 20, 425, 425))



  playerlocation = pygame.Rect((c, r, 25, 25))





  running = True

  e = (0, 150, 150)
  u = (0, 0, 100)
  mapexpolist = []
  for room in allrooms[0:26]:
    mapexpolist.append(room[1][1])


  #e was 0, 150, 150
  for item in mapexpolist:
    if item == 'e':
      mapexpolist[mapexpolist.index('e')] = (48, 213, 200)
    elif item == 'u':
      mapexpolist[mapexpolist.index('u')] = (0, 0, 100)







  filled = (150, 75, 0)

  while running:

    screen.fill(filled)



    pygame.draw.rect(screen,(255, 255, 255), bigmap)
    pygame.draw.rect(screen,(255, 0, 0), mover)
    pygame.draw.rect(screen,(mapexpolist[1]), roomone)
    pygame.draw.rect(screen,(mapexpolist[2]), roomtwo)
    pygame.draw.rect(screen,(mapexpolist[3]), roomthree)
    pygame.draw.rect(screen,(mapexpolist[4]), roomfour)
    pygame.draw.rect(screen,(mapexpolist[5]), roomfive)
    pygame.draw.rect(screen,(mapexpolist[6]), roomsix)
    pygame.draw.rect(screen,(mapexpolist[7]), roomseven)
    pygame.draw.rect(screen,(mapexpolist[8]), roomeight)
    pygame.draw.rect(screen,(mapexpolist[9]), roomnine)
    pygame.draw.rect(screen,(mapexpolist[10]), roomten)
    pygame.draw.rect(screen,(mapexpolist[11]), roomeleven)
    pygame.draw.rect(screen,(mapexpolist[12]), roomtwelve)
    pygame.draw.rect(screen,(mapexpolist[13]), roomthirteen)
    pygame.draw.rect(screen,(mapexpolist[14]), roomfourteen)
    pygame.draw.rect(screen,(mapexpolist[15]), roomfifteen)
    pygame.draw.rect(screen,(mapexpolist[16]), roomsixteen)
    pygame.draw.rect(screen,(mapexpolist[17]), roomseventeen)
    pygame.draw.rect(screen,(mapexpolist[18]), roomeighteen)
    pygame.draw.rect(screen,(mapexpolist[19]), roomnineteen)
    pygame.draw.rect(screen,(mapexpolist[20]), roomtwenty)
    pygame.draw.rect(screen,(mapexpolist[21]), roomtwentyone)
    pygame.draw.rect(screen,(mapexpolist[22]), roomtwentytwo)
    pygame.draw.rect(screen,(mapexpolist[23]), roomtwentythree)
    pygame.draw.rect(screen,(mapexpolist[24]), roomtwentyfour)
    pygame.draw.rect(screen,(mapexpolist[25]), roomtwentyfive)

    pygame.draw.rect(screen, (255, 255, 0), playerlocation)

    pygame.draw.rect(screen, (filled), cover)





    if onlyonce == 0:

      roomnum = 0
      roomnumlist = []
      for item in mapexpolist:
        if item == (48, 213, 200):

          roomnumlist.append(roomnum)
        roomnum = roomnum + 1

      for item in roomnumlist:
        normalcoords = getcoords(item)
        namecoordx = (normalcoords[0] - 22)
        namecoordy = (normalcoords[1] - 25)



        draw_text(shortrooms[item], text_font, (filled),namecoordx, namecoordy) 















    key = pygame.key.get_pressed()

    if key[pygame.K_a] == True:
      mover.move_ip(-80, 0)
      time.sleep(.2)
      moverplace = moverplace - 1
      counter = 0

    elif key[pygame.K_d] == True:
        mover.move_ip(80, 0)
        time.sleep(.2)
        moverplace = moverplace + 1
        counter = 0

    elif key[pygame.K_w] == True:
      mover.move_ip(0, -80)
      time.sleep(.2)
      moverplace = moverplace - 5
      counter = 0





    elif key[pygame.K_s] == True:
      mover.move_ip(0, 80)
      time.sleep(.2)
      moverplace = moverplace + 5
      counter = 0

    elif key[pygame.K_c] == True:
      #if map in certain location or if mapclosed = false
      if mapclosed == False:
        time.sleep(.5)
        cover.move_ip(-500, 0)
        time.sleep(.5)
        mapclosed = True
      else:
        print("the map is already closed")

      pygame.display.update()
      #time.sleep(.5)

    elif key[pygame.K_b] == True:
      if mapclosed == True:

        print("you put away your map. you can update it again later.")
        return moverplace
      else:
        if readonce == "read":
          print("you need to close the map first. to do this, press c.")
          readonce = "done"


    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

    pygame.display.update()

    if counter == 0:
      counter = 1
  pygame.quit()
