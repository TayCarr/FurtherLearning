/**
 * Taylor Carreiro 2026
 * CH4 programming projects
*/

/**
 * 1. program that asks for a 2 digit number then prints it to user in reverse
 * 2. extend above to handle 3 digit
 * 3. rewrite #2 so that it prints the reverse without using aritmetic
 * 4. read in an integer and display it in octal base
 * 5. rewrite upc program so that the user enters one long digit instead of groups of 5
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
    ex4();
    //ex5();
    //ex7();
    //ex8();


    return 0;
}

//*********************
//
float ex8(){
    
    return 0.0; 
}

//*********************
//
float ex7(){
   
    return 0.0;
}

//*********************
//
float ex5(){

    return 0.0;
}


//*********************
//read in an integer and display it in octal base
//TODO maybe have an array to toss the numbers in instead of doing math
float ex4(void){
    int num, octal, temp; 

    printf("Enter a number between 0 and 32767: ");
    scanf(" %d", &num);

    octal = num % 8;
    num = num / 8;
    temp = (num % 8) * 10;
    octal = octal + temp; 
    printf("In octal your number is: %d\n", octal);

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