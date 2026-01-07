/*Sample program demonstrates putchar()*/


#include <stdio.h>
#include <string.h>

int main(){
    int i;
    char msg[] = "C is fun";

    for (i = 0; i < strlen(msg); i++){
        putchar(msg[i]); //outputs single char
    }
    putchar('\n'); 
    
    return 0;

}