#include <stdio.h>
#include <time.h>
#include <queue>
using std::queue;

int main()
{
	// Make a queue called x
	queue <signed char> x;
	// Start Timer. Push to queue
	long timestart = clock();
	for (int i=0; i<32000000; i++)
	{
		x.push(1);
	}
	// End timer and print Write IOPS of RAM.
	long timefinish = clock();
	double ramwritetime = double(timefinish)-double(timestart);
	printf("%f\n", 32000000.0/ramwritetime*CLOCKS_PER_SEC);
	// Start Timer for Read. Pop from queue into Y.
	timestart = clock();
	for (int i=0; i<32000000; i++)
	{
		x.front(); x.pop();
	}
	// End timer and print Read IOPS of RAM.
	timefinish = clock();
	printf("%f\n", 32000000.0/(double(timefinish)-double(timestart)-ramwritetime)*CLOCKS_PER_SEC);
}