#include <iostream>

int main ()
{
int bestand[3] {0,20,4};
int abbuchung;
char antwort;
char antwort2;

do
{
for (int eingabe : bestand)
	{
std::cout << "Bitte Artikelnummer eingeben: ";
std::cin >> eingabe;
if ((eingabe>=0)&& (eingabe <= 2))
{
if (bestand[eingabe] == 0)
{
std::cout << "Achtung!: Keine Waren mehr auf Lager" << std::endl;
}
else if (bestand[eingabe]>0 && bestand[eingabe] <= 10)
{
std::cout << "Nur noch " << bestand[eingabe]<< " verf\201gbar" << std::endl;
std::cout << "Bitte nachbestellen! " << std::endl;
}
else 
{
std::cout << "Noch " << bestand[eingabe] << " verf\201gbar" << std::endl;
}
}
else
{
std::cout << "Artikelnummer nicht gefunden." << std::endl;
}


if ( (bestand[eingabe] > 0) && (eingabe>=0) && (eingabe<=2))
{
	{
std::cout << "Wie viele Artikel sollen abgebucht werden? " << std::endl;
}
std::cin >> abbuchung;
if (abbuchung >=0)
{
if (abbuchung < bestand[eingabe])
{
int c;
c = bestand[eingabe] - abbuchung;
std::cout << "Erfolgreich abgebucht! Noch " << c << " Waren verf\201gbar." << std::endl;
}
else if (abbuchung == bestand[eingabe])
{
std::cout << "Erfolgreich abgebucht! Neuer Artikelstand: 0 " << std::endl;
}
else if (abbuchung > bestand[eingabe])
{
        std::cout << "Es sind nicht gen\201gend Artikel vorr\204tig, wollen sie die restlichen trotzdem abbuchen? (J/N)" << std::endl;
        std::cin >> antwort;
        if (antwort == 'J')
        {
        std::cout << "Erfolgreich abgebucht, der Bestand wurde auf 0 gesetzt. " << std::endl;
        }
else if (antwort == 'N')
{
std::cout << "Vorgang abgebrochen! " << std::endl;
}
}
}
}

std::cout << "Wollen sie weitere Artikel bestellen? (Ja/Nein)" << std::endl;
std::cin >> antwort2;


if ( antwort2 == 'N')
{
	std::cout << "Vorgang beendet... " << std::endl;
}
}
}
 while ( antwort2 == 'J');
}

