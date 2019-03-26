#include <bits/stdc++.h>
using namespace std;

int main() {
    map<string,int> days;
    days["monday"]=1;
    days["tuesday"]=2;
    days["wednesday"]=3;
    days["thursday"]=4;
    days["friday"]=5;
    days["saturday"]=6;
    days["sunday"]=7;
    int t;
    cin>>t;
    string a,b;
    while(t--)
    {
        int l,r,te1,te,count=0,i=0,ans;
        cin>>a>>b>>l>>r;
        if(days.at(a)<days.at(b))
        te=days.at(b)-days.at(a)+1;
        else if(days.at(b)<days.at(a))
        te=7-(days.at(a)-days.at(b))+1;
        else
        te=1;
        te1=0;

        // cout << "Diff: " << te << "\n";
       while(te1<=r)
       {
           te1=te+7*i;
           if(te1>=l&&te1<=r)
           {count++;
           ans=te1;
           }
           i++;
       }
       if(count==1)
       cout<<ans<<endl;
       else if(count>1)
       cout<<"many"<<endl;
      else
      cout<<"impossible"<<endl;
    }
	// your code goes here
	return 0;
}