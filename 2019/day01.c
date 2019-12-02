#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(int argc, char *argv[]) {

	FILE *fid = fopen("day01_input.txt","r");
	int fuel = 0;
	int f;
	while (!feof(fid)) {
		fscanf(fid, "%d", &f);
		fuel = fuel + floor(f/3)-2;
	}
	fclose(fid);
	printf("Part 1: fuel = %d\n", fuel);

	fid = fopen("day01_input.txt","r");
	int fm;
	fuel = 0;
	while (!feof(fid)) {
		fm = 0;
		fscanf(fid, "%d", &f);
		f = floor(f/3)-2;
		while (f > 0) {
			fm = fm + f;
			f = floor(f/3)-2;
		}
		fuel = fuel + fm;
	}
	fclose(fid);
	printf("Part 2: fuel = %d\n", fuel);

	return 0;
}