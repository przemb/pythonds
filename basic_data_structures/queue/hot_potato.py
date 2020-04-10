from nose.tools import assert_equal, assert_true, assert_false
from queue import Queue


def hot_potato(name_list, number):
    tmp_queue = Queue(*name_list)
    while tmp_queue.size() > 1:
        for i in range(0, number):
            elem = tmp_queue.deque()
            tmp_queue.enque(elem)

        tmp_queue.deque()
    return tmp_queue.deque()

result = hot_potato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7)
assert_equal('Susan', result)
