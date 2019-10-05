# Giving WA

tc = int(input())

for _ in range(tc):
    n = int(input())

    fav_team_score = 0
    for _ in range(n):
        option, A, B = list(map(int, input().split(" ")))

        if option == 1:
            fav_team_score = A
            
            print("YES")
        else:
            if fav_team_score > 0:
                if A > fav_team_score and B <= fav_team_score:
                    fav_team_score = A
                    print("YES")
                elif B > fav_team_score and A <= fav_team_score:
                    fav_team_score = B
                    print("YES")
                elif A == B and A > fav_team_score:
                    fav_team_score = A
                    print("YES")
                else:
                    print("NO")
            else:
                print("NO")
