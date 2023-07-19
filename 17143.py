def catch_shark():
    global catch_cnt
    for row in range(R):
        if map_data[row][person]:
            catch_cnt+=map_data[row][person][2]
            map_data[row][person]=[]
            return

def shark_move():
    global map_data
    tmp_shark = [[[] for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if map_data[i][j]:
                direction = map_data[i][j][1]
                ni=i
                nj=j
                if 1<=direction<=2: # 세로방향
                    for _ in range(map_data[i][j][0]%(2*len(map_data)-2)):
                        ni=ni+di.get(direction)[0]
                        nj=nj+di.get(direction)[1]
                        if ni==-1 or ni == len(map_data):    # 끝까지 간 경우 방향전환
                            direction= 2 if direction==1 else 1
                            ni = ni + di.get(direction)[0]
                            ni = ni + di.get(direction)[0]
                            map_data[i][j][1]=direction

                elif 3<=direction<=4: # 가로방향
                    for _ in range(map_data[i][j][0]%(2*len(map_data[0])-2)):
                        ni=ni+di.get(direction)[0]
                        nj=nj+di.get(direction)[1]
                        if nj==-1 or nj == len(map_data[0]):
                            direction = 4 if direction == 3 else 3
                            nj = nj + di.get(direction)[1]
                            nj = nj + di.get(direction)[1]
                            map_data[i][j][1] = direction

                if tmp_shark[ni][nj]:   # 이미 상어가 있는 경우
                    if tmp_shark[ni][nj][2]<map_data[i][j][2]:
                        tmp_shark[ni][nj] = map_data[i][j]
                else:
                    tmp_shark[ni][nj] = map_data[i][j]
    map_data=tmp_shark


R,C,M = map(int,input().split())
map_data = [[[] for _ in range(C)] for _ in range(R)]
di = {1:[-1,0],2:[1,0],3:[0,1],4:[0,-1]}

for _ in range(M):
    r,c,s,d,z = map(int,input().split())
    map_data[r-1][c-1]=[s,d,z]

person=-1
catch_cnt=0
while person<C-1:
    person+=1   # 사람을 오른쪽 열로 이동
    catch_shark()
    shark_move()
print(catch_cnt)