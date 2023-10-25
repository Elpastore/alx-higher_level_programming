#!/usr/bin/python3
"""
Singly linked list Class Node
"""


class Node:
    """ Class node"""
    def __init__(self, data, next_node=None):

        """Class of node"""
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """ return the data"""

        return self.__data

    @data.setter
    def data(self, value):
        """
            sets data
            Args:
            -value (int)
            Raise:
                -TypeError: check if integer
        """
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """ Retrive the next_node """

        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ set the value
        Args:
            -value (int)
        """
        if (value is not None and not isinstance(value, Node)):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


"""
Module for the singly linked list itself
"""


class SinglyLinkedList:
    """ Singly linked list"""
    def __init__(self):
        """ Initialization of SLL"""

        self.__head = None

    def sorted_insert(self, value):
        """
        Method that insert a new_node
        Args:
            -value (int)
        """
        new_node = Node(value)
        if not self.__head or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return
        else:
            current = self.__head
            while current.next_node and current.next_node.data < value:
                current = current.next_node
            if current.next_node:
                new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Method for printing list"""
        new_list = []
        current = self.__head
        while current:
            new_list.append(str(current.data))
            current = current.next_node
        return "\n".join(new_list)
