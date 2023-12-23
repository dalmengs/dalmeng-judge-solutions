#include <iostream>
using namespace std;

int min(int a, int b){
    if(a < b) return a;
    return b;
}

int max(int a, int b){
    if(a > b) return a;
    return b;
}

int main(){
    int* arr = {9, 3, 8, 5, 10, 4, 7, 2, 1, 6};
    
    int mininum_value = 65535;
    int maxinum_value = 0;
    
    for(int i = 0; i < 10; i++){
        mininum_value = min(mininum_value, arr[i]);
        maxinum_value = max(maxinum_value, arr[i]);
    }
    
    return 0;
}
