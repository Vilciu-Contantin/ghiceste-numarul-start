from art import logo
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer, turns):
  """Verifica ce a ghicit utilizatorul cu raspunul corect. Returneaza numarul de ture ramase"""
  if guess > answer:
    print("Prea sus")
    return turns - 1
  elif guess < answer:
    print("Prea jos")
    return turns -1
  else:
    print(f"Felicitari! Raspunsul coreste a fost {answer}")

def set_difficulty():
  """Alege dificultatea. Returneaza numarul de ture pentru dificultatea respectiva"""
  level = input("Ce nivel de dificultate ai vrea? Scrie 'easy' sau 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
  print(logo)
  print("Bine ati venit la Jocul de GUESS NUMBER")
  print("Eu ma gandesc la un numar d ela 1 la 100")
  answer = randint(1, 101)

  print(f"PSST! Raspunsul este {answer}")

  turns = set_difficulty()

  guess = 0 

  while guess != answer:
    print(f"Mai ai {turns} incercari de a ghici numarul")
    print("\n")

    guess = int(input("Ghiceste numarul: "))

    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("Ai ramas fara ture de ghicit, ai pierdut :( ")
    elif guess != answer:
      print("Mai incearca o data")
    

game()
