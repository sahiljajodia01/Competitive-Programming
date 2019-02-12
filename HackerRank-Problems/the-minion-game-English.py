def minion_game(string):
    # your code goes here
    score1 = 0
    score2 = 0
    for j in range(len(string)):
        for i in range(0, len(string), j+1):
            if i+j+1 < len(string):
                if string[i:i+j+1][0] in ['a', 'e', 'i', 'o', 'u', 'A', 'E','I', 'O', 'U']:
                    score1 = score1 + 1
                if string[i:i+j+1][0] not in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                    score2 = score2 + 1
                    print(string[i:i+j+1])
    
    if score1 > score2:
        print("Kevin {}".format(score1))
    elif score2 > score1:
        print("Stuart {}".format(score2))
    else:
        print("Draw")


if __name__ == '__main__':
    # s = input()
    minion_game("BANANA")