#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int min(x,y) {
  if (x<y) return x;
  else return y;
}

int max(x,y) {
  if (x>y) return x;
  else return y;
}

struct bot {
  int val0;
  int val1;
  int *low_to;
  int *high_to;
} bots[300];

int outputs[300];

void give(val,botno) {
  if (bots[botno].val0 == 0) {
    bots[botno].val0 = val;
  }
  else {
    bots[botno].val1 = val;
  }
}

int main(int argc, char *argv[]) {

char buf[256];
int r, value, botno, low, high;

  FILE *fid = fopen("day10_input.txt","r");

  while (fgets(buf, 256, fid) != NULL) {
    if ((r=sscanf(buf, "value %d goes to bot %d", &value, &botno)) != 0) {
      printf("value %d goes to bot %d\n", value, botno);
      give(value,botno);
    }
    else if ((r=sscanf(buf, "bot %d gives low to bot %d and high to bot %d", \
		       &botno, &low, &high)) == 3) {
      printf("bot %d gives low to bot %d and high to bot %d\n", \
	     botno, low, high);
      bots[botno].low_to = &(bots[low].val0);
      bots[botno].high_to = &(bots[high].val1);
}
    else if ((r=sscanf(buf, "bot %d gives low to output %d "
		       "and high to bot %d", &botno, &low, &high)) == 3) {
      printf("bot %d gives low to output %d and high to bot %d\n", \
	     botno, low, high);
      bots[botno].low_to = &(outputs[low]);
      bots[botno].high_to = &(bots[botno].val1);
    }
    else if ((r=sscanf(buf, "bot %d gives low to output %d "
		       "and high to output %d", &botno, &low, &high)) == 3) {
      printf("bot %d gives low to output %d and high to output %d\n", \
	     botno, low, high);
      bots[botno].low_to = &(outputs[low]);
      bots[botno].high_to = &(outputs[high]);
    }
  }


  fclose(fid);
  return 0;
  
}

