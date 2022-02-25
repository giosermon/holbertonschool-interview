#include "slide_line.h"
#include <stdio.h>

/**
 * slide_line - function that reporduce 2048 game but in a single line
 * @line: pointer to the array
 * @size: size of array
 * @direction: direction 
 * Return: 1 in success, or 0 on failure
 */
int slide_line(int *line, size_t size, int direction)
{
	int end = size, i = 0, j = 1;

	if (direction == SLIDE_RIGHT)
	{
		end = -1;
		i = size - 1;
		j = size - 2;
	}
	else if (direction != SLIDE_LEFT)
		return (0);

	for (; j != end; j += direction)
	{
		/* slide to 'i' position */
		if (line[i] == 0 && line[j] != 0)
		{
			line[i] = line[j];
			line[j] = 0;
			continue;
		}
		/* merge */
		if (line[i] != 0 && line[i] == line[j])
		{
			line[i] += line[j];
			line[j] = 0;
			i += direction;
			continue;
		}
		/* slide to 'i'+1/'i'-1 position */
		if (line[i] != 0 && line[j] != 0 && line[i] != line[j])
		{
			if (i + direction != j)
			{
				line[i + direction] = line[j];
				line[j] = 0;
			}
			i += direction;
		}
	}
	return (1);
}
