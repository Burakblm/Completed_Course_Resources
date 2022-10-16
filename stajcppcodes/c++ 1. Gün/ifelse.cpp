#include<iostream>

int main(){

    int islem;
    std::cin >> islem;

    if(islem == 1){
        std::cout << "islem 1" << std::endl;
    }
    else if(islem == 2){
        std::cout << "islem 2" << std::endl;
    }
    else{
        std::cout << "yanlis islem numarasi" << std::endl;
    }

    return 0;
}