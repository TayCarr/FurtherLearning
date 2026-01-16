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
 * 6. modify addfrac.c program from the chapter to allow user to enter both fractions seperated by a +
*/

#include <stdio.h>

//defines 

//prototype functions 
void ex1(void);
float ex2(void);
float ex4(void);
float ex5(void);
float ex7(void);
float ex8(void);


int main(){

    //ex1();
    //ex2();
    //ex4();
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
//
float ex4(void){
    

    return 0.0;
}

//*********************
// 
float ex2(void){

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