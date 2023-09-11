#include "lists.h"
#include <stddef.h>

listint_t *reverse_listint(listint_t **head);


/**
 *  reverse_listint - function reverses a singly_linked list
 *  @head: a pointer to a pointer
 *  Return: a pointer to the head of the reverse list.
 */

listint_t *reverse_listint(listint_t **head)
{
	listint_t *current = *head, *node, *previous = NULL;

	while (current)
	{
		node = current->next;
		current->next = previous;
		previous = current;
		current = node;
	}
	*head = previous;

	return (*head);
}

/**
 * is_palindrome - a function in C that checks if a singly
 * linked list is a palindrome.
 * @head: a pointer to a pointer
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *current, *rvs, *rvs_copy;
	size_t count = 0, i;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	current = *head;
	while (current)
	{
		count++;
		current = current->next;
	}
	current = *head;
	for (i = 0; i < (count / 2) - 1; i++)
	{
		current = current->next;
	}
	if ((count % 2) == 0 && current->n != current->next->n)
	{
		return (0);
	}
	current = current->next->next;
	rvs = reverse_listint(&current);
	rvs_copy = rvs;

	current = *head;
	while (rvs)
	{
		if (current->n != rvs->n)
			return (0);
		current = current->next;
		rvs = rvs->next;
	}
	reverse_listint(&rvs_copy);

	return (1);
}
