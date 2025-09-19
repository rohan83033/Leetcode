#include <iostream>
using namespace std;

int main()
{
    int a = 10, b = 20;

    for (int i = a; i <= b; i++)
    {
        int c = 0;
        for (int j = 1; j <= i; j++)
        {
            if (i % j == 0)
            {
                c = c + 1;
            }
            if (c > 2)
            {
                cout << i + ",";
            }
        }
    }
    return 0;
}
