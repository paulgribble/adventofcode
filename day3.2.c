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
  int s1[3], s2[3], s3[3];
  int n_valid = 0;
  while (fscanf(fid,"%d %d %d\n",&s1[0],&s2[0],&s3[0]) != EOF) {
    fscanf(fid,"%d %d %d\n",&s1[1],&s2[1],&s3[1]);
    fscanf(fid,"%d %d %d\n",&s1[2],&s2[2],&s3[2]);
    qsort(s1,3,sizeof(int),compare);
    qsort(s2,3,sizeof(int),compare);
    qsort(s3,3,sizeof(int),compare);
    if ((s1[0]+s1[1])>s1[2]) n_valid = n_valid + 1;
    if ((s2[0]+s2[1])>s2[2]) n_valid = n_valid + 1;
    if ((s3[0]+s3[1])>s3[2]) n_valid = n_valid + 1;
  }
  printf("%d valid triangles\n", n_valid);
 
  fclose(fid);
  return 0;

}
