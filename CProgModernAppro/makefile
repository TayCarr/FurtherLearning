#-------------------------
# Taylor Carreiro 
# just for ease of compiling and w/e
#--------------------------


CFLAGS= -Wall #-std=c11 
CC= gcc 

example: tempcalc.o
	$(CC) $(CFLAGS) tempcalc.o -o ex
	./ex
ch26ex1.o: tempcalc.c
	$(CC) $(CFLAGS) -g -c tempcalc.c


 
valgrindTest: convert 
	valgrind -s --leak-check=yes ./ex1

clean:
	rm -f *.o *~ 
	rm ex*

tar:
	