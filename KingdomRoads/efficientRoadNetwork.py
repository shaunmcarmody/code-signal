"""
https://app.codesignal.com/arcade/graphs-arcade/kingdom-roads/ty4w8WJZ4sZSBNK5Q
"""

# First Pass Solution

def efficientRoadNetwork(n, roads):
    if n == 1:
        return True

    connections = {}

    for i in range(n):
        connections[i] = set()

    for x, y in roads:
        connections[x].add(y)
        connections[y].add(x)

    for origin in range(n - 1):
        for destination in range(origin + 1, n):
            connected_city = False

            for i in range(n):
                if connected_city != True:
                    if i != origin and i != destination:
                        if origin in connections[i] and destination in connections[i]:
                            connected_city = True
                    elif i == origin:
                        if destination in connections[i]:
                            connected_city = True
                    elif i == destination:
                        if origin in connections[i]:
                            connected_city = True

            if connected_city == False:
                return False

    return True

"""
Alternative Solution
https://wxtp.wordpress.com/2017/01/30/how-to-solve-efficientroadnetwork-in-codefights/
"""

def efficientRoadNetwork(n, roads):
    dist = [[4] * n for x in range(n)]

    for x in range(n):
        dist[x][x] = 0

    for x, y in roads:
        dist[x][y] = 1
        dist[y][x] = 1

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]
                    dist[i][j] = dist[i][k] + dist[k][j]

    for i in range(n):
        for j in range(n):
            if dist[i][j] >= 3:
                return 0
    
    return 1





