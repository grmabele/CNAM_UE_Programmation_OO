#include <iostream>
#include <vector>
using namespace std;

int main()

{
    vector<double> notes;

    notes.push_back(12.5);
    notes.push_back(15.0);
    notes.push_back(18.0);
    notes.push_back(20.0);
    notes.push_back(22.0);

    double moyenne(0);
    for (int i(0); i < notes.size(); i++){
        moyenne += notes[i];
    }

    moyenne /= notes.size();

    cout << "Votre moyenne est : " << moyenne << endl;

    return 0;   

}