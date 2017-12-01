#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// 1 2 3   0,0 0,1 0,2
// 4 5 6   1,0 1,1 1,2
// 7 8 9   2,0 2,1 2,2

int main(int argc, char *argv[]) {

  int PAD[3][3] = {{1,2,3},{4,5,6},{7,8,9}};
  
  int row=1; // 
  int col=1; // start at "5" key

  FILE *fid = fopen("day2_input.txt","r");
  char c;
  while ((c=fgetc(fid)) != EOF) {
    if (c=='L') col=col-1;
    if (c=='R') col=col+1;
    if (c=='U') row=row-1;
    if (c=='D') row=row+1;
    if (row<0) row=0; if (row>2) row=2;
    if (col<0) col=0; if (col>2) col=2;
    if (c=='\n') printf("*** (%d,%d): %d ***\n",row,col,PAD[row][col]);
  }
  
  fclose(fid);
  return 0;

}
