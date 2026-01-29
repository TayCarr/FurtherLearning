#-------------------------
# Taylor Carreiro 
# just for ease of compiling and w/e
#--------------------------


CFLAGS= -Wall #-std=c11 
CC= gcc 

example: ch7.o
	$(CC) $(CFLAGS) ch7.o -o ex
	./ex
ch7.o: ch7.c
	$(CC) $(CFLAGS) -g -c ch7.c


 
valgrindTest: convert 
	valgrind -s --leak-check=yes ./ex1

clean:
	rm -f *.o *~ 
	rm ex*

tar:
	