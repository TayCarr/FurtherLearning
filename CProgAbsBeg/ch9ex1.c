/*Sample program showing math operators, and dif types of division */

#include <stdio.h>

int main(){
    //variable set up
    float a = 19.0;
    float b = 5.0;
    float floatAnswer;

    int x = 19;
    int y = 5;
    int intAnswer;

    //using two float vars gives 3.8
    floatAnswer = a / b;
    printf("%.1f divided by %.1f equals %.1f\n", a, b, floatAnswer);

    //using two int vars into float var gives 3.0
    floatAnswer = x / y;
    printf("%d divided by %d equals %.1f\n", x, y, floatAnswer);

    //also 3 but truncated
    intAnswer = a / b;
    printf("%.1f divided by %.1f equals %d\n", a, b, intAnswer);

    //calcs remainder
    intAnswer = x % y;
    printf("%d modulus %d equals %d\n", x, y, intAnswer);

    return 0;

}