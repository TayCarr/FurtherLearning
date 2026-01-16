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
 * 5.
 * 6.
 * 7.
 * 8.
*/

#include <stdio.h>
#include <math.h>

//defines 
#define TAX 1.05 //5% tax

//prototype functions 
void ex1(void);
float ex2(void);
float ex4(void);


int main(){

    //ex1();
    //ex2();
    ex4();

    return 0;
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