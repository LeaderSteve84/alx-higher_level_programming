#!/usr/bin/python3
"""Write a class Node that defines a node of a singly linked list"""


class Node:
    """Define class Node"""

    def __init__(self, data, next_node=None):
        """Initialize a class Node..

        Args:
            size (int): The size of the new square.
            position (int, int): The position of the class square.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrive the current size of square"""
        return (self.__data)

    @data.setter
    def data(self, value):
        """set the value into the data.

        Args:
            value (int): an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieve the position of the square"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """insert the value into the new_node.

        Args:
            value (int): an integer value.
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Define class SinglyLinkedList"""

    def __init__(self):
        """Initialize a class Singly-linked list"""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node to the Singly-linked list.
        In order of numerical position.

        Args:
            value (Node): The data value for the new Node to insert.
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            current = self.__head
            while (
                    current.next_node is not None and
                    current.next_node.data < value
            ):
                current = current.next_node
            new.next_node = current.next_node
            current.next_node = new

    def __str__(self):
        """a print function rep. of a singly Linked-list"""
        values = []
        current = self.__head
        while current is not None:
            values.append(str(current.data))
            current = current.next_node
        return ('\n'.join(values))
