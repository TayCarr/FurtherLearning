#-------------------------
# Taylor Carreiro 
# just for ease of compiling and w/e
#--------------------------


CFLAGS= -Wall #-std=c11 
CC= gcc 

example: ch3.o
	$(CC) $(CFLAGS) ch3.o -o ex
	./ex
ch3.o: ch3.c
	$(CC) $(CFLAGS) -g -c ch3.c


 
valgrindTest: convert 
	valgrind -s --leak-check=yes ./ex1

clean:
	rm -f *.o *~ 
	rm ex*

tar:
	