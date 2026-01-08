/*Sample program asks user for username and password, tets if the password has digit, upper and lower case
    if it does congratulates user else suggests a password change*/


#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(){
    int i;
    int hasUpper, hasLower, hasDigit;
    char user[25], password[25];

    //init all three test variables to 0 (false)
    hasUpper = hasLower = hasDigit = 0;

    printf("What is your username? ");
    scanf(" %s", user);

    printf("Please create a password for your account: ");
    scanf(" %s", password);

    //loop goes through each char of the password and tests if it is a digit, upper, or lower letter

    for (i = 0; i < strlen(password); i++){
        if(hasDigit && hasLower && hasUpper){
            break;
        }
        if (isdigit(password[i])){
            hasDigit = 1;
            continue;
        }
        if (isupper(password[i])){
            hasUpper = 1;
            continue;
        }
        if (islower(password[i])){
            hasLower = 1;
            continue;
        }
    }

    if (hasDigit && hasLower && hasUpper){
        printf("Good password!\n");
    }
    else{
        printf("You should pick a password with lower and uppercase letters and a digit.\nTry again.\n");
    }
    
    return 0;

}