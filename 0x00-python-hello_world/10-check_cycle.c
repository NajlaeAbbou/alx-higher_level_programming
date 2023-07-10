#include "lists.h"

/**
 * check_cycle - function checks if a singly linked list has a cycle in it.
 * @list: pointer
 * Return: 0 if no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *curr, *check;

	if (!list)
	{
		return (0);
	}
	
	curr = list;
	check = list->next;
	while (check && curr && check->next)
	{
		if (curr == check)
		{
			return (1);
		}
		curr = curr->next;
		check = check->next->next;
	}
	return (0);
}
