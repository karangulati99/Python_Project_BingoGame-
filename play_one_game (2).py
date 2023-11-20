import generate_bingo
import random
import numpy as np
import time


def  draw_check(draw_set):
    number_drawn = draw_set.pop()
    return number_drawn

def card_check(all_cards, num_drawn):   
    for card in all_cards:
        card[card==num_drawn] = 0

def IsBingo(all_cards,number_call,full_house_cards,playerwon):
    count = 0
    for card in all_cards:
        count+=1
        if IsBingo_checkonecard(card):
            playerwon.append(['B',number_call])
            # print(f'Bingo!! player {count} has won')
            # print(f'Player {count} will not be counted other than for full house')
            full_house_cards.append(all_cards[count-1])
            all_cards.pop(count-1)

    #to remove the last card for bingo
    if len(all_cards)==1:
        full_house_cards.append(all_cards[0])
        all_cards.pop()

              
def check_full_house(filtered_cards,number_drawn,number_call,playerwon):
    count = 0
    card_check(filtered_cards,number_drawn)
    a = False
    for card in filtered_cards:
        count+=1
        if np.all(card == 0):
            playerwon.append(['FH',number_call])
            a = True
            filtered_cards.pop(count-1)
    return a

def IsBingo_checkonecard(card):
    for i in range (5):
            row_zeros=np.count_nonzero(card[i,:])
            col_zeros=np.count_nonzero(card[:,i])
            if not row_zeros or not col_zeros: #check if we have 0 non-zeros
                # print("row or column : \n",card)
                return True
    diagonal_zeros=np.count_nonzero(np.diag(card))
    diagonal1_zeros=np.count_nonzero(np.diag(np.fliplr(card)))
    if not diagonal_zeros or not diagonal1_zeros:
        # print("dialognal : \n",card)
        return True
    return False

def get_number_players():
    # GET_CARDNUMS = int(input('Enter the number of Bingo cards to generate : '))
    # print("type : ",type(GET_CARDNUMS))
    # if type(GET_CARDNUMS)== int:
    #     while GET_CARDNUMS < 1:
    #         GET_CARDNUMS = input('Enter the number of Bingo cards to generate that is greater than zero! : ')
    #     return GET_CARDNUMS
            
    
    # while type(GET_CARDNUMS)!= int:
    #     GET_CARDNUMS = input('Enter the number of Bingo cards to generate in numeric form for example 2, 3 etc : ')
    #     if type(GET_CARDNUMS)!= int:
    #         GET_CARDNUMS = input('Enter the number of Bingo cards to generate in numeric form for example 2, 3 etc : ') 
    # return GET_CARDNUMS
    while True:
        try:
            card_count = int(input('Enter the number of Bingo cards to generate: '))
            if card_count > 0:
                return card_count
            else:
                print('Please enter a number greater than zero.')
        except ValueError:
            print('Please enter a valid integer.')

 
 
def main():
    count=0
    simulation_game = 100
    Output_Simulation = []
    num_player = get_number_players()


    for game in range(simulation_game):
        full_house_cards = []
        bingo_cards = generate_bingo.generate(num_player)
        random_draw_set = random.sample(range(1, 76), 75)
        Output_per_Simulation = []
        sequence = 0 
        while random_draw_set :
            sequence+=1

            # Get the number drawn from the list of random numbers
            number_drawn =draw_check(random_draw_set)

            # check whether a number is present in the bingo card
            card_check(bingo_cards,number_drawn)

            #check of bingo is reached or not that is line or diagonal check
            IsBingo(bingo_cards,sequence,full_house_cards,Output_per_Simulation) 

            #Full house check
            if len(full_house_cards)>0:
                check_full_house(full_house_cards,number_drawn,sequence,Output_per_Simulation)

        # print("Output : ",Output_per_Simulation)

        Output_Simulation.append(Output_per_Simulation)

    print("Output total : ",Output_Simulation)
       
 
start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))