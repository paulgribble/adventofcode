#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{

  FILE *fid = fopen("day9_input.txt", "r");
  FILE *fnew = fopen("day9_output.txt", "w");
  
  char *buf = malloc(16384*sizeof(char));
  
  char *c, *c1, *c2, *ctmp, *m;
  int ci0, ci1, ci2, clen, m1, m2;
  
  fscanf(fid,"%s\n",buf);

  c = buf;

  c1 = strchr(c,'(');
  if (c1 != NULL) {
    ci1 = (int)(c1-c);
    for (int i=0; i<ci1; i++) {
      fprintf(fnew,"%c",c[i]);
    }
    c = c1;
  }
  
  while ( (c1=strchr(c,'(')) != NULL) {

    ci1 = (int)(c1-c);
    for (int i=0; i<ci1; i++) {
      printf("*%c*",c[i]);
      fprintf(fnew,"%c",c[i]);
    }
    
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
    
    for (int i=0; i<m2; i++) {
      for (int j=0; j<m1; j++) {
	if (c2[j+1] != ' ') {
	  printf("+%c+",c2[j+1]);
	  fprintf(fnew,"%c",c2[j+1]);
	}
      }
    }
    printf("\n");
    
    free(ctmp);
    c = c2+(sizeof(char)*m1 + 1);
    
  }

  ci1 = (int)(c-buf);
  ci2 = strlen(buf)-ci1;
  for (int i=0; i<(ci2); i++) {
    printf("_%c_",buf[ci1+i]);
    fprintf(fnew,"%c",buf[ci1+i]);
  }
  printf("\n");
  
  free(buf);
  fclose(fnew);
  fclose(fid);

  return 0;
}

