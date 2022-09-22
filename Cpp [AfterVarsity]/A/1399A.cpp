#include<iostream>
#include <bits/stdc++.h>
using namespace std;



int main(int argc, char const *argv[])
{
    int t;
    cin>>t;
    m:
    while(t--){
        int n;
        cin>>n;
        int ar[n];
        for (int i = 0; i < n; i++) cin>>ar[i];
        sort(ar, ar + n);
        for (int i =1; i < n; i++)
        {
            if(ar[i] - ar[i-1]>1){
                cout<<"No"<<endl;
                goto m;
                } 
                
        }
         cout<<"YES"<<endl;       
        }
 return 0;
}