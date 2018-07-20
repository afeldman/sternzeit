#!/usr/bin/env python3

import datetime
from year import year

jetzt = datetime.datetime.now()
jahr = jetzt.year
monat = jetzt.month
tag = jetzt.day
stunde = jetzt.hour
minute = jetzt.minute
sekunde = jetzt.second

#$sternzeit = 1000 *
#($jahr + 1 / $jahreslaenge * ($jahrestag - 1 + $stunde/24 + $min/1440) - 2063);

print (year.__author__)

# year 2063 is the year the humans invented the warp engine in star track 
print(1000.0 * (jahr + 1 / year.length_of_year(jahr) *  year.minuts_in_the_year(jahr,monat,tag, stunde, minute)) - 2063)
