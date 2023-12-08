import random


def isnumber(book):
  conclusion = True
  nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
  for char in book:
    if char not in nums:
      conclusion = False
  return bool(conclusion)

def cardgame(coins, name):


  print("the bug person shook your hand as you sat down. 'now listen up,", name, ",while I explain the rules, because here in my casino, theyre a little bit different then you are used to. my hand will always be between 12 and 21, with an equal chance of every possibilty. the cards you pick up will be between 1 and 10, again with an equal probability of all numbers betwenn 1 and 10. you get two cards to start, and have the choice to pick up more cards, or stick with your current total. any additional cards you chose to pick up are added to your total. if you go over 21, you lose. and lets say, for the sake of sportsmanship, that you will win if its a tie. at the start of every round, you will choose how much to gamble. if you lose, you lose that much money. if you win, you win that amount. when you want to stop playing, you will bid zero dollars, then you'll leave. you get all that? are you ready?' you nod, and after placing your bet, recieve your first hand.")
  nthcard = ['third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth']
  while coins > 0 and coins < 257:
    anthand = random.randrange(12,22)
    print(" ")
    print(" ")

    print(" ")
    print("you have", coins, "coins")
    bidset = False
    goodnumber = False
    while bidset is False and goodnumber is False: #and something else, repeat if isnumber fails
      cashmoney = (input("how much would you like to gamble? ")) #int
      print(" ")
      print("______________________________")
      print(" ")

      validbid = True
      if isnumber(cashmoney) is True:
        cashmoney = int(cashmoney)
        goodnumber = True
        #print("nice")
      else:
        if "-" in cashmoney:
          print("the ant fellow sneered at you. he began to tell you:")
          print("'you know, friend, somewhere in an alternate universe, in another python program, one where andrew forgot to program in a failsafe... ")
          print(" ")
          print("trying that would have worked. i must say, bidding a negative amount of money, so that you can lose on purpose and gaurentee that youll win the pot? thats pretty clever. i bet you really thought you were going to outsmart me there. well, since you didnt, Ill give you a consolation prize, in the form of secret lore!")
          print(" ")
          print("did you know that the vampire over in the drawing room isnt really a vampire? hes just an adult man who loves playing dress up. he committed some seriously awful crimes on earth, and he definitly belongs down here in hell.")
          print(" ")
          print("humans arent usually allowed to live in the devils mansion. one day, that man came in dressed like a vampire, complete with the fake fangs, and the devil deemed him scary enough to live here, to be one of the lucky few monsters that gets a nice place to live in exchange for killing people that break in. not a bad deal, really.")
          print(" ")
          print("this dude has loved dressing up in costumes his whole life, so he doesnt mind pretending to be a vampire 24 /7. the devil either hasnt caught on, or doesnt care, because the man does his job, and does it well. his name is William Afton, and ill spare you the details of the crimes he committed on earth. though i gotta say, through my few interactions with him, it seems like hes been pretty harmless since he got here.")
          print(" ")
          print("other than that one time that he bit the cyclops after an arguement in 1987, he hasnt really caused any trouble.")
          print(" ")
          print("alright, now lets get back to the game! you still need to make your bid, and you cant bid a negative number, unless you want to hear me tell this whole story a second time.'")
          break
        else:
          print("that is totally not a number. like, not at all. just for refrence, on most keyboards, the numbers are the ones at the top. hope that helps!")
          break
      print(" ")
      print(" ")
      print("________________________________________")
      print(" ")
      print(" ")
      if cashmoney == 0 and validbid:
        print("'leaving so soon,", name, "? we were just getting started!' you stand up from the table, and tell the giant ant humanoid that you're done with playing cards for now, but you might come back later.")
        if coins < 10:
          print("'hey, wait!' the dealer remarked. 'I feel bad that you lost so badly, so here is a gift, given in good faith, to motivate you to come back and play with me later. im going to give you", (10 - coins), "coins!'")
          print("you thank the card dealer.")
          coins = 10
        print("you walk away from the dealers table, to the centre of the casino.")
        return(coins)

      elif cashmoney > coins and validbid:
        print("the insect card dealer laughed. 'I love your enthusiasm,", name, ", but you cant bid that much, you only have", coins, "coins. ill set your current bid at", coins, "coins")
        print(" ")
        cashmoney = coins
        bidset = True
      elif cashmoney < 0 and validbid:
        print("'thats pretty clever trying to bid a negative number of coins, so you can lose on purpose and take the pot.' said the card dealer.'I wont fall for it though. since you want to bet low, Ill set your current bid at one coin'")
        cashmoney = 1
        bidset = True
      elif cashmoney > 0 and cashmoney < (coins + 1) and validbid:
        print("and then, the cards were dealt.")
        bidset = True

      #print("you bid", cashmoney)
      acard = random.randrange(1,11)
      bcard = random.randrange(1,11)
      print("your first two cards are", acard, "and", bcard)
      total = acard + bcard
      print("your total is", total)
      finish = 0
      tally = 0
      while total < 22 and finish == 0:

        anothercard = input("would you like another card? ")
        print(" ")
        print(" ")
        print("________________________________________")
        print(" ")
        print(" ")
        if anothercard == 'yes':
          card = random.randrange(1,11)
          print("your", nthcard[tally], "card is", card)
          tally = tally + 1
          total = total + card
          print("your total is", total)
        elif anothercard == 'no':
          print("your total was", total)
          print("the dealers total was", anthand)
          if total < anthand:
            #print("you lost the hand!")
            print("you lost", cashmoney, "dollars.")
            coins = coins - cashmoney
            finish = 1
          else:
            #print("you won the hand!")
            print("you won", cashmoney, "dollars!!!")
            coins = coins + cashmoney
            finish = 1
        if total > 21:
          print("you went over 21, so you lose the hand.")
          print("you lost", cashmoney, "dollars!")
          coins = coins - cashmoney
      if coins == 0:
        print("the card dealer looked delighted.'ha ha ha, youve lost all of your coins! I win! Im the best card player of all time! hey, ill tell you what," , name, ", because im in a good mood, and because i'm having so much fun playing with you, Ill give you 10 coins, so that we can keep the game going.'")
        coins = 10
        print("the ant fellow gave you 10 coins")
        finish = 1
  if coins > 254:
    print("you have", coins, "coins.")
    print("the dealers antennae shook with excitement. 'wow! what a hand! ive gotta level with you here, you've really cleaned me out, i dont have any more money to gamble. but that was a hell of a game!' you both stand up from the table, and shake hands once again. 'that was a lot of fun! hey, by the way, i dont remember if i already introduced myself or not, but my name is Lasius.'")
    print("you tell Lasius it was nice to meet him, and wave goodbye as you walk away from his table, to the middle of the casino.")
    return(coins)
