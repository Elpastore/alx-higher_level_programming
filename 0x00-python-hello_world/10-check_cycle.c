#include "lists.h"
/**
 * check_cycle - function that checks presence of a cycle in list
 * @list: the pointer to the list head
 * Return: 1 if there is a cycle otherwise 0
 */
int check_cycle(listint_t *list)
{
	listint_t *harse = list;
	listint_t *tortoise = list;

	while (harse != NULL && harse->next != NULL)
	{
		tortoise = tortoise->next;
		harse = harse->next->next;

		if (tortoise == harse)
		{
			return (1);
		}
	}
	return (0);
}
