#include <stdio.h>

int main(int argc, char *argv[]) {

	FILE *fid = fopen("day1_input.txt","r");
	char c,cprev;
	cprev = 0;
	int sum = 0;
	int is_first = 1;
	int n_first;
	while ((c=fgetc(fid)) != EOF) {
		if (is_first) {
			n_first = c-'0';
			is_first = 0;
		}
		if (c==cprev) {
			sum = sum + (c-'0');
			printf("%c %c %d\n", c, cprev, sum);
		}
		cprev = c;
	}
	if ((cprev-'0')==n_first) sum = sum +  n_first;
	printf("%d %d %d\n", cprev-'0', n_first, sum);
	fclose(fid);
	printf("sum = %d\n", sum);
	return 0;
}
