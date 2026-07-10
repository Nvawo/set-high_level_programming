#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the list
 *
 * Return: 1 if palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *current;
	int *array;
	int count, i;

	if (head == NULL || *head == NULL)
		return (1);

	/* Count the nodes */
	count = 0;
	current = *head;
	while (current != NULL)
	{
		count++;
		current = current->next;
	}

	array = malloc(sizeof(int) * count);
	if (array == NULL)
		return (0);

	current = *head;
	for (i = 0; i < count; i++)
	{
		array[i] = current->n;
		current = current->next;
	}

	for (i = 0; i < count / 2; i++)
	{
		if (array[i] != array[count - 1 - i])
		{
			free(array);
			return (0);
		}
	}

	free(array);
	return (1);
}
