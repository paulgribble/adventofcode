#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int bots[210][2];

void showbots() {
  printf("-------------------\n");  
  for (int i=0; i<210; i++) {
    printf("bot %4d: %4d %4d\n",i,bots[i][0],bots[i][1]);
  }
  printf("-------------------\n");  
}

int main(int argc, char *argv[]) {

  for (int i=0; i<210; i++) for (int j=0; j<2; j++) bots[i][j] = -1;

  
  FILE *fid = fopen("day10_input.txt","r");
  
  fclose(fid);

  
  showbots();
  
  return 0;

}
