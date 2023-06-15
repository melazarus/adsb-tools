import sys
from rich import print
import haversine as hs

my_location = (50.94738773522911, 4.708740861599119)

shortest = 1000
farthest = 0

for line in sys.stdin:
    fields = line.strip().split(",")
    if len(fields) != 22: continue
    lat = fields[14]
    lon = fields[15]
    if not lat or not lon: continue
    plane=(float(lat), float(lon))
    distance = hs.haversine(my_location,plane)
    shortest = min(distance,shortest)
    farthest = max(distance, farthest)
    color = "[red]" if distance < 5 else ""
    color = "[yellow]" if distance < 2 else color
    close_tag = "[/]" if color else ""
    print(float(lat), float(lon),":",f"{color}{distance:0.2f} km{close_tag} (min:{shortest:0.2f} km) (max:{farthest:0.2f} km)")



