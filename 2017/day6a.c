#include <stdio.h>
#include <stdlib.h>


int found(int **Blist, int *B, int Bn) {

	int match;
	for (int i=0; i<Bn; i++) {
		match = 1;
		for (int j=0; j<16; j++) {
			if (Blist[i][j] != B[j]) {
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


int main(int argc, char *argv[]) {

	int **Blist = malloc(1000*sizeof(int *));
	Blist[0] = malloc(16*sizeof(int));
	int Bn=1;

	FILE *fid = fopen("day6_input.txt","r");
	for (int i=0; i<16; i++) {
		fscanf(fid, "%d ", &Blist[0][i]);
	}
	fclose(fid);

	int done = 0;
	int imax;
	while (!done) {
		imax = max(Blist[Bn-1]);
		
	}

	for (int i=0; i<Bn; i++) {
		free(Blist[i]);
	}
	free(Blist);
	return 0;
}






