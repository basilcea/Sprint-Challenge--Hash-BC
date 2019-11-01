#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    for i in range(length):
        hash_table_insert(ht, weights[i] , i)
        searchedKey = limit - weights[i]
        if hash_table_retrieve(ht, searchedKey) and hash_table_retrieve(ht, weights[i]) != hash_table_retrieve(ht , searchedKey) :
            if (hash_table_retrieve(ht , weights[i]) >= hash_table_retrieve(ht , searchedKey)):
                return (hash_table_retrieve(ht, weights[i]), hash_table_retrieve(ht , searchedKey))
            else:
                return (hash_table_retrieve(ht, searchedKey), hash_table_retrieve(ht , weights[i]))
        if hash_table_retrieve(ht, searchedKey) and hash_table_retrieve(ht, weights[i]) == hash_table_retrieve(ht , searchedKey) :
            return(1, 0)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
