import random
import numpy as np

def generate(num):
  numCards = num
  totalCards = []
  for _ in range(numCards):
    card = generate_numbers()
    totalCards.append(card)
    print_bingo_card(card)

  # print("Total cards :  ",totalCards)
  return totalCards
 


  


def generate_numbers():
  row1 = np.array(random.sample(range(1, 16), 5))
  row2 = np.array(random.sample(range(16, 31), 5))
  row3 = np.array(random.sample(range(31, 46), 5))
  row4 = np.array(random.sample(range(46, 61), 5))
  row5 = np.array(random.sample(range(61, 76), 5))

  bingo_card = np.concatenate((row1,row2,row3,row4,row5))
  bingo_card =  bingo_card.reshape(5,5)
  bingo_card[2,2]=0

  return bingo_card


def print_bingo_card(card):
  print ('   B   I   N   G   O   ')
  print (f' {card[0][0]:>3} {card[1][0]:>3} {card[2][0]:>3} {card[3][0]:>3} {card[4][0]:>3}')
  print (f' {card[0][1]:>3} {card[1][1]:>3} {card[2][1]:>3} {card[3][1]:>3} {card[4][1]:>3}')
  print (f' {card[0][2]:>3} {card[1][2]:>3} {card[2][2]:>3} {card[3][2]:>3} {card[4][2]:>3}')
  print (f' {card[0][3]:>3} {card[1][3]:>3} {card[2][3]:>3} {card[3][3]:>3} {card[4][3]:>3}')
  print (f' {card[0][4]:>3} {card[1][4]:>3} {card[2][4]:>3} {card[3][4]:>3} {card[4][4]:>3}')
  print('\n\n')




