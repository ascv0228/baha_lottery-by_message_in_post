#include <iostream>
#include <ctime>
#include <vector>
using namespace std;

int main()
{
    srand(time(NULL));
    string a[11];
    vector<string> v1 = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"};
    for (int i = 0; i < 10; i++)
    {
        int j = rand() % v1.size();
        a[i] = v1[j];
        v1.erase(v1.begin() + j);
    }
    for (int i = 0; i < 10; i++)
    {
        cout << a[i] << "\t";
    }
}