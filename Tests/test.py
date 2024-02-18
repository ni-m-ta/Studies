N = int(input())
coordinates = []
for i in range(N):
    x,y = input().split()
    coordinates.append((x,y))

for i in range(N-1):
    for j in range(i+1,N):
        x1 = coordinates[i][0]
        y1 = coordinates[i][1]
        x2 = coordinates[j][0]
        y2 = coordinates[j][1]
        dx = x1-x2
        dy = y1-y2
        