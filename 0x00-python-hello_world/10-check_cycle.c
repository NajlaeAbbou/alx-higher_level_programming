#include "lists.h"

/**
 * check_cycle - function checks if a singly linked list has a cycle in it.
 * @list: pointer
 * Return: 0 if no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *now, *flag;

	if (list == NULL || list->next == NULL)
		return (0);
	now = list;
	flag = now->next;

	while (now != NULL && flag->next != NULL
		&& flag->next->next != NULL)
	{
		if (now == flag)
			return (1);
		now = flag->next;
		flag = flag->next->next;
	}
	return (0);
}
