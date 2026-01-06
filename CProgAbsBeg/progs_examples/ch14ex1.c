/*Sample program that increases a counter from 1 to 5, prints updates then counts back down */


#include <stdio.h>

int main(){
    int ctr = 0;

    while (ctr < 5){
        printf("Counter is at %d\n", ++ctr);
    }

    while (ctr > 1){
        printf("Counter is at %d\n", --ctr);
    }

    //ex 2 multiply two numbers and display the result as long as the user wants 'N' will break loop

    char choice;
    float num1, num2, result;

    do {
        printf("Enter your first number: ");
        scanf(" %f", &num1);
        printf("Enter your second number: ");
        scanf(" %f", &num2);

        result = num1 * num2;

        printf("%.2f * %.2f = %.2f\n\n", num1, num2, result);

        printf("Go again? (N to escape): ");
        scanf(" %c", &choice);

        /*if (choice == 'n'){
            choice = 'N';
        }*/ //can use AND below too

    } while (choice != 'N' && choice != 'n');
    
    return 0;

}