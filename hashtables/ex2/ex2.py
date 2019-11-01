#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    for i in range(len(tickets)):
        hash_table_insert(hashtable ,tickets[i].source , tickets[i].destination)
    route[0] = hash_table_retrieve(hashtable, "NONE")
        
        # if tickets[i].source == 'NONE':
        #     route[0] = tickets[i].destination
        # if tickets[i].destination == 'NONE':
        #     route[length -1] = tickets.destination
        # elif route[0] is not None:
    for i in range(1 , len(route)):  
        route[i] = hash_table_retrieve(hashtable , route[i - 1])
    return route
