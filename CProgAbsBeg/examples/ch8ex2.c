/*Sample program that asks users for some basic data and prints it to screen in order  */

#include <stdio.h>
#include <string.h>

int main(){
    //variable set up
    char topping[24];
    int slices;
    int month, day, year;
    float cost;

    printf("How much does a pizza cost? \n");
    printf("Enter as $xx.xx \n");
    scanf(" %f", &cost);

    printf("What is your favourite one word pizza topping? \n");
    scanf(" %s", topping); //pointer doesnt need &

    printf("How many pieces of %s pizza do you want? \n", topping);
    scanf(" %d", &slices);

    printf("What is todays date? (enter in form mm/dd/yy) \n");
    scanf(" %d/%d/%d", &month, &day, &year); //need to type / between each to be stored properly

    printf("\n\nWhy not treat yourself to dinner on %d/%d/%d \nand have %d slices of %s pizza!\n", month, day, year, slices, topping);
    printf("It will only cost you $%.2f.\n\n", cost);

    return 0;

}