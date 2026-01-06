/*examples of escape chars and conversion chars*/

#include <stdio.h>

int main(){
    printf("Quantity\tCost\tTotal\n");
    printf("%d\t\t$%.2f\t$%.2f\n", 3, 9.99, 29.97);
    printf("Too many spaces    \b\b\b\b can be fixed with the ");
    printf("\\%c Escape character\n", 'b');
    printf("\n\a\n\a\n\aSkip a few lines, and beep");
    printf(" a few beeps.\n\n\n");
    printf("%s %c", "great job learning", 'c');
    printf("There was more examples of writing different floats but I am too lazy to write those out...\n");

    return 0;
}