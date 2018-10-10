// compile using:
// gcc -o aoc201504 aoc201504.c -lssl -lcrypto -I /usr/local/opt/openssl/include -L /usr/local/opt/openssl/lib

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <openssl/md5.h>

int main(int argc, char *argv[]) {

	char key[] = "yzbqklnj";
	char coin[33];
	char hash[33];
	unsigned char result[MD5_DIGEST_LENGTH];
	int n = 0;
	int part_1_found_it = 0;
	int part_2_found_it = 0;
	while (part_2_found_it == 0) {
		n = n + 1;
		sprintf(coin, "%s%d", key, n);
		MD5((unsigned char*)coin, strlen(coin), result);
		for(int i = 0; i < MD5_DIGEST_LENGTH; i++) {
			sprintf(&hash[i*2], "%02x", result[i]);
		}
		if (hash[0]=='0' && hash[1]=='0' && hash[2]=='0' && hash[3]=='0' && hash[4]=='0') {
			if (part_1_found_it==0) {
				printf("part 1: %7d : %s\n", n, hash);
				part_1_found_it = 1;
			}
		}
		if (hash[0]=='0' && hash[1]=='0' && hash[2]=='0' && hash[3]=='0' && hash[4]=='0' && hash[5]=='0') {
			printf("part 2: %d : %s\n", n, hash);
			part_2_found_it = 1;
		}
	}

	return 0;
}

