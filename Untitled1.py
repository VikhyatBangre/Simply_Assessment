#!/usr/bin/env python
# coding: utf-8

# In[1]:


def find_route(tickets, start, cities):
    graph = {}
    for ticket in tickets:
        src, dest = ticket.split('-')
        if src not in graph:
            graph[src] = []
        graph[src].append(dest)
    
    path = []
    visited = set()

    def dfs(current):
        path.append(current)
        visited.add(current)

        if len(path) == len(cities):
            return True

        for neighbor in graph.get(current, []):
            if neighbor not in visited and dfs(neighbor):
                return True

        path.pop()
        visited.remove(current)
        return False

    dfs(start)

    return path

tickets = [
    "Paris-Skopje", "Zurich-Amsterdam", "Prague-Zurich",
    "Barcelona-Berlin", "Kiev-Prague", "Skopje-Paris",
    "Amsterdam-Barcelona", "Berlin-Kiev", "Berlin-Amsterdam"
]

cities = ["Amsterdam", "Kiev", "Zurich", "Prague", "Berlin", "Barcelona"]

start = "Kiev"

route = find_route(tickets, start, cities)
print("Route:", route)


# In[ ]:




