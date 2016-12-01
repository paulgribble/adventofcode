#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]) {

  FILE *fid = fopen("day1_input.txt", "r");
  fseek(fid, 0, SEEK_END);
  long fsize = ftell(fid);
  fseek(fid, 0, SEEK_SET);
  char *buf = malloc(fsize + 1);
  fread(buf, fsize, 1, fid);
  fclose(fid);

  char *pt;
  char dir;
  int steps;
  int X = 0;
  int Y = 0;
  
  int facing = 0; // 0=N, 1=W, 2=S, 3=E
  pt = strtok(buf,", ");
  while (pt != NULL) {
    //    printf("%s\n", pt);
    if (pt !=NULL) {
      dir = pt[0];
      steps = atoi(&(pt[1]));
      printf("%d | %4d,%4d | ", facing, X, Y);
      if (dir=='L') facing = (facing+1 % 4 + 4) % 4;
      if (dir=='R') facing = (facing-1 % 4 + 4) % 4;
      if (facing==0) Y = Y + steps;
      if (facing==1) X = X - steps;
      if (facing==2) Y = Y - steps;
      if (facing==3) X = X + steps;
      printf("%c | ", dir);
      printf("%3d | ", steps);
      printf("%d | %4d,%4d\n", facing, X, Y);

    }
    pt = strtok(NULL,", ");
  }
  
  free(buf);

  printf("X,Y = %d,%d\n", X, Y);
  printf("blocks away = %d\n", abs(X)+abs(Y));
  
  return 0;

}

