#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int ischar(char c) {

  int a_i = (int)'a';
  int z_i = (int)'z';
  int c_i = (int)c;
  if ( (c_i >= a_i) & (c_i <= z_i) ) {
    return 1;
  }
  else {
    return 0;
  }
}

int main()
{

  FILE *fid = fopen("day7_input.txt", "r");
  char *buf = malloc(256*sizeof(char));
  int buflen;
  int inbrackets = 0;
  char c3[16][3];
  for (int i=0; i<16; i++) for (int j=0; j<3; j++) c3[i][j]='\0';
  int c3n = 0;
  char c3b[16][3];
  for (int i=0; i<16; i++) for (int j=0; j<3; j++) c3b[i][j]='\0';
  int c3bn = 0;
  int nvalid = 0;
  int foundvalid = 0;
  
  while (fscanf(fid,"%s",buf) != EOF) {
    buflen = strlen(buf);
    for (int i=0; i<(buflen-2); i++) {
      if (buf[i]=='[') inbrackets=1;
      if (buf[i]==']') inbrackets=0;
      if ( (buf[i]==buf[i+2]) & (buf[i]!=buf[i+1]) & ischar(buf[i]) & ischar(buf[i+1]) ) {
	if (inbrackets) {
	  //	  printf("[ %c%c%c ]\n", buf[i],buf[i+1],buf[i+2]);
	  c3b[c3bn][0] = buf[i];
	  c3b[c3bn][1] = buf[i+1];
	  c3b[c3bn][2] = buf[i+2];
	  printf("[ %c%c%c ]\n", c3b[c3bn][0],c3b[c3bn][1],c3b[c3bn][2]);
	  c3bn = c3bn + 1;
	}
	else {
	  //	  printf("%c%c%c\n", buf[i],buf[i+1],buf[i+2]);
	  c3[c3n][0] = buf[i];
	  c3[c3n][1] = buf[i+1];
	  c3[c3n][2] = buf[i+2];
	  printf("%c%c%c\n", c3[c3n][0],c3[c3n][1],c3[c3n][2]);
	  c3n = c3n + 1;
	}
      }
    }
    printf("%d + [%d]\n", c3n,c3bn);
    if ( (c3n>0) & (c3bn>0) ) {
      for (int i=0; i<c3n; i++) {
	for (int j=0; j<c3bn; j++) {
	  if ( (c3[i][0]==c3b[j][1]) & (c3[i][1]==c3b[j][0]) & (c3[i][2]==c3b[j][1]) ) {
	    foundvalid = 1;
	  }
	}
      }
    }
    if (foundvalid) {
      nvalid = nvalid + 1;
      printf("**************");
    }
    printf("--------------------------\n");
    c3n = 0;
    c3bn = 0;
    foundvalid = 0;
  }

  free(buf);
  fclose(fid);

  printf("nvalid is %d\n", nvalid);
  
  return 0;
}

