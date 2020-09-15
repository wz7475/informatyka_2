#include <iostream>
#include <cstring>
using namespace std;

bool check(string s1, string s2)
{
    int length1 = s1.size();
    if (length1 != s2.size())
        return false;
    else
    {
        int counter1 = 0, counter2 = 0;
        for (int i = 0; i < length1; i++)
        {
            if (s1[i] == 'x')
                counter1++;
            if (s2[i] == 'x')
                counter2++;
        }
        if (counter1 == counter2)
            return true;
        return false;
    }
}

int main()
{
    string s1, s2;
    cout << "enter 2 words containing of 'x' and 'y':\n";
    cin >> s1 >> s2;
    if (check(s1, s2))
        cout << "they're anagrams\n";
    else
        cout << "they aren't anagrams\n";
    return 0;
}