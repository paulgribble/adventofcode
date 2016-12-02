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
  char *pt;
  char dir;
  int steps;
  int X = 0;
  int Y = 0;
  int grid[500][500];
  for (int i=0; i<500; i++) {
    for (int j=0; j<500; j++) {
      grid[i][j]=0;
    }
  }
  
  int facing = 0; // 0=N, 1=W, 2=S, 3=E
  pt = strtok(buf,", ");
  int visits;
  int stop = 0;
  while (pt != NULL) {
    //    printf("%s\n", pt);
    if (pt !=NULL) {
      dir = pt[0];
      steps = atoi(&(pt[1]));
      printf("%d | %4d,%4d | ", facing, X, Y);
      if (dir=='L') facing = facing+1;
      if (dir=='R') facing = facing-1;
      if (facing<0) facing=facing+4;
      if (facing>3) facing=facing-4;
      for (int i=0; i<steps; i++) {
        if (facing==0) Y = Y + 1;
        if (facing==1) X = X - 1;
        if (facing==2) Y = Y - 1;
        if (facing==3) X = X + 1;
        grid[X+200][Y+200] = grid[X+200][Y+200] + 1;
        visits = grid[X+200][Y+200];
        if (visits>1) {
          printf("*** blocks away = %d\n", abs(X)+abs(Y));
          stop = 1;
        }
	if (stop) break;
      }
      if (stop) break;
      printf("%c | ", dir);
      printf("%3d | ", steps);
      printf("%d | %4d,%4d | %d\n", facing, X, Y, visits);
    }
    pt = strtok(NULL,", ");
  }
  
  free(buf);

  printf("X,Y = %d,%d\n", X, Y);
  printf("blocks away = %d\n", abs(X)+abs(Y));
  
  return 0;

}

