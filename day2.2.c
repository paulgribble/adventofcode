#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//     1               0,2
//   2 3 4         1,1 1,2 1,3
// 5 6 7 8 9   2,0 2,1 2,2 2,3 2,4
//   A B C         3,1 3,2 3,3
//     D               4,2

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

  char PAD[5][5] = {'0','0','1','0','0',
		    '0','2','3','4','0',
		    '5','6','7','8','9',
                    '0','A','B','C','0',
                    '0','0','D','0','0'};
  
  int row=2; // 
  int col=0; // start at "5" key
  char *buf = plg_readfile("day2_input.txt");

  char *pt = strtok(buf,"\n");
  char c;
  while (pt != NULL) {
    for (int i=0; i<strlen(pt); i++) {
      //      printf("(%d,%d) ",row,col);
      c = pt[i];
      //      printf("%c ",c);
      if (c=='L') if (col>0) if (PAD[row][col-1]!='0') col=col-1;
      if (c=='R') if (col<4) if (PAD[row][col+1]!='0') col=col+1;
      if (c=='U') if (row>0) if (PAD[row-1][col]!='0') row=row-1;
      if (c=='D') if (row<4) if (PAD[row+1][col]!='0') row=row+1;      
      //      printf("(%d,%d)\n",row,col);
    }
    printf("*** (%d,%d): %c ***\n",row,col,PAD[row][col]);
    pt = strtok(NULL,"\n");
  }
    
  free(buf);
  return 0;

}
