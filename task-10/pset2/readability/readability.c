#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <math.h>
#include <ctype.h>

int letter_count(string text){
    int letters = 0;
    for (int i = 0; i < len; i++){
        if (isupper(text[i])){
            letters++;
        } else if (islower(text[i])){
            letters++;
        }
    }
    return letters;
}

int word_count(string text){
    int words = 0;
    for (int i = 0; i < len; i++){
        if (text[i]== ' '){
            words++;
        }
    }
    return words + 1;
}

int sentence_count(string text){
    int sentences = 0;
    for (int i = 0; i < len; i++){
        if (text[i] == '.' || text[i] == '!' || text[i] == '?'){
            sentences++;
        }
    }
    return sentences;
}

int main(void){

    string text = get_string("Type: ");
    int len = strlen(text)
    float grade = 0.0588 * (100 * (float) letter_count(text) / (float) word_count(text)) - 0.296 * (100 * (float) sentence_count(text) / (float) word_count(text)) - 15.8;

    if (grade >= 0 && grade < 16){
        printf("Grade %i\n", (int) round(grade));
    } else if (grade >= 16){
        printf("Grade 16+\n");
    } else{
        printf("Before Grade 1\n");
    }
}
