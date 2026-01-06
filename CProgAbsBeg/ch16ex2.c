/*Sample program that loops through 10 numbers and tests if a number is odd or even and prints message for each
    if it is odd uses continue to go to next number in the loop otherwise does even message */


#include <stdio.h>

int main(){
    int i;

    //loops through the numbers 1 through 10 
    for (i = 1; i <= 10; i++){
        if ((i%2) == 1){ //odd nums have a rem==1
        printf("I'm odd..\n");
        //jump to next iteration of loop
        continue;

        }
        printf("Even!\n");
    }
    
    return 0;

}