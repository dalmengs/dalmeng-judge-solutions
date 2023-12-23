#include <iostream>
#include <cstdlib>
using namespace std;

const int SIZE = 5000;

const int LOWER_LIMIT = -(1 << 17 - 1);
const int UPPER_LIMIT = 1 << 17 - 1;

int main(){
    int arr[SIZE];
    for(int i = 0; i < SIZE; i++){
        arr[i] = rand() % (UPPER_LIMIT + UPPER_LIMIT) + LOWER_LIMIT;
    }
    
    int result = 0;
    for(int i = 0; i < SIZE; i += 2){
        result += (arr[i + 1] - arr[i]);
    }

	return 0;
}
