#-------------------------
# Taylor Carreiro 
# just for ease of compiling and w/e
#--------------------------


CFLAGS= -Wall #-std=c11 
CC= gcc 

example: ch4.o
	$(CC) $(CFLAGS) ch4.o -o ex
	./ex
ch4.o: ch4.c
	$(CC) $(CFLAGS) -g -c ch4.c


 
valgrindTest: convert 
	valgrind -s --leak-check=yes ./ex1

clean:
	rm -f *.o *~ 
	rm ex*

tar:
	