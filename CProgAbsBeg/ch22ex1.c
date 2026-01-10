/*Sample program */

#include <stdio.h>

int main(){
    
    int counter;//loop counter
    int idSearch;//customer to look for (the key)
    int found = 0; //will be 1 (true) if customer is found

    //defines the 10 elements in the two parallel arrays
    int custID[10] = {313, 453, 502, 101, 892, 475, 792, 912, 343, 633};
    float custBal[10] = {0.00, 45.43, 71.23, 301.56, 9.08, 192.41, 389.00, 229.67, 18.31, 59.54};

    //interact with user looking for a balance
    printf("\n\n*** Customer Balance Lookup ***\n");
    printf("Enter your customer ID: ");
    scanf(" %d", &idSearch);

    //search to see if ID exists in array 
    for (counter = 0; counter < 10; counter++){
        if (idSearch == custID[counter]){
            found = 1;
            break;
        }
    }

    if (found){
        if (custBal[counter] > 100.00){
            printf("\n** Balance is $%.2f.\n", custBal[counter]);
        }
        else{
            printf("Credit is good\n");
        }
    }
    else{
        printf("Incorrect ID no customer found for %3d\n", idSearch);
    }

  
    return 0;

}