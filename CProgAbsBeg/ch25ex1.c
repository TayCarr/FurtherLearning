/*Sample program that declares and initializes an array of character pointerss and then asks for ratings */

#include <stdio.h>
#include <ctype.h>

int main(){
    int i;
    int counter = 0;
    char ans;

    //declare movie array of 9 characters and then initializing them
    char * movies[9] = {"Amour", "Argo", "Beasts", "Django", "Les Mis", "Life of Pi", "Lincoln", "SLP", "ZDT"};

    int movieRatings[9]; //corresponding array of 9 ints for movie ratings

    char * tempMovie = "This will be used to sort rated movies";

    int outer, inner, didSwap, tempRating; //sort loop variables

    printf("\n\n*** Movie Ratings!! ***\n\n");
    for(i = 0; i < 9; i++){
        printf("Did you watch %s? (Y/N): ", movies[i]);
        scanf(" %c", &ans);

        if ((toupper(ans)) == 'Y'){
            printf("What would you rate %s on a scale of 1-10:  ", movies[i]);
            scanf(" %d", &movieRatings[i]);
            counter++;//used later to only print movies you have seen
            continue;
        }
        else{
            movieRatings[i] = -1;
        }
    }

    //sort the movies by rating, unseen go to the bottom 
    for(outer = 0; outer < 8; outer++){
        didSwap = 0;
        for(inner = outer; inner < 9; inner++){
            if(movieRatings[inner] > movieRatings[outer]){
                tempMovie = movies[inner];
                tempRating = movieRatings[inner];
                movies[inner] = movies[outer];
                movieRatings[inner] = movieRatings[outer];
                movies[outer] = tempMovie;
                movieRatings[outer] = tempRating;
                didSwap = 1;

            }
        }
        if(didSwap == 0){
            break;
        }
    }

    //print movies seen in order
    printf("\n\n*** Your Ratings ***\n\n");
    for(i = 0; i < counter; i++){
        printf("%s rated a score of %d\n", movies[i], movieRatings[i]);
    }

  
    return 0;

}