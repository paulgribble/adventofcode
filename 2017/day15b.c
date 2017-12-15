
#include <stdio.h>
#include <math.h>

int main(int argc, char *argv[]) {


	long int mask = (1 << 16) - 1; // create bit mask for lowest 16 bits of a long int
	// if ((a & mask) == (b & mask)) // compare lowest 16 bits of a and b

	long int a = 516;
	long int b = 190;

//	long int a = 65;
//	long int b = 8921;

	long int af = 16807;
	long int bf = 48271;
	long int m = 2147483647;

	int match = 0;

	int n = 5e6;
	int count = 0;
	int aok, bok;
	for (int i=0; i<n; i++) {
		aok = 0;
		bok = 0;
		while (aok==0){
			a = a*af % m;
			if ((a % 4)==0) aok = 1;
		}
		while (bok==0){
			b = b*bf % m;
			if ((b % 8)==0) bok = 1;
		}
		match = ((a & mask) == (b & mask));
		if (match) count += 1;
//		printf("%12ld %12ld %3d\n", a, b, match);
	}
	printf("part 2: the judge's final count is %d\n", count);

	return 0;
}
