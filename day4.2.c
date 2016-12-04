#include <stdio.h>
#include <stdlib.h>
#include <string.h>

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
  char roomname[64];
  char roomname_d[64];
  int roomname_i = 0;
  int sid;
  while (fscanf(fid,"%c",&c) != EOF) {
    ci = (int)c;
    cii = ci - c_a;
    if ((ci <= c_z) & (ci >= c_a)) {
      if (reading_code == 1) {
	count[cii] = count[cii] + 1;
	roomname[roomname_i] = c;
	roomname_i = roomname_i + 1;
      }
      else if (reading_checksum == 1) {
	checksum[checksum_i] = c;
	checksum_i = checksum_i + 1;
      }
    }
    else if (c=='-') {
      roomname[roomname_i] = ' ';
      roomname_i = roomname_i + 1;
    }
    else if ((c<=c_9) & (c>=c_0)) {
      sectorID[sectorID_i] = c;
      sectorID_i = sectorID_i + 1;
    }
    else if (c=='[') {
      reading_checksum = 1;
      reading_code = 0;
      sectorID_i = 0;
      roomname[roomname_i-1] = '\0';
      roomname_i = 0;
    }
    else if (c==']') {
      reading_checksum = 0;
      checksum_i = 0;
      reading_code = 1;      
    }
    else if (c=='\n') {
      //      printf("|");
      //     for (int i=0; i<26; i++) printf("%d|",count[i]);
      //      printf("%s|", sectorID);
      for (int i=0; i<5; i++) {
	maxes[i] = findmax_i(count,26);
	count[maxes[i]] = 0;
      }
      //      for (int i=0; i<5; i++) printf("%c",(char)(maxes[i]+c_a));
      //      printf("|%s", checksum);
      for (int i=0; i<26; i++) count[i]=0;
      for (int i=0; i<5; i++) {
	if (checksum[i] != ((char)(maxes[i]+c_a)))
	  isreal = 0;
      }
      if (isreal == 1) {
	num_real = num_real + 1;
	sid = atoi(sectorID);
	sectorIDsum = sectorIDsum + sid;
	sid = atoi(sectorID);
	int charshift = (sid % 26);
	printf("%d|", sid);
	for (int i=0; i<strlen(roomname); i++) {
	  if (roomname[i] != ' ') {
	    roomname_d[i] = (char)((((((int)roomname[i])-c_a) + charshift) % 26) + c_a);
	  }
	  else roomname_d[i]=' ';
	  printf("%c",roomname_d[i]);
	}
	printf("\n");
	//	printf(" * | %s", roomname);
      }
      //      printf("\n");
      isreal = 1;
    }
  }
  
  
  fclose(fid);
  
  return 0;

}
