#include<iostream>
#include<string>

using namespace std;
 
 
struct product
{
	float Preis1;
	string Produktname;	
};

 
float bestellen (product Produktinfo[3],int eingabe, float bestellwert)
{
	float preis;
    preis = Produktinfo[eingabe].Preis1;
	cout << "Preis des Warenkorbs: " << bestellwert + preis << endl;
	return (bestellwert + preis);
	   
}


int main ()
{
	float rechnungsbetrag = 0;
	char weiter = 'j';
	int nummer;
	
	product Produkte [3];
	
	Produkte[0].Produktname = "Messer";
	Produkte[0].Preis1 = 6.49;
	Produkte[1].Produktname = "Teller";
	Produkte[1].Preis1 = 7.99;
	Produkte[2].Produktname = "Tasse";
	Produkte[2].Preis1 = 2.29;
	cout << "Produkt 1: " << Produkte[0].Produktname ;
	cout << "  Preis : " << Produkte[0].Preis1 << endl;
	cout << "Produkt 2: " << Produkte[1].Produktname;
	cout << "  Preis : " << Produkte[1].Preis1 << endl;
	cout << "Produkt 3: " << Produkte[2].Produktname;
	cout << "  Preis : " << Produkte[2].Preis1 << endl;
	


if ( weiter == 'j')
{
	
	cout << "Bitte Artikelnummer eingeben. " << endl;
	cin >> nummer;
	rechnungsbetrag = bestellen (Produkte, nummer, rechnungsbetrag);
	cout << "Wollen sie noch einen weiteren Artikel bestellen?(j/n) " << endl;
	cin >> weiter;
}
else
{
cout << "Danke f\201r ihre Bestellung. " << endl;
}
}

