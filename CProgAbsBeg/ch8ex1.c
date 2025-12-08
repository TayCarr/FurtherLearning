/*Sample program that asks users for some basic data and prints it to screen in order  */

#include <stdio.h>
#include <string.h>

int main(){
    //variable set up
    char firstInitial;
    char lastInitial;
    int age;
    int fav_num;

    printf("What letter does your first name start with? \n");
    scanf(" %c", &firstInitial);

    printf("What letter does your last name start with? \n");
    scanf(" %c", &lastInitial);

    printf("How old are you? \n");
    scanf(" %d", &age);

    printf("What is your favourite number? \n");
    scanf(" %d", &fav_num);

    printf("\nYour initials are %c.%c. and you are %d years old", firstInitial, lastInitial, age);
    printf("\nYour favourite number is %d.\n\n", fav_num);

    return 0;

}