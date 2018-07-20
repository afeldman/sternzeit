# sternzeit
In Star Track gibt es die sogenannte Sternzeit. Eigentlich ist das ganz einfach zu berechnen aber damit ich mal wieder einwenig mit Python spiele, habe ich daraus ein Module gemacht, mit dem sich die Tage und Stunden in einem Monat berechnen lassen.
Am Ende gab es ein kleines Testfile, dass das Datum und die aktuelle Stunde nach den Vorgaben von Star Track berechnet.
Vorausgesetzt wir erfinden im Jahr **2063** den Worb-Antrieb oder wir erreichen sonst etwas ganz besonderes im Jahr **2063** stimmt die berechnung eigentlich auch

```python
sternzeit = 1000 * (Jahr + 1 / LaengeDesJahres * TagImJahr - 1 + Stunde / 24 + Minute / 1440 - 2063)
```

Diese Formel muss nicht richtig sein, aber es was lustig fuer mich das mal in Python zu schreiben.