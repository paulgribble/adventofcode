#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// 1 2 3   0,0 0,1 0,2
// 4 5 6   1,0 1,1 1,2
// 7 8 9   2,0 2,1 2,2

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

  int PAD[3][3] = {1,2,3,4,5,6,7,8,9};
  
  int row=1; // 
  int col=1; // start at "5" key
  char *buf = plg_readfile("day2_input.txt");

  char *pt = strtok(buf,"\n");
  char c;
  while (pt != NULL) {
    for (int i=0; i<strlen(pt); i++) {
      //      printf("(%d,%d) ",row,col);
      c = pt[i];
      //      printf("%c ",c);
      if (c=='L') col=col-1;
      if (c=='R') col=col+1;
      if (c=='U') row=row-1;
      if (c=='D') row=row+1;
      if (row<0) row=0; if (row>2) row=2;
      if (col<0) col=0; if (col>2) col=2;
      //      printf("(%d,%d)\n",row,col);
    }
    printf("*** (%d,%d): %d ***\n",row,col,PAD[row][col]);
    pt = strtok(NULL,"\n");
  }
    
  free(buf);
  return 0;

}
