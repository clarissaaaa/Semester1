import random

def survey_results():
  categories = ["favorite drinks", "breakfast food", "favorite phone brands", "favorite laptop brands", "favorite lunch meal"]
  select = random.randint(0, 6)
  answers = {}
  if select == 0:
   answers = {"MILK" : 10, 'COFFEE' : 32, 'TEA': 25 , 'LONG ISLAND' : 40}
  elif select == 1:
    answers = {'EGG' :50, 'BREAD' : 32, 'CEREAL': 35, 'FRIED RICE' : 35}
  elif select == 2:
    answers = {"APPLE" : 35, "SAMSUNG" : 23, "OPPO" : 20, 'XIAOMI' : 12}
  elif select == 3:
    answers = {"HP": 24, "APPLE": 22, "DELL"  : 15, "ASUS" : 20}
  elif select == 4:
    answers = {"RICE": 30, " BURGER": 20, "SPAGHETTI": 15, "MEAT":10}

  print ("We surveyed 100 people on", categories[select])
  return answers

def guess(answers):
  print ("You need to accumulate 200 points from both players to win a prize!, each player has 5 turns")
  turns = 0
  points = 0
  guessed = []
  while turns < 5:
    print ("Total points:", points)
    guess = input("Guess: ")
    if guess.upper() in answers:
      points += answers[guess.upper()]
      print ("You get", answers[guess.upper()], "points.")
      answers.pop (guess.upper())
      guessed += [guess.upper()]
      
    else:
      print ("Answer is already listed / Incorrect answer!")
    turns += 1
  return points


def gameplay():
  while True:
    answers = survey_results()
    points = guess(answers)
    print ("You won", points, "points.")
    if points <= 200 :
        points_left = 200 - int(points)
        print("Player two needs", points_left, "left")
        continue
    else :
        print ("Congratulation you won the prize!")
        print ("Thanks for playing!")
        break

gameplay()




 
    
