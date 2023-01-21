#include<stdio.h>
#include<cs50.h>
#include<math.h>

int main(){
    float change = get_float("Change owed: ");
    int cents = round(change * 100);
    int count = 0;

    while (cents > 0){
        if (cents >= 25){
            cents -= 25;
            count++;
        } else if (cents >= 10){
            cents -= 10;
            count++;
        } else if (cents >= 5){
            cents -= 5;
            count++;
        } else{
            cents -= 1;
            count++;
        }
    }
    printf("%d\n", count);
}