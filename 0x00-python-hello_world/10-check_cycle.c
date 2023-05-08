#include "lists.h"

/**
 * check_cycle - function for checking loop in a linked list
 * @list: start of a LL
 *
 * Return: 1 when passed, and 0 when failed
 */

int check_cycle(listint_t *list)
{
	listint_t *notFast, *whenFast;

	if (!list)
	{
		return (0);
	}
	notFast = list;
	whenFast = list->next;
	while (whenFast && notFast && whenFast->next)
	{
		if (notFast == whenFast)
		{
			return (1);
		}
		notFast = notFast->next;
		whenFast = whenFast->next->next;
	}
	return (0);
}
