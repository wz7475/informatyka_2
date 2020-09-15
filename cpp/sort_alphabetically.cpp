#include <iostream>
#include <string>
using namespace std;

string sort(string s)
{
    int length = s.size();

    for (int i = 0; i < length; i++)
    {
        for (int j = i + 1; j < length; j++)
        {
            if(s[j] < s[i]) 
                swap(s[i], s[j]);
        }
    }
    return s;
}

int main()
{
    string s="asdgsdfg";
    cout << sort(s) << endl;
    char z;
    cin>>z;
    return 0;
}