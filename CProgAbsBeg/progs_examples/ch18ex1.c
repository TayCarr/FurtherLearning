/*Sample program demonstrates putchar() also added the second example in here which shows getchar*/


#include <stdio.h>
#include <string.h>

int main(){
    int i;
    char msg[] = "C is fun";
    //vars for 2nd ex
    int j;
    char words[25];

    //first ex
    for (i = 0; i < strlen(msg); i++){
        putchar(msg[i]); //outputs single char
    }
    putchar('\n'); 

    //second ex
    printf("Type up to 25 chars and then press enter...\n");
    for (j = 0; j < 25; j++){
        words[j] = getchar(); //single char
        if (words[j] == '\n'){
            i--;
            break;
        }
    }
    putchar('\n');

    for (; j >= 0; j--){
        putchar(words[j]);
    }
    putchar('\n');

    
    return 0;

}