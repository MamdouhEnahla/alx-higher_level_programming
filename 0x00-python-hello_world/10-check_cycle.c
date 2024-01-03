#include <stdio.h>
#include <stdlib.h>
#include <lists.h>

/**
 * check_cycle - check code
 * @list: a pointer to list
 * 
 * Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
	listint_t *s = list, *f = list;

	while (f && f->next)
	{
		s = s->next;
		f = f->next->next;
		if (f == s)
			return (1);
	}
	return (0);
}
