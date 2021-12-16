#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: Double pointer to head of list.
 * @number:  Number to insert.
 * Return: address of the new element or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;
	listint_t *tmp;

	current = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	if (*head == NULL)
	{
		new->next = NULL;
		*head = new;
	}
	else if (number < current->n)
	{
		new->next = current;
		*head = new;
	}
	else
	{
		while (current->next != NULL)
		{
			if (number < current->next->n)
				break;
			current = current->next;
		}
		tmp = current->next;
		current->next = new;
		new->next = tmp;
	}
	return (new);
}
