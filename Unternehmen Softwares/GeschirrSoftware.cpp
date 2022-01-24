#include <iostream>
#include <string>
#include "GeschirrKlasse.h"

using namespace std;


 void b ()
        {
		    //Betsätigung
			cout << "Artikel wurde hinzugef\201gt. " << endl;
			cout << "Aktueller Preis des Warenkorbs: " ;
		}


int main()
{
	
	cout << "Unsere Angebote: " << endl;
	cout << "  " << endl;
	cout << "Teller und Eigenschaften: " << endl;
	cout << " " << endl;
	cout << "Teller: " << endl;
	teller teller1 = teller("Schwarz", 120, "Porzelan", true, 7.99, true, "1");
	teller1.show ();
	cout << " " << endl;
	cout << "Tassen und Eigenschaften: " << endl;
	cout << " " << endl;
	cout << "Tasse: " << endl;
	tasse tasse1 = tasse("Gelb", 50, "Porzelan", true, 4.79, true, false, "2");
	tasse1.show();
	cout << " " << endl;
	cout << "Sch\201sseln und Eigenschaften: " << endl;
	cout << " " << endl;
	cout << "Schuessel: " << endl;
	schuessel schuessel1 = schuessel("Blau", 70, "PP", false, 5.99, false,"3");
	schuessel1.show();
	cout << " " << endl;
	cout << "Gl\204ser und Eigenschaften: " << endl;
	cout << " " << endl;
	cout << "Glas: " << endl;
	glaeser glas1 = glaeser("Transparent", 30, "Glas", true, 12.99, 470,"4");
	glas1.show();
	cout << " " << endl; 
	cout << " " << endl;
	
	cout << "Wollen sie einen Artikel bestellen? " << endl;
	
    char eingabe = 'j';
    
   
    
    cin >> eingabe;
    float rechnungsbetrag = 0;
   
	if (eingabe == 'j')
	{
		string nummer;
		cout << "Bitte geben sie eine Artikelnummer ein: " << endl;
		cin >> nummer;
        
        
        if (nummer == "1")
        {
		    
			b();
		    cout << rechnungsbetrag + teller1.preis ;
			return (rechnungsbetrag + teller1.preis);
			
	    }
	    else if (nummer == "2")
	    {
			
			b();
			cout << rechnungsbetrag + tasse1.preis;
			return (rechnungsbetrag + tasse1.preis);
			
		}
	    else if (nummer == "3")
	    {
			
			b();
			cout << rechnungsbetrag + schuessel1.preis;
			return (rechnungsbetrag + schuessel1.preis);
			
		}
		else if (nummer == "4")
	    {
		 
			b();
			cout << rechnungsbetrag + glas1.preis;
			return (rechnungsbetrag + glas1.preis);
		
	    }
	    
	    
	    cout << "Wollen sie einen weiteren Artikel bestellen? " << endl;
	    cin >> eingabe;
		
	        
	    
	  }
	    else 
		{
			cout << "Artikelnummer nicht gefunden... " << endl;
		} 
		
	
	    cout << "Danke f\201r ihre Bestellung... " << endl;

}
