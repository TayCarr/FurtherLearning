/*Sample program asks the user their birth year and calculates how old they will be in the current year
    verifies the year entered isnt in the future, tells the user if they were born in a leap year*/

//including example 2 changes to not make a whole new program if-else

//just gonna start putting all the examples in one prog while they are small
//example 3 asks user for happiness on a scale then gives message based on range


#include <stdio.h>
#define CURRENTYEAR 2025

int main(){
    //variable set up
    int yrBorn, age;//ex1/2
    //ex 3
    int prefer;

    //ex 1/2
    printf("What year were you born?\n");
    scanf(" %d", &yrBorn);
    
    //check if year is in the future if is ask for year again
    if (yrBorn > CURRENTYEAR){
        printf("That year is in the future. Enter your birth year: \n");
        scanf(" %d", &yrBorn);
    }
    else{
        printf("You were born in %d!\n", yrBorn);
    }
    age = CURRENTYEAR - yrBorn;

    printf("\nSo this year you will be %d on your birthday!\n", age);

    //check if user was born on a leap year
    if ((yrBorn % 4) == 0){
        printf("\nYou were born in a Leap Year!!\n");
    }

    //ex 3
    printf("On a scale of 1 to 10, how happy are you?\n");
    scanf(" %d", &prefer);

    if (prefer >= 8){
        printf("Great for you! Things are going great!\n");
    }
    else if (prefer >= 5){
        printf("Better than average, still doing good!\n");
    }
    else if (prefer >= 3){
        printf("Sorry things arent going well, they will get better!\n");
    }
    else{
        printf("oh... uhh...\n");
    }
    
    


    return 0;

}