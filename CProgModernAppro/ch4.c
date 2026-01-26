/**
 * Taylor Carreiro 2026
 * CH4 programming projects
*/

/**
 * 1./program that asks for a 2 digit number then prints it to user in reverse
 * 2./extend above to handle 3 digit
 * 3./rewrite #2 so that it prints the reverse without using aritmetic
 * 4./read in an integer and display it in octal base(not using the built in)
 * 5./rewrite upc program so that the user enters one long 11 digit then the check digit instead of groups of 5
 * TODO
 * 6.modify upc program to work for EAN barcode numbers too  
*/

#include <stdio.h>
#include <string.h>

//defines 

//prototype functions 
void ex1(void);
float ex3(void);
float ex4(void);
float ex5(void);
float ex6(void);



int main(){

    //ex1();
    //ex3();
    //ex4();
    ex5();

    //ex7();
    //ex8();


    return 0;
}


//*********************
//rewrite upc program so that the user enters one long 11 digit then the check digit instead of groups of 5
//modify upc program to work for EAN barcode numbers too 
float ex5(){

    long int d; 
    int i = 0, first_sum, second_sum, total;
    int nums[12];

    nums[11] = -1;

    printf("Enter the first 11 digits of a UPC or the first 12 digits of a EAN: ");
    scanf(" %ld", &d);
    
    //printf("in the first 11 digits: %ld\n", d);

    while(d != 0 || i < 11){ //if first digit is 0 it skips over it now was originally using range of 11 but with addition of possibly 12 number 
    //i swapped to a while loop for the input not 0 but ran into the problem 
        nums[i] = d % 10; //number will be saved in reverse this way
        d = d / 10;
        //printf("%d :%d\n", i, nums[i]);
        i++;
    }
    //printf("nums11: %d\n", nums[11]);

    //UPC
    if (nums[11] == -1){
        //printf("UPC\n");
        first_sum = nums[10] + nums[8] + nums[6] + nums[4] + nums[2] + nums[0]; //first digit + third +5th + 7th + 9th +11
        second_sum = nums[9] + nums[7] + nums[5] + nums[3] + nums[1] ; //2nd, 4th, 6th, 8th,10th

    }
    else{ //EAN
    //printf("EAN\n");
        first_sum = nums[10] + nums[8] + nums[6] + nums[4] + nums[2] + nums[0] ; //2nd, 4th, 6th, 8th,10th, 12th
        second_sum = nums[11] + nums[9] + nums[7] + nums[5] + nums[3] + nums[1]; //first digit + third +5th + 7th + 9th +11

    }

    
    total = 3 * first_sum + second_sum;

    printf("Check digit: %d\n", 9 - ((total - 1) % 10));

    return 0.0;
}


//*********************
//read in an integer and display it in octal base
//TODO maybe have an array to toss the numbers in instead of doing math
float ex4(void){
    int num, i = 0, j; 
    int nums[10];

    printf("Enter a number between 0 and 32767: ");
    scanf(" %d", &num);

    while(num != 0){
        nums[i] = num % 8;
        num = num / 8;
        i++;
    }

    printf("In octal your number is: ");
    for(j = i-1; j > -1; j--){
        printf("%d", nums[j]);

    }
    printf("\n");
    

    return 0.0;
}

//*********************
//3. rewrite #2 so that it prints the reverse without using aritmetic
float ex3(void){
    char num[4];

    printf("Enter a two or three digit number: ");
    scanf(" %s", num);
    
    if(strlen(num) == 3){
        printf("\nThe reversal is: %c%c%c\n\n", num[2], num[1], num[0]);
    }
    else{
        printf("\nThe reversal is: %c%c\n\n", num[1], num[0]);
    }
    

    return 0.0;
}



//*********************
//1. program that asks for a 2 digit number then prints it to user in reverse
//n%10 = last digit
//n/10 = first digit
//2. extend above to handle 3 digit

void ex1(void){

    int num;

    printf("Enter a two or three digit number: ");
    scanf(" %d", &num);

    if(num >= 100){
        printf("\nThe reversal is: %d%d%d\n\n", num%10, num%100/10, num/100%10);
    }
    else{
        printf("\nThe reversal is: %d%d\n\n", num%10, num/10);
    }

    
}