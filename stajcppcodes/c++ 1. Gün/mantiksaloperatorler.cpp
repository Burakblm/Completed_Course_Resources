#include<iostream>

int main(){

    int a = 12;
    int b = 3;

    std::cout << a + b << std::endl; // 15
    std::cout << a - b << std::endl; // 9
    std::cout << a / b << std::endl; // 4
    std::cout << a * b << std::endl; // 36
    std::cout << a % b << std::endl; // 0
    b = b+1;
    b = b-1;
    b++;
    b--;
    --b;
    ++b;

    return 0;
}