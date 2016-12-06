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

  int fmax;
  char cmax;
  for (int i=0; i<8; i++) {
    fmax = 0;
    cmax = 'a';
    for (int j=0; j<26; j++) {
      if (freqs[i][j] > fmax) {
	fmax = freqs[i][j];
	cmax = (char)(ia+j);
      }
    }
    printf("%c",cmax);
  }
  printf("\n");
  
  free(buf);
  fclose(fid);
  
  return 0;
}

