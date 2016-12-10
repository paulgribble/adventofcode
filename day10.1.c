#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]) {

  char *buf = malloc(sizeof(char)*16);
  FILE *fid = fopen("day10_input.txt","r");
  int b1,blo,bhi,dummyint1,dummyint2;
  int bots[256][2];
  int val;
  for (int i=0; i<256; i++) { bots[i][0] = -1; bots[i][1] = -1; }
  char *dummy = malloc(sizeof(char)*64);
  
  while (fscanf(fid,"%s",buf) != EOF) {
    if (strcmp(buf,"bot")==0) {
      fscanf(fid,"%d",&b1);
      fscanf(fid,"%s%s%s",dummy,dummy,dummy); // gives low to
      fscanf(fid,"%s",buf);
      if (strcmp(buf,"output")==0) {
	bots[b1][0] = -1;
	fscanf(fid,"%d",&dummyint1);
	fscanf(fid,"%s%s%s",dummy,dummy,dummy); // and hi to
	fscanf(fid,"%s",buf);
	if (strcmp(buf,"output")==0) {
	  bots[b1][1] = -1;
	  fscanf(fid,"%d",&dummyint2);
	  printf("bot %d gives low to output %d and high to output %d\n",b1,dummyint1,dummyint2);
	}
	else {
	  fscanf(fid,"%d",&bhi);
	  // give bots[b1] hi to bots[bhi]
	  // (need to write code to do it here)
	  printf("bot %d gives low to output %d and high to bot %d\n",b1,dummyint1,bhi);
	}
      }
      else {
	fscanf(fid,"%d",&blo);
	// give bots[b1] lo to bots[blo]
	// (need to write code to do it here)

	printf("bot %d gives low to bot %d",b1,blo);
	bots[b1][0] = -1;
	fscanf(fid,"%s%s%s",dummy,dummy,dummy); // and high to
	fscanf(fid,"%s",buf);
	if (strcmp(buf,"output")==0) bots[b1][1] = -1;
	else {
	  fscanf(fid,"%d",&bhi);
	  // give bots[b1] hi to bots[bhi]
	  // (need to write code to do it here)
	  printf(" and high to bot %d\n",bhi);

	  bots[b1][1] = -1;
	}
      }
    }
    else {
      fscanf(fid,"%d",&val);
      fscanf(fid,"%s%s%s",dummy,dummy,dummy); // goes to bot
      fscanf(fid,"%d",&b1);
      // give bots[b1] value val
      // (need to write code to do it here)

      printf("value %d goes to bot %d\n",val,b1);
    }    
  }

  free(dummy);
  fclose(fid);
  free(buf);
  
  return 0;

}
