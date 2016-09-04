#include <stdio.h>
#include <time.h>

int main()
{
	int x=0;
	// Start timer. Increment x many times.
	long timestart = clock();
	for (int i=0; i<500000000; i++)
	{
		x+=2;
	}
	// End timer. Print Int Operations Per Second.
	long timefinish = clock();
	printf("%f\n", 500000000.0/((double)timefinish-(double)timestart)*CLOCKS_PER_SEC);
}
