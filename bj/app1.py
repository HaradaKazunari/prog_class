deck = [1,2,3,4,5,6,7,8,9,10,11,12,12] * 4

def play_again():
    again = input("もう一度プレイしますか？（Y/N) : ")
    if again == 'y' or again == 'Y':
        return
    else :
        print("お疲れ様でした")
        exit()

play_again()
