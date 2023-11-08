print("Hello! In this program, you will choose a number, one through four, and the code will decide your career in the sports industry. Good Luck!")
career = input("pick one, two, three, four: ")

if career == "one":
    print("You chose soccer!")
    country = input("America or Europe: ")
    print()

    if country == "America":
        print("Congrats! You and the San Jose Earthquakes manager agreed on a 2-year, one-million-dollar contract. In your first season, you scored four goals, and your team came in second to last place. Not an ideal start, but you are working your way up... hopefully")
        decision = input("Do you wish to play another season or retire? Yes or no ")

        if decision == "yes":
            print()
            print("good choice! your team wins this season + you scoring 45 goals, a record that hasn't been broken, but in your last game of the season, you suffer a career-ending leg injury, and your season is over... 2 years pass, and the team wants you to become the head coach")
        else:
            print("hmm interesting choice. you retire and become a bum")

    else:
        print("Great Decision on Playing in Europe!")
        print()
        europe_decision = input("Do you want to play in England for Arsenal or Spain for Barcelona?")

        if europe_decision == "Arsenal":
            print("good luck in an amazing career at Arsenal!")
        else:
            print("Ah, Barcelona is a classic team. you will look good wearing red and blue. I hope to see you in the World Cup one day")

elif career == "two":
    print("Nice. you chose to play golf; the most peaceful sport in the world ")
    golf_decision = input("Do you want to play casually with your Grandpa or professionally? Choose one: ")

    if golf_decision == "professionally":
        print("Your career starts in Maine, US, and you just got invited to the PGA Championship in Scotland")
        pga_decision = input("Do you want to join or practice more? if you join now, you likely will not win: ")
        print()

        if pga_decision == "practice more":
            print(f'You decided to {pga_decision}. Smart Choice.')
            print()
            print("you decide to stay in Maine and practice with your friends every single day")
            print()
            print("you improve your technique and your handicap goes from 1 to scratch!")
            print("it's your time to compete")
            practice_decision = input("Do you wish to play? type 'Yes'")

            if practice_decision == "Yes":
                print("great choice!")
                print()
                print("you travel and compete but unfortunately come up short. you come in 7th place out of 10 players")
                print()
                print("yikes")

            last_practice_decision = input("do you want to try again? The next tournament that you are eligible to play in is in 3 years. You can either... give up forever, try again, or find a different career. choose one")

            if last_practice_decision == "give up forever":
                print("damn")
                print(f'You decided to {last_practice_decision}. Disappointing choice.')
                print("You had such a promising career and quit. I am so upset I am not giving you anything else. Goodbye")

            else:
                print("trying again is a very honorable choice")
                print()
                print("3 years pass, and the next PGA championship arrives. Good Luck")
                retry_decision = input("You are on the 18th hole and you are tied for first place. do you take the risky shot to hope to take the lead and win, or play it safe and tie (type 'take the risky shot' or 'play it safe')")

                if retry_decision == "take the risky shot":
                    print("AH!")
                    print()
                    print(f'You decided to {retry_decision} and it failed!')
                    print("your shot has an intense slice and it smacks into the tree, falling in the water")
                    print("you rage and snap your 6 iron over your knee and show a very immature reaction")
                    print()
                    print('you embarrassing actions get you expelled from all future tournaments and you become a bum')

                elif retry_decision == "play it safe":
                    print('good choice, you stick it on the green and one-putt for a birdie. your opponent missed his putt and...')
                    print('you win!')
                    print('Congrats!')

        elif last_practice_decision == "find a different career":
            print("hmm.ok")
            print()
            print("you drop out of golf and become a barber for golf players")
            print()
            print("you give everyone the exact same haircut, either a preppy crew cut or a complete shave, and make them bald")

    elif golf_decision == "casually":
        print("I love to play golf with my grandpa so I admire your choice")
        print()
        print("Although you don't make a career out of golf and you become a lawyer, you play golf every week on Fridays at 2 pm with your grandpa!")
        print()
        print("he is very appreciative of you and transfers his ownership of BMW all to you, and you make Interpol's top 100 wealthiest men alive")
elif career == "three":
  print('You are playing basketball!')
  print()
  print('instead of making decisions of your career, here you are in game 7 of the NBA finals')
  print()
  print('it is a tie game with 5 seconds left and you have the ball.')
  print()
  print('do you want to take a 3-pointer or a layup?{note: you have a higher chance of making a two pointer but it is boring} choose a number, 3 or 2')
  shot_choice = input('pick 2 or 3')
  if shot_choice == "3":
      print()
      print('you dribble up, fake left then go right')
      print('you shoot the 3 pointer and it rolls...and rolls. and bounces... and it eventually falls out')
      print()
      print(' you did get fouled and have three shots')
      number = int(input("enter either an even or odd number, and if it is  the one i am thinking of, you make all three free throws and your team wins the game.: "))
      if number % 2 == 0:
          print()
          print("you make one...you make the second, and you make the third!.")
          print()
          print(' You win! Congrats')
      else:
          print("Ah, unlucky, you miss all three.")
          print()
          print('sounds to me like you are a bum')
  
  
  elif shot_choice == "2":
    print(f'You decided to shoot for {shot_choice}. Smart Choice.')
    print()
    print('you go up for the layup and get blocked. your team looses the game and everybody hates you.')
    print()
    print(' the hate you receive is so bad you stick to playing pickup basketball at the OFJCC')
if career =="four":
  print()
  print('you are a mailman')
  print()
  print('you have been working as a mailman for 5 years and you deliver 399 pieces of mail today')
  print('this is your daily route')
  import turtle
  turtle.forward(100)
  turtle.right(90)
  turtle.forward(50)
  

    