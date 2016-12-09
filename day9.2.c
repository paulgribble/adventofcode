#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// need to go backwards starting at end and expanding

int main()
{

  FILE *fid = fopen("day9_input_test.txt","r");
  char *buf = malloc(sizeof(char)*12000);
  long int dflen = 0;
  
  fscanf(fid,"%s\n",buf);
  dflen = strlen(buf);
  printf("%ld\n", dflen);

  fclose(fid);
  
  return 0;
}

