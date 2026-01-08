/*Sample program that asks user to input grades for students but in the loop shows example of break */


#include <stdio.h>

int main(){
    int numTest;
    float stTest, avg, total = 0.0;

    //asks for up to 25 tests
    for (numTest = 0; numTest < 25; numTest++){
        //get test score and check if -1 is entered 
        printf("\nWhat is the next students test score? ");
        scanf(" %f", &stTest);

        if (stTest < 0.0){ //-1 to end the loop early
            break;
        }

        total += stTest;
    }

    avg = total / numTest; 
    printf("\nThe avg is: %.1f%%.\n", avg);//%% double needed to print % since it is considered control
    
    return 0;

}