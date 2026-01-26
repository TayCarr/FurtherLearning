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
 * 3./modify broker.c to ask the user to enter the number of shares and price per share, instead of value of trade 
 *      AND add statements that compute the commision charged by a rival broker ($33 plus 3 cents per share for 
 *      fewer than 2000 shares; $33 plus 2 cents per share for 2000 shares or more) display rivals commission as well as original broker
 * 4./write a program that asks the user to enter a wind speed (in knots), then display the corresponding description
 * 5. write a program that asks the user to enter the amount of taxable income, then display the tax due
 * 6. modify upc.c program so that it checks if a UPC is valid, after the user enters a upc it will display valid or not valid
 * 7./write a program that finds the smallest of four integers entered by the user
 * 8. write a program that asks user to enter a time (hours and minutes, using 24 hour) program displays the dep and arrival times for flight
 *      whose dep time is closest to input 
 * 9. prompt user to enter two dates and then indicate which date comes earlier on the calendar 
 * 10. using switch statement write a program that converts a numerical grade to a letter grade
 * 11./ask user for two-digit number, use one switch statement to print the word for the first digit use a second switch statement to print the 
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
float ex11(void);


int main(){

    //ex1();
    //ex2();
    //ex7();
    //ex11();
    //ex3();
    ex4();

    //ex5();

    return 0;
}

//*********************
//ask user for two-digit number, use one switch statement to print the word for the first digit use a second 
//switch statement to print the word for the second digit
float ex11(){
    int num;
    int first, second;

    printf("Enter a two-digit number: ");
    scanf(" %d", &num);

    first = num/10;
    second = num%10;

    printf("You entered the number ");
    if (num > 10 && num < 20){
        //special cases
        switch (num)
        {
        case 11:
            printf("Eleven\n");
            return 0.0;
        case 12:
            printf("Twelve\n");
            return 0.0;
        case 13:
            printf("Thirteen\n");
            return 0.0;
        case 14:
            printf("Fourteen\n");
            return 0.0;
        case 15:
            printf("Fifteen\n");
            return 0.0;
        case 16:
            printf("Sixteen\n");
            return 0.0;
        case 17:
            printf("Seventeen\n");
            return 0.0;
        case 18:
            printf("Eighteen\n");
            return 0.0;
        case 19:
            printf("Nineteen\n");
            return 0.0;
        
        default:
            break;
        }
    }

    switch (first)
    {
    case 1:
        printf("Ten\n");
        return 0.0;
    case 2:
        printf("Twenty-");
        break;
    case 3:
        printf("Thirty-");
        break;
    case 4:
        printf("Fourty-");
        break;
    case 5:
        printf("Fifty-");
        break;
    case 6:
        printf("Sixty-");
        break;
    case 7:
        printf("Seventy-");
        break;
    case 8:
        printf("Eighty-");
        break;
    case 9:
        printf("Ninety-");
        break; 
    default:
        break;
    }

    switch (second)
    {
    case 1:
        printf("one.\n");
        break;
    case 2:
        printf("two.\n");
        break;
    case 3:
        printf("three.\n");
        break;
    case 4:
        printf("four.\n");
        break;
    case 5:
        printf("five.\n");
        break;
    case 6:
        printf("six\n");
        break;
    case 7:
        printf("sevem\n");
        break;
    case 8:
        printf("eight.\n");
        break;
    case 9:
        printf("nine\n");
        break; 
    default:
        break;
    }
    
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
//write a program that asks the user to enter a wind speed (in knots), then display the corresponding description
float ex4(void){
    float speed;

    printf("Enter wind speed in knots: ");
    scanf("%f", &speed);

    if(speed < 1){
        printf("Wind is calm\n");
    }
    else if(speed < 3){
        printf("Wind is a light air\n");
    }
    else if(speed < 27){
        printf("Wind is a breeze\n");
    }
    else if(speed < 47){
        printf("Wind is gale\n");
    }
    else if(speed < 63){
        printf("Wind is storming\n");
    }
    else{
        printf("Wind is a hurricane\n");
    }
    

    return 0.0;
}

//*********************
/*modify broker.c to ask the user to enter the number of shares and price per share, instead of value of trade 
 *  AND add statements that compute the commision charged by a rival broker ($33 plus 3 cents per share for 
 *  fewer than 2000 shares; $33 plus 2 cents per share for 2000 shares or more) display rivals commission as well as original broker*/
float ex3(void){

    float commission, value, shares, priceps, rival;

    printf("Enter the number of shares: ");
    scanf(" %f", &shares);
    printf("Enter the price per share: ");
    scanf(" %f", &priceps);

    //UMMMM googled calculation commission based on price per share and it said Totalvalue = pps * numShares sooooo...

    value = priceps * shares;

    if(value < 2500.00f)
        commission = 30.00f + .017f * value;
    else if( value < 6250.00f)
        commission = 56.00f + .0066f * value;
    else if( value < 20000.00f)
        commission = 76.00f + .0034f * value;
    else if( value < 50000.00f)
        commission = 100.00f + .0022f * value;
    else if( value < 500000.00f)
        commission = 155.00f + .0011f * value;
    else
        commission = 255.00f + .0009f * value;

    if(commission < 39.00f)
        commission = 39.00f;

    printf("Commission: $%.2f\n", commission);


    //i think doing the calcs right idk how to do these commission things lol
    if(shares < 2000){
        rival = 33.00f + (.03 * shares);
    }
    else
        rival = 33.00f + (.02 * shares);

    printf("Rivals Commission: $%.2f\n", rival);

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