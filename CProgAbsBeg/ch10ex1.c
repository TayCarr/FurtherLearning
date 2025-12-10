/*Sample program increases a counter from 1 to 5, printing updates then counts back down to 1*/

#include <stdio.h>

int main(){
    //variable set up
    int ctr = 0;

    ctr = ctr + 1;
    printf("Counter is at %d\n", ctr);
    ctr = ctr + 1;
    printf("Counter is at %d\n", ctr);
    ctr = ctr + 1;
    printf("Counter is at %d\n", ctr);
    ctr = ctr + 1;
    printf("Counter is at %d\n", ctr);
    ctr = ctr + 1;
    printf("Counter is at %d\n", ctr);

    //down
    ctr = ctr - 1;
    printf("Counter is at %d\n", ctr);
    ctr = ctr - 1;
    printf("Counter is at %d\n", ctr);
    ctr = ctr - 1;
    printf("Counter is at %d\n", ctr);
    ctr = ctr - 1;
    printf("Counter is at %d\n", ctr);

    //i dont wanna do the same prog using += and -= so just gonna do it here
    ctr += 1;
    printf("Counter is at %d\n", ctr);
    ctr -= 1;
    printf("Counter is at %d\n", ctr);

    return 0;

}