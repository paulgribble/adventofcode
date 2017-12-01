#include <stdio.h>
#include <stdlib.h>

int compare(const void *a, const void *b) {
  int int_a = * ( (int*) a );
  int int_b = * ( (int*) b );
  if (int_a == int_b) return 0;
  else if (int_a < int_b) return -1;
  else return 1;
}

int main(int argc, char *argv[]) {

  FILE *fid = fopen("day3_input.txt","r");
  int s[3];
  int n_valid = 0;
  while (fscanf(fid,"%d %d %d\n",&s[0],&s[1],&s[2]) != EOF) {
    //    printf("%d %d %d | ",s[0],s[1],s[2]);
    qsort(s,3,sizeof(int),compare);
    //    printf("%d %d %d \n",s[0],s[1],s[2]);
    if ((s[0]+s[1])>s[2]) n_valid = n_valid + 1;
  }
  printf("%d valid triangles\n", n_valid);
 
  fclose(fid);
  return 0;

}
