#-------------------------
# Taylor Carreiro 
# just for ease of compiling and w/e
#--------------------------


CFLAGS= -Wall #-std=c11 
CC= gcc 

example: ch2.o
	$(CC) $(CFLAGS) ch2.o -o ex
	./ex
ch2.o: ch2.c
	$(CC) $(CFLAGS) -g -c ch2.c


 
valgrindTest: convert 
	valgrind -s --leak-check=yes ./ex1

clean:
	rm -f *.o *~ 
	rm ex*

tar:
	