#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{

  FILE *fid = fopen("day9_input.txt", "r");

  char *buf = malloc(16384*sizeof(char));
  char *c, *c1, *c2, *ctmp;
  int ci1, ci2, clen;
  
  fscanf(fid,"%s\n",buf);

  c = buf;
  while ( (c1=strchr(c,'(')) != NULL) {
  
    c2 = strchr((c1+sizeof(char)),')');
    clen = (int)(c2-c1+1);
    ctmp = malloc((clen+1)*sizeof(char));
    for (int i=0; i<clen; i++) {
      ctmp[i] = c1[i];
    }
    ctmp[clen] = '\0';
    printf("%s\n", ctmp);
    free(ctmp);
    
    c = c1+sizeof(char);
    
  }

  printf("\n");
  
  free(buf);
  fclose(fid);

  return 0;
}

