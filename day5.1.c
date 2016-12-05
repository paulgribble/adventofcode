#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <openssl/md5.h>
  
int main()
{
  int i;
  char *string = "The quick brown fox jumped over the lazy dog's back";
  unsigned char result[MD5_DIGEST_LENGTH];
  MD5(string, strlen(string), result);
 
  // output
  for(i = 0; i < MD5_DIGEST_LENGTH; i++)
    printf("%02x", result[i]);
  printf("\n");
 
  return EXIT_SUCCESS;
}

