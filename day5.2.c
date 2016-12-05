#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <openssl/md5.h>
  
int main()
{
  /*
  // example code for using MD5
  int i;
  char *string = "The quick brown fox jumped over the lazy dog's back";
  unsigned char result[MD5_DIGEST_LENGTH];
  MD5((const unsigned char *)string, strlen(string), result);
 
  for(i = 0; i < MD5_DIGEST_LENGTH; i++) {
    printf("%02x", result[i]);
  }
  printf("\n");
  */
  
  char *doorID = "cxdnnyjw";
  char input[32];
  unsigned char result[MD5_DIGEST_LENGTH];
  char hexresult[MD5_DIGEST_LENGTH*2];
  int numfound = 0;
  long int index = 0;
  long int i = 0;
  char password[9];
  for (int i=0; i<9; i++) password[i]='\0';
  int position;
  while (numfound < 8) {
    sprintf((char *)&input, "%s%ld", doorID, i);
    MD5((const unsigned char *)input, strlen(input), result);
    for(int j=0; j<MD5_DIGEST_LENGTH; j++) {
      sprintf(&(hexresult[j*2]),"%02x",result[j]);
    }
    if ((hexresult[0]=='0')&(hexresult[1]=='0')&(hexresult[2]=='0')&(hexresult[3]=='0')&(hexresult[4]=='0') & (((int)hexresult[5])>=((int)'0')) & (((int)hexresult[5])<=((int)'7')) & (password[(int)hexresult[5] - (int)'0'] == '\0')) {
      printf("%s %s| ", input, hexresult);
      numfound = numfound + 1;
      position = (int)hexresult[5] - (int)'0';
      password[position] = hexresult[6];
      printf("%c %d : %c\n", hexresult[5], position, hexresult[6]);
    }
    i = i + 1;
  }
  printf("password is %s\n", password);
  return EXIT_SUCCESS;
}

