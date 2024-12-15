#include <iostream>

using namespace std;

int designeRectangle(int l, int h, char symbole)
{

    if (l < 0 || h < 0){
        cout << "Les dimensions ne peuvent pas être négatives. " << endl;
        return 0;
    }

    for (int ligne(0); ligne < h; ligne++)
    {
        for (int colonne(0); colonne < l; colonne++){

            cout << "*";

        }
        cout << endl;
    }

    return l*h;
}

int main()
{
    int largeur, hauteur;
    char symbole;

    

    cout << "Largeur du rectangle : ";
    cin >> largeur;
    cout << "Hauteur du hauteur : ";
    cin >> hauteur;

    cout << "Symbole pour dessiner le rectangle :";
    cin >> symbole;

    int surface = designeRectangle(largeur, hauteur, symbole);

    if (surface > 0){
        cout << "La surface du rectangle est de : " << surface << endl;
    }
    return 0;

}