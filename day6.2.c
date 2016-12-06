#include <stdio.h>
#include <stdlib.h>
#include <string.h>
  
int main()
{

  FILE *fid = fopen("day6_input.txt", "r");

  char message[9]; message[8] = '\0';
  int freqs[8][26];
  for (int i=0; i<8; i++) {
    for (int j=0; j<26; j++) {
      freqs[i][j] = 0;
    }
  }
  char *buf = malloc(7*sizeof(char));
  int ic;
  int ia = (int)'a';
  while (fscanf(fid,"%s",buf) != EOF) {
    printf("%s ", buf);
    for (int i=0; i<8; i++) {
      ic = (int)buf[i];
      freqs[i][ic-ia] = freqs[i][ic-ia] + 1;
      printf("%3d(%2d)", ic-ia, freqs[i][ic-ia]);
    }
    printf("\n");
  }

  for (int i=0; i<26; i++) {
    printf("%c", (char)(ia+i));
    for (int j=0; j<8; j++) {
      printf("%3d ", freqs[j][i]);
    }
    printf("\n");
  }

  int fmin;
  char cmin;
  for (int i=0; i<8; i++) {
    fmin = 99999;
    cmin = 'a';
    for (int j=0; j<26; j++) {
      if (freqs[i][j] < fmin) {
	fmin = freqs[i][j];
	cmin = (char)(ia+j);
      }
    }
    printf("%c",cmin);
  }
  printf("\n");
  
  free(buf);
  fclose(fid);
  
  return 0;
}

