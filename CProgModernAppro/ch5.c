/**
 * Taylor Carreiro 2026
 * CH5 programming projects
 * 
 * probably wont be doing all will do a couple here and there
 * / means done
*/

/**
 * 1./calculates how many digits a number contains 
 * 2./ask user for 24 hour time, display in 12 hour 
 * 3. modify broker.c to ask the user to enter the number of shares and price per share, instead of value of trade 
 *      AND add statements that compute the commision charged by a rival broker ($33 plus 3 cents per share for 
 *      fewer than 2000 shares; $33 plus 2 cents per share for 2000 shares or more) display rivals commission as well as original broker
 * 4. write a program that asks the user to enter a wind speed (in knots), then display the corresponding description
 * 5. write a program that asks the user to enter the amount of taxable income, then display the tax due
 * 6. modify upc.c program so that it checks if a UPC is valid, after the user enters a upc it will display valid or not valid
 * 7./write a program that finds the smallest of four integers entered by the user
 * 8. write a program that asks user to enter a time (hours and minutes, using 24 hour) program displays the dep and arrival times for flight
 *      whose dep time is closest to input 
 * 9. prompt user to enter two dates and then indicate which date comes earlier on the calendar 
 * 10. using switch statement write a program that converts a numerical grade to a letter grade
 * 11. ask user for two-digit number, use one switch statement to print the word for the first digit use a second switch statement to print the 
 *      word for the second digit
*/

#include <stdio.h>

//defines 

//prototype functions 
void ex1(void);
float ex2(void);
float ex3(void);
float ex4(void);
float ex5(void);
float ex6(void);
float ex7(void);


int main(){

    ex1();
    //ex2();
    //ex7();

    //ex4();
    //ex5();
    //ex8();


    return 0;
}

//*********************
//
float ex8(){
    
    return 0.0; 
}

//*********************
//write a program that finds the largest and smallest of four integers entered by the user
float ex7(){
    int nums[3];
    int i;
    int min, max;

    printf("Enter four integers: ");
    scanf(" %d %d %d %d", &min, &nums[0], &nums[1], &nums[2]);

    max = min;
    for (i = 0; i < 3; i++){
        if (nums[i] < min){
            min = nums[i];
        }
        if (nums[i] > max){
            max = nums[i];
        }

    }

   printf("Largest: %d\nSmallest: %d\n\n", max, min);
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
float ex3(void){
    

    return 0.0;
}

//*********************
// ask user for 24 hour time, display in 12 hour 
float ex2(void){
    int hour, minute;
    printf("Enter a 24-hour time: ");
    scanf(" %d:%d", &hour, &minute);

    if (hour < 13){
        printf("Equivalent 12-hour time: %d:%02d AM\n", hour, minute);
    }
    else{
        
        printf("Equivalent 12-hour time: %d:%02d PM\n", hour-12, minute);

    }

    return 0.0;

}

//*********************
//calculates how many digits a number contains 
//can assume there is no more than 4 digits, use if statements to test the number
void ex1(void){
    int num;

    printf("Enter a number: ");
    scanf(" %d", &num);

    if(num > 999){
        printf("The number %d has 4 digits\n", num);
        return;
    }
    else if (num > 99){
        printf("The number %d has 3 digits\n", num);
        return;
    }
    else if (num > 9){
        printf("The number %d has 2 digits\n", num);
        return;
    }
    else if (num < 10){
        printf("The number %d has 1 digit\n", num);
        return;
    }
    
}