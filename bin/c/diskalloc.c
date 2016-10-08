#include <string.h>
#include <time.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
	// Read args
	if (argc!=2)
	{
		return 1;
	}
	char * arg = malloc(1024);
	strcpy(arg,argv[1]);
	// Open File
	FILE *testfile = fopen(arg, "w");
	if (!testfile) { return 1; }
	// Start timer. Write to file many times.
	long timestart = clock();
	for (int i=0; i<100000000; i++)
	{
		fputc(32, testfile);
	}
	// End timer. Print write Bps of file.
	long timefinish = clock();
	printf("%f\n", 100000000.0/((double)timefinish-(double)timestart)*CLOCKS_PER_SEC);
	// Close file and reopen.
	fclose(testfile);
	testfile=fopen(arg, "r");
	// Start timer. Read to file many times.
	timestart = clock();
	for (int i=0; i<100000000; i++)
	{
		fgetc(testfile);
	}
	timefinish = clock();
	// End timer. Print read Bps of file.
	printf("%f\n", 100000000.0/((double)timefinish-(double)timestart)*CLOCKS_PER_SEC);
	remove(arg);
}
