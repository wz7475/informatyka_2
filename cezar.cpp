#include <iostream>
#include <cstring>
using namespace std;

string text, alphabet = "abcdefghijklmnoprstuwzxyz", score = "";
int key;

int main()
{
    cout << "enter text: ";
    cin >> text;
    cout << "enter key: ";
    cin >> key;

    int lenght_A = text.size();
    int length_T = alphabet.size();

    for (int i = 0; i < length_T; i++)
    {
        for (int j = 0; j < lenght_A; j++)
        {
            if (text[i] == alphabet[j])
                score += alphabet[(j + key) % lenght_A];
        }
    }

    cout << score << endl;
    return 0;
}