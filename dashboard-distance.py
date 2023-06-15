import sys
from rich import print
import haversine as hs

my_location = (50.94738773522911, 4.708740861599119)

import time

from rich.live import Live
from rich.table import Table


def generate_table(planes) -> Table:
    table = Table()
    table.add_column("Hex")
    table.add_column("Distance", justify="right")
    table.add_column("Elevation", justify="right")

    for key,value in planes.items():
        if value[0] < 30:
            table.add_row(
                f"{key} {value[1]}", f"{value[0]:3.2f}", f"{value[2]:3.2f} km"
            )
    return table


planes = {}
with Live(generate_table(planes), refresh_per_second=4) as live: 
    for line in sys.stdin:
        fields = line.strip().split(",")
        if len(fields) != 22: continue
        plane_hex = fields[4]
        lat = fields[14]
        lon = fields[15]
        elevation = fields[11]
        if not lat or not lon: continue
        plane=(float(lat), float(lon))
        distance = hs.haversine(my_location,plane)
        dist_dir = ""
        if plane_hex in planes:
            if distance < planes[plane_hex][0]:
                dist_dir = "🠺🠸"
        elevation = float(elevation)/3281
        planes[plane_hex] = (distance, dist_dir, elevation)

        live.update(generate_table(planes))