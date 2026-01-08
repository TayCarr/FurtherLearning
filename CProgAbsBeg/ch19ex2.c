/*Sample program asks user for their home town and the two letter abbrev of their province, then uses str concat to 
    build a new string */

/*GETS AND PUTS are depricated and unsafe to use in programs */


#include <stdio.h>
#include <string.h>

int main(){
    char city[25];
    char prov[3]; //2 letters and null char
    char fullLocation[28] = "";

   puts("What town do you live in? ");
   gets(city);

   puts("What is the two letter abbreviation for the province you live in? ");
   gets(prov);

   //concate
   strcat(fullLocation, city);
   strcat(fullLocation, ", ");
   strcat(fullLocation, prov);

   puts("You live in ");
   puts(fullLocation);

    
    return 0;

}