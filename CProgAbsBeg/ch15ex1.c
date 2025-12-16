/*Sample program that  */


#include <stdio.h>
#include <string.h>

int main(){

    int counter, numMovies, rating, favRating, leastRating;
    char movieName[40], favourite[40], least[40];

    //init fav rating to 0 so any movie with any rating of 1 or higher will replace it 
    favRating = 0;
    leastRating = 10;
    //loop will continue until they enter a number more than 0

    do {
        printf("How many movies have you seen this year? ");
        scanf(" %d", &numMovies);

        if (numMovies < 1){
            printf("Enter a number greater than 0\n");
        }
    } while (numMovies < 1);

    for (counter = 1; counter <= numMovies; counter++){
        //get the name and rating of the movie
        printf("\nWhat was the name of the movie? (1 word titles only) ");
        scanf("%s", movieName);
        printf("On a scale of 1-10 what do you rate the movie? ");
        scanf(" %d", &rating);

        //printf("\n%s\n", movieName);

        //check if fave movie
        if (rating > favRating){
            strcpy(favourite, movieName);
            favRating = rating;
        }

        //check if least
        if (rating < leastRating){
            strcpy(least, movieName);
            leastRating = rating;
            //printf("\nleast: %s\n", least);
        }
    }

    printf("\n\nYour favourite movie is %s with a rating of %d\nand your least liked movie was %s with a rating of %d\n\n", favourite, favRating, least, leastRating);
    
    
    
    return 0;

}