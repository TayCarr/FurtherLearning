#-------------------------
# Taylor Carreiro 
# just for ease of compiling and w/e
#--------------------------


CFLAGS= -Wall #-std=c11 
CC= gcc 

example: ch15ex1.o
	$(CC) $(CFLAGS) ch15ex1.o -o ex
	./ex
ch15ex1.o: ch15ex1.c
	$(CC) $(CFLAGS) -g -c ch15ex1.c


example14: ch14ex1.o
	$(CC) $(CFLAGS) ch14ex1.o -o ex
	./ex
ch14ex1.o: ch14ex1.c
	$(CC) $(CFLAGS) -g -c ch14ex1.c
example13: ch13ex1.o
	$(CC) $(CFLAGS) ch13ex1.o -o ex
	./ex
ch13ex1.o: ch13ex1.c
	$(CC) $(CFLAGS) -g -c ch13ex1.c
example12: ch12ex1.o
	$(CC) $(CFLAGS) ch12ex1.o -o ex
	./ex
ch12ex1.o: ch12ex1.c
	$(CC) $(CFLAGS) -g -c ch12ex1.c
example11: ch11ex1.o
	$(CC) $(CFLAGS) ch11ex1.o -o ex
	./ex
ch11ex1.o: ch11ex1.c
	$(CC) $(CFLAGS) -g -c ch11ex1.c

example10: ch10ex1.o
	$(CC) $(CFLAGS) ch10ex1.o -o ex
	./ex
ch10ex1.o: ch10ex1.c
	$(CC) $(CFLAGS) -g -c ch10ex1.c

example9b: ch9ex2.o
	$(CC) $(CFLAGS) ch9ex2.o -o ex
	./ex
ch9ex2.o: ch9ex2.c
	$(CC) $(CFLAGS) -g -c ch9ex2.c	
example9a: ch9ex1.o
	$(CC) $(CFLAGS) ch9ex1.o -o ex
	./ex
ch9ex1.o: ch9ex1.c
	$(CC) $(CFLAGS) -g -c ch9ex1.c
example1: ch2ex1.o
	$(CC) $(CFLAGS) ch2ex1.o -o ex1
	./ex1
example2: ch2ex2.o
	$(CC) $(CFLAGS) ch2ex2.o -o ex
	./ex2

example3: ch3ex1.o
	$(CC) $(CFLAGS) ch3ex1.o -o ex
	./ex
example4: ch4ex2.o
	$(CC) $(CFLAGS) ch4ex2.o -o ex
	./ex

example5: ch5ex1.o
	$(CC) $(CFLAGS) ch5ex1.o -o ex
	./ex

example6: ch6ex1.o
	$(CC) $(CFLAGS) ch6ex1.o -o ex
	./ex

example7: ch7ex1.o
	$(CC) $(CFLAGS) ch7ex1.o -o ex
	./ex
ch7ex1.o: ch7ex1.c
	$(CC) $(CFLAGS) -g -c ch7ex1.c
example8a: ch8ex1.o
	$(CC) $(CFLAGS) ch8ex1.o -o ex
	./ex
ch8ex1.o: ch8ex1.c
	$(CC) $(CFLAGS) -g -c ch8ex1.c
example8b: ch8ex2.o
	$(CC) $(CFLAGS) ch8ex2.o -o ex
	./ex
ch8ex2.o: ch8ex2.c
	$(CC) $(CFLAGS) -g -c ch8ex2.c

ch2ex2.o: ch2ex2.c
	$(CC) $(CFLAGS) -g -c ch2ex2.c

ch2ex1.o: ch2ex1.c
	$(CC) $(CFLAGS) -g -c ch2ex1.c
 
valgrindTest: convert 
	valgrind -s --leak-check=yes ./ex1

clean:
	rm -f *.o *~ 
	rm ex*

tar:
	