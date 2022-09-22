#include<iostream>
#include<bits/stdc++.h>
using namespace std;

void dn(int a,int b, int c){
        if(abs(a-c)==b){
            cout<<b<<endl;
        }else{
            cout<<max(abs(a-b),abs(a-c))<<endl;
        }


}

int main(int argc, char const *argv[])
{
    int a[3];
    for (int i = 0; i < 3; i++)
    {
        cin>>a[i];
    }
    
    sort(a,a+3);
    dn(a[2],a[1],a[0]);
    


return 0;
}

