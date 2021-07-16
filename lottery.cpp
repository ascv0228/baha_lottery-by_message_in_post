#include <iostream>
#include <ctime>
#include <fstream>
#include <vector>
using namespace std;

void lottery(vector<string> info, int winner_number = 10)
{
    string winner[winner_number]={0};
    for (int i = 0; i < winner_number; i++)
    {
        int j = rand() % info.size();
        winner[i] = info[j];
        info.erase(info.begin() + j);
    }
    for (int i = 0; i < winner_number; i++)
    {
        cout << winner[i] << "\t";
    }
}

int main()
{
    srand(time(NULL));
    ifstream ifs("lottery.txt", ios::in);
    vector<string> info;
    if (!ifs.is_open()) {
        cout << "Failed to open file.\n";
        ifs.close();
    }
    else{
        string s;
        while (getline(ifs, s)) {
            //cout << s << endl;
            info.push_back(s);
        }
        lottery(info, 10);
        ifs.close();
    }
}
