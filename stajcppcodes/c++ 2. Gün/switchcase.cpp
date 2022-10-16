#include<iostream>

int main(){

    int islem;
    std::cout << "Bir işlem numarasi giriniz : ";
    std::cin >> islem;

    switch (islem)
    {
    case 1:
        std::cout << "1. islemi sectiniz" << std::endl;
        break;
    case 2:
        std::cout << "2. islemi sectiniz" << std::endl;
        break;
    case 3:
        std::cout << "3. islemi sectiniz" << std::endl;
        break;
    
    default:
        std::cout << "hatali giris yaptiniz" << std::endl;
        break;
    }

    return 0;
}