#include "lists.h"

/**
 * insert_node - puts a number in a sorted singly-linked list.
 * @head: points the head of the linked list.
 * @number: number to put in SLL.
 * Return: NULL if fail
 *         Otherwise - return pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *newNode;

	newNode = malloc(sizeof(listint_t));
	if (newNode == NULL)
		return (NULL);
	newNode->n = number;

	if (node == NULL || node->n >= number)
	{
		newNode->next = node;
		*head = newNode;
		return (newNode);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	newNode->next = node->next;
	node->next = newNode;

	return (newNode);
}
