/*Sample program creates an array of 10 game scores for a basketball player*/

#include <stdio.h>

int main(){
    int gameScores[10] = {12, 5, 21, 15, 32, 10};
    int totalPoints = 0;
    int i;
    float avg;

    //only need scores for last 4 games so the loop will cover array elements 6-9
    for (i = 6; i < 10; i++){
        //add one since first index is 0 but it is game one not game 0
        printf("What did the player score in game %d? ", i+1);
        scanf(" %d", &gameScores[i]);
    }

    //now you have all scores loop through and calculate the avg
    for (i = 0; i < 10; i++){
        totalPoints += gameScores[i];
    }

    avg = ((float)totalPoints/10);

    printf("\n\nThe players scoring average is %.1f.\n", avg);
  
    return 0;

}