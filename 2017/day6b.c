#include <stdio.h>
#include <stdlib.h>


int found(int **Blist, int Bn) {

	int match;
	for (int i=0; i<(Bn-1); i++) {
		match = 1;
		for (int j=0; j<16; j++) {
			if (Blist[i][j] != Blist[Bn-1][j]) {
				match = 0;
			}
		}
		if (match==1) return 1;
	}
	return 0;
}

int max(int *B) {
	int index = 0;
	int maxval = B[0];
	for (int i=0; i<16; i++) {
		if (B[i] > maxval) {
			index = i;
			maxval = B[i];
		}
	}
	return index;
}

void printBlist(int **Blist, int Bn) {
	for (int i=0; i<Bn; i++) {
		for (int j=0; j<16; j++) {
			printf("%3d ", Blist[i][j]);
		}
		printf("\n");
	}
	printf("----------------------------------------------------------------\n");
}

int main(int argc, char *argv[]) {

	int **Blist = malloc(10000*sizeof(int *));
	Blist[0] = malloc(16*sizeof(int));
	int Bn=1;

	FILE *fid = fopen("day6_input.txt","r");
	for (int i=0; i<16; i++) {
		fscanf(fid, "%d ", &Blist[0][i]);
	}
	fclose(fid);

	int done = 0;
	int imax;
	int nblocks;
	int ib;
	int steps = 0;
	while (!done) {
//		printBlist(Blist, Bn);
		imax = max(Blist[Bn-1]);
		nblocks = Blist[Bn-1][imax];
		Bn = Bn + 1;
		Blist[Bn-1] = malloc(16*sizeof(int));
		for (int i=0; i<16; i++) {
			Blist[Bn-1][i] = Blist[Bn-2][i];
		}
		for (int i=0; i<=nblocks; i++) {
			ib = (imax+i) % 16;
			Blist[Bn-1][ib] = Blist[Bn-1][ib] + 1;
			Blist[Bn-1][imax] = Blist[Bn-1][imax] - 1;
		}
		if (found(Blist, Bn)) {
			done = 1;
		}
		steps = steps + 1;
	}

	printf("steps=%d for first repeat.\n", steps);

	for (int i=0; i<16; i++) {
		Blist[0][i] = Blist[Bn-1][i];
	}
	Bn = 1;

	done = 0;
	steps = 0;
	while (!done) {
//		printBlist(Blist, Bn);
		imax = max(Blist[Bn-1]);
		nblocks = Blist[Bn-1][imax];
		Bn = Bn + 1;
		Blist[Bn-1] = malloc(16*sizeof(int));
		for (int i=0; i<16; i++) {
			Blist[Bn-1][i] = Blist[Bn-2][i];
		}
		for (int i=0; i<=nblocks; i++) {
			ib = (imax+i) % 16;
			Blist[Bn-1][ib] = Blist[Bn-1][ib] + 1;
			Blist[Bn-1][imax] = Blist[Bn-1][imax] - 1;
		}
		if (found(Blist, Bn)) {
			done = 1;
		}
		steps = steps + 1;
	}

	printf("steps=%d for second repeat.\n", steps);

	for (int i=0; i<Bn; i++) {
		free(Blist[i]);
	}
	free(Blist);
	return 0;
}






