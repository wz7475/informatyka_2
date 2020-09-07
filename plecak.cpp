#include <iostream>
using namespace std;

void enter(int w[], int c[], int n)
{
    cout << "enter values and weights of items:\n";
    for(int i = 1; i <= n; i++)
    {
        cout << "value: ";
        cin >> w[i];
        cout << "weight: ";
        cin >> c[i];
    }
}

int pack_backpack(int w[], int c[], int n, int weight, int k[])
{
    int score = 0;
    for (int i = 1; i <= n; i++)
    {
        k[i] = weight / c[i];
        weight -= k[i] * c[i];
        score += k[i] * w[i];
    }
    return score; 
}

int main()
{   
    int w[50], c[50], k[50], weight, n;
    //w - value, c - weight, k - amount, n - amount of all items
    cout << "enter max weight of packpack: ";
    cin >> weight;
    cout << "enter amount of items: ";
    cin >> n;

    enter(w, c, n);

    cout << "value of packback: " << pack_backpack(w, c, n, weight, k) << endl;

    cout << "\n\npacked items:\n";
    for (int i = 1; i <= n; i++)
    {
        if (k[i] != 0)
        {
            cout << "amount: " << k[i] << endl;
            cout << "value: " << w[i] << endl;
            cout << "weight: " << c[i] << endl;
        }
    }
    return 0;
}