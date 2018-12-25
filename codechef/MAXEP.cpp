#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n,c,x;
    cin>>n>>c;
    int u,l=0,check=-1;
    int good=0,broke;
    int count=3;
    int amount=1000;
    u=pow(10,count);
    if(u>n)
    u=n;
    if(n<=10)
    count=0;
    else if(n<=100)
    count=1;
    else if(n<1000)
    count=2;
    while(amount>0)
    {
        if(u>n)
        u=n;
        cout<<"1 "<<u<<endl;
        cin>>check;
        if(check==0)
        {
            good=u;
            amount--;
            l=u;
            u+=pow(10,count);
        }
        else if(check==1)
        {
            broke=u;
            amount-=c;
            cout<<"2"<<endl;
            if(count>0)
            { 
               count--;
            }
            u=l+pow(10,count);
        }
        if(broke-good==1)
        {
            x=broke;
            cout<<"3 "<<x<<endl;
            break;
        }
        
        
        
    }
    return 0;
}