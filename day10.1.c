#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]) {

  char buf[256];
  int r, value, botno, low, high;

  FILE *fid = fopen("day10_input.txt","r");

  while (fgets(buf, 256, fid) != NULL) {
    if ((r=sscanf(buf, "value %d goes to bot %d", &value, &botno)) != 0) {
      printf("value %d goes to bot %d\n", value, botno);
    }
    else if ((r=sscanf(buf, "bot %d gives low to bot %d and high to bot %d", \
		       &botno, &low, &high)) == 3) {
      printf("bot %d gives low to bot %d and high to bot %d\n", \
	     botno, low, high);
    }
    else if ((r=sscanf(buf, "bot %d gives low to output %d "
		       "and high to bot %d", &botno, &low, &high)) == 3) {
      printf("bot %d gives low to output %d and high to bot %d\n", \
	     botno, low, high);
    }
    else if ((r=sscanf(buf, "bot %d gives low to output %d "
		       "and high to output %d", &botno, &low, &high)) == 3) {
      printf("bot %d gives low to output %d and high to output %d\n", \
	     botno, low, high);
    }
  }


  fclose(fid);
  return 0;
  
}

