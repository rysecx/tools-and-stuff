#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main ()
{
	char eing = 'j';
	while(eing == 'j')
	{
		char eingabe;
		cout << endl;
		cout << "Wollen sie einen neuen Kunden hinzuf\201gen?(1) , die vorhandenen Kunden mit Daten anzeigen lassen(2) oder alle Kundendaten l\224schen(3)?" << endl ;
		cin >> eingabe ;
		
		if ( eingabe == '1')
	{
		string inhalt;
		fstream f;
		f.open("kunden.txt" ,  ios::app);
		getline(cin, inhalt);
		cout << "Kundennummer: " << endl;
		getline(cin, inhalt);
		inhalt += "\n";
		f << inhalt;
		cout << "Vorname: " << endl; 
		getline(cin, inhalt);
		inhalt += "\n";
		f << inhalt;
		cout << "Name: " << endl;
		getline(cin, inhalt);
		inhalt += "\n";
		f << inhalt;
		cout << "Telefonummer: " << endl;
		getline(cin, inhalt);
		inhalt += "\n";
		f << inhalt;
		f.close ();
		cout << endl;
	}
	    else if ( eingabe == '2')
	{
		cout << endl;
		cout << "Kundendaten: " << endl;
		string inhalt;
		fstream f;
		f.open("kunden.txt" , ios::in);
		while(!f.eof())
		{	
			getline(f, inhalt);
			cout << inhalt << endl;
		}
		f.close();
		
    }
        else if ( eingabe == '3')
		{
	    cout << endl;
	    cout << "Kundendaten werden gel\224scht... " << endl;
	    cout << endl;
		string inhalt;
		fstream f;
		f.open("kunden.txt" , ios::out | ios::trunc);
		f.close();
	    }
    
    string inhalt;
    int i = 0;
    fstream f;
    f.open("kunden.txt", ios::in);
    while (!f.eof())
    {
		
		getline(f,inhalt);
		if (inhalt == "")
		{
			i++;
		}
	}
	cout << "Anzahl der vorhandenen Daten: " << i-1 <<endl;
	f.close();
    
    cout << "Wollen sie einen weitere Aktion ausf\201hren(j) oder das Programm beenden(n)? " << endl;
    cin >> eing;
    }
  
  
  
    cout << "Programm beendet... " << endl;
}
