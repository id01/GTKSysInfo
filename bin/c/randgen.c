#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int main()
{
	srand(clock());
	long timestart = clock();
	for (int i=0; i<25000000; i++)
	{
		rand();
	}
	long timefinish = clock();
	printf("%f\n", 25000000.0/((double)timefinish-(double)timestart)*CLOCKS_PER_SEC);
}
