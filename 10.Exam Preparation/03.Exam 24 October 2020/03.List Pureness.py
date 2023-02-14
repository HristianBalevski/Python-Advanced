from collections import deque
from sys import maxsize


def best_list_pureness(lst, k):
  
    my_list = deque(lst)
    rotation = 0
    best_rotation = 0
    best_result = - maxsize

    while True:
        total_result = 0
        for index, number in enumerate(my_list):
            summary = index * number
            total_result += summary
            
        if total_result > best_result:
            best_result = total_result
            best_rotation = rotation
        my_list.appendleft(my_list.pop())
        
        if rotation == k:
            return f"Best pureness {best_result} after {best_rotation} rotations"
        rotation += 1
