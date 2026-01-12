/*Sample program that demonstrates pointers by declaring and initializing both regular and pointer variables 
    for int, float, and char types then displays the value of each*/

#include <stdio.h>

int main(){

    int kids;
    int * pKids;
    float price;
    float * pPrice;
    char code;
    char * pCode;

    price = 17.50;
    pPrice = &price; //the address of price variable

    printf("\nHow many kids are you dropping off at the waterpark? ");
    scanf(" %d", &kids);

    pKids = &kids;

    printf("\nDo you have a discount ticket? (E)mployee, (S)ave-more, (N)o: ");
    scanf(" %c", &code);

    pCode = &code;

    switch(code){
        case('E'): 
            printf("Employee: 25%%, on $%.2f", price);
            printf("\nTotal ticket cost for %d tickets: $%.2f\n", kids, (price*.75*kids));
            break;
        case('S'):
            printf("Save-more: 15%%, on $%.2f", price);
            printf("\nTotal ticket cost for %d tickets: $%.2f\n", kids, (price*.85*kids));
            break;
        default:
            printf("Ticket cost: $%.2f", price);
            printf("\nTotal ticket cost for %d tickets: $%.2f\n", kids, (price*kids));
            break;

    }

    //below is same actions but with deref pointers
    switch(*pCode){
        case('E'): 
            printf("Employee: 25%%, on $%.2f", *pPrice);
            printf("\nTotal ticket cost for %d tickets: $%.2f\n", *pKids, (*pPrice * .75 * *pKids));
            break;
        case('S'):
            printf("Save-more: 15%%, on $%.2f", *pPrice);
            printf("\nTotal ticket cost for %d tickets: $%.2f\n", *pKids, (*pPrice * .85 * *pKids));
            break;
        default:
            printf("Ticket cost: $%.2f", price);
            printf("\nTotal ticket cost for %d tickets: $%.2f\n", *pKids, (*pPrice  * *pKids));
            break;

    }

    
  
    return 0;

}