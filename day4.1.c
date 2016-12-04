#include <stdio.h>
#include <stdlib.h>

int findmax_i(int *array, int n) {
  int themax_i = 0;
  for (int i=0; i<n; i++) {
    if (array[i] > array[themax_i]) themax_i = i;
  }
  return themax_i;
}

int main(int argc, char *argv[]) {

  FILE *fid = fopen("day4_input.txt","r");
  char c;
  int n_valid = 0;
  int count[26];
  int ci,cii;
  int c_a = (int)'a';
  int c_z = (int)'z';
  int c_0 = (int)'0';
  int c_9 = (int)'9';
  int reading_code = 1;
  int reading_checksum = 0;
  char checksum[5];
  int checksum_i = 0;
  for (int i=0; i<26; i++) count[i]=0;
  int maxes[5];
  int num_real = 0;
  int isreal = 1;
  int sectorIDsum = 0;
  int sectorID_i = 0;
  char sectorID[4]; sectorID[3]='\0';
  while (fscanf(fid,"%c",&c) != EOF) {
    ci = (int)c;
    cii = ci - c_a;
    if ((ci <= c_z) & (ci >= c_a)) {
      if (reading_code == 1) {
	count[cii] = count[cii] + 1;
      }
      else if (reading_checksum == 1) {
	checksum[checksum_i] = c;
	checksum_i = checksum_i + 1;
      }
    }
    else if ((c<=c_9) & (c>=c_0)) {
      sectorID[sectorID_i] = c;
      sectorID_i = sectorID_i + 1;
    }
    else if (c=='[') {
      reading_checksum = 1;
      reading_code = 0;
      sectorID_i = 0;
    }
    else if (c==']') {
      reading_checksum = 0;
      checksum_i = 0;
      reading_code = 1;      
    }
    else if ((ci <= c_9) & (ci >= c_0)) {

    }
    else if (c=='\n') {
      int index[26];
      printf("|");
      for (int i=0; i<26; i++) printf("%d|",count[i]);
      printf("%s|", sectorID);
      for (int i=0; i<5; i++) {
	maxes[i] = findmax_i(count,26);
	count[maxes[i]] = 0;
      }
      for (int i=0; i<5; i++) printf("%c",(char)(maxes[i]+c_a));
      printf("|%s", checksum);
      for (int i=0; i<26; i++) count[i]=0;
      for (int i=0; i<5; i++) {
	if (checksum[i] != ((char)(maxes[i]+c_a)))
	  isreal = 0;
      }
      if (isreal == 1) {
	num_real = num_real + 1;
	sectorIDsum = sectorIDsum + atoi(sectorID);
	printf(" *");
      }
      printf("\n");
      isreal = 1;
    }
  }
  printf("found %d real rooms\n", num_real);
  printf("sectorIDsum is %d\n", sectorIDsum);

  fclose(fid);
  
  return 0;

}
