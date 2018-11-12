#include<bits/stdc++.h>
#define mod 10000007
using namespace std;
typedef long long int ll;
string cf(string &s)
{
     set<char> s1;
     for(int i=0;i<s.length();++i)
        s1.insert(s[i]);
     string s2("\0");
     set<char>::iterator it;
     for(it=s1.begin();it!=s1.end();++it)
         s2+=(*it);
     return s2;
}
int main()
{
    int n;
    cin>>n;
    map<string,string> m;
    for(int i=0;i<n;++i)
    {
        char c;cin>>c;
        int t;
        cin>>t;
        while(t--)
        {
            string s("\0");
            cin>>s;
            m[s]+=c;
        }
    }
    string s("\0");
    cin>>s;
    vector< vector<string> > A;
    vector<string>B;
    int l=s.length();
    for(int i=0;i<=l;++i)
    {
       A.push_back(B);
       A[i].push_back("fhd");
    }

    for(int i=1;i<=l;++i){A.push_back(B);
            string t("\0");
        t+=s[i-1];
        A[1].push_back(m[t]);
    }

    int i;
    for( i=2;i<=l;++i){
        int r=i;
        for(int j=1;j<=l-i+1;(++j&&++r)){string t("\0");
            for(int k=j;k<r;++k){
                string s1("\0"),s2("\0"),p("\0");

                s1+=A[k-j+1][j];
                s2+=A[r-k][k+1];
                if(s1.length()==0){
                    for(int w=0;w<s2.length();++w){
                        string q("\0");
                        q+=s2[w];string e("\0");
                        e=m[q];
                        if(e!="\0")
                        p+=e;
                    }
                }
                if(s2.length()==0){
                    for(int w=0;w<s1.length();++w){
                        string q("\0");
                        q+=s1[w];string e("\0");
                        e=m[q];
                        if(e!="\0")
                        p+=e;
                    }
                }else{
                for(int v=0;v<s1.length();++v){
                    for(int w=0;w<s2.length();++w){
                        string q("\0");
                        q+=s1[v];
                        q+=s2[w];string e("\0");
                        e=m[q];
                        if(e!="\0")
                        p+=e;
                    }
                }}
                t+=p;
            }
            A[i].push_back(t);
        }

    }
  for(int i=1;i<=l;++i){
    for(int j=1;j<=l-i+1;++j)
    {
        string s("\0"),s1("\0");
        s=A[i][j];
       s1= cf(s);
       if(s1!="\0")
            cout<<s1<<" ";
        else {cout<<"$"<<" ";}
    }cout<<endl;
  }
    return 0;
}
