#include <stdio.h>
#include <stdlib.h>
#include <string.h>
  
int main()
{

  FILE *fid = fopen("day7_input.txt", "r");
  char *buf = malloc(256*sizeof(char));

  int buflen;
  int nvalid = 0;
  int inbrackets = 0;
  int isvalid = 0;
  int foundbrackets = 0;
  while (fscanf(fid,"%s",buf) != EOF) {
    buflen = strlen(buf);
    for (int i=0; i<(buflen-3); i++) {
      if (buf[i]=='[') inbrackets=1;
      else if (buf[i]==']') inbrackets=0;
      if ( (buf[i]==buf[i+3]) & (buf[i+1]==buf[i+2]) & (buf[i]!=buf[i+1]) ) {
	if (inbrackets==0) {
	  isvalid = 1;
	  printf("%c%c%c%c\n", buf[i],buf[i+1],buf[i+2],buf[i+3]);
	}
	else if (inbrackets==1) {
	  isvalid = 0;
	  foundbrackets = 1;
	  printf("[[[[[]]]]]\n");
	}
      }
    }
    if ((isvalid==1) & (foundbrackets==0)) {
      nvalid = nvalid + 1;
      printf("%s\n\n", buf);
    }
    isvalid = 0;
    inbrackets = 0;
    foundbrackets = 0;
  }

  free(buf);
  fclose(fid);

  printf("nvalid = %d\n", nvalid);
  
  return 0;
}

