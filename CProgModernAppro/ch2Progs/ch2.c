/**
 * Taylor Carreiro 2026
 * CH2 programming projects, probably will just do them as functions in one program, unless they are decent 
 * sized programs...
*/

/**
 * 1. create a program that uses printf to display the following picture (checkmark made of stars)
 * 2. prog that computes the volume of a sphere with a 10 metre radius using the formula v=4/(3*pi*r^3)
 * 3. modify prog 2 to prompt the user to enter a radius to use in calculations
 * 4. ask user to enter a dollar and cents amount, display amount with 5% tax
 * 5. ask user for a value x and calculate 3x^5+2x^4-5x^3-x^2+7x-6
 * 6. modify prog 5 to horners rule ((((3x+2)x-5)x-1)x+7)x-6
 * 7. ask user for a dollar amount then show how to pay amount in the smallest number of bills 20/10/5 etc
 * 8. calculate the remaining balance on a loan after the first, second, and third monthly payments
*/

#include <stdio.h>
#include <math.h>

//defines 
#define TAX 1.05 //5% tax

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
    ex8();


    return 0;
}

//*********************
//calculate the remaining balance on a loan after the first, second, and third monthly payments
float ex8(){
    float loan, interest, payment, rate;
    int i;

    printf("Enter loan amount: ");
    scanf(" %f", &loan);
    printf("Enter interest amount: ");
    scanf(" %f", &interest);
    printf("Enter monthly payment amount: ");
    scanf(" %f", &payment);

    rate = (interest / 100.00);
    rate = rate / 12.0;
    printf("%.6f\n", rate);

    for(i = 0; i < 3; i++ ){
        loan = loan + (loan * rate);
        loan = loan - payment;
        
        printf("Balance remaining after payment #%d: $%.2f\n", i+1, loan); //ummmm the cents is off?? idk why...
        //googled the like process of interest calculations /month and this should be correct way so w/e this is good enough lol

    }


    return 0.0;
}

//*********************
//ask user for a dollar amount then show how to pay amount in the smallest number of bills
//recd to /20 and use that did it a dif way maybe that way is better? could do that logic in my loop 
float ex7(){
    float dollar, temp;
    int twenty = 0, ten = 0, five = 0, toonie = 0, loonie = 0;

    printf("Enter a dollar amount: ");
    scanf(" %f", &dollar);

    while(dollar >= 20.0){
        twenty++;
        dollar = dollar - 20;
        //printf("\n twenty %.1f\n", dollar);

    }
    while(dollar >= 10.0){
        ten++;
        dollar = dollar - 10;
        //printf("\n ten %.1f\n", dollar);
        
    }
    while(dollar >= 5.0){
        five++;
        dollar = dollar - 5;
        //printf("\n five %.1f\n", dollar);
        
    }
    while(dollar >= 2.0){
        toonie++;
        dollar = dollar - 2;
        //printf("\n toonie %.1f\n", dollar);
        
    }
    while(dollar >= 1.0){
        loonie++;
        dollar = dollar - 1;
        //printf("\n loonie %.1f\n", dollar);
        
    }

    printf("$20 bills: %d\n$10 bills: %d\n$5 bills: %d\ntoonies: %d\nloonies: %d\n\n", twenty, ten, five, toonie, loonie);
    return 0.0;
}

//*********************
//ask user for x value and calculate below (using math.h for pow)
//3x^5+2x^4-5x^3-x^2+7x-6
//then calculate with horners ((((3x+2)x-5)x-1)x+7)x-6
float ex5(){
    float x, total, horner;
    printf("Enter a value for x: ");
    scanf(" %f", &x);

    total = (3 * pow(x, 5)) + (2 * pow(x, 4)) - (5 * pow(x, 3)) - (pow(x, 2)) + (7 * x) - 6;
    horner = ((((3 * x + 2) * x - 5) * x - 1) * x + 7) * x - 6;

    printf("Total: %.1f\nHorner: %.1f\n\n", total, horner);

    return horner;
}


//*********************
//get user $ input calculate total after tax 5%
float ex4(void){
    float amount, total;

    printf("Enter an amount: ");
    scanf(" %f", &amount);
    total = amount * TAX;
    printf("With tax added: %.2f\n\n", total);

    return total;
}

//*********************
//calculate volume of sphere
//using math library instead of r*r*r
//2, 3-> add ability for user to input radius 
float ex2(void){
    float volume;
    //float radius = 10.0f; 
    float radius;

    printf("Radius: ");
    scanf(" %f", &radius);
    

    volume = (4.0f * 3.0f) * 3.14f * pow(radius, 3.0);
    printf("Volume of a sphere with the radius %.1f: %.2f\n", radius, volume);

    return volume;

}

//*********************
//prints a simple picture
//originally tried to do \t BUT the spaces were too large and it made a wide checkmark, 
//I wanted it to look more like the picture in the textbook

void ex1(void){
    printf("       *\n      *\n     *\n*   *\n * *\n  *\n\n");
}