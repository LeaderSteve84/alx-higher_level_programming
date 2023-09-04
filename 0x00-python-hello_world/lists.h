#ifndef LISTS_H
#define LISTS_H

#include <stdio.h>
#include <stdlib.h>
int check_cycle(listint_t *list);
void free_listint(listint_t *head);
listint_t *add_nodeint(listint_t **head, const int n);
size_t print_listint(const listint_t *h);




#endif
