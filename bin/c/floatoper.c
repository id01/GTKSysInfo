#include <stdio.h>
#include <time.h>

int main()
{
	double x=0;
	// Start timer. Increment x many times.
	long timestart = clock();
	for (int i=0; i<250000000; i++)
	{
		x+=2.5;
	}
	// End timer. Print Int Operations Per Second.
	long timefinish = clock();
	printf("%f\n", 250000000.0/((double)timefinish-(double)timestart)*CLOCKS_PER_SEC);
}
