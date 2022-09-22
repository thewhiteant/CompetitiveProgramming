#include<iostream>
using namespace std;


int main(int argc, char const *argv[])
{
    
    int n,k;
    cin>>n>>k;
    int p[n];
    int count = 0;  
    for (int i = 0; i < n; i++)
    {
        cin>>p[i];
    }
  
    for (int i = 0; i < n; i++)
    {   if(p[i]<5){
            if (5-p[i] >= k  )
            {
                count++;       
            }
    }}

    if (count >= 3)
    {
        cout<<count/3;
    }else{
        cout<<0;
    }  
    

    
    return 0;
}
