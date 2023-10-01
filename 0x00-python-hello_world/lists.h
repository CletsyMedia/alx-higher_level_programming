#ifndef _LISTS_H
#define _LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - Structure for singly linked list
 * @n: Integer data stored in the node
 * @next: Pointer to the next node in the list
 *
 * Description: This structure defines a node for a singly linked list,
 * as used in the Holberton project.
 */
typedef struct listint_s
{
	int n;									/* Integer data stored in the node */
	struct listint_s *next; /* Pointer to the next node in the list */
} listint_t;

/* Function to add a new node to the beginning of a linked list */
listint_t *add_nodeint(listint_t **head, const int n);

/* Function to print elements of a linked list */
size_t print_listint(const listint_t *h);

/* Function to check if a linked list has a cycle */
int check_cycle(listint_t *list);

/* Function to free memory allocated for a linked list */
void free_listint(listint_t *head);

#endif /* _LISTS_H */
