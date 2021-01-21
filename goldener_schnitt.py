#!/usr/bin/env python3
# -*- coding: utf-8 -*

import math
import sys

ausgangszahl = ""
if len(sys.argv) > 1:
    ausgangszahl = sys.argv[1].replace(",", ".")

while not (ausgangszahl.isnumeric() or ausgangszahl.replace(".", "").isnumeric()):
    ausgangszahl = input("Goldenen Schnitt berechnen für Zahl: ").replace(",", ".")

ausgangszahl = float(ausgangszahl)
majorfaktor = (-1 + math.sqrt(5)) / 2.0
minorfaktor = 1.0 - majorfaktor
outputformat = "{:10.3f}"
einrueckung = 16
linie = 28 * "-"
punktzukomma = {46:44}

print("")
print("Ausgangszahl:".ljust(einrueckung), outputformat.format(ausgangszahl).translate(punktzukomma))
print("Majorfaktor:".ljust(einrueckung), outputformat.format(majorfaktor).translate(punktzukomma))
print("Minorfaktor:".ljust(einrueckung), outputformat.format(minorfaktor).translate(punktzukomma))
print(linie, "\n")

gesamt = ausgangszahl
major = majorfaktor * ausgangszahl
minor = minorfaktor * ausgangszahl
print("Gesamt(x):".ljust(einrueckung), outputformat.format(gesamt).translate(punktzukomma))
print("Major:".ljust(einrueckung), outputformat.format(major).translate(punktzukomma))
print("Minor:".ljust(einrueckung), outputformat.format(minor).translate(punktzukomma))
print(linie, "\n")

gesamt = ausgangszahl / majorfaktor
major = ausgangszahl
minor = minorfaktor * gesamt
print("Gesamt:".ljust(einrueckung), outputformat.format(gesamt).translate(punktzukomma))
print("Major(x):".ljust(einrueckung), outputformat.format(major).translate(punktzukomma))
print("Minor:".ljust(einrueckung), outputformat.format(minor).translate(punktzukomma))
print(linie, "\n")

gesamt = ausgangszahl / minorfaktor
major = majorfaktor * gesamt
minor = ausgangszahl
print("Gesamt:".ljust(einrueckung), outputformat.format(gesamt).translate(punktzukomma))
print("Major:".ljust(einrueckung), outputformat.format(major).translate(punktzukomma))
print("Minor(x):".ljust(einrueckung), outputformat.format(minor).translate(punktzukomma))
print(linie, "\n")

if len(sys.argv) != 2:
    input("Enter drücken zum beenden")
