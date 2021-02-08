import csv
from xml.etree import ElementTree as et
import time
import svgutils as sg
import math

with open('data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    row = reader.__next__()
    for row in reader:
        number = row[0]
        sym = row[1]
        name = row[2]

        root = et.parse('element.svg')
        for target in root.findall(".//tspan"):
            if target.get('id') == "sym":
                target.text = sym
            if target.get('id') == "name":
                target.text = name
            if target.get('id') == "number":
                target.text = number

        root.write("elements/" + number + ".svg")
        # time.sleep(0.2)

# create new SVG figure
print(sg)
fig = sg.compose.Figure("33.3cm", "33.3cm")  # 2.5mm * 10 + margin of 3mm * 11
plots = []
for i in range(0, 110):
    fig = sg.transform.fromfile("elements/" + str(i+1) + ".svg")
    plot = fig.getroot()
    plot.moveto(3 + (30+3)*(i % 10), 3 + (30+3)*math.floor(i/10))
    plots.append(plot)

# append plots and labels to figure
fig.append(plots)

# save generated SVG files
fig.save("final.svg")

# data = ""

with open("final.svg", "r") as f:
    data = f.read()
    data = data.replace("""ns0:""", "")
    data = data.replace("""<svg height="30mm" viewBox="0 0 30 30" width="30mm">
""", """<svg height="333mm" viewBox="0 0 333 333" width="333mm">""")

with open('final3.svg', 'w') as file:
    file.write(data)
