#!/bin/python3
#BMI-Rechner

def main():
    gr = input("Please enter your height(in cm): ")
    gw = input("Please enter your weight(in kg): ")
    gr = float(gr)
    gw = float(gw)
    gr /= 100
    gr *= gr
    erg = gw / gr
    print("Your BMI is ", "%.2f" % erg)

try:
    main()

except KeyboardInterrupt:
    print("\r\n^C")
    exit()

except ZeroDivisionError:
    print("ZeroDivisionError")
    exit()
