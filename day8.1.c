#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int show_screen(int screen[50][6]) {
  int lit_pixels = 0;
  printf("\n+--------------------------------------------------+\n");
  for (int j=0; j<6; j++) {
    printf("|");
    for (int i=0; i<50; i++) {
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
  printf("+--------------------------------------------------+\n\n");
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
  
  int screen[50][6];
  memset(screen, 0, sizeof(int)*50*6);
  
  while (fscanf(fid,"%s",(char *)&cmd) != EOF) {
    if (strcmp(cmd,"rect")==0) {
      printf("%s ", cmd);
      fscanf(fid,"%s",(char *)&rect_arg);
      rect_arg_len = strlen(rect_arg);
      x = strchr(rect_arg,'x');
      rect_arg_x = (int)(x-rect_arg);
      rect_arg[rect_arg_x]='\0';
      rect_rows = atoi(rect_arg);
      rect_cols = atoi(&(rect_arg[rect_arg_x+1]));
      printf("%dx%d\n",rect_rows,rect_cols);
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
      
    }
  }

  fclose(fid);

  int lit_pixels = show_screen(screen);
  printf("%d lit pixels\n",lit_pixels);
  
  return 0;
}

