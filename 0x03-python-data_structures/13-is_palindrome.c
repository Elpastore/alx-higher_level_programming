#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * is_palindrome - function that checks if a SL is a palindrome
 * @head: pointer to head of the list
 * Return: 0 if not palindrome, 1 if it is
 */
int is_palindrome(listint_t **head)
{
	listint_t *original = *head;
	listint_t *current = *head;
	int len_list = 0;
	int i = 0;
	int *list;

	if (*head == NULL)
		return (1);
	while (current != NULL)
	{
		len_list++;
		current = current->next;
	}

	list = malloc(sizeof(int) * len_list);

	if (list == NULL)
	{
		return (0);
	}
	/*Copy the list into the array*/
	while (original != NULL)
	{
		list[i] = original->n;
		original = original->next;
		i++;
	}
	/*Compare the elements for palindromicity*/
	for (i = 0; i < len_list / 2; i++)
	{
		if (list[i] != list[len_list - i - 1])
		{
			free(list);
			return (0);    /* Not a palindrome*/
		}
	}
	free(list);
	return (1); /*It's a palindrome*/
}

