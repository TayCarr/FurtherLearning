/*Sample program asks the user their birth year and calculates how old they will be in the current year
    verifies the year entered isnt in the future, tells the user if they were born in a leap year*/

#include <stdio.h>
#define CURRENTYEAR 2025

int main(){
    //variable set up
    int yrBorn, age;

    printf("What year were you born?\n");
    scanf(" %d", &yrBorn);
    
    //check if year is in the future if is ask for year again
    if (yrBorn > CURRENTYEAR){
        printf("That year is in the future. Enter your birth year: \n");
        scanf(" %d", &yrBorn);
    }
    age = CURRENTYEAR - yrBorn;

    printf("\nSo this year you will be %d on your birthday!\n", age);

    //check if user was born on a leap year
    if ((yrBorn % 4) == 0){
        printf("\nYou were born in a Leap Year!!\n");
    }

    return 0;

}