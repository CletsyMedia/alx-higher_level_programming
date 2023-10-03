#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly linked list.
 * @head: A pointer to a pointer to the head of the list.
 * @number: The integer to insert into the list.
 *
 * Return: The address of the new node, or NULL if it fails.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current, *prev;

	if (head == NULL)
	return (NULL);

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
	return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	current = *head;
	prev = NULL;

	/* Traverse the list to find the correct position to insert the new node. */
	for (; current != NULL && current->n < number; prev = current, current =
	current->next)
	{
	/* Do nothing in the loop; the traversal is handled in the header. */
	}

	if (prev == NULL)
	{
	new_node->next = *head;
	*head = new_node;
	}
	else
	{
	prev->next = new_node;
	new_node->next = current;
	}

	return (new_node);
}
