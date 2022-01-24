#include <iostream>
#include <string>

int main()
{
std::string Gast[2][3] = {{"Falko", "Bausch", "16"},{"Fabian", "Deni", "16"}};

std::cout << "Vorname: " << Gast[0][0];
std::cout << "  Name: " << Gast[0][1];
std::cout << "  Alter: " << Gast[0][2] << std::endl;
std::cout << "Vorname: " << Gast[1][0];
std::cout << "  Name: " << Gast[1][1];
std::cout << "  Alter: " << Gast[1][2] << std::endl;
}
