/* Strings in c are terminated by the null zero \0
    you dont need to add this c will auto do it, this is how it knows that the string has reached the end
    length of strings do not include the null but it is there 
    length of characters is 1 but for example 'x' is 1 and "x" is also length 1 but "x" takes 2 spaces of mem for the null
*/
#include <stdio.h>
#include <string.h>//need to have for strcopy

int main(){
    //defining a character array
    //char month[10]; //longest month name is september (9 chars) need additional space for null

    //can assign at the same time too like 
    char month[10] = "January";
    printf("%s\n", month);
    //when declaring an array declare as much as the max you would need, can't declare smaller than you would need

    //if individually changing the contents of you array then must add the null 
    month[0] = 'M';
    month[1] = 'A';
    month[2] = 'R';
    month[3] = 'C';
    month[4] = 'H';

    printf("%s\n", month); //will see the end of jan still printed
    
    month[5] = '\0';//need to add the null
    printf("%s\n", month);

    //if you define an array at the time of initi then you do not need to include a number in the brackets
    char myMonth[] = "August";
    printf("%s\n", myMonth);
    //cannot assign a new string like myMonth = "December"; this will error
    //but you can strcopy, needs to be the same or less length though
    strcpy(myMonth, "July");
    printf("%s\n", myMonth);

    //now for the "program"
    //this program compares three kids with their fav superhero
    char kid1[12];
    //kid1 can hold an 11 character name
    //kid2 will be 7 chars, maddie plus null
    char kid2[] = "Maddie";
    //kid 3 is also 7 chars but specifically defined
    char kid3[7] = "Andrew";

    //Hero1 will be 7 chars
    char hero1[] = "Batman";
    //Hero2 will have extra room just incase
    char hero2[34] = "Spiderman";
    char hero3[25];

    kid1[0] = 'K';
    kid1[1] = 'a';
    kid1[2] = 't';
    kid1[3] = 'i';
    kid1[4] = 'e';
    kid1[5] = '\0'; //not efficient but works, must include null

    strcpy(hero3, "The Incredible Hulk");

    printf("%s\'s fav hero is %s.\n", kid1, hero1);
    printf("%s\'s fav hero is %s.\n", kid2, hero2);
    printf("%s\'s fav hero is %s.\n", kid3, hero3);


    return 0;
}


