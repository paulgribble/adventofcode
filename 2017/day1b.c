#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *plg_readfile(char *filename) {
  FILE *fid = fopen(filename, "r");
  fseek(fid, 0, SEEK_END);
  long fsize = ftell(fid);
  fseek(fid, 0, SEEK_SET);
  char *buf = malloc(fsize + 1);
  fread(buf, fsize, 1, fid);
  fclose(fid);
  return buf;
}

int main(int argc, char *argv[]) {

	char *buf = plg_readfile("day1_input.txt");
	int buflen = strlen(buf);
	
	
	free(buf);
	return 0;
}
