#include<stdio.h>
#include<cs50.h> //For getting get_string function

int main(void){
    string name = get_string("What is your name?\n"); // gets the name(input)
    printf("hello, %s\n", name); // prints hello followed by name
}