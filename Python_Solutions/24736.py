score = [6,3,2,1,2]
team1_score = 0
team2_score = 0
team1=list(map(int, input().split()))
team2=list(map(int, input().split()))

for i in range(5):
    team1_score += team1[i]*score[i]
    team2_score += team2[i]*score[i]
print(team1_score,team2_score)