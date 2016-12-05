

all:	day1.1 day1.2 day2.1 day2.2 day3.1 day3.2 day4.1 day4.2 day5.1 day5.2

day1.1:	day1.1.c
	gcc -Wall -o day1.1 day1.1.c

day1.2:	day1.2.c
	gcc -Wall -o day1.2 day1.2.c

day2.1:	day2.1.c
	gcc -Wall -o day2.1 day2.1.c

day2.2:	day2.2.c
	gcc -Wall -o day2.2 day2.2.c

day3.1:	day3.1.c
	gcc -Wall -o day3.1 day3.1.c

day3.2:	day3.2.c
	gcc -Wall -o day3.2 day3.2.c

day4.1:	day4.1.c
	gcc -Wall -o day4.1 day4.1.c

day4.2:	day4.2.c
	gcc -Wall -o day4.2 day4.2.c

day5.1:	day5.1.c
	gcc -o day5.1 day5.1.c -lssl -lcrypto -lz -I/usr/local/opt/openssl/include

day5.2:	day5.2.c
	gcc -o day5.2 day5.2.c -lssl -lcrypto -lz -I/usr/local/opt/openssl/include

clean:
	rm -f day1.1 day1.2 day2.1 day2.2 day3.1 day3.2 day4.1 day4.2 day5.1 day5.2


