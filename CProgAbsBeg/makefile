#-------------------------
# Taylor Carreiro 
# just for ease of compiling and w/e
#--------------------------


CFLAGS= -Wall #-std=c11 
CC= gcc 

example: ch7ex1.o
	$(CC) $(CFLAGS) ch7ex1.o -o ex
	./ex
ch7ex1.o: ch7ex1.c
	$(CC) $(CFLAGS) -g -c ch7ex1.c

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
	