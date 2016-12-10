#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]) {

  char *buf = malloc(sizeof(char)*16);
  FILE *fid = fopen("day10_input.txt","r");
  int b1,blo,bhi;
  int outputs[20][24];
  for (int i=0; i<20; i++) for (int j=0; j<24; j++) outputs[i][j]=0;
  int bots[256][24];
  for (int i=0; i<256; i++) for (int j=0; j<24; j++) bots[i][j]=0;
  
  while (fscanf(fid,"%s",buf) != EOF) {
    if (strcmp(buf,"bot")==0) {
      
    }
  }
  
  fclose(fid);
  free(buf);
  
  return 0;

}
