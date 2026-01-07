/*Sample program presents a menu of choices and gets the user input and uses switch statements to execute a line
    the choice is not actually a function just shows how the switch statement works with some print statements*/


#include <stdio.h>
#include <stdlib.h>

int main(){
    int choice;

    printf("What do you want to do?\n");
    printf("1. Add New Contact\n");
    printf("2. Edit Existing Contact\n");
    printf("3. Call Contact\n");
    printf("4. Text Contact\n");
    printf("5. Exit\n");
    
    do {
        printf("Enter your choice: ");
        scanf(" %d", &choice);

        switch(choice){
            case (1): printf("\nAdding contact...\n");
                        break;
            case (2): printf("\nEditing contact...\n");
                        break;
            case (3): printf("\nCalling contact...\n");
                        break;
            case (4): printf("\nTexting contact...\n");
                        break;
            case (5): exit(1);
            default: printf("\n%d is not an option.\n", choice);
                    printf("Try again.\n");
                    break;
        }
    } while ((choice < 1) || (choice > 5));

    
    return 0;

}