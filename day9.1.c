#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{

  FILE *fid = fopen("day9_input.txt", "r");
  FILE *fnew = fopen("day9_output.txt", "w");
  
  char *buf = malloc(16384*sizeof(char));
  
  char *c, *c1, *c2, *ctmp, *m;
  int ci1, ci2, clen, m1, m2;
  
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
    printf("%s ", ctmp);

    m = strchr(ctmp,'x');
    ctmp[(int)(m-ctmp)] = '\0';
    m1 = atoi(&(ctmp[1]));
    m2 = atoi(&(ctmp[(int)(m-ctmp)+1]));
    printf("%d %d\n",m1,m2);

    free(ctmp);
    c = c1+sizeof(char);
    
  }
  
  free(buf);
  fclose(fnew);
  fclose(fid);

  return 0;
}

