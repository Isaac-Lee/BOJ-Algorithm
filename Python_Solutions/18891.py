import sys

def main():
    p, v = map(int, sys.stdin.readline().split())
    partyDict = {}
    seatSum = 0
    validVoteSum = 0

    # 정당 데이터 파싱 부
    for _ in range(p):
        name, seat, vote = map(str, sys.stdin.readline().split())
        seat = int(seat)
        vote = int(vote)
        partyDict[name] = [_ + 1, seat, vote]
        seatSum += seat
        validVoteSum += vote
    
    # 무소속 당선인
    noPartySeat = 253 - seatSum
    
    # 유효 정당 체크
    validParty = []
    ratioValidVoteSum = 0
    invalidPartyCnt = noPartySeat
    for i in partyDict:
        ratio = partyDict[i][2] / validVoteSum
        validFlag = False
        if ratio >= 0.03 or seat >= 5:
            validFlag = True
            validParty.append(i)
            ratioValidVoteSum += partyDict[i][2]
        # else:
        #     invalidPartyCnt += partyDict[i][1]
        partyDict[i] += [ratio, validFlag]
    
    # 유효 정당 득표수 갱신
    ratioSeatDict = {}
    for i in validParty:
        ratioSeatDict[i] = [partyDict[i][2] / ratioValidVoteSum]
    
    # calculate ratio seat
    validSeatSum = 0
    for i in ratioSeatDict:
        temp = ((300 - invalidPartyCnt) * ratioSeatDict[i][0] - partyDict[i][1]) / 2
        if temp < 1:
            seat = 0
        else:
            seat = int(temp)
            if temp - int(temp) >= 0.5:
                seat += 1
        ratioSeatDict[i].append(seat)
        validSeatSum += seat
    
    # update ratio seat to 30
    if validSeatSum > 30:
        underPriority = []
        newSeatSum = 0
        for i in ratioSeatDict:
            newSeat = 30 * ratioSeatDict[i][1] / validSeatSum
            underPriority.append([-(newSeat - int(newSeat)), partyDict[i][0], i])
            ratioSeatDict[i][1] = int(newSeat)
            newSeatSum += int(newSeat)
        underPriority.sort()
        for i in range(30 - newSeatSum):
            ratioSeatDict[underPriority[i][2]][1] += 1
    
    elif validSeatSum < 30:
        underPriority = []
        newSeatSum = 0
        for i in ratioSeatDict:
            newSeat = ratioSeatDict[i][1] + (30 - validSeatSum) * ratioSeatDict[i][0]
            underPriority.append([-(newSeat - int(newSeat)), partyDict[i][0], i])
            ratioSeatDict[i][1] = int(newSeat)
            newSeatSum += int(newSeat)
        underPriority.sort()
        for i in range(30 - newSeatSum):
            ratioSeatDict[underPriority[i][2]][1] += 1
    
    # calculate left 17 seats
    underPriority = []
    leftSeatSum = 0
    for i in ratioSeatDict:
        leftSeat = 17 * ratioSeatDict[i][0]
        leftSeatSum += int(leftSeat)
        ratioSeatDict[i][1] += int(leftSeat)
        underPriority.append([-(leftSeat - int(leftSeat)), partyDict[i][0], i])
    underPriority.sort()
    for i in range(17 - leftSeatSum):
        ratioSeatDict[underPriority[i][2]][1] += 1

    # final seat calculate
    finalSeatList = []
    for i in partyDict:
        seat = partyDict[i][1]
        if partyDict[i][4]:
            seat += ratioSeatDict[i][1]
        finalSeatList.append([-seat, i])
    finalSeatList.sort()
    for i in finalSeatList:
        print(i[1], -i[0])
    return

if __name__ == "__main__":
    main()