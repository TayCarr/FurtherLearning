/**
 * Taylor Carreiro 2026
 * CH7 programming projects
*/

/**
 * 1. skipping cause its just changing previous prog int types to see overflow 
 * 2.\modify square2.c of section 6.3 so that it pauses every 24 squares and displays "Press enter to continue...", 
 *      after displaying program waits for enter key (using getchar)
 * 3.\modify sum2.c program from section 7.1 to sum a series of double values
 * 4. write a program that translates an alphabetic phone number to numeric, assume that all letters entered are uppercase 
 * 5. using scrabble face values for letters make a program that computes the value of words entered, allow mix of upper and lower (use toupper)
 * 6. program that prints the values of sizeof(int), short, long, float, double, long double
 * 7. modify prog project 6 from ch3 to allow users to add subtract multiply or divide two fractions
 * 8. i simply do not want to do this one lol
 * 9. ask user for a 12 hour time then display it in 24 hour time 
 * 10. program that counts the number of vowels in a sentence
 * 11. program that takes first and last name then displays it as last name, first initial.
 * 12 program that evaluates an expression (evaluated left to right no higher order)
 * 13. program that calculates avg word length for a sentence 
 * 14. idk if i wanna do this one....
 * 15. program that computes the factorial of a positive int
*/

#include <stdio.h>

//defines 

//prototype functions 
float ex2(void);
float ex3(void);
float ex4(void);
float ex5(void);
float ex6(void);


int main(){

    //ex2();
    ex3();


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
//modify sum2.c program from section 7.1 to sum a series of double values
float ex3(void){
    double n, sum = 0;

    printf("This program sums a series of integers.\n");
    printf("Enter integers (0 to terminate): ");
    scanf("%lf", &n);
    while (n != 0)
    {
        sum += n;
        scanf("%lf", &n);
    }
    printf("The sum is: %.3lf\n", sum);
    

    return 0.0;
}

//*********************
// modify square2.c of section 6.3 so that it pauses every 24 squares and displays "Press enter to continue...", 
//     after displaying program waits for enter key (using getchar)
float ex2(void){
    int i, n, counter = 0;
    char cont;

    printf("This program prints a table of squares. \n");
    printf("Enter number of entries in the table: ");
    scanf(" %d", &n);
    getchar();//clear new line, need to flush since there is lingering from scanf

    for( i = 0; i <= n; i++){
        printf("%10d%10d\n", i, i*i);
        counter++;

        if(counter == 24){
            counter = 0;
            printf("\nPress Enter to continue...");

            do{
                cont = getchar();
            }while (cont != '\n');    

        }
    }


    return 0.0;

}
