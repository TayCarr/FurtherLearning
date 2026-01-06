/*Sample program asks users for a number of tires and price per tire then calculates the price with sales tax*/

#include <stdio.h>
#define SALESTAX .07

int main(){
    //variable set up
    int numTires;
    float tirePrice, beforeTax, netSales;

    //get num of tires and price
    printf("How many tires did you purchase? ");
    scanf(" %d", &numTires);
    printf("What was the cost per tire (xx.xx)? ");
    scanf(" %f", &tirePrice);

    //compute price
    beforeTax = tirePrice * numTires;
    netSales = beforeTax + (beforeTax * SALESTAX);

    printf("You spent $%.2f on your tires\n\n", netSales);

    return 0;

}