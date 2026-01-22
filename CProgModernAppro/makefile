#-------------------------
# Taylor Carreiro 
# just for ease of compiling and w/e
#--------------------------


CFLAGS= -Wall #-std=c11 
CC= gcc 

example: ch6.o
	$(CC) $(CFLAGS) ch6.o -o ex
	./ex
ch6.o: ch6.c
	$(CC) $(CFLAGS) -g -c ch6.c


 
valgrindTest: convert 
	valgrind -s --leak-check=yes ./ex1

clean:
	rm -f *.o *~ 
	rm ex*

tar:
	