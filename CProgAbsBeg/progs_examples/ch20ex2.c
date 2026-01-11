/*Sample program that rolls two dice and presents the total then asks the user to guess if the next 
    total will be higher or lower then tells them if they are correct*/

#include <stdio.h>
#include <string.h>
#include <time.h>
#include <ctype.h>
#include <stdlib.h>

int main(){
    int dice1, dice2;
    int total1, total2;

    time_t t;
    char ans;

    //added my own check
    char flag;

    //need to seed with current time so that a true random number is generated each time
    srand(time(&t));

    //this gives a random number between 1 and 6
    dice1 = (rand() % 5) + 1;
    dice2 = (rand() % 5) + 1;
    total1 = dice1 + dice2;

    printf("First roll of the dice was %d and %d, ", dice1, dice2);
    printf("for the total being %d\n\n", total1);

    do {
        printf("Do you think the next roll total will be higher or lower than the current total?\n(H)igher, (L)ower, or (S)ame?");
        printf("Enter H, L, or S for your guess: ");

        scanf(" %c", &ans);
        ans = toupper(ans);

    } while ((ans != 'H') && (ans != 'L') && (ans != 'S'));

    //roll the dice a second total
    dice1 = (rand() % 5) + 1;
    dice2 = (rand() % 5) + 1;
    total2 = dice1 + dice2;

    //display the total
    printf("\nSecond roll of the dice was %d and %d, ", dice1, dice2);
    printf("for the total being %d\n\n", total2);
    
    
    //compare the two totals
    //im doing my own here thew book did nested if else
    if (total1 == total2){
        flag = 'S';
    }
    else if (total2 > total1){
        flag = 'H';
    }
    else{
        flag = 'L';
    }

    if (flag == ans){
        printf("You were correct!\n");
    }
    else{
        printf("You were incorrect!\n");
    }
    return 0;

}