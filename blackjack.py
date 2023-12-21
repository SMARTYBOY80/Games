import random

#load cards
with open('cards.txt') as file:
    cards = file.read().split(',')

    
#functions


#pick a random card
def pickCard():
    card = random.choice(cards)
    cards.remove(card)
    return card

def isAceOrFace(card, total):            
    if card in ['K', 'Q', 'J']:
        return '10', 0
    
    if card == 'A':
        if total + 11 > 21:
                return '1', 0
        else:
            print('you have an ace')
            return '11', 1  
    
    return card, 0



def playerChoice(playerTotal):
    canChange3 = 0
    #ask hit or stay
    while playerTotal < 21:
        hit = input("Hit or Stay? ")
        if hit == "hit":
            card = pickCard()
            card, canChange3 = isAceOrFace(card, playerTotal)
            playerTotal = playerTotal + int(card)
            print("Player Total: " + str(playerTotal))
        elif hit == "stay" or hit == "stand":
            break
        else:
            print("Please enter 'hit' or 'stay'")
    return playerTotal, canChange3

def ai(aiCard):
    aiTotal = 0
    aiCard, canChange = isAceOrFace(aiCard, aiTotal)
    aiCard2 = pickCard()
    aiCard2, canChange = isAceOrFace(aiCard2, aiTotal)
    aiTotal = int(aiCard) + int(aiCard2)
    
    
    
    while aiTotal < 17:
        card = pickCard()
        card, canChange = isAceOrFace(aiCard, aiTotal)
        aiTotal = aiTotal + int(card)
        print("AI Total: " + str(aiTotal))
        if aiTotal > 21 and canChange == True:
            aiTotal = aiTotal - 10
            print("AI Total: " + str(aiTotal))
    return aiTotal

def player():
    playerTotal = 0

    playerCard = 'A'
    playerCard2 = pickCard()
    #checks if ace is 1 or 11 or if its a face card
    playerCard, canChange = isAceOrFace(playerCard, playerTotal)
    playerCard2, canChange2 = isAceOrFace(playerCard2, playerTotal)
    #adds total of cards
    playerTotal = int(playerCard) + int(playerCard2)
    #prints total of cards
    if playerTotal <= 21:
        print("Player Total: " + str(playerTotal))
    
    total, canChange3 = playerChoice(playerTotal)

    if total >21 and canChange == 1 or total >21 and canChange2 == 1 or total >21 and canChange3 == 1:
        total = total - 10
        print("Player Total: " + str(total))
        total, canChange3 = playerChoice(playerTotal)
    return total

def compare(playerTotal, aiTotal):
    if playerTotal > 21:
        print("Player Busts!\nAI Wins!")
    elif aiTotal > 21:
        print("AI Busts!\nPlayer Wins!")
    elif playerTotal > aiTotal and playerTotal < 22:
        print(f"Player has {playerTotal} and AI has {aiTotal}")
        print("Player Wins!")
    elif playerTotal < aiTotal and aiTotal < 22:
        print(f"Player has {playerTotal} and AI has {aiTotal}")
        print("AI Wins!")
    else:
        print("Tie!")


def welcome():
    print(f"""Welcome to the thrilling world of Blackjack!
           Get ready to experience the excitement of strategic gameplay and the rush of the cards.
           Whether you're a seasoned pro or a newcomer, we're delighted to have you at the table.
           Good luck, and may the cards be in your favor!\n Press Enter to continue""")
    input("")


#main
        
welcome()

aiCard = pickCard()
print(f'ai has a: {aiCard}')
playerTotal = player()
aiTotal = ai(aiCard)
compare(playerTotal, aiTotal)