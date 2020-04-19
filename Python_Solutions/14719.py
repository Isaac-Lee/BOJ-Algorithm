def trapping_rain(buildings):
    raindrop = 0
    for i in range(len(buildings)):
        # 현재 인덱스의 왼쪽에서 가장 높은 건물의 높이
        max_left = max(buildings[:i+1])
        # 현재 인덱스의 오른쪽에서 가장 높은 건물의 높이
        max_right = max(buildings[i:])
        # 둘중에 어떤 값이 더 큰가?
        which_low = min(max_left, max_right)
        # 절대값 주의
        raindrop = raindrop + abs(buildings[i] - which_low)
    return raindrop

input()
building = list(map(int, input().split()))
print(trapping_rain(building))