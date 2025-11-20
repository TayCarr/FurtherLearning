/*Program that is just showing off the different types if comments and stuff*/
/*Totals how much money will be spent on holiday gifts*/
#include <stdio.h>

int main(){
    float gift1, gift2, gift3, gift4, gift5; //variables to hold costs
    float total; //var hold total amount

    //ask for each amount
    printf("How much do you want to spend on your mom? ");
    scanf(" %f", &gift1);
    printf("How much do you want to spend on your dad? ");
    scanf(" %f", &gift2);
    printf("How much do you want to spend on your sister? ");
    scanf(" %f", &gift3);
    printf("How much do you want to spend on your brother? ");
    scanf(" %f", &gift4);
    printf("How much do you want to spend on your dog? ");
    scanf(" %f", &gift5);

    total = gift1 + gift2 + gift3 + gift4 + gift5; //compute total

    printf("The total holiday spending is $%.2f \n", total);
    return 0;
}