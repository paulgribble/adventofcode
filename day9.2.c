#include <stdio.h>
#include <stdlib.h>
#include <string.h>

long int buflen(char *buf) {

  long int bufall_len = (long int)strlen(buf);
  char *cb1 = strchr(buf,'(');
  if (cb1 != NULL) {
    char *cb2 = strchr(buf,')');
    int cbi1 = (int)(cb1-buf);
    int cbi2 = (int)(cb2-buf);
    char *cx = strchr(buf,'x');
    int cxi = (int)(cx-buf);
    char *m = malloc(sizeof(char)*(cbi2-cbi1+1));
    for (int i=0; i<(cbi2-cbi1+1); i++) m[i]=buf[cbi1+i];
    m[cbi2-cbi1+1]='\0';
    m[cxi]='\0';
    int m1 = atoi(m+sizeof(char));
    int m2 = atoi(m+(sizeof(char)*cxi+1));
    free(m);
    char *mbuf = malloc((sizeof(char)*m1*m2) + 1);
    mbuf[sizeof(char)*m1*m2] = '\0';
    int mbufi = 0;
    for (int i=0; i<m2; i++) {
      for (int j=0; j<m1; j++) {
	mbuf[mbufi] = buf[cbi2+1+j];
	mbufi = mbufi + 1;
      }
    }
    long int mbl = (long int)buflen(mbuf);
    printf("%s|",mbuf);
    free(mbuf);
    char *rest = &(buf[cbi2+1+m1]);
    printf("%s\n",rest);
    return cbi1 + mbl + buflen(rest);
  }
  else {
    long int blen = (long int)strlen(buf);
    return blen;
  }
  
}

int main()
{

  FILE *fid = fopen("day9_input_test.txt","r");
  char *buf = malloc(sizeof(char)*12000);
  long int dflen = 0;
  
  fscanf(fid,"%s\n",buf);
  dflen = buflen(buf);
  printf("%ld\n", dflen);

  fclose(fid);
  
  return 0;
}

