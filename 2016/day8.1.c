#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define ROWS 6
#define COLS 50

int show_screen(int screen[COLS][ROWS]) {
  int lit_pixels = 0;
  printf("\n+");
  for (int i=0; i<COLS; i++) {
    printf("-");
  }
  printf("+\n");
  for (int j=0; j<ROWS; j++) {
    printf("|");
    for (int i=0; i<COLS; i++) {
      if (screen[i][j]==1) {
	printf("#");
	lit_pixels = lit_pixels + 1;
      }
      else {
	printf(".");
      }
    }
    printf("|\n");
  }
  printf("+");
  for (int i=0; i<COLS; i++) {
    printf("-");
  }
  printf("+\n\n");
  return lit_pixels;
}


int main()
{

  FILE *fid = fopen("day8_input.txt", "r");
  char cmd[16];
  char rect_arg[16];
  char rotate_arg1[16];
  char rotate_arg2[16];
  char rotate_arg3[16];
  char rotate_arg4[16];
  int rect_rows, rect_cols;
  int rect_arg_len;
  int rect_arg_x;
  char *x;
  int rotate_arg_i, rotate_arg_n;
  int col[ROWS];
  int row[COLS];    
  int screen[COLS][ROWS];
  memset(screen, 0, sizeof(int)*ROWS*COLS);

  int nlines = 0;
  show_screen(screen);
  while (fscanf(fid,"%s",(char *)&cmd) != EOF) {
    printf("-----\n");
    if (strcmp(cmd,"rect")==0) {
      printf("%s ", cmd);
      fscanf(fid,"%s",(char *)&rect_arg);
      rect_arg_len = strlen(rect_arg);
      x = strchr(rect_arg,'x');
      rect_arg_x = (int)(x-rect_arg);
      rect_arg[rect_arg_x]='\0';
      rect_cols = atoi(rect_arg);
      rect_rows = atoi(&(rect_arg[rect_arg_x+1]));
      printf("%dx%d\n",rect_cols,rect_rows);
      for (int i=0; i<rect_cols; i++) {
	for (int j=0; j<rect_rows; j++) {
	  screen[i][j] = 1;
	}
      }
    }
    else if (strcmp(cmd,"rotate")==0) {
      printf("%s ", cmd);
      fscanf(fid,"%s",(char *)&rotate_arg1);
      printf("%s ",rotate_arg1);
      fscanf(fid,"%s",(char *)&rotate_arg2);
      printf("%s ",rotate_arg2);
      fscanf(fid,"%s",(char *)&rotate_arg3);
      printf("%s ",rotate_arg3);
      fscanf(fid,"%s",(char *)&rotate_arg4);
      printf("%s\n",rotate_arg4);
      x = strchr(rotate_arg2,'=');
      rect_arg_x = (int)(x-rotate_arg2);
      rotate_arg_i = atoi(&(rotate_arg2[rect_arg_x+1]));
      rotate_arg_n = atoi(rotate_arg4);
      
      if (strcmp(rotate_arg1,"column")==0) {
	memset(col,0,sizeof(int)*ROWS);
	for (int i=0; i<rotate_arg_n; i++) {
	  col[0] = screen[rotate_arg_i][ROWS-1];
	  for (int j=0; j<(ROWS-1); j++) {
	    col[j+1] = screen[rotate_arg_i][j];
	  }
	  for (int i=0; i<ROWS; i++) screen[rotate_arg_i][i]=col[i];
	}
      }
      else if (strcmp(rotate_arg1,"row")==0) {
	memset(row,0,sizeof(int)*COLS);
	for (int i=0; i<rotate_arg_n; i++) {
	  row[0] = screen[COLS-1][rotate_arg_i];
	  for (int j=0; j<(COLS-1); j++) {
	    row[j+1] = screen[j][rotate_arg_i];
	  }
	  for (int i=0; i<COLS; i++) screen[i][rotate_arg_i]=row[i];
	}
      }
    }
  }

  fclose(fid);

  int lit_pixels = show_screen(screen);
  printf("%d lit pixels\n",lit_pixels);
  
  return 0;
}

