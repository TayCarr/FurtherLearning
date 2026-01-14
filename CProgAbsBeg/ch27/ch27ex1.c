/*Sample program that gets the bookinfo struct and asks the user to fill in three structures and then prints out */
//ch28 is showing how to write to a file for this prog soooo just gonna add that bit into this instead of new prog
//tbh skipping reading and append example... cause ya...

#include <stdio.h>
#include "bookinfo.h"
#include <stdlib.h>
FILE * fptr;

int main(){
    int counter;
    struct bookInfo books[3]; //array of three struct vars

    //get info about each book from user
    for(counter = 0; counter < 3; counter++){
        printf("What is the name of book #%d? ", counter+1);
        scanf(" %s", &books[counter].title);

        printf("Who is the authour? ");
        scanf(" %s", &books[counter].authour);

        printf("How much did it cost? ");
        scanf(" %f", &books[counter].price);

        printf("How many pages in the book? ");
        scanf(" %d", &books[counter].pages);

    }
    //open file
    fptr = fopen("exbookinfo.txt", "w");

    //test to make sure properly opened
    if(fptr == 0){
        printf("Error -- file could not be opened\n");
        exit(1);
    }

    //print header line and then loop through and print the info
    printf("\n\nHere is the collection of books: \n");

    for(counter = 0; counter < 3; counter++){
        printf("#%d: %s by %s", counter+1, books[counter].title, books[counter].authour);
        printf("\nIt has %d pages and costs $%.2f\n\n", books[counter].pages, books[counter].price);

        fprintf(fptr, "#%d: %s by %s", counter+1, books[counter].title, books[counter].authour);
        fprintf(fptr, "\nIt has %d pages and costs $%.2f\n\n", books[counter].pages, books[counter].price);

    }
    fclose(fptr); //close file 
  
    return 0;

}