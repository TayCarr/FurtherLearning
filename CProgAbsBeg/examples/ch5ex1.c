/*Examples of how to declare various types of variables*/

#include <stdio.h>

int main(){
    char answer;
    int quantity;
    float price;

    char first_initial;
    char middle_initial;

    char first_letter, last_letter;

    quantity = 14;
    price = 7.95; //can directly assign

    price = 8.50 * .65; //can use an expression to assign
    float totalAmount = price * quantity; //can use expression of other variables to assign 

    /*Sample program that lists 3 kids and their supplies, then the costs*/
    int number_of_pencils;
    int number_of_notebooks;
    float pencils = 0.23;
    float notebooks = 2.89;
    float lunchbox = 4.99;

    //first child info
    first_initial = 'J';
    middle_initial = 'R';
    number_of_pencils = 7;
    number_of_notebooks = 4;

    printf("%c%c needs %d pencils, %d notebooks, amd 1 lunchbox\n", first_initial, middle_initial, number_of_pencils, number_of_notebooks);
    printf("The total cost is $%.2f\n\n", (number_of_notebooks * pencils) + lunchbox + (number_of_notebooks * notebooks));

    //second child info
    first_initial = 'A';
    middle_initial = 'J';
    number_of_pencils = 10;
    number_of_notebooks = 3;

    printf("%c%c needs %d pencils, %d notebooks, amd 1 lunchbox\n", first_initial, middle_initial, number_of_pencils, number_of_notebooks);
    printf("The total cost is $%.2f\n\n", (number_of_notebooks * pencils) + lunchbox + (number_of_notebooks * notebooks));

    //third child info
    first_initial = 'M';
    middle_initial = 'T';
    number_of_pencils = 9;
    number_of_notebooks = 2;

    printf("%c%c needs %d pencils, %d notebooks, amd 1 lunchbox\n", first_initial, middle_initial, number_of_pencils, number_of_notebooks);
    printf("The total cost is $%.2f\n\n", (number_of_notebooks * pencils) + lunchbox + (number_of_notebooks * notebooks));

    return 0;

}