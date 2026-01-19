/**
 * Taylor Carreiro 2026
 * CH3 programming projects
*/

/**
 * 1. get date from user input in format mm/dd/yyyy and print in the form yyyymmdd
 * 2. formats product info entered by user
 * 3. splitting the codes for isbn 
 * 4. get telephone number from user in (xxx) xxx-xxxx format display xxx.xxx.xxxx
 * 5. ask user to input numbers from 1-16 in any order then display in a 4x4 arrangement show row sums, column sums, diagonal sums
 * 6. 
*/

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

//defines 

//prototype functions 
void ex1(void);
float ex2(void);
float ex4(void);
float ex5(void);
float ex3(void);


int main(){

    //ex1();
    //ex2();
    //ex4();
    ex5();
    //ex7();
    //ex3();


    return 0;
}



//*********************
//ask user to input numbers from 1-16 in any order then display in a 4x4 arrangement show row sums, 
//column sums, diagonal sums
float ex5(){
    char line[40];
    char *token; 
    int nums[16];
    int i = 0;
    int temp;

    printf("Enter the numbers from 1 to 16 in any order: ");
    //scanf(" %s", line);
    fgets(line, 40, stdin);
    printf("\n");

    token = strtok(line, " ");
    while(token != NULL && i < 40){
        nums[i] = atoi(token);
        //printf("%d\n", nums[i]);
        token = strtok(NULL, " ");
        i++;

    }

    for (i = 0; i < 16; i++){
        printf("%2d ", nums[i]);

        if (i == 3 || i == 7 || i == 11 || i == 15){
            printf("\n");
        }
    }
    temp = nums[0] + nums[1] + nums[2] + nums[3];
    printf("\nRow sums: %d ", temp);
    temp = nums[0] + nums[1] + nums[2] + nums[3];
    printf("%d ", temp);
    temp = nums[4] + nums[5] + nums[6] + nums[7];
    printf("%d ", temp);
    temp = nums[8] + nums[9] + nums[10] + nums[11];
    printf("%d ", temp);
    temp = nums[12] + nums[13] + nums[14] + nums[15];
    printf("%d\n", temp);
    
    temp = nums[0] + nums[4] + nums[8] + nums[12];
    printf("Column sums: %d ", temp);
    temp = nums[1] + nums[5] + nums[9] + nums[13];
    printf("%d ", temp);
    temp = nums[2] + nums[6] + nums[10] + nums[14];
    printf("%d ", temp);
    temp = nums[3] + nums[7] + nums[11] + nums[15];
    printf("%d\n", temp);

    temp = nums[0] + nums[5] + nums[10] + nums[15];
    printf("Diagonal sums: %d ", temp);
    temp = nums[3] + nums[6] + nums[9] + nums[12];
    printf("%d\n", temp);

    return 0.0;
}


//*********************
//get telephone number from user in (xxx) xxx-xxxx format display xxx.xxx.xxxx
float ex4(void){
    int first, second, third;
    printf("Enter phone number [(xxx) xxx-xxxx]: ");
    scanf(" (%d) %d-%d", &first, &second, &third);

    printf("%d.%d.%d\n", first, second, third);
    

    return 0.0;
}

//*********************
//splitting the codes for isbn 13 digits arranged in 5 groups 
float ex3(){

    int gsi, group, publisher, item, check;

    printf("Enter ISBN: ");
    scanf(" %d-%d-%d-%d-%d", &gsi, &group, &publisher, &item, &check);

    printf("GSI prefix: %d\n", gsi);
    printf("Group identifier: %d\n", group);
    printf("Publisher Code: %d\n", publisher);
    printf("Item Number: %d\n", item);
    printf("Check Digit: %d\n", check);

    
    return 0.0; 
}

//*********************
//formats product info entered by user
float ex2(void){
    int item, day, month, year;
    float price; 

    printf("Enter item number: ");
    scanf(" %d", &item);
    printf("Enter unit price: ");
    scanf(" %f", &price);
    printf("Enter purchase date (mm/dd/yyyy): ");
    scanf(" %d/%d/%d", &month, &day, &year);

    printf("Item\t\tUnit\t\tPurchase\n\t\tPrice\t\tDate\n");
    printf("%d\t\t$%7.2f\t%d/%d/%d\n\n", item, price, month, day, year);

    return 0.0;
}

//*********************
//get date from user input in format mm/dd/yyyy and print in the form yyyymmdd

void ex1(void){
    int year, month, day;

    printf("Enter a date (mm/dd/yyyy): ");
    scanf(" %d/%d/%d", &month, &day, &year);

    printf("You entered the date %d%d%d\n\n", year, month, day);
    
}