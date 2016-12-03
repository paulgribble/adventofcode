

all:	day1.1 day1.2 day2.1 day2.2 day3.1 day3.2

day1.1:	day1.1.c
	gcc -o day1.1 day1.1.c

day1.2:	day1.2.c
	gcc -o day1.2 day1.2.c

day2.1:	day2.1.c
	gcc -o day2.1 day2.1.c

day2.2:	day2.2.c
	gcc -o day2.2 day2.2.c

day3.1:	day3.1.c
	gcc -o day3.1 day3.1.c

day3.2:	day3.2.c
	gcc -o day3.2 day3.2.c

clean:
	rm -f day1.1 day1.2 day2.1 day2.2 day3.1 day3.2

