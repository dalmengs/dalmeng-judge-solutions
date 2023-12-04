#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

// 정렬 기준 함수 
bool cmp(string a, string b){
    vector<pair<string, bool>> a_v; // a의 그룹 
    vector<pair<string, bool>> b_v; // b의 그룹 
    
    string now = "";
    bool isNumber = false;
    
    for(int i = 0; i < a.length(); i++){
        if(a[i] == '.'){ // 파일 이름과 확장자 사이, 그룹 만들기 끝 
            a_v.push_back({now, isNumber});
            break;
        }
        
        if(i != 0 && isNumber && !('0' <= a[i] && a[i] <= '9')){ // 숫자 그룹 -> 문자 그룹
            a_v.push_back({now, true});
            isNumber = false;
            now = "";
        }
        else if(i != 0 && !isNumber && ('0' <= a[i] && a[i] <= '9')){ // 문자 그룹 -> 숫자 그룹 
            a_v.push_back({now, false});
            isNumber = true;
            now = "";
        }
        
        if('0' <= a[i] && a[i] <= '9') isNumber = true; // 숫자인 경우 
        else isNumber = false; // 문자인 경우 

        now += a[i];
    }
    
    now = "";

    for(int i = 0; i < b.length(); i++){
        if(b[i] == '.'){ // 파일 이름과 확장자 사이, 그룹 만들기 끝 
            b_v.push_back({now, isNumber});
            break;
        }
        
        if(i != 0 && isNumber && !('0' <= b[i] && b[i] <= '9')){ // 숫자 그룹 -> 문자 그룹
            b_v.push_back({now, true});
            isNumber = false;now = "";
        }
        else if(i != 0 && !isNumber && ('0' <= b[i] && b[i] <= '9')){ // 문자 그룹 -> 숫자 그룹 
            b_v.push_back({now, false});
            isNumber = true;now = "";
        }
        
        if('0' <= b[i] && b[i] <= '9') isNumber = true; // 숫자인 경우 
        else isNumber = false; // 문자인 경우 
        
        now += b[i];
    }

    // 그룹 간 비교 
    for(int i = 0; i < min(a_v.size(), b_v.size()); i++){
        if(a_v[i].second == b_v[i].second){ // 종류가 같은 경우 

            if(a_v[i].second == true){ // 숫자 그룹끼리 비교 
                int x = stoi(a_v[i].first);
                int y = stoi(b_v[i].first);

                if(x == y){ // 숫자로 변환했을 때, 값이 같은 경우 
                    if(a_v[i].first.length() == b_v[i].first.length()) continue; // 값과 문자열의 길이가 모두 같으면 다음 그룹 확인 
                    return a_v[i].first.length() < b_v[i].first.length(); // 값은 같지만 문자열의 길이가 다르면 사전 순으로 정렬 
                }
                return x < y; // 값이 다르면 작은 수가 먼저 온다 
            }
            else{ // 문자 그룹끼리 비교 
                if(a_v[i].first == b_v[i].first) continue; // 문자열이 완전히 같으면 다음 그룹 확인 
                return a < b; // 문자열이 다르면 사전 순 정렬 
            }
        }
        else{ // 종류가 다른 경우 
            if(a_v[i].second == true) return true; // a가 숫자인 경우, a가 먼저 온다 
            return false;
        }
    }
    
    if(a_v.size() != b_v.size())
        return a_v.size() < b_v.size(); // 비교한 그룹이 전부 같지만, 그룹의 크기가 다른 경우에는 크기가 작은 그룹이 먼저 온다 
    
    return a < b; // 나머지 부분(확장자)는 사전 순 정렬 
}

int main(){
    int n; cin >> n;

    vector<string> v;
    for(int i = 0; i < n; i++){
        string s; cin >> s;
        v.push_back(s);
    }
    
    sort(v.begin(), v.end(), cmp); // 위의 정렬 기준 함수 사용 
    
    for(string s: v) cout << s << "\n";
    return 0;
}
