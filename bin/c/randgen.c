// id01
// checks random number generation speed
#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#define TESTOS 25000000

int main()
{
	srand(clock());
	long timestart = clock();
	for (int i=0; i<TESTOS; i++)
	{
		rand();
	}
	long timefinish = clock();
	printf("%f\n", (double)TESTOS/((double)timefinish-(double)timestart)*CLOCKS_PER_SEC);
}
