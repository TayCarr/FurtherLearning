#-------------------------
# Taylor Carreiro 
# just for ease of compiling and w/e
#--------------------------


CFLAGS= -Wall #-std=c11 
CC= gcc 

example: ch26ex1.o
	$(CC) $(CFLAGS) ch26ex1.o -o ex
	./ex
ch26ex1.o: ch26ex1.c
	$(CC) $(CFLAGS) -g -c ch26ex1.c


 
valgrindTest: convert 
	valgrind -s --leak-check=yes ./ex1

clean:
	rm -f *.o *~ 
	rm ex*

tar:
	