#include <stdio.h>
#include <string.h>

int passes1(int x) {

	char s[7];
	sprintf(s, "%d", x);
	int inc = 1;
	int rep = 0;
	for (int i=1; i<strlen(s); i++) {
		if (s[i] < s[i-1]) {
			inc = 0;
			break;
		}
		if (s[i-1] == s[i]) {
			rep = 1;
		}
	}
	return(inc & rep);
}

int passes2(int x) {

	char s[7];
	sprintf(s, "%d", x);
	int inc = 1;
	int rep = 0;
	for (int i=1; i<strlen(s); i++) {
		if (s[i] < s[i-1]) {
			inc = 0;
			break;
		}
		if (s[i-1] == s[i]) {
			int multiple = 0;
			for (int j=0; j<(i-1); j++) {
				if (s[j]==s[i]) {
					multiple = 1;
					break;
				}
			}
			if (multiple==0) {
				for (int j=i+1; j<strlen(s); j++) {
					if (s[j]==s[i]) {
						multiple = 1;
						break;
					}
				}
			}
			if (multiple==0) { rep = 1; }
		}
	}
	return(inc & rep);
}

int main(int argc, char *argv[]) {

	int min = 265275;
	int max = 781584;
	int count1 = 0;
	int count2 = 0;
	for (int i=min; i<=max; i++) {
		count1 = count1 + passes1(i);
		count2 = count2 + passes2(i);
	}
	printf("Part 1: answer is %d\n", count1);
	printf("Part 2: answer is %d\n", count2);

	return 0;
}