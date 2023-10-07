#include "lists.h"
#include "lists.h"
#include <stdio.h>
/**
 * reverse_listint -  reverses a listint_t linked list.
 * @head: the head of list
 * Return: pointer to the first
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t  *next;

	if (*head == NULL)
		return (NULL);
	while (*head != NULL)
	{
		next = (*head)->next; /*Store the next node*/
		(*head)->next = prev; /*Reverse the pointer*/
		prev = *head; /*Move prev one step ahead*/
		*head = next; /*Move head one step ahead*/
	}
	*head = prev;
	return (*head);
}
/**
 * is_palindrome - function that checks if a SL is a palindrome
 * @head: pointer to head to the list
 * Return: 0 if not palindrome 1 if it is
 */
int is_palindrome(listint_t **head)
{
	listint_t *original = *head;
	listint_t *current = *head;
	listint_t *reverse = reverse_listint(head);
	int len_list = 0;
	int i;
	if(*head == NULL)
		return (1);
	while (current != NULL)
	{
		len_list++;
		current = current->next;
	}
	if (len_list == 1)
		return (1);
	for (i = 0; i < (len_list / 2); i++)
	{
		if (original->n != reverse->n)
			return (0);
		original = original->next;
		reverse = reverse->next;
	}
	return (1);
}
