#include<iostream>
using namespace std;


int main(){
    int x,y;
    cin>>x>>y;
    int sum = 0;
    int i = 1;
    while(true){

        sum = sum + x;
        if(sum%10==0||sum%10==y){
            cout<<i;
            break;
        }
        i++;

    }    



    return 0;
}



