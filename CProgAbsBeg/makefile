#-------------------------
# Taylor Carreiro 
# just for ease of compiling and w/e
#--------------------------


CFLAGS= -Wall #-std=c11 
CC= gcc 

example: ./ch27/ch27ex1.o
	$(CC) $(CFLAGS) ./ch27/ch27ex1.o -o ex
	./ex
ch26ex1.o: ./ch27/ch27ex1.c ./ch27/bookinfo.h
	$(CC) $(CFLAGS) -g -c ./ch27/ch27ex1.c


 
valgrindTest: convert 
	valgrind -s --leak-check=yes ./ex1

clean:
	rm -f *.o *~ 
	rm ex*

tar:
	