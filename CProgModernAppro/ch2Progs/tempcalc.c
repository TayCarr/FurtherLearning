/**
 * converts fahrenheit temp to cels
*/

#include <stdio.h>

#define FREEZING_PT 32.0f //leaving f at the end of floating point 
#define SCALE_FACTOR (5.0f / 9.0f)

int main(){
    float fahrenheit, celsius;

    printf("Enter fahrenheit temperature: ");
    scanf(" %f", &fahrenheit);

    celsius = (fahrenheit - FREEZING_PT) * SCALE_FACTOR;
    printf("Celsius: %.1f\n", celsius);

    return 0;
}