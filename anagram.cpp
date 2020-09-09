#include <iostream>
#include <cstring>
using namespace std;

string sort(string s)
{
    int length = s.size(), k;

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

bool check( string s1, string s2)
{
    if (s1.size() != s2.size())
        return false;
    if (sort(s1) != sort(s2))
        return false;
    return true;
}
int main()
{
    string s1, s2;
    cout << "enter 2 words:\n";
    cin >> s1 >> s2;
    if (check(s1, s2))
        cout << "they are anagrams\n";
    else
        cout << "they aren't anagrams\n";
    return 0;
}