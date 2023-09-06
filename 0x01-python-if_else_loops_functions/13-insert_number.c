#include "lists.h"
/**
* insert_node - a function in C that inserts a number
* into a sorted singly linked list.
* @head: pointer to the head of the linked list
* @number: The number to insert
* Return: the address of the new node, or NULL if it failed
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *new_node;

	current = *head;
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
	{
		return (NULL);
	}
	new_node->n = number;

	if (current == NULL || current->n >= number)
	{
		new_node->next = current;
		*head = new_node;
		return (new_node);
	}
	while (current && current->next && current->next->n < number)
	{
		current = current->next;
	}
	new_node->next = current->next;
	current->next = new_node;

	return (new_node);
}
