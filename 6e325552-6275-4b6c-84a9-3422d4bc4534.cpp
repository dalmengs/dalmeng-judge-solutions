#include <iostream>
using namespace std;

int main(){
    int n = 0;
    int result = 1;
    
    while(++n){
        result += (result + n);
    }

	return 0;
}
