/*Sample program generates 10 rand nums then bubble sort, compares first index with the rest swaps if first is a higher value, 
    next pass looks at second index and so on*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(){
    int counter, inner, outer, didSwap, temp;
    int nums[10];
    time_t t;

    //seed to generate true random ints
    srand(time(&t));

    //fill the array with random gen nums 
    for(counter = 0; counter < 10; counter++){
        nums[counter] = (rand() % 99) + 1; 
    }

    //list the before sorting 
    printf("Here is the list before sorting: \n");
    for(counter = 0; counter < 10; counter++){
        printf("%d\n", nums[counter]);
    }

    //sort array
    for(outer = 0; outer < 9; outer++){
        didSwap = 0; //1 if true if list is not yet ordered
        for(inner = outer; inner < 10; inner++){
            if(nums[inner] < nums[outer]){
                temp = nums[inner];
                nums[inner] = nums[outer];
                nums[outer] = temp;
                didSwap = 1;
            }
            //during prints
            /*
            printf("Here is the list during sorting: \n");
            for(counter = 0; counter < 10; counter++){
                printf("%d, ", nums[counter]);
            }
            printf("\n");*/
        }
        if(didSwap == 0){
            break;
        }

    }
    //now list array for after sorting 
    printf("\nHere is the list after sorting: \n");
    for(counter = 0; counter < 10; counter++){
        printf("%d\n", nums[counter]);
    }

  
    return 0;

}