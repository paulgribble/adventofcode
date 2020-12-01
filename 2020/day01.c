#include <stdio.h>
#include <stdlib.h>
#include <string.h>

long int plg_filelen(char *filename) {
  FILE *fid = fopen(filename, "r");
  fseek(fid, 0, SEEK_END);
  long int len = ftell(fid);
  fclose(fid);
  return len;
}

char * plg_readfile(char *filename, long int fsize) {
  char *buf = malloc(fsize + 1);
  FILE *fid = fopen(filename, "r");
  fread(buf, fsize, 1, fid);
  fclose(fid);
  return buf;
}

int main(int argc, char *argv[]) {
	long int n = plg_filelen("day01_input.txt");
	// printf("file len is %ld\n", n);
	char *buf = malloc(sizeof(char)*n);
	buf = plg_readfile("day01_input.txt", n);

	for (int i=0; i<n; i++) {
		printf("%c", buf[i]);
	}

	free(buf);
	return 0;
}
