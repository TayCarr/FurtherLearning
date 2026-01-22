#-------------------------
# Taylor Carreiro 
# just for ease of compiling and w/e
#--------------------------


CFLAGS= -Wall #-std=c11 
CC= gcc 

example: ch5.o
	$(CC) $(CFLAGS) ch5.o -o ex
	./ex
ch5.o: ch5.c
	$(CC) $(CFLAGS) -g -c ch5.c


 
valgrindTest: convert 
	valgrind -s --leak-check=yes ./ex1

clean:
	rm -f *.o *~ 
	rm ex*

tar:
	