/*Sample program that defines a series of variables and expressions, then uses both relational and logical
    operators to test them against each other*/




#include <stdio.h>

int main(){
    //set up common ints for the program

    int planets = 8;
    int friends = 6;
    int potterBooks = 7;
    int starWars = 6;
    int months = 12;
    int beatles = 4;
    int avengers = 6;
    int baseball = 9;
    int basketball = 5;
    int football = 25;

    //AND operator if the casts of the shows would have enough members to make a team
    if ((friends + beatles >= baseball) && (friends + avengers >= football)){
        printf("Friends and Beatles have enough to make a baseball team AND Friends and Avengers have enough for a football team.\n\n");
    }
    else{
        printf("Either Friends and Beatles do not have enough for a baseball team or Friends and Avengers do not have a enough for a football team.\n\n");
    }

    //OR operator 
    if ((starWars <= months) || (potterBooks <= months)){
        printf("You could read one Harry Potter book a month and finish them in less than a year or\nyou could watch one Star Wars movie a month and finish them all within a year.\n\n");
    }
    else{
        printf("You can't finish either the Star wars series or Harry Potter series if you consume one piece each month.\n\n");
    }

    //NOT operator 
    if (!(baseball + basketball > football)){
        printf("There are fewer players on combined baseball and basketball team than there is on a football team.\n\n");
    }
    else{
        printf("If you combine a baseball and basketball team there is more players than on a football team.\n\n");
    }

    
    return 0;

}