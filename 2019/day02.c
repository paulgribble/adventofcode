#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int day2run(int *oc, int oclen) {
 	int i = 0;
 	int i1, i2, i3;
	while (i <= oclen-4) {
		i1 = oc[i+1];
		i2 = oc[i+2];
		i3 = oc[i+3];
		if (oc[i]==1)
			oc[i3] = oc[i1] + oc[i2];
		else if (oc[i]==2)
			oc[i3] = oc[i1] * oc[i2];
		else if (oc[i]==99)
			break;
		i = i + 4;
	}
  	return oc[0];
}

int main(int argc, char *argv[]) {

	FILE *fid = fopen("day02_input.txt", "r");
	int opcodes[500];
	int i=0;
	while (!feof(fid)) {
		fscanf(fid, "%d,",&opcodes[i]);
		i = i + 1;
	}
	fclose(fid);
	int n = i;

	int opcodesp1[n];
	for (int i=0; i<n; i++) opcodesp1[i] = opcodes[i];
	opcodesp1[1] = 12;
	opcodesp1[2] = 2;
	int p1 = day2run(opcodesp1, n);
	printf("Part 1: answer is = %d\n", p1);

	int opcodesp2[n];
	int p2;
	for (int i=0; i<100; i++) {
		for (int j=0; j<100; j++) {
			for (int i=0; i<n; i++) opcodesp2[i] = opcodes[i];
			opcodesp2[1] = i;
			opcodesp2[2] = j;
			p2 = day2run(opcodesp2, n);
			if (p2 == 19690720) {
				printf("Part 2: answer is %d\n", 100*i+j);
				break;
			}
		}
		if (p2 == 19690720) break;
	}

	return 0;
}