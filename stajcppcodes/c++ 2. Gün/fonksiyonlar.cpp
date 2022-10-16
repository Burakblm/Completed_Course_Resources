#include<iostream>

void selamla(){
    std::cout << "Merhaba Dünya" << std::endl;
}

int topla(int a, int b){
    return a+b;
}

int main(){

    std::cout << topla(24,54) << std::endl;
    selamla();

    return 0;
}