#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <pthread.h>
#include <sys/sysinfo.h>
#define TESTOS 500000000

void *test(void *args)
{
	int x=0;
	for (int i=0; i<TESTOS; i++)
	{
		x+=2;
	}
}

int main()
{
	int numCPU=get_nprocs();
	pthread_t threads[numCPU];
	// Start timer. Increment x many times.
	long timestart = clock();
	for (int i=0; i<numCPU; i++)
	{
		pthread_create(&threads[i], NULL, test, NULL);
	}
	for (int i=0; i<numCPU; i++)
	{
		pthread_join(threads[i], NULL);
	}
	long timefinish = clock();
	printf("%f\n", (double)TESTOS/((double)timefinish-(double)timestart)*CLOCKS_PER_SEC*numCPU*numCPU);
}
