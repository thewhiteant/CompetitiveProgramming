#include<iostream>
#include<bits/stdc++.h>
using namespace std;

int main()
{   
    int t;
    cin>>t;
    while (t--)
    {

    

    int n;
    cin>>n;
    vector<int>my;
    int ans;
    if(n%10!=0){ my.push_back(n%10); }
     ans = n%10;
    n-=ans;
    if(n%100!=0){ my.push_back(n%100); }
     ans = n%100;
    n-=ans;
      if(n%1000!=0){ my.push_back(n%1000); }
     ans = n%1000;
    n-=ans;
      if(n%10000!=0){ my.push_back(n%10000); }
      if(n>=10000 && n%10000==0) {my.push_back(n);}
      cout<<my.size()<<endl;
      for (int i = 0; i < my.size(); i++)
      {
        cout<<my[i]<<" ";
      }
      

    }
    
    return 0;
}
