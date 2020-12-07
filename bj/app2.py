import random

deck = [1,2,3,4,5,6,7,8,9,10,11,12,12] * 4


def draw():
    random.shuffle(deck)
    card = deck.pop()
    if card  == 11:
        card = 'J'
    if card  == 12:
        card = 'Q'
    if card  == 13:
        card = 'K'
    if card  == 1:
        card = 'A'
    return card

def deal():
    hand = []
    for i in range(2):
        card = draw()
        hand.append(card)
    return hand

def hit(hand):
    card = draw()
    hand.append(card)

def total(hand):
    score = 0
    for card in hand:
        if card == "J" or card == "Q" or card == "K":
            score += 10
        elif card == "A":
            if score >= 11:
                score += 1
            else:
                score += 11
        else:
            score += card
    return score


def play_again():
    again = input("もう一度プレイしますか？（Y/N) : ").lower()
    if again == 'y':
        return
    else :
        print("お疲れ様でした")
        exit()

def result(player_hand, dealer_hand):
    player = total(player_hand)
    dealer = total(dealer_hand)
    if player > dealer:
        print(f'\nディーラーの合計点数は { dealer } あなたの合計点数は { player } です。 YOU WIN')
    else:
        print(f'\nディーラーの合計点数は { dealer } あなたの合計点数は { player } です。 YOU LOSE')

def game():
    while True:
        dealer_hand = deal()
        player_hand = deal()
        print(f'ディーラーは{ dealer_hand[0] } ? です。')
        print(f'プレイヤーは{ player_hand } です。')
        print(f'あなたの合計点数は{ total(player_hand) }')

        choice = 0

        while choice != quit:
            choice = input('ヒットしますか？ スタンドしますか？ (HIT/STAND) : ').lower()
            if choice == 'hit':
                hit(player_hand)
                print(f'あなたに{player_hand[-1]} が配られ、手札は{player_hand}　合計は{total(player_hand)}')
                if total(player_hand) > 21:
                    print('あなたは 21 を超えてしまいました。 YOU LOSE...')
                    choice = quit
                elif total(player_hand) == 21:
                    print('あなたは 21 ぴったりです。 YOU WIN')
                    choice = quit


            elif choice == 'stand':
                print(f'ディーラーの手札は{dealer_hand} 合計は{total(dealer_hand)}')
                while total(dealer_hand) < 17:
                    hit(dealer_hand)
                    print(f'あなたに{dealer_hand[-1]} が配られ、手札は{dealer_hand}　合計は{total(dealer_hand)}')
                    
                    if total(dealer_hand) > 21:
                        print('ディーラーは 21 を超えてしまいました。 YOU WIN')
                        choice = quit

                    elif total(dealer_hand) == 21:
                        print('ディーラーは 21 ぴったりです。 YOU LOSE')
                        choice = quit

                if total(dealer_hand) < 21:
                    result(player_hand, dealer_hand)
                    choice = quit

        play_again()


game()
