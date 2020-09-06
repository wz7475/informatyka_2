#include <iostream>
using namespace std;

int main()
{
    int T[9] = {500, 200, 100, 50, 20, 10, 5, 2, 1};
    int change, amount, i;

    cout << "enter the change: ";
    cin >> change;
    i = 0;

    while (change > 0)
    {
        if(change >= T[i])
        {
            amount = change / T[i];
            change -= T[i] * amount;
            cout << T[i] << "zl * " << amount << "\n";
        }
        i++;
    }
    return 0;
}