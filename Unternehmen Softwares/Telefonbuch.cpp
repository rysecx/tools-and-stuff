#include <iostream>
#include <string>

using namespace std;

struct person
{
	string Vorname;
	string Nachname;
	long Telefonnummer;
	string Adresse1, Adresse3;
	int Adresse2, Adresse4;
};

int main ()
{
	person Person1;
	cout << "Adressbuch von John Ryder " << endl;
	cout << "Bitte geben sie den Vornamen und Nachname ihrer Person ein. " << endl;
	cout << "Vorname: ";
	cin >> Person1.Vorname;
	cout << "Nachname: ";
	cin >> Person1.Nachname;
	cout << "Bitte geben sie eine Telefonnummer ein. " << endl;
	cout << "Telefonnummer: ";
	cin >> Person1.Telefonnummer;
	cout << "Bitte geben sie eine Adresse ein. " << endl;
	cout << "Adresse: " << endl;
	cout << "Postleitzahl: ";
	cin >> Person1.Adresse2;
	cout << "Wohnort: ";
	cin >> Person1.Adresse1;
	cout << "Stra\341e: ";
	cin >> Person1.Adresse3;
	cout << "Hausnummer: "; 
	cin >> Person1.Adresse4;
	
	cout << "Hier ihre Personendaten: " << endl;
	
	cout << Person1.Vorname << endl;
	cout << Person1.Nachname << endl;
	cout << Person1.Telefonnummer << endl;
	cout << Person1.Adresse2 << " ";
	cout << Person1.Adresse1 << endl;
	cout << Person1.Adresse3 << " ";
	cout << Person1.Adresse4 << endl;
}
