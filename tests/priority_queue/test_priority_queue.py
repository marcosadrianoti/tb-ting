import pytest
from ting_file_management.priority_queue import PriorityQueue
from tests.priority_queue.mocks import mock_list


def test_basic_priority_queueing():
    # [9, 4, 2, 5, 7, 3] => Entradas

    priority_queue = PriorityQueue()
    for item in mock_list:
        priority_queue.enqueue(item)

    assert len(priority_queue) == 6

    assert priority_queue.search(0) == mock_list[1]

    # https://pytest.org/en/7.4.x/reference/reference.html#pytest.raises
    with pytest.raises(IndexError) as teste:
        priority_queue.search(7)
    assert teste.type is IndexError

    # [4, 2, 3, 9, 5, 7] = Saídas
    assert priority_queue.dequeue() == mock_list[1]
    assert priority_queue.dequeue() == mock_list[2]
    assert priority_queue.dequeue() == mock_list[5]
    assert priority_queue.dequeue() == mock_list[0]
    assert priority_queue.dequeue() == mock_list[3]
    assert priority_queue.dequeue() == mock_list[4]
