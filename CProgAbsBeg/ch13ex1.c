/*Sample program that asks the user for a number from 1 to 100 and tells you if it is divisible by numbers 2-9*/




#include <stdio.h>

int main(){
    //define var to store user pick 
    int numPick;

    printf("Pick a number between 1 and 100 to calculate its divisors from 2-9\n");
    scanf(" %d", &numPick);

    printf("%d %s divisible by 2.\n", numPick, (numPick % 2 == 0) ? ("is") : ("is not"));
    printf("%d %s divisible by 3.\n", numPick, (numPick % 3 == 0) ? ("is") : ("is not"));
    printf("%d %s divisible by 4.\n", numPick, (numPick % 4 == 0) ? ("is") : ("is not"));
    printf("%d %s divisible by 5.\n", numPick, (numPick % 5 == 0) ? ("is") : ("is not"));
    printf("%d %s divisible by 6.\n", numPick, (numPick % 6 == 0) ? ("is") : ("is not"));
    printf("%d %s divisible by 7.\n", numPick, (numPick % 7 == 0) ? ("is") : ("is not"));
    printf("%d %s divisible by 8.\n", numPick, (numPick % 8 == 0) ? ("is") : ("is not"));
    printf("%d %s divisible by 9.\n\n", numPick, (numPick % 9 == 0) ? ("is") : ("is not"));

    //prefix and postfix example
    int post = 1;
    int pre = 1;
    int j = 2;
    int n;

    printf("before: %d", pre);
    n = ++pre * j; //increment then use
    printf(" ,calculate: %d, after: %d\n", n, pre);

    printf("before: %d", post);
    n = post++ * j; //use then increment
    printf(" ,calculate: %d, after: %d\n", n, post);

    printf("Another example showing pre/post (%d, %d), then the values again (%d, %d)\n\n", ++pre, post++, pre, post);


    
    return 0;

}