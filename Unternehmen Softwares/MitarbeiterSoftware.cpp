#include <iostream>
#include <string>

using namespace std;

class mitarbeiter 
{
	string vorname;
	string nachname;
	int mitarbeiternummer;
	float gehalt;
	bool bonus;
	
	public:
	
	mitarbeiter( string vn, string nn, int mn, float g, bool b):
	vorname(vn),
	nachname(nn),
	mitarbeiternummer(mn),
	gehalt(g),
	bonus(b)
	{}
	
	string getVorname ()
	{
		return vorname;
	}
	string getNachname ()
	{
		return nachname;
	}
	int getMitarbeiternummer ()
	{
		return mitarbeiternummer;
	}
	void setGehalt (float g)
	{
		gehalt = g;
	}
	float getGehalt ()
	{
		return gehalt;
	}
	bool getBonus ()
	{
		return bonus;
	}
			
		void show ()
		{
		cout << "Mitarbeitereintrag erfolgreich erstellt. " << endl;
		cout << vorname << endl;
		cout << nachname << endl;
		cout << mitarbeiternummer << endl;
		cout << gehalt << endl;
		cout << bonus << endl;
	    }
};


int main ()
{
	 cout << "Aktuelle Mitarbeiterinfo: " << endl;
	 mitarbeiter mitarbeiter0 = mitarbeiter ("Selina", "Kyle", 10, 15.000, true );
	 mitarbeiter0.show ();
    
}
