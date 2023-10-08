#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer of the head of the list *
 * Return: 1 if the list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow_ptr = *head, *fast_ptr = *head;
	listint_t *second_half, *prev_of_slow_ptr = *head;
	listint_t *mid_node = NULL;
	int res = 1; /* Initialize the result */

	if (*head == NULL || (*head)->next == NULL)
	return (1); /* A single node is a palindrome */
	/* Get the middle of the list */
	while (fast_ptr != NULL && fast_ptr->next != NULL)
	{
	fast_ptr = fast_ptr->next->next;
	prev_of_slow_ptr = slow_ptr;
	slow_ptr = slow_ptr->next;
	}
	/* Fast_ptr would become NULL only if there are even nodes in the list */
	/* MidNode of the linked list */
	if (fast_ptr != NULL)
	{
	mid_node = slow_ptr;
	slow_ptr = slow_ptr->next;
	}
	/* Reverse the second half and compare it with the first half */
	second_half = slow_ptr;
	prev_of_slow_ptr->next = NULL; /* NULL-terminate first half */

	reverse_list(&second_half); /* Reverse the second half */
	res = compare_lists(*head, second_half); /* Compare */
	/* Construct the original linked list back */
	reverse_list(&second_half); /* Reverse the second half again */
	if (mid_node != NULL)
	{
	prev_of_slow_ptr->next = mid_node;
	mid_node->next = second_half;
	}
	else
	{
	prev_of_slow_ptr->next = second_half;
	}
	return (res);
}

/**
 * reverse_list - reverses a linked list
 * @head_ref: pointer to pointer of the head of the list
 */
void reverse_list(listint_t **head_ref)
{
	listint_t *prev = NULL;
	listint_t *current = *head_ref;
	listint_t *next = NULL;

	while (current != NULL)
	{
	next = current->next;
	current->next = prev;
	prev = current;
	current = next;
	}

	*head_ref = prev;
}

/**
 * compare_lists - compares two linked lists
 * @head1: pointer to the head of the first list
 * @head2: pointer to the head of the second list
 *
 * Return: 1 if the lists are equal, 0 otherwise
 */
int compare_lists(listint_t *head1, listint_t *head2)
{
	listint_t *temp1 = head1;
	listint_t *temp2 = head2;

	while (temp1 && temp2)
	{
	if (temp1->n == temp2->n)
	{
	temp1 = temp1->next;
	temp2 = temp2->next;
	}
	else
	{
	return (0);
	}
	}

	if (temp1 == NULL && temp2 == NULL)
	return (1);

	return (0);
}
