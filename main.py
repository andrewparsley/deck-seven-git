import random
import time
twotwolocked = True
metupdownman = False
fourdigit = random.randrange(1000, 9999)
#print("the password is", fourdigit)
moverplace = 13
foundcouch = False
allrooms = [ 
  ['nothing here zero room', [0, 'u', 0]],
  ['Grand Entrance', [1, 'u', 0]], 
  ['art room', [2, 'u', 0], 'flying monkey', 'yellow key'],
  ['pool hall', [3, 'u', 0], 'lamp', 'small silver key'], 
  ['dungeon', [4, 'u', 0], 'cage'], 
  ['trophy room', [5, 'u', 0], 'whetstone', 'thick winter jacket'], 
  ['private home gym', [6, 'u', 0], 'red pouch'], 
  ['room with the brick walls', [7, 'u', 0], 'cyclops', 'blue key', 'gun'], 
  ['room with the black diamond patterned rug', [8, 'u', 0], 'rug'], 
  ['dark, dusty room', [9, 'u', 0]], 
  ['living room', [10, 'u', 0], 'couch'], 
  ['master bedroom', [11, 'u', 0], 'wooden chest'], 
  ['small bedroom', [12, 'u', 0], 'demon', 'green, bubbly potion', 'viking helmet'], 
  ['collectors room', [13, 'u', 0], 'box of bullets'], 
  ['Library', [14, 'u', 0], 'goblin', 'chocolate chip cookie', 'elder wand'], 
  ['computer room', [15, 'u', 0], 'yellow locker'], 
  ['drawing room', [16, 'u', 0], 'vampire', 'captain america shield', 'lemon meringue pie', 'purple pouch'], 
  ['guitar room', [17, 'u', 0]], 
  ['upside down room', [18, 'u', 0], 'upside down man'], 
  ['strange room', [19, 'u', 0]], 
  ['haunted basement', [20, 'u', 0], 'table'], 
  ['casino', [21, 'u', 0], 'card dealer'], 
  ['haunted stairwell', [22, 'u', 0]], 
  ['kitchen', [23, 'u', 0], 'club sandwich'], 
  ['supply closet', [24, 'u', 0]], 
  ['area with lots of clown paintings', [25, 'u', 0], 'clown painting'],
  ['Devils private quarters', [26, 'u', 0], 'devil', 'cooked bladderfish', 'figurine'], 
  ['middle of the long corridor', [27, 'u', 0]], 
  ['end of the long corridor', [28, 'u', 0]], 
  ['gates of hell', [29, 'u', 0]], 
  ['the pathway leading away from hell, towards earth', [30, 'u', 0]]
]
#continue adding items to the expand function
name = input("what is your characters name? ")
print(" ")
print(" ")
print("________________________________________")
print(" ")
print(" ")
player = [name,'health:', 25,'defense:', 0, 'coins', 10, 'empty', 'empty', 'empty', 'empty','empty','empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty',]

def startingmessage(): 
  print ("several months ago, your brother made a deal with the devil himself. he signed over his soul in exchange for riches, fame, and success.")
  print("Rick was supposed to live out his days on earth as a famous rockstar, and go to hell and the end of his long and happy life. however, it didnt take long for the devil to grow impatient. he wanted Ricks soul NOW.")
  print(" ")
  print("one day, the devil decieded he'd had enough. he reached up through the realms and grabbed your brother, before pulling him down to his home in hell. in doing so, the devil had breached the contract, rendering it null and void, but who can expect the devil to play fair?")
  print(" ")
  print("with the contract out of the way, the devil had no right to keep your brother in hell, and if he were to somehow ever escape, the devil would be powerless to pull him back. unfortunatley, as long as your brother was physicaly down in hell, there was nothing the powers that be could do to rescue him.")
  print(" ")
  print("you prayed and prayed for months with no results, until finally, God responded to you. he told you that the devil had reigns over all of hell, and that there was nothing God could do to take your brother back out. the only powers God had in that regard were sending people TO hell, not taking them out. God told you he was sorry, but there was nothing you could do.")
  print(" ")
  print("suddenly, you had an idea. 'send me down.' you said. God looked at you as if you were crazy. 'I mean it. send me down to hell. Ill find my brother and rescue him, and together we will find a way to escape back to earth.' God considered this. he told you it was risky, and that if you couldnt find an escape route, then both of you would be trapped in hell forever.")
  print(" ")
  print("after some time, God understood just how committed you were to saving your brother.'okay.' he said. 'there might possibly be a way out of hell, but ive never been down there myself, so i really cant say for certain whether this is true or not. down in hell, the devil lives in a great big mansion.")
  print(" ")
  print("according to ancient legend, somewhere hidden in the devils mansion, is a secret magical corridor leading from hell to earth. as the story goes, the devil rarely ever uses it. but honestly, all of that might be a myth, there no way of knowing for sure.'") 
  print(" ")
  print("you tell god that you'll take the chance, and once again ask him to send you to hell. God looks at you with admiration. 'you're a good man. I wish you the best of luck. I am going to damn you to hell, so that you can find your brother. Ill make sure when you get there that you appear right in the entrance way of the devils mansion.") 
  print(" ")
  print("and, ill make you a promise: if you and your brother make it back to earth, you come and tell me everything you saw down there. its very valuable information to me. you do that, and I can gaurentee that both you and your brother will have tickets into heaven when you die. deal?' you tell God you will absolutely take that deal.") 
  print(" ")
  print("God tells you to brace yourself, and in a few short seconds, you feel the ground cave undeneath your feet, and suddenly, you are free falling, into the depths of hell. ")


def instructions(): 
  print("here are the instructions for the game.")
  print(" ")
  print("NORTH, SOUTH, EAST, or WEST: type any of these words to move from room to room in the devils mansion.")
  print(" ")
  print("EXPLORE: explore the room youre currently in. this will let you see what is in the room.")
  print(" ")
  print("NAME OF SOMETHING IN THE ROOM: after you explore the room, you will have a list of things in the room. typing the name of any of these things will let you interact with it. sometimes, interacting with something in the room will let you pick it up and add it to your inventory. other times, it will ask additional questions about what you would like to do next.")
  print(" ")
  print("INVENTORY: typing inventory will let you see your health, defense, and any items you are carrying.")
  print(" ")
  print("CHECK ITEM: typing this lets you check a certain item, and get more information on it.")
  print(" ")
  print("MAP: typing this will bring up the map. the map will show you which room youre currently in, as well as which rooms you have explored so far. to use the map, click on it. you will notice a red circle on the map. once you click on the map, you can move this red circle using W, A, S, or D. move the red circle to a room you want to come back to later, and the next time you open the map, the location of the red circle will serve as a reminder. to close the map and go back to exploring, first press C. if this doesnt work, make sure you have clicked on the map, and are not typing in the text box down below. after you close the map, press B to go back to exploring the mansion. the whole map function does work, however, i have found in my personal expierence that it is a pain to use. you have to drag the window down so you can see it, but then you cant see as much of the textbox. youre welcome to use it if you like, but have personally found that its not worth the hassle. its also very laggy, which I cant do anything about.")
  print(" ")
  print("sometimes, the game will ask you questions. read them carefully. most of them require a yes or no response, but sometimes they will require your response to be a number. in these case, make sure your answer is a number, and does not contain any letters of other special characters. sometimes, entering a certain room will ask you a question right away, so make sure you always read what happens in the game before you type your next action.")
  print(" ")
  print("in every other circumstance where the game asks you a question, it give you choices to pick from, so it is pretty easy to understand.")
  print(" ")
  print("HEAL: typing heal lets you use a healing item, if you have any in your inventory.")
  print(" ")
  print("to read this message again at any point during the game, type HELP. all of the commands in this message must be typed in lowercase.")



travelanywhere = [7, 8, 9, 12, 13, 14, 17, 18, 19]
farleftrooms = [1, 6, 11, 16, 21, 26, 30]
farrightrooms = [5, 10, 15, 20, 25, 29, 30]
fartoprooms = [1, 2, 3, 4, 5, 26, 28, 29, 30]
farbottomrooms = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
forbiddendirections = ''
#roomdoor = lock or unlocked
'''
theres a big grid the player never sees. each room is assigned a number the player never sees. picture a 5 by 5 grid. moving up or down means room number is plus 5 or minus 5. left and right is plus one or minus one. just need to figure out how to stop the players from moving further then the edge.
'''


currentroom = 1 #starting room
allrooms[currentroom][1][1] = 'e'
num = 0 #change to one to see room numbers

def isnumber(book):
  conclusion = True
  nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
  for char in book:
    if char not in nums:
      conclusion = False
  if conclusion:
    return int(book) + 5
  else:
    return False


#for i in range(100):
#book = input("type something ")
  #print(isnumber(book))



def nomonstersinroom():
  for item in allrooms[currentroom]:
   if item in monsterlist:
     return False
  return True


def locked(box):
  if box == 'blue safe':
    lookingfor = 'blue key'
    loot = 'key with the horned goat head'
    boxtwo = {'blue key': 'unlocked'}
  elif box == 'wooden chest':
    lookingfor = 'small silver key'
    loot = 'flashlight'
    boxtwo = {'small silver key': 'unlocked'}
  elif box == 'yellow locker':
    lookingfor = 'yellow key'
    loot = 'brown pouch'
    boxtwo = {'yellow key': 'unlocked'}
  elif box == 'cage':
    lookingfor = 'rusty brass key'
    loot = 'prisoner'
    boxtwo = {'rusty brass key': 'unlocked'}

  print("the", box, "is locked!")
  keychain = input("what will you use to try and unlock it? ")
  havekey = 'no'
  for item in player:
    if isinstance(item, list):
      if item [0] == keychain:
        verifykey = keychain
        havekey = 'yes'

  if havekey == 'no':
    if keychain == lookingfor:
      print("you dont have a", keychain)
    else:
      print("that didnt work, try something else.")


  if havekey == 'yes':
    if (boxtwo.get(verifykey, 'locked')) == 'unlocked':
      print("you unlocked the", box)
      print("inside, was a", loot)
      print("as soon as you unlocked the", box, ", it dissapered, along with the", lookingfor, "you used to open it.")
      for item in player:
        if isinstance(item, list):
          if item[0] == lookingfor:
            player[player.index(item)] = 'test'
      allrooms[currentroom][allrooms[currentroom].index(box)] = loot
    else:
      print("that didnt work")

def move(currentroom, direction):
  select = 1
  while select == 1:

    #direction = input("which direction do you want to travel? north, east, south, or west?")

    if direction == 'north':
      if currentroom not in fartoprooms:
        print("you have entered the", allrooms[currentroom - 5][num])
        currentroom = currentroom - 5
        if allrooms[currentroom][1][1] == 'u':
          allrooms[currentroom][1][1] = 'e'
        return currentroom
        select = 2
      else:
        print("you can not travel any further north. you are still in the", allrooms[currentroom][num])
        return currentroom

    elif direction == 'east':
      if currentroom not in farrightrooms:

        print("you have entered the", allrooms[currentroom + 1][num])
        select = 2
        currentroom = currentroom + 1
        if allrooms[currentroom][1][1] == 'u':
          allrooms[currentroom][1][1] = 'e'
        return currentroom
      else:
        print("you can not travel any further east. you are still in the", allrooms[currentroom][num])
        return currentroom

    elif direction == 'south':
      if currentroom not in farbottomrooms:
        print("you have entered the", allrooms[currentroom + 5][num])
        select = 2
        currentroom = currentroom + 5
        if allrooms[currentroom][1][1] == 'u':
          allrooms[currentroom][1][1] = 'e'
        return currentroom
      else:
        print("you can not travel any further south. you are still in the", allrooms[currentroom][num])
        return currentroom

    elif direction == 'west':
      if currentroom not in farleftrooms:

        print("you have entered the", allrooms[currentroom - 1][num])
        select = 2
        currentroom = currentroom - 1
        if allrooms[currentroom][1][1] == 'u':
          allrooms[currentroom][1][1] = 'e'
        return currentroom

      else:
        print("you can not travel any further west. you are still in the", allrooms[currentroom][num])
        return currentroom

    elif direction == 'stay':

      print("you decided to stay in the", allrooms[currentroom][num])
      select = 2
  return currentroom

#--------------------------------------------------------------
def story(currentroom, twotwolocked):
  if currentroom == 26:
    if monstersleft() > 0:
      print("its not decorated at all like how thought it might be. judging from all the posters on the wall, the devil is a huge fan of green day. you feel incredibly uneasy being in the bedroom of satan. you remember the sign you saw in the room before: 'to go to earth, travel east.' you think to yourself that theres no reason to be here, and that you should just leave while you have the chance. youre pretty sure you dont need to fight satan in order to escape from hell. suddenly, you hear the sound of breathing, and you realise that the devil is in the room with you. you cant see him, he must be hiding in the shadows, waiting to pounce. you feel like if you were to explore the room carefully you would find him, and you could fight him. ")
  if currentroom == 17:
    print("hanging on all four walls of the room, are lots and lots of guitars, of all colors, shapes and sizes. one guitar in paticular catches your eye: a bright red Epiphone ES-335. in any other circumstance you would be tempted to stop and play it for a while, but right now you are in a rush to save your brother, and you really dont want to stay in any hell longer than you need to.")
  if currentroom == 27:
    print("theres a sign on the wall. it reads: 'to go to earth, travel east.'")

  if currentroom == 28:
    print("it is eerie and quiet. theres cobwebs all over the place up and down the corridor. the air was humid, and the whole corridor smelled musty and stale.")
  if currentroom == 29:
    if ' and ' in player[0]:
      print("the gates of hell are locked. Rick reaches into his hoodie pocket, and shows you a key. as the key sits in his open palm, you both take a closer look at it. it looks likes its made of fire. its color flitters from red, to orange, to yellow in a never ending loop, as its shapes curves and changes, just as the shape of the tip of a flame in a campfire. 'I found this outside of the mansion before i was captured'. Rick said. he fit it into the lock on the gates, and as he turned it, the giant golden gates, along with the fire key, melted away, until there was nothing left but a puddle of thick, golden liquid on the ground.")
      print("'are you ready, my friend?' asked Rick. you told him you were, and you both took a deep breath as you prepared to leave")
      if 29 in farrightrooms:
        deltwentynine = farrightrooms.index(29)
        farrightrooms[deltwentynine] = 'test'
    else:
      print("the gates of hell are locked, and you dont have the key to open it. you try using every weapon you have and all the strength you can muster to break down the gates, but it becomes apparent that they are heavily enchanted, and nothing but the proper key can open them. you can see the pathway to earth through the bars in the gate, and you feel defeated. youre so close to freedom, but it is just outside of your grasp. you tell yourself you cant give up. you were never going to leave without your brother anyway, so you decide to come back here once you find him. maybe he will have some way of opening the gates.")
  if currentroom == 30:
    print("you have found freedom at last. you dove into the depths of hell to save your brother, and you both made it out alive. while you are walking, Rick turns to you and asks:")
    print("'hey, bro, I was just wondering... do you have any suggestions for this game? any critiques, or ideas for cool things that could be added?'")
    print("what is your answer?")
  if currentroom == 21:
    print("in the casino, you see a card dealer sitting alone at a table")
  elif currentroom == 9:
    print("the room was pitch black, you couldnt even see your hands. you thought there might have been something written on the wall, but you couldnt read it.")
    havelight = 'no'
    for item in player:
      if item == 'flashlight':
        havelight = 'yes'
    if havelight == 'yes':
      print("would you like to use your flashlight to look around the room? its very old, you can only use it once before the battery dies.")
      uselight = input("yes or no? ")
      print(" ")
      print(" ")
      print("_________________________")
      print(" ")
      print(" ")
      if uselight != 'yes':
        print("you decide not to use the flashlight right now. in hindsight, you feel like you should have. the flashlight probably wont be useful for anything else.")
      elif uselight == 'yes':
        print("you turn on the flashlight, and illuminate the room. on the back wall, a four digit number is written in bold black lettering. it reads,", fourdigit,". you know this number must be important, and you should probably remember it for later.")
        player[player.index('flashlight')] = 'test'
        print("the flashlight ran out of battery, so you threw it away.")





  elif currentroom == 22:
    if ' and ' in player[0]:
      print("'this should be it. just through these doors, should be the pathway that leads us back to earth.' says Rick. the two of you high five. you're almost free.")
    if twotwolocked:
      print("you see a huge wooden door on the south side of the", allrooms[currentroom][0], ". its locked.")
      twotwolocked = True
      youhavethegoatkey = False
      for item in player:
        if isinstance(item, list):
          if item[0] == 'key with the horned goat head':
            youhavethegoatkey = True
      if youhavethegoatkey:
        print("you pull a key out of your pocket, and admire the the craftmanship that went into making it. its a large cast iron key with an emblem of a goats head on the handle. you have a feeling that it fits the door in front of you, and that it might lead you out of the devils mansion. do you want to try the key in the lock?")
        hauntdoor = input("yes or no? ")
        print(" ")
        print(" ")
        print("________________________________________________________")
        print(" ")
        print(" ")
        if hauntdoor != 'yes':
          print("you decide to leave the door closed for now, and come back later.")
          twotwolocked = True
        elif hauntdoor == 'yes':
          twotwolocked = False
          farbottomrooms[farbottomrooms.index(22)] = 'test'
          for item in player:
            if isinstance(item, list):
              if item[0] == 'key with the horned goat head':
                deletegoat = player.index(item)
                player[deletegoat] = 'test'
                #print(deletegoat, "delete the goat key!!!")
          print("you turn the key in the lock, and with the heavy sound of metal clunking together, the door on the south wall of the room creaks and slowly swings open.")
    return twotwolocked








def expanditem(player):
  for item in player:
    if item in itemlist:
      if item == 'gun':
        j = player.index('gun') 
        player[j] = newgun
      if item == 'sword':
        j = player.index('sword')
        player[j] = newsword
      if item == 'viking helmet':
        j = player.index('viking helmet')
        player[j] = newvikinghelmet
      if item == 'blue key':
        j = player.index('blue key')
        player[j] = newbluekey
      if item == 'small silver key':
        j = player.index('small silver key')
        player[j] = newsilverkey
      if item == 'green, bubbly potion':
        j = player.index('green, bubbly potion')
        player[j] = newgreenbubblypotion
      if item == 'lemon meringue pie':
        j = player.index('lemon meringue pie')
        player[j] = newlemonpie
      if item == 'chocolate chip cookie':
        j = player.index('chocolate chip cookie')
        player[j] = newchocolatechipcookie
      if item == 'captain america shield':
        j = player.index('captain america shield')
        player[j] = newcapshield
      if item == 'thick winter jacket':
        j = player.index('thick winter jacket')
        player[j] = newwintercoat
      if item == 'elder wand':
        j = player.index('elder wand')
        player[j] = newelderwand
      if item == 'key with the horned goat head':
        j = player.index('key with the horned goat head')
        player[j] = newgoatkey
      if item == 'brown pouch':
        player[player.index('brown pouch')] = newbrownpouch
      if item == 'red pouch':
        player[player.index('red pouch')] = newredpouch
      if item == 'purple pouch':
        player[player.index('purple pouch')] = newpurplepouch
      if item == 'yellow key':
        player[player.index('yellow key')] = newyellowkey
      if item == 'rusty brass key':
        player[player.index('rusty brass key')] = newrustybrasskey
      if item == 'club sandwich':
        player[player.index('club sandwich')] = newclubsandwich
      if item == 'temmie armour':
        player[player.index('temmie armour')] = newtemmiearmour
      if item == 'cooked bladderfish':
        player[player.index('cooked bladderfish')] = newbfish






newgun = ['gun', 'shoot', 20, 1, 'the gun ran out of bullets']
newsword = ['sword', 'stab', 15, 3, 'the sword became too dull to attack']
newvikinghelmet = ['viking helmet', 2]
newbluekey = ['blue key', 1]
newgreenbubblypotion = ['green, bubbly potion', 10, 'drank', 'drinking']
newlemonpie = ['lemon meringue pie', 15, 'ate', 'eating']
newchocolatechipcookie = ['chocolate chip cookie', 12, 'ate', 'eating']
newcapshield = ['captain america shield', 4]
newwintercoat = ['thick winter jacket', 4]
newelderwand = ['elder wand', 'cast a curse on', 100, 1, 'the elder wand rejected you, because you are not its true owner']
newsilverkey = ['small silver key', 2]
newgoatkey = ['key with the horned goat head', 3]
newbrownpouch = ['brown pouch', 4]
newredpouch = ['red pouch', 2]
newpurplepouch = ['purple pouch', 3]
newyellowkey = ['yellow key', 4]
newrustybrasskey = ['rusty brass key', 5]
newclubsandwich = ['club sandwich', 22, 'ate', 'eating']
newtemmiearmour = ['temmie armour', 2000]
newbfish = ['cooked bladderfish', 100, 'ate', 'the cooked bladderfish has a small sticker on it, like an apple. it reads: property of the Alterra Corporation. eating']


travellist = ['north', 'east', 'south', 'west', 'stay']
battlelist = ['dodge', 'attack']
useitemlist= ['eat', 'use', 'examine']
roomaction = ['explore', 'unlock']

testingthings = ['expand']

itemlist = ['blue key', 'key with the horned goat head', 'gun', 'sword', 'viking helmet', 'captain america shield', 'thick winter jacket', 'lamp', 'couch', 'table', 'green, bubbly potion', 'chocolate chip cookie', 'club sandwich','lemon meringue pie', 'elder wand', 'card dealer', 'clown painting', 'blue safe', 'wooden chest', 'small silver key', 'brown pouch', 'red pouch', 'purple pouch', 'yellow locker', 'yellow key', 'flashlight', 'rug', 'padlock', 'whetstone', 'box of bullets', 'cage', 'rusty brass key', 'prisoner', 'upside down man', 'temmie armour', 'cooked bladderfish', 'figurine']

weapon = ['sword', 'gun', 'elder wand']

armour = [['viking helmet', 1], ['captain america shield', 1], ['thick winter jacket', 1], ['temmie armour', 1]]

furniture = ['couch', 'table', 'clown painting', 'blue safe', 'wooden chest', 'yellow locker', 'rug', 'padlock', 'whetstone', 'box of bullets', 'cage', 'lamp', 'figurine']

lockedthings = ['blue safe', 'wooden chest', 'yellow locker', 'cage']

key = ['blue key', 'key with the horned goat head', 'small silver key', 'yellow key', 'rusty brass key']

coinpouch = ['brown pouch', 'red pouch', 'purple pouch']

misclist = ['options', 'inventory', 'check item'] #item stats

monsterlist = ['cyclops', 'goblin', 'demon', 'vampire', 'flying monkey', 'devil']

healingitems = ['green, bubbly potion', 'chocolate chip cookie', 'club sandwich', 'lemon meringue pie', 'cooked bladderfish']

reloaders = ['whetstone', 'box of bullets'] # cant be picked up, stays there. [whetstone, sword] examining the whetstone checks if you have a sword, asks if you want to sharpen your sword, then, changes sword[2] to 6 or something. sharpening your sword means giving it more uses. same with the gun and the bullets.

extraitems = ['flashlight']

pickuplist = [weapon, healingitems, armour, key, coinpouch, extraitems]

people = ['card dealer', 'prisoner', 'upside down man']

def heal():
  elselect = 0
  for item in player:
    if isinstance(item, list):
      if item[0] in healingitems:
        elselect = 1
  if elselect == 0:
    print("you dont have any healing items")
  else:
    healquestion = input("which healing item would you like to use? ")

    print(" ")
    print("______________________________")
    print(" ")

    burt = 0
    for item in player:
      if isinstance(item, list):

        if item[0] == healquestion:

          if healquestion in healingitems:
            print("you", item[2], "the", item[0], ". it gave you", item[1], "health")
            player[2] = player[2] + item[1]
            turf = player.index(item)
            player[turf] = 'test'
            burt = 1
    if burt == 0:
      print("you dont have a", healquestion)

def pickupable(item):
  done = 0
  for section in pickuplist:
    for stuff in section:
      if isinstance(stuff, list):
        for thing in stuff:
          if thing == item:

            done = 1
            return True
      else: 
        if stuff == item  :
          done = 1
          return True


  if done == 0:
    return False



def damageplayertakes(player, enemy):
  playerdefense = player[4]
  monsterattack = enemy[2]
  dice = random.randrange(-1,2)
  saved = player[4] * 0.5
  finalpdamage = (monsterattack + dice) - saved
  return finalpdamage

  #test. this will just return values



def damagemonstertakes(enemy, WOC):
  initial = WOC[2]

  dice = random.randrange(-1,2)
  finalmdamage = initial + dice
  return finalmdamage





def checkhowmany(player):
  answer = 0
  for item in player:
    if isinstance(item, list):
      if item[0] in weapon:
        answer = answer + 1
  return answer

#-------------------------BATTLE------------------------------










#monster template: name, health, normal damge they do(influenced by player aurmor and a dice roll)
def battle(player, enemy):
  howmanyweapons = 0
  fightchoice = ''
  if enemy == 'cyclops':
    enemy = ['cyclops', 25, 10]
  elif enemy == 'goblin':
    enemy = ['goblin', 20, 8]
  elif enemy == 'demon':
    enemy = ['demon', 19, 9]
  elif enemy == 'vampire':
    enemy = ['vampire', 30, 7]
  elif enemy == 'flying monkey': 
    enemy = ['flying monkey', 15, 7]
  elif enemy == 'devil':
    enemy = ['devil', 150, 1013]#health, than damage. with full armour, 10 damage

  #the weak monsters have armour behind them, you cant fight them with full armour because you need to beat them to get the armour. the stronger monsters are always accessable, but you shouldnt fight them when you dont have much defense, because you will lose. when you leave a fight and come back, the monster goes back to full health. i will keep that. it will say that in the instructions



  for item in player:
    if isinstance(item, list):
      for info in item:
        if info in weapon:
         howmanyweapons = howmanyweapons + 1
  while enemy[1] > 0 and fightchoice != 'surrender' and player[2] > 0:
    if howmanyweapons == 1:
      print("you have", player[2], "health, and", player[4], "defense. you have", howmanyweapons, "weapon.")
      print(" ")
      print("the", enemy[0], "has", enemy[1], "health.")
      print("the", enemy[0], "deals between", enemy[2] - 1, "and", enemy[2] + 1, "damage with each hit, if you dont have any armour on.")
      print(" ")
    elif howmanyweapons > 1:
      print("you have", player[2], "health, and", player[4], "defense. you have", howmanyweapons, "weapons.")
      print(" ")
      print("the", enemy[0], "has", enemy[1], "health.")

      print("the", enemy[0], "deals between", enemy[2] - 1, "and", enemy[2] + 1, "damage with each hit if you dont have any armour on")
      print(" ")


    set = 0
    #monsterchoice = random.randrange(0,2)
    monsterchoice = 0
    #0 means attack, 1 means dodge, because 1 sounds like run
    things = ['attacked', 'dodged']
    while set == 0:
      fightchoice = input('do you want to attack, dodge, heal, or surrender? ')
      print(" ")
      print(" ")
      print("____________________________")
      print(" ")
      print(" ")


      if fightchoice == 'heal':
        heal()

      elif fightchoice == 'attack':
        set = 1
        playerchoice = 0

        if howmanyweapons > 0:
          selection = 0
          while selection == 0:
            whatweapon = input("which weapon will you use? if none of your weapons are useable, type fists. ")
            print(" ")
            print(" ")
            print("___________________________")
            print(" ")
            print(" ")
            if whatweapon == 'fists':
              fists = ["fists","punch", 1, 100, "punched", "you ran out of punching energy"]
              weaponofchoice = fists
              addfists = 0
              for item in player:
                if item == 'empty':
                  if addfists == 0:
                    player[player.index(item)] = fists
                    addfists = 1


              selection = 1
            if whatweapon in weapon:
              #print("thats a valid weapon")
              for item in player:
                if isinstance(item, list):
                  if item[0] == whatweapon:
                    if item[3] != 0:
                      #print("thats a weapon and you have it")
                      selection = 1
                      weaponofchoice = item
                      #print("WOC is", weaponofchoice)
                    else:
                      print(item[4])

                    #result = damagemonstertakes(enemy, weaponofchoice) #this will be a list of info that we can use like result[1]
              if selection == 0:
                print("you dont have a", whatweapon)



        else:
          print("you dont have any weapons. you cant do any damage to the monster, but you try anyway. you should surrender.") #take damage, dont do any damage. loop restarts and they have a chance to surrender. if monster attacked, call the damage player takes function



      elif fightchoice == 'dodge':
        set = 1
        dodgemessage = random.randrange(1,3)
        if dodgemessage == 1:
          print("the", enemy[0], "took a huge swing at you, but you manage to dodge it. youre glad you moved, that looked like it would have hurt.")
        else:
          print("the", enemy[0], "winds up to wallop you, but ends up swinging thier fist in your direction rather weakly. you dodge out of the way. that didnt look like it would have hurt that much.")
        playerchoice = 1
      elif fightchoice == 'surrender':
        set = 1
        print("you have chosen to leave the", allrooms[currentroom][0], "and explore the next room over.")
        return 'surrender'

    #print("you", things[playerchoice])
    #print("the", enemy[0], things[monsterchoice])


    if monsterchoice == 0 and playerchoice == 0: 

      pdamage = damageplayertakes(player, enemy)
      if howmanyweapons != 0:
        mdamage = damagemonstertakes(enemy, weaponofchoice)
      else:
        mdamage = 0
      print("the", enemy[0], "attacks you, and deals", pdamage, "damage")
      print(" ")
      print("you", weaponofchoice[1], "the", enemy[0], "with your", weaponofchoice[0], ", and deal", mdamage, "damage")
      print(" ")
      enemy[1] = enemy[1] - mdamage
      player[2] = player[2] - pdamage
      bobert = player.index(weaponofchoice)
      player[bobert][3] = player[bobert][3] - 1
      if player[bobert][3] < 1:
        print(player[bobert][4])
      for item in player:
        if isinstance(item, list):
          if item[0] == "fists":
            player[player.index(item)] = 'empty'
      #print("BOBERT IS", bobert)
      if enemy[1] < 1:
        return 'win'
      #print(player)
      #print(enemy)
    #number of uses on weapon goes down
    #cant use weapon if its empty






#-------------------------------------------------------------



#explore will give story about the room, and list the items in the room. it will say: safe, lamp, table. if you type table, it will say 'there is nothing unordinary about the table.' if you type lamp, it might say 'there is a key hidden in the lamp.' if you type safe, it might say ' you need a key to open the safe. if you type unlock, it will ask which key, and what item. you need to already know the items. if you dont know theres a safe, typing unlock will ask what to unlock, and you wont know what to type.

typedlettercount = ''
didiwinthegame = 'no'
startingmessage()
print(" ")
print(" ")
instructions()

def monstersleft():
  monstersleftcount = 0 #should be 0.
  for room in allrooms:
    for item in room:
      if item in monsterlist:
        monstersleftcount = monstersleftcount + 1
  return monstersleftcount    #at start of game, total, twill be 6







while player[2] > 1 and didiwinthegame == 'no':

  action = input(" ")
  print(" ")
  print(" ")
  print("_______________________________________")
  print(" ")
  print(" ")
  if currentroom == 30:
    didiwinthegame = 'yes'


  if action in travellist:
    currentroom = (move(currentroom, action))
    istwolocked = story(currentroom, twotwolocked)
    if istwolocked == True:
      twotwolocked = True
    elif istwolocked == False:
      twotwolocked = False

  elif action in roomaction:

    if action == 'explore':
      #print(allrooms[currentroom])
      for enemy in allrooms[currentroom]:

        if enemy in monsterlist:
          selected = 0
          while selected == 0:
            howappearnum = random.randrange(1, 4)
            if howappearnum == 1:
              howappear = ("stepped out of the shadows")
            elif howappearnum == 2:
              howappear = ("dropped down from the ceiling")
            elif howappearnum == 3:
              howappear = ("appeared behind you in the doorway")
            print("while you were looking around the room, a", enemy, howappear, ". they looked violent and bloodthirsty.")
            engagebattle = input("would you like to battle, or leave? ")
            print(" ")
            print("_________________")
            print(" ")
            if engagebattle == 'leave':
              selected = 1
              print("you ran eastward out of the room and explored the room next door")
              currentroom = (move(currentroom, 'east'))

            elif engagebattle == 'battle':
              selected = 1
              quantityweapons = checkhowmany(player)
              if quantityweapons > 0:
                fightoutcome = battle(player, enemy)
              else:
                print("you cant fight the", enemy, ". you dont have any weapons. you decide to run away, and enter the room to the east of the", allrooms[currentroom][0], ".")
                fightoutcome = 'surrender'

              if fightoutcome == 'surrender':
                currentroom = (move(currentroom, 'east'))
              elif fightoutcome == 'win':
                print("you won the battle! The monster gave up and ran out of the mansion, out into the open wasteland of hell. now that the monster is gone, you can help yourself to the loot that they were gaurding!")
                print(" ")



                kit = allrooms[currentroom].index(enemy)
                allrooms[currentroom][kit] = 'test'
                print(" ")
                if monstersleft() == 1:
                  print("that was the last monster!")
                  print("while the", enemy, "was running away from you, trying to get outside, it did not take a straight path to the grand entrance of the mansion. instead, he rampaged through nearly every room, trying to find his way out. through the doorway of the", allrooms[currentroom][0], "you saw him tear a piece of armour off his back, and throw it wildly. he clearly wasnt wearing it correctly. he threw it so hard it went through a couple of walls, and you have no idea which room it ended up landing in. eventually, the", enemy, "found its way to the grand entrance, and ran away from the devils mansion, out into the rest of hell")

                  temroomselect = False
                  while temroomselect == False:
                    temroom = random.randrange(1, 26)
                    if temroom != currentroom:
                      temroomselect = True
                  allrooms[temroom].append('temmie armour')
                  #print("tem room is", temroom)

                elif monstersleft() == 0:
                  if 'and Rick' in player[0]:
                    print("or so you thought. in reality, the Devil had cast an illusion spell, making you halucinate and see things that didnt really happen. while you were in a trance, staring at the door you thought the devil had left through, he had snuck up behind you and tried to stab you in the back with his dagger. luckily, Rick, who had been watching your fight, petrified and too weak from his malnutrition to join, mustered all of the strength that he could, and hit the devil in the knee with a golden fiddle he had found hanging on the wall. the devil was on his last legs after enduring your attacks, and Ricks strike with the golden fiddle was enough to make him fall on his knees and scream. you snap out of your daze, and turn around to see the devil writhing in pain on the ground of his bedroom, as your brother stands over him with a vengeful look in his eye. 'He tortured me for months.' said Rick. 'me and billions of other people. not everyone down here deserves to be down here, you know. there are many innocent souls who he has tricked down here, not to mention the people who have been framed, or the people who have the potential to redeem themselves if given the oppurtunity for rehabilitation.' Rick picks up the dagger up off the floor, and looks over to you, as if he was waiting for your approval. you told him you wouldnt stop him. Rick raises the dagger above his head, and the devil, having been beaten by your attacks already, was too weak to stop him. Rick plunged the dagger into the devils heart, and the devil died rather quickly. now that the devil was only a soul, his power over hell was gone along with his body. with the evil king of the underworld no longer a threat, God and his team of angels up in heaven would be able to seize control over hell, and all of the creatures and humans that lived here, and they would decide what the best thing to do with them was. you knew that while some inhabitants of hell had really earned their spot here during their time on earth, God and the angels of heaven would be much more merciful than the devil was, and the people who might benifit from a second chance would likley recieve one. the devils soul had left the room entirely now, and had floated outside of his mansion to join the rest of the people in hell in their labour and torment. soon enought, what remained of the devils body slowly crumpled into dust, and later, vanished entirely. You and Rick decide to search the rest of the room and see what you could find.")
                  else:
                    print("or so you thought. in reality, the Devil had cast an illusion spell, making you halucinate and see things that didnt really happen. while you were in a trance, staring at the door you thought the devil had left through, he carefully snuck up behind you, and stabbed in the back with his dagger. you had just enough time left before you died to think that maybe if Rick had been with you, he could have helped you fight. than, as you gasped for air, rolling around on the floor, the devil kicked you with the force of a thousand suns, sending you flying into the wall.")
                    player[2] = 0




                #print stats, replace monster with test, so you can explore the rest of the room

              elif fightoutcome == 'lose':
                print("you lost!")
                #if health is less then one, health = 2, and player gets kicked out of room. monsters health goes back to full. or players health goes to full because theres a limited amount of healing items


      numthingsinroom = 0
      itemsinroom = []
      for thing in allrooms[currentroom]:
        if thing in itemlist:
          numthingsinroom  = numthingsinroom + 1
          itemsinroom.append(thing)


      if numthingsinroom == 1: 
        print("there is", numthingsinroom, "thing in the", allrooms[currentroom][0])
        onlyitem = ''
        for item in allrooms[currentroom]:
          if item in itemlist:
            onlyitem = onlyitem + item
        print("you found a", onlyitem)

      elif numthingsinroom > 1:
        print("there are", numthingsinroom, "things in the", allrooms[currentroom][0])


        founditemmessage = ("you found")
        for item in itemsinroom[:-1]:
          founditemmessage = founditemmessage + " a "
          founditemmessage = founditemmessage + item
          founditemmessage = founditemmessage + ","
        founditemmessage = founditemmessage + " and a "
        founditemmessage = founditemmessage + itemsinroom[-1]


        print(founditemmessage)
        #print(allrooms[currentroom])






      else: 

        print("there is nothing interesting in the", allrooms[currentroom][0])


  elif action in itemlist:
    if action in allrooms[currentroom] and nomonstersinroom():
      if pickupable(action): 

        print("you picked up the", action)
        othercount = 0
        for thing in allrooms[currentroom]:
          if thing != action:
            othercount = othercount + 1
          else:

            count = 0
            f = 0
            for slot in player:
              #print (slot)
              if action not in player:
                if slot == 'empty':
                  player[count] = action
                  expanditem(player)

                  for section in armour:
                    for info in section:
                      if action == info:
                        if f == 0:
                          f = 1
                          player[4] = player[4] + player[count][1]



                else:
                  count = count + 1
                  #print(count)
            allrooms[currentroom][othercount] = 'test'


      else:  
        print("you examine the", action)
        if action in furniture:
          if action == 'figurine':
            print("the figurine is about four inches tall. its a red cartoon crab with a gold crown, and a nametag that says 'king Acre, the crab.' it appears to be a character from the devils favourite video game.")
          if action == 'table':
            print("it is a very boring table. theres nothing on it. on one of the legs, you notice a tiny drawing of a ruby colored fish. when you look closer, you realize its a red herring.")
          if action == 'couch':
            if foundcouch == False:
              print("you found a gold coin between the cushions of the couch! you put it in your pocket.")
              player[6] = player[6] + 1
              print("you now have a total of", player[6], "coins!")
              foundcouch = True
            else: 
              print("there is nothing interesting about the couch")
          if action == 'lamp':
            print("once every 20 seconds or so, the lamp flickers off and back on again. its old and dusty. theres nothing useful hidden in or around it.")
          elif action == 'clown painting':
            print("behind one of the clown paintings hanging up, you found a sturdy looking blue safe embedded into the wall.")
            replacewsafe = allrooms[currentroom].index('clown painting')

            allrooms[currentroom][replacewsafe] = 'blue safe'

          elif action == 'rug':
            print("you lifted up the black rug with the diamond pattern, and found a trapdoor underneath. there is a four digit combination padlock keeping it shut.")
            replacewlock = allrooms[currentroom].index('rug')
            allrooms[currentroom][replacewlock] = 'padlock'

          elif action == 'padlock':
            print("the padlock on the trapdoor can be opened by entering the correct four digit combination.")
            phonenumber = False
            while phonenumber == False:
              locktry = (input("what combo will you try? "))
              print(" ")
              print(" ")
              print("____________________________")
              print(" ")
              print(" ")
              if isnumber(locktry):
                locktry = int(locktry)
                phonenumber = True
              else:
                print("that is totally not a number. like, not at all. just for refrence, on most keyboards, the numbers are the ones at the top. hope that helps!")
                break
              if locktry == fourdigit:
                replacewloot = allrooms[currentroom].index('padlock')
                allrooms[currentroom][replacewloot] = 'sword'
                print("you popped off the padlock, opened the trapdoor, and peered inside. underneath the room was a small chamber, about 2 feet deep, and just wide enough to conceal the sword that was hidden inside.")
              else:
                print("that wasnt the right combination")

          elif action == 'whetstone':
            print("this could be useful for sharpening a blade.")
            havesword = False
            swordloc = 'no sword'
            for item in player:
              if isinstance(item, list):
                if item[0] == 'sword':
                  havesword = True
                  swordloc = item
            if havesword:
              print("would you like to sharpen your sword on the whetstone?")
              sharpensword = input("yes or no? ")
              print(" ")
              print(" ")
              print("______________________________")
              print(" ")
              print(" ")
              if sharpensword != 'yes':
                print("you choose not to sharpen your sword right now, which was foolish. but you can come back later.")
              else:
                print("you sharpen your sword on the whetstone.") 
                player[player.index(swordloc)][3] = player[player.index(swordloc)][3] + 5
                for item in allrooms[currentroom]:
                  if item == 'whetstone':
                    allrooms[currentroom][allrooms[currentroom].index('whetstone')] = 'test'
                print("sharpening the blade added an extra five uses to the sword. you can now use it a total of ", player[player.index(swordloc)][3], "times before the blade becomes too dull. as soon as you were done sharpening your sword, the whetstone broke. you cant use it again.")


          elif action == 'box of bullets':
            print("bullets could come in handy for reloading a gun")
            havegun = False
            gunloc = 'no gun'
            for item in player:
              if isinstance(item, list):
                if item[0] == 'gun':
                  havegun = True
                  gunloc = item
            if havegun:
              print("would you like to use the bullets in the box to reload your gun?")
              reloadgun = input("yes or no? ")
              print(" ")
              print(" ")
              print("______________________________")
              print(" ")
              print(" ")
              if reloadgun != 'yes': 
                print("you decide to leave the box of bullets alone, which is foolish. but you can come back later")
              elif reloadgun == 'yes':
                print("you took all six bullets out of the box and put them in your gun.")
                player[player.index(gunloc)][3] = player[player.index(gunloc)][3] + 6
                for item in allrooms[currentroom]:
                  if item == 'box of bullets':
                    allrooms[currentroom][allrooms[currentroom].index('box of bullets')] = 'test'
                    for item in player:
                      if isinstance(item, list):
                        if item[0] == 'gun':
                          numbullets = item[3]
                    print("you can now use your gun a total of", numbullets, "times before it runs out of bullets.")
                    print("there are no more bullets in the box")



          elif action in lockedthings:
            #lockbox = expand(action)
            locked(action)






        if action in people:
          if action == 'upside down man':
            if metupdownman == False:
              print("he looked unlike any other person you had seen before. he was completely upside down, with his feet in the air and his head on the floor, and yet you could tell by the folds in his clothes, and the way they fell upward rather then toward the floor, that he was supporting his weight with his legs and not his neck. it was as if there was an invisible floor above his feet that he was standing on. when he paced around the room, his legs moved just the same as anyone elses, and he moved around the room even though he was seemingly pushing off of nothing, his head just barely dragging along the ground. it almost looked like he was moonwalking.")
              print("he was wearing an orange mask, with big X's for eyes, and a simple curvy smile, illistrated with a single line. he was wearing the mask upside down relative to his own body, so that it was right side up from your perspective. his feet were a little below your eye level, he was just a small bit shorter than you. you decide to talk to him, and you look down to the ground, at his face.")
              print("'hi, sir, I was wondering if you had seen my brother?'the upside down man answered 'no, no, no, I havent seen anyone in months! ive got everything i need in this room right here, I only leave in emergencies, and youre the only person thats come into my room in ages! sorry, buddy, i wish i could help. however, since youre here, let me ask if you would be interested in a deal!'")
            print("the upside down man says to you: 'I found this rusty brass key a little while back, the last time i had to leave my room. i have no idea what it unlocks, but maybe it will help you find your brother?")
            if player[6] < 175:
              print("ill sell it to you for 175 coins!'")
              print("you tell him that you dont have that many coins, and he tells you its no problem, if you want to buy the key you can come back later when you have more money")

            elif player[6] > 174:
              print("ill sell it to you for", player[6], "coins!")
              print("do you want to buy the key?")
              buykey = input("yes or no? ")
              print(" ")
              print(" ")
              print("______________________________")
              print(" ")
              print(" ")
              if buykey != 'yes':
                print(" you decided not to buy the key.")
                print("the upside down man tells you to come back any time if you change your mind.")
              elif buykey == 'yes':
                print("you agree to buy the key, and you give him", player[6], "coins. 'delightful!' said the upside down man. 'its on the nightstand next to my bed, help yourself!' you look up to the nightstand, which is sitting on the ceiling rather then the floor, and see a rusty brass key sitting on it. it looks like it should fall, but the gravity in this room is pulling it up instead of down.")
                print("the upside down man says to you: 'its been great talking to you, and thank you for the coins, but I think im going to go to bed now, im tired. please dont talk to me anymore, so that i can sleep peacefully.' you agree, and tell him goodnight")
                player[6] = 0
                replacewbrasskey = allrooms[currentroom].index("upside down man")
                allrooms[currentroom][replacewbrasskey] = "rusty brass key"




            metupdownman = True



          if action == 'prisoner':
            print("you called out to the prisoner, and as they stepped out of the corner of the dungeon and into the light, you saw that it was your brother, Rick!")
            print("you are both relieved to see each other. Rick tells you he knows the way out of the mansion. he tells you:") 
            print("'through the door on the south wall of the haunted stairwell is the exit out of hell! if we make it there, we can escape!'")
            print("Rick is weak from being trapped in a cage for so long, so you lead the way, as you and your brother attempt to navigate to the exit from hell.")
            prisonerloc = allrooms[currentroom].index('prisoner')
            allrooms[currentroom][prisonerloc] = 'test'
            player[0] = player[0] + ' and Rick'

          if action == 'card dealer':
            print("the card dealer smiles as you approach his table. 'well, hello there,", player[0], "!' he cries. 'what a joy it is to see you, its been so long since ive had someone to play blackjack with!'")

            if player[6] < 10:
              print("the card dealer looks you up and down, than exclaims; 'you dont have enough money,", player[0],"! I cant gamble with you if you dont have any money! this game is a 10 coin buy-in, and you only have", player[6], "coins. tell you what, why dont you come back to my casino later when you find more cash, then you and I can have some fun!' you leave the dealers table, and hear him cackling as you walk away." )
            else:
              print("the card dealer looks you up and down, then says in a cool and calm voice; 'this game of blackjack has a 10 dollar buy-in, and it looks like you have just enough.' you have no idea how he knows that, or how he knew your name. hes starting to creep you out.")
              print("the card dealer, who looked almost human, but not quite, appeared as if he was growing more impatient and excited by the minute.'well?' he hissed. 'what will it be? would you like to gamble those hard earned coins away, in the hopes of winning big?'")
              cardrequest = input("are you in for a game of blackjack? yes or no ")
              print(" ")
              print(" ")
              print("__________________________________")
              print(" ")
              print(" ")
              if cardrequest == 'no':

                print("the card dealer looked disappointed.'pity.' he said, as he slumped back in his chair. 'come again if you change your mind.' you walk away from the table, back to the middle of the casino.")
              elif cardrequest == 'yes':
                print("a look of glee flashed across the face of the man sitting before you. his eyes went black, and long antennas grew out of his head, his face was changing as if he was revealing his true self.")
                print("his eyes continued to get bigger and blacker, his cheekbones became narrower, until he became a creture with the body of a man and the head of some sort of insect.")
                print("'excellent. have a seat,", player[0], ", and lets begin.'you had a bad feeling that the insect monster was going to win all of your coins away from you.")
                import jackblack
                endgame = jackblack.cardgame(player[6], player[0])
                #print(endgame, "endgame")
                player[6] = endgame
                print("you exited the blackjack table with", player[6], "coins")




    else:
      if nomonstersinroom():
        print("there is no", action, "in the", allrooms[currentroom][0])
      else:
        print("you have to fight the monster first")


  elif action in misclist:
    if action == 'inventory':
      yourthings = []
      for slot in player[:]:
        if isinstance(slot, list):
          slot = slot[0]
        if slot != 'empty' and slot != 'test':
          yourthings.append(slot)
      print("your name is", yourthings[0])
      print (yourthings[1:7])
      print("your items are:", yourthings[7:])
      #print(player)




    elif action == 'check item':
      checkwhichitem = input("which item do you want to check? ")
      print(" ")
      print(" ")
      print("______________________________")
      print(" ")
      print(" ")
      found = 'no'
      if checkwhichitem == 'flashlight':
        print("this flashlight could come in handy for seeing hidden things in dark spaces")
      if checkwhichitem == 'coin' or checkwhichitem == 'coins':
        print("you have", player[6], "coins")
        found = 'yes'

      for item in player:
        if isinstance(item, list):
          if item[0] == checkwhichitem:

            print("you have one", checkwhichitem, "in your inventory")
            found = 'yes'

            for bunch in weapon:

              if checkwhichitem == bunch:
                print("the", checkwhichitem, "is a weapon")
                print("it does between", item[2] - 1, "and", item[2] + 1, "damage, depending on aim.")
                print("you can use it", item[3], "more times before you will discover", item[4])

            for bunch in armour:
              for thing in bunch:
                if checkwhichitem == thing:
                  print("the", checkwhichitem, "is a piece of armour")
                  for item in player:
                    if isinstance(item, list):
                      if item[0] == checkwhichitem:
                        print("wearing the", item[0], "gives you", item[1], "extra defense against attacks.")

                        print("for every armour level you have, you can block .5 damage. right now, you will block", player[4] / 2, "damage every time the monster attacks.")
            for bunch in healingitems:
              #for thing in bunch:
              if checkwhichitem == bunch:
                print("the", checkwhichitem, " is a healing item")
                for item in player:
                  if isinstance(item, list):
                    if item[0] == checkwhichitem:
                      print(item[3], "the", item[0], "will give you an additional", item[1], "health.")
                      print("right now, your health is", player[2])
            if checkwhichitem in key:
              print("the", checkwhichitem, "is a key.")
              print("it probably unlocks something, but who knows?")
            if checkwhichitem in coinpouch:
              print("you looked inside of the", checkwhichitem)
              print("there were", item[1], "coins contained within!")

              player[player.index(item)] = 'test'
              player[6] = player[6] + item[1]
              print("you now have a total of", player[6], "coins!")




      if found == 'no':
        print("you dont have a", checkwhichitem)






  elif action == 'map':
    if currentroom < 26:
      import mansionmap
      moverplace = mansionmap.map(allrooms, currentroom, moverplace)
    else:
      print("this room doesnt appear on your map. its a secret corridor within the devils home")








  elif action == 'heal':
    heal()

  elif action == 'help':
    print(instructions)

  elif action == 'wholeroom':
    print(allrooms[currentroom])

  elif action == 'MLC':
    print("there are", monstersleft(), "monsters left in the mansion!")





if player[2] < 1:
  print(" ")
  print(" ")
  print("_____________________________")
  print(" ")
  print("with one final blow, the monster kills you. your body goes flying across the room, propelled by the monsters attack, and hits the wall, and then the floor. it is there, slumped over on the ground, leaning against the northern wall of the room, where your body will sit for all of eternity. your soul now lives outside of your body, where it will send the rest of time enduring the harshest punishments the devil has to offer, backbreaking labour all day, everyday. you have failed God. you have failed your brother Rick. may satan have mercy on your soul.")

  print("if you are the sort of person the believes in reincarnation, feel free to try again by clicking on the green RUN button at the top of the page. maybe next time, you will be able to rescue your brother and escape back to earth.")

if didiwinthegame == 'yes':
  print("Rick smiles. 'huh, that sounds pretty cool. maybe if i ever get trapped in hell again, that could be added to the game!' you tell Rick that hes crazy if he thinks youre going to dive into hell to save him a second time, and that he should definitly never do that again. the two of you continue down the magical pathway. soon enough, you find yourselves back on earth, back in the realm of the living. that night, you order pizza, and the two of you have an excellent time playing mario Kart deep into the night. life is good.")
  print(" ")
  print("THE END")
