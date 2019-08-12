"""
roadsBuilding
-------------
https://app.codesignal.com/arcade/graphs-arcade/kingdom-roads/CSzczQWdnYwmyEjvv
"""

def roadsBuilding(cities, roads):
    visited = set()
    new_routes = []

    for road in roads:
        x = road[0] if road[0] < road[1] else road[1]
        y = road[1] if road[1] > road[0] else road[0]

        visited.add((x, y))

    for city in range(cities):
        for route in range(cities):
            if city != route:
                x = city if city < route else route
                y = route if route > city else city

                if (x, y) not in visited:
                    visited.add((x, y))
                    new_routes.append([x, y])


    return new_routes

"""
Alternative Solution
https://wxtp.wordpress.com/2017/01/23/how-to-solve-newroadsystem-in-codefights-2/
"""
# def roadsBuilding(cities, roads):
#     adj = [[0] * cities for x in range(cities)]

#     for x, y in roads:
#         adj[x][y] = 1
#         adj[y][x] = 1
    
#     to_be_built = []

#     for x in range(cities):
#         for y in range(x + 1, cities):
#             if not adj[x][y]:
#                 to_be_built.append([x, y])

#     return to_be_built;