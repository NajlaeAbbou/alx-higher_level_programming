#include "lists.h"
#include <stddef.h>
/**
  * listint_len - Counts the number of elements in a linked list
  * @h: The linked list to count
  *
  * Return: Number of elements in the linked list
  */
size_t listint_len(const listint_t *h)
{
        int l = 0;

        while (h != NULL)
        {
                ++l;
                h = h->next;
        }

        return (l);
}
/**
  * is_palindrome - Checks if a singly linked list is a palindrome
  * @head: The head of the singly linked list
  *
  * Return: 0 if it is not a palindrome, 1 if it is a palindrome
  */
int is_palindrome(listint_t **head)
{
    listint_t *st = NULL, *end = NULL;
    unsigned int i = 0, lenght = 0, lencyc = 0, lenlist = 0;

    if (head == NULL)
        return (0);

    if (*head == NULL)
        return (1);
    
    st = *head;
    lenght = listint_len(st);
    lencyc = lenght * 2;
    lenlist = lencyc - 2;
    end = *head;

    for (; i < lencyc; i = i + 2)
    {
        if (st[i].n != end[lenlist].n)
            return (0);

        lenlist = lenlist - 2;
    }

    return (1);
}

