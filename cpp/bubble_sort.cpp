#include <iostream>
using namespace std;

void sort(int tab[], int n)
{
    for (int i = 0; i < n; i++)
    {
        for (int j = i + 1; j < n; j++)
        {
            if (tab[i] > tab[j])
                swap(tab[j], tab[i]);
        }
    }
}

int main()
{   
    int tab[5] = {1, 3, 5, 4, 2};
    sort(tab, 5);
    for (int i = 0; i < 5; i++)
        cout << tab[i] << endl;

    return 0;
}