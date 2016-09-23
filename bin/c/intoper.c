#include <stdio.h>
#include <time.h>
#define TESTOS 500000000

int main()
{
	int x=0;
	// Start timer. Increment x many times.
	long timestart = clock();
	for (int i=0; i<TESTOS; i++)
	{
		x+=2;
	}
	// End timer. Print Int Operations Per Second.
	long timefinish = clock();
	printf("%f\n", (double)TESTOS/((double)timefinish-(double)timestart)*CLOCKS_PER_SEC);
}
