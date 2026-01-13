#-------------------------
# Taylor Carreiro 
# just for ease of compiling and w/e
#--------------------------


CFLAGS= -Wall #-std=c11 
CC= gcc 

example: ch25ex1.o
	$(CC) $(CFLAGS) ch25ex1.o -o ex
	./ex
ch25ex1.o: ch25ex1.c
	$(CC) $(CFLAGS) -g -c ch25ex1.c


 
valgrindTest: convert 
	valgrind -s --leak-check=yes ./ex1

clean:
	rm -f *.o *~ 
	rm ex*

tar:
	