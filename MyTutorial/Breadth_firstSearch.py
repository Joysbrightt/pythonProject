# Todo GRAPHS ARE THE WAYS TO SORT A FIND THE SHORTEST PATH PROBLEM

# GRAPHS: Are made up nodes and edges. A node can be directly connected to many other nodes
# A Graph consists of several nodes and each node are called its neighbours.
#todo Breadth_first search takes O(number of perople + number of edges), written as O(V + E
#TODO where V-> number of vertices, E-> for number of edges
#TODO A directed graph has arrows, and the relationship follows the direction of the arrow
#TODO Undirected graphs don’t have arrows, and the relationship goes both ways
# Todo QUEUES

graph = {
}

graph["you"] = ["alice", "bob", "claire"]
# having a bigger graph in python
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom"]
graph["anuj"] = []
graph["bob"] = []
graph["bob"] = []
graph["bob"] = []

from collections import deque

search_queue = deque()
search_queue += graph["you"]


def person_is_seller(person):
    return person[-1] == 'm'


while search_queue:
    person = search_queue.popleft()
    if person_is_seller(person):
        print(person + "is a mango seller!")
    else:
        search_queue += graph[person]



def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched =[]
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person + "is a mango seller")
            else:
                search_queue += graph[person]
                searched.append(person)


    return False

search("you")