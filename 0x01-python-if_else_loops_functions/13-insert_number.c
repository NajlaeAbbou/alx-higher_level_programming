#include "lists.h"

/**
 * insert_node - xxx
 * @head: A pointer 
 * @number: The number to insert.
 * Return: If the function fails NULL.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *nv;

	nv = malloc(sizeof(listint_t));
	if (nv == NULL)
		return (NULL);
	nv->n = number;

	if (node == NULL || node->n >= number)
	{
		nv->next = node;
		*head = nv;
		return (nv);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	nv->next = node->next;
	node->next = nv;

	return (nv);
}

