#include <bits/stdc++.h>
using namespace std;
int main()
{
    int a;
    string s;
    stack<char> c;

    while(cin>>s)
    {
        a = 0;
        for(auto t:s)
        {
            if(t=='(' || t== '['|| t=='{')
            c.push(t);
            else
                if(!c.empty()
                    && t==')'
                    && c.top()==('(')

                    ||t==']'
                    && c.top()==('[')

                    ||t=='}'
                    && c.top()==('{') )

                    c.pop();
                else
                {
                    a = 1;
                    break;
                }
        }
        if(!c.empty())
        {
        a=1;
        while(c.empty())
            c.pop();
        }
        cout<<a;
    }
    return 0;
}