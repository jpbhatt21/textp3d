jug1, jug2, aim = 10, 1, 3
visited = {}
queue=[]
def waterJugSolver():
    global queue
    queue.append([0,0,""])
    while queue:
        [amt1,amt2,prev]=queue.pop(0)
        if (amt1 == aim and amt2 == 0) or (amt2 == aim and amt1 == 0):
            return prev+"("+str(amt1)+","+str(amt2)+")\n"
        visited[str(amt1)+" "+str(amt2)] = True
        arr=[[0,amt2],[amt1,0],[jug1,amt2],[amt1,jug2],[amt1+min(amt2,jug1-amt1),amt2-min(amt2,jug1-amt1)],[amt1-min(amt1,jug2-amt2),amt2+min(amt1,jug2-amt2)]]
        for i in arr:
            if i in queue or visited.get(str(i[0])+" "+str(i[1])):
                continue
            queue.append([i[0],i[1],prev+"("+str(amt1)+","+str(amt2)+")\n"])
result = waterJugSolver()
print(result if result else "No solution")