#include <iostream>
#include <string>

using namespace std;

class geschirr 
{
	public:
	string farbe;
	float groesse;
	string material;
	bool spuelfest;
	float preis;
	string artikelnummer;
	
	
	
	
	geschirr (string f, float g, string m, bool s, float p, string a):
	farbe(f),
	groesse(g),
	material(m),
	spuelfest(s),
	preis(p),
	artikelnummer(a)
	
	{}
	
	
	string getfarbe()
	{
		return farbe;
	}
	float getGroesse()
	{
		return groesse;
	}
	 string getMaterial()
	{
		return material;
	}
	bool getSpuelfest()
	{
		return spuelfest;
	}
	void setPreis(float p) 
	{
		preis = p;
	}
	float getPreis()
	{
		return preis;
	}
	string getArtikelnummer()
	{
		return artikelnummer;
	}
	
	
	void show ()
	{
		    cout << "Farbe: " << farbe << endl;
			cout << "Gr\224\341e(d in cm): " << groesse << endl;
			cout << "Material: " << material << endl;
			cout << "Sp\201lmaschinenfest(nein=0,ja=1): " << spuelfest << endl;
			cout << "Preis: " << preis << endl;
			cout << "Artikelnummer: " << artikelnummer << endl;
	}
};
	
	   class teller : public geschirr
	   {
		  public :
		  bool flach;
		  teller(string f, float g, string m, bool s, float p, bool fl, string a) : 
		  geschirr(f,g,m,s,p,a),
		  flach(fl)
		  {erfolgsmeldung();}		
		  void erfolgsmeldung()
		  {
			cout << "Flacher Teller(nein=0,ja=1): " << flach << endl;
		  }
		  
	   };
	  
	   class tasse : public geschirr 
	   {
		   public:
		   bool untertasse;
		   bool espressotasse;
		   tasse(string f, float g, string m, bool s, float p, bool u, bool e, string a) : 
		   geschirr(f,g,m,s,p,a),
		   untertasse(u),
		   espressotasse(e)
		   {erfolgsmeldung2();}
		   void erfolgsmeldung2()
		   {
			cout << "Untertasse enthalten(nein?=0,ja=1): " << untertasse << endl;
			cout << "Espressotasse(nein=0,ja=1): " << espressotasse << endl;
		   }
	    };
	    
	    class schuessel : public geschirr
	    {
		   public:
		   bool deckel;
		   schuessel(string f, float g, string m, bool s, float p, bool d, string a) :
		   geschirr (f,g,m,s,p,a),
		   deckel(d)
		   {erfolgsmeldung3 ();}
		   void erfolgsmeldung3()
		   {
			   cout << "Deckel enthalten (nein=0,ja=1): " << deckel << endl;
		   }
	    };
	    
	    class glaeser : public geschirr 
	    {
			public:
			float inhalt;
			glaeser(string f, float g, string m, bool s, float p, float i, string a) :
			geschirr(f,g,m,s,p,a),
			inhalt(i)
			{erfolgsmeldung4();}
			void erfolgsmeldung4 ()
			{
				cout << "Inhalt des Glases(in ml): " << inhalt << endl;
			}
			
		};
	   

