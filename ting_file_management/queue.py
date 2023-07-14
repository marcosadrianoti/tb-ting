from ting_file_management.abstract_queue import AbstractQueue
from ting_file_management.linked_list import LinkedList


class Queue(AbstractQueue):
    def __init__(self):
        self.__data = LinkedList()

    def __len__(self):
        return len(self.__data)

    def enqueue(self, value):
        self.__data.insert_last(value)

    def dequeue(self):
        return self.__data.remove_first()

    def search(self, index):
        print('----->', index, len(self.__data))
        if 0 <= index <= len(self.__data) - 1:
            return self.__data.get_element_at(index)
        else:
            raise IndexError("Índice Inválido ou Inexistente")
