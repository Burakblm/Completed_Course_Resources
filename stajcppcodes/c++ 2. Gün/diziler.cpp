#include<iostream>

int main(){

    int array[3];
    int array1[] = {1,2,3,4};
    double array2[4];
    double array3[] = {1.2,34.6};
    std::string strarray[] = {"Staj","dizi"};
    
    for(int i = 0; i < 3; i++){
        array[i] = i;
    }
    for(int i = 0; i < 3; i++){
        std::cout << array[i] << std::endl;
    }


    return 0;
}