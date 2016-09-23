#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#define TESTBYTES 250000000

int main()
{
	// Make char pointer called testpointer
	char * testpointer;
	// Start timer for write.
	long timestart=clock();
	// Malloc pointer and assign all values to 0
	testpointer=malloc(TESTBYTES);
	for (int i=0; i<TESTBYTES; i++) { *(testpointer+i)=0; }
	// End timer, print write IOPS of RAM
	long timefinish = clock();
	double ramwritetime = (double)timefinish-(double)timestart;
	printf("%f\n", (double)TESTBYTES/ramwritetime*CLOCKS_PER_SEC);

	// Start timer for read.
	timestart=clock();
	// Read all values once.
	for (int i=0; i<TESTBYTES; i++) { *(testpointer+i); }
	// End timer and print Read IOPS of RAM.
	timefinish=clock();
	printf("%f\n", (double)TESTBYTES/((double)timefinish-(double)timestart)*CLOCKS_PER_SEC);
}