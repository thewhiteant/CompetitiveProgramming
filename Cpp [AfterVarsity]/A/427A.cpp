#include<iostream>
using namespace std;

int main(int argc, char const *argv[])
{

    int n;
    cin>>n;
    int polic = 0;
    int crime = 0;
    for (int  i = 0; i < n; i++)
    {
        
        int x;
        cin>>x;
        if(x>0){
            polic+=x;
        }else{
            if(polic<1){
                ++crime;
            }else{
                --polic;
            }
        }
    }
    cout<<crime<<endl;


    


    




    return 0;
}
