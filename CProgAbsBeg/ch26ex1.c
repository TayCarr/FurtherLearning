/*Sample program that looks for a number of random integers, allocates an array and fills it with 
    numbers between 1-500 and then loops through all numbers and finds the smallest, the biggest 
    and the avg, the frees memory used
 */

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(){
    int i, aSize;

    int * randomNums; 

    time_t t;

    double total = 0;
    int biggest, smallest;
    float average;

    srand(time(&t));

    printf("How many random numbers do you want in your array? ");
    scanf(" %d", &aSize);

    //allocate an array of ints equal to the number of elements requested
    randomNums = (int *) malloc(aSize * sizeof(int));

    //test to ensure it allocated memory correctly
    if(!randomNums){
        printf("Allocation failed\n");
        exit(1);
    }

    //loops through array and assigns a random number between 1-500 to each element
    for(i = 0; i < aSize; i++){
        randomNums[i] = (rand() % 500) + 1;
    }

    //initialize the biggest and smallest number for comparison
    biggest = 0;
    smallest = 500;

    //loop through the array testing the numbers and adding all for avg calculation
    for(i = 0; i < aSize; i++){
        total += randomNums[i];
        if (randomNums[i] > biggest){
            biggest = randomNums[i];
        }
        if(randomNums[i] < smallest){
            smallest = randomNums[i];
        }
    }

    average = ((float)total)/((float)aSize);

    printf("The biggest number: %d\n", biggest);
    printf("The smallest number: %d\n", smallest);
    printf("The average is: %.2f\n", average);

    //now free memory
    free(randomNums);

  
    return 0;

}