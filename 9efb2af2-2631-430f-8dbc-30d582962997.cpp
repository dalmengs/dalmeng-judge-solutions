#include <iostream>
using namespace std;

int main(){
    int score = 100;
    char result = 'F';
    
    if(score == 100) result = 'S';
    else if(score >= 90) result = 'A';
    else if(score >= 80) result = 'B';
    else if(score >= 70) result = 'C';
    else if(score >= 60) result = 'D';

	return 0;
}
