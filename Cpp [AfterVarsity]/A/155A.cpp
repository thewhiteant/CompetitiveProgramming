#include<iostream>

using namespace std;



int main()
{
    int a;
    int count = 0;
    cin>>a;
    int ar[a];
    for (int i = 0; i < a; i++)
    {
        cin>>ar[i];
    }
    
    int max = ar[0];
    int min = ar[0];

    for (int i = 0; i < a; i++)
    {
            if(ar[i]>max){
                max = ar[i];
                count++;
            }
            if(ar[i]< min){
                min = ar[i];
                count++;
            }

    }
    cout<<count<<endl;

    
    return 0;
}
