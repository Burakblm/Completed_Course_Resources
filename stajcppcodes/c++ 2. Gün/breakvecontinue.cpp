#include<iostream>

int main(){

    int i = 0;

    while(i < 10){
        if(i == 3 || i == 5){
            continue;
        }
        std::cout << i << std::endl;
        i++;

    }

    int b = 0;

    while(b < 100){

        if(b == 34){
            break;
        }
        std::cout << b << std::endl;
    }

    return 0;
}