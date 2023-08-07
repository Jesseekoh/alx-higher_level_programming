#include "lists.h"

/**
 * is_circular - checks if a singly linked list is circular
 * @head: pointer to head ot list
 * Return: 1 if list is circular; 0 if list is not circular
 */

int is_circular(listint_t *head)
{
	listint_t *current, *check;

	if (head == NULL || head->next == NULL)
		return (0);
	current = head;
	check = current->next;

	while (current != NULL && check->next != NULL && check->next->next != NULL)
	{
		if (current == check)
			return (1);
		current = current->next;
		check = check->next->next;
	}
	return (0);
}
