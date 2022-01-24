#include <iostream>
#include <string>

using namespace std;

class mitarbeiter 
{
	string vorname;
	string nachname;
	int mitarbeiternummer;
	float gehalt;
	
	public:
	
	mitarbeiter( string vn, string nn, int mn, float g):
	vorname(vn),
	nachname(nn),
	mitarbeiternummer(mn),
	gehalt(g)
	{erfolgsmeldung();}
	
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
	
	void erfolgsmeldung ()
	{
		cout << "Mitarbeitereintrag erfolgreich erstellt. " << endl;
		
		cout << vorname << endl;
		cout << nachname << endl;
		cout << mitarbeiternummer << endl;
		cout << gehalt << endl;
	}
};

int main ()
{
	mitarbeiter mitarbeiter1 = mitarbeiter ("Bruce", "Wayne", 10001, 5000 );
}
