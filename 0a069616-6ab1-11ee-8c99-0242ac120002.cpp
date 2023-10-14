#include <iostream>
#include <memory.h>
#include <queue>
#define min(a, b) (a < b ? a : b)
#define max(a, b) (a > b ? a : b)
#define M(a) memset(a, 0, sizeof(a))
using namespace std;

const int SIZE = 1e5 + 6;

int main(){
    int a, b, x; cin >> a >> b >> x;
    
    bool vis[SIZE]; M(vis);
    vis[x] = true;
    
    queue<pair<int, int>> q;
    q.push({x, 0});
    
    int ans = 0;
    
    while(!q.empty()){
        pair<int, int> now = q.front(); q.pop();
        int hp = now.first;
        int cnt = now.second;
        
        if(hp == 0){
            ans = cnt;
            break;
        }
        
        int next;
        
        // Skill 1
        next = min((int)(hp / 2) + a, x);
        if(!vis[next]){
            q.push({next, cnt + 1});
            vis[next] = true;
        }
        
        // Skill 2
        next = max(hp - a, 0);
        if(!vis[next]){
            q.push({next, cnt + 1});
            vis[next] = true;
        }
    }
    
    cout << max(b - a * ans, 0);
    
    return 0;
}
