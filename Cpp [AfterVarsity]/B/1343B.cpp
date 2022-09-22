#include<iostream>
#include<bits/stdc++.h>
using namespace std;

int main(int argc, char const *argv[])
{
int t;
cin>>t;
while (t--)
{
    

   
    int n;
    cin>>n;
      if(n%4==0){
        cout<<"YES"<<endl;

    int jor = 0;
    int bijor = 0;
    vector<int> test;

    for (int i = 1; i <= n; i++)
    {
        if(i%2==0){
            test.push_back(i);
            jor+=i;

        }

    }
    for (int i = 1; i <= n; i++)
    {
        if(i%2!=0){
        test.push_back(i);
        bijor+=i;}
    }
    
     if(jor>bijor){
        int s = jor-bijor;
        test.back() = test.back() + s;
     }


     for (int i = 0; i < n; i++)
     {
        cout<<test[i]<<" ";
     }
     cout<<endl;
      }else{
        cout<<"NO"<<endl;
      }
}


    return 0;
}
