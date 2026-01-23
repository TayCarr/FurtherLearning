/**
 * Taylor Carreiro 2026
 * CH6 programming projects
*/

/**
 * 1./program that finds the largest in a series of numbers entered by user
 * 2./asks user to enter two ints, then calculates and displays the GCD
 * 3./write program that asks user to enter a fraction then display it in lowest terms
 * 4. add a loop to broker.c so that the user can enter more than one trade and the program will calculate the commission on each
 * 5. generalize project 1 ch4 
 * 6./program that asks user to enter number n then displays even squares between 1-n
 * 7. rearrange square3.c so that the for loop inits i, tests i, and increments i
 * 8. print one-month calendar, user specifies days and the day month begins
 * 9. proj 8 ch2 uhhhhh
 * 10. proj 9 ch5 user can now enter more dates until 0/0/0
 * 11. approximate e by computing value of ... n is int entered by user
 * 12. modify above to uhhhh
*/

#include <stdio.h>

//defines 

//prototype functions 
void ex1(void);
int ex2(int first, int second);
float ex3(void);
float ex4(void);
float ex5(void);
float ex6(void);
void ex11(void);


int main(){

    //ex1();
    //ex2();
    //ex3();
    //ex6();
    ex11();

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
//approximate e by computing value of ... n is int entered by user
//TODO idk the calculation is off...
void ex11(void){
    float n, i = 0, e = 0, j, temp = 1;
    float denom = 0;
    

    printf("Enter an integer: ");
    scanf(" %f", &n);


    while(i < n+1){
        if (i == 0 || i == 1){
            e++;
            i++;

        }
        else{
            for (j = 1; j < i+1; j++){
                temp = temp * j;
            }
            e += (1/temp);
            i++;

        }
        
        //printf("current series: %f\n", 1/temp);
        

    }
    printf(" e: %f\n", e);

    
}


//*********************
//program that asks user to enter number n then displays even squares between 1-n
float ex6(void){
    int n, i = 2, square = 0;

    printf("Enter an integer: ");
    scanf(" %d", &n);
    //square of even number always even same is true for odd SO mod 2 == 0 means even if not continue
    while (square < n + 1){
        square = i*i;
        if (i % 2 == 0){
            
            printf("%d\n", square);
        }
        
        i++;
    }
    

    return 0.0;
}

//*********************
//write program that asks user to enter a fraction then display it in lowest terms
float ex3(void){
    int num, denom;
    int gcd = 0;

    printf("Enter a fraction:" );
    scanf(" %d/%d", &num, &denom);
    gcd = ex2(num, denom);
    //printf("GCD: %d\n", gcd);
    printf("In lowest terms: %d/%d\n\n", num/gcd, denom/gcd);

    

    return 0.0;
}

//*********************
// asks user to enter two ints, then calculates and displays the GCD
int ex2(int first, int second){
    int gcd = 0;
    int m = first, n = second, r;

    //printf("Enter two integers: ");
    //scanf(" %d %d", &m, &n);

    //euclids algorithm

    do{
        r = m%n;

        if (r == 0)
        {
            gcd = n;
            //comment out cause im gonna use this function in func 3 to calc gcd
            //printf("Greatest common divisor: %d\n", gcd);
            return gcd;
        }
        m = n;
        n = r;
        
    } while (n != 0);


    return gcd;

}

//*********************
//program that finds the largest in a series of numbers entered by user, prompt user to enter numbers one by one once 0
//is entered program will display the largest num, can be floats 

void ex1(void){
    float temp, max;

    printf("Enter a number: ");
    scanf(" %f", &max);
    temp = max;

    while(temp != 0){
        printf("Enter a number: ");
        scanf(" %f", &temp);
        if (temp > max){
            max = temp;
        }
    }
    printf("The largest number entered was %.6f\n\n", max);
    
}