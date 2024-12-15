#include <iostream>

using namespace std;

int main(){

    cout << "Entrez une temperature en Celsius : ";
    double celsius;
    cin >> celsius; // Lecture de l'entrée utilisateur pour le celsius

    double fahrenheit = (celsius * 9/5) + 32; // Conversion


    cout << "La température équivalente en Fahrenheit est : " << fahrenheit << endl;
}