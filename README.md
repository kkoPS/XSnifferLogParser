# XSnifferLogParser
XSniffer Motes Light and Temperature Parser, using **Python 2.7**.

## Install ?

I did not find any convincing way to ship the app. I let my IDE do all the modules installation work, so i don't know precisely which steps lead to a quick way to run the app.

I used **PySide** for the GUI and **matplotlib** for the histograms. Parsing the csv uses the **csv** module.

## Usage !

- Clic the [Browse] button to select a .csv file, formatted with the XSniffer-Motes style (Light on rows '9' and '10', temperature on rows '7' and '8', and 'ElapsedTime', 'msec', '2' rows)
- Clic the [Parse] buttun to parse the selected file. The min, max and average will be displayed on the window, the histogram will display.
- The [Exit] button closes the app.
- The Light and Temperature check-boxes toggle the display of the histograms.


![text parsing](screens/GUI_details.png)

---

## History and motivation

For a ADR's course in the last semester of Embedded Systems at HEIG-VD, we had to fetch the min, max and average of light measures froms sensors.
At first we sugested to simply use Excel (or equivalent) to import, convert and calculate "by hand" the data, but it was suggested we write a small python script to parse the data.

Finally I decide to discover Python scripting and GUI usages, and this small project was the perfect pretext.