#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * main - create even numbered list non-palindrome, each half with equal sum, and check if it is a palindrome
 *
 * Return: Always 0.
 */
int main(void)
{
	listint_t *head;

	head = NULL;
	add_nodeint_end(&head, 8);
	add_nodeint_end(&head, 50);
	add_nodeint_end(&head, 0);
	add_nodeint_end(&head, 72);
	add_nodeint_end(&head, 72);
	add_nodeint_end(&head, 0);
	add_nodeint_end(&head, 8);
	add_nodeint_end(&head, 50);
	print_listint(head);

	if (is_palindrome(&head) == 1)
		printf("Linked list is a palindrome\n");
	else
		printf("Linked list is not a palindrome\n");

	free_listint(head);

	return (0);
}
