/*Sample program that gets the bookinfo struct and asks the user to fill in three structures and then prints out */

#include <stdio.h>
#include "bookinfo.h"

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

    //print header line and then loop through and print the info
    printf("\n\nHere is the collection of books: \n");

    for(counter = 0; counter < 3; counter++){
        printf("#%d: %s by %s", counter+1, books[counter].title, books[counter].authour);

        printf("\nIt has %d pages and costs $%.2f\n\n", books[counter].pages, books[counter].price);

    }
  
    return 0;

}