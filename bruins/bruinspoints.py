import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = "Karla"
plt.rcParams['font.family'] = "sans-serif"

def bruins_points():
    rawdata = pd.read_csv("bruins.csv")
    rawdata = rawdata[["No.", "Player", "Pos", "Summary"]]

    rawdata[["Goals", "G", "Assists", "A", "Points", "P"]] = rawdata.Summary.str.split(" ", expand = True)
    splitdata = rawdata[["No.", "Player", "Pos", "Goals", "Assists", "Points"]]
    splitdata = splitdata.loc[splitdata["Pos"] != "G"]
    splitdata = splitdata.replace(np.nan, 0)

    splitdata["No."] = pd.to_numeric(splitdata["No."])
    splitdata["Goals"] = pd.to_numeric(splitdata["Goals"])
    splitdata["Assists"] = pd.to_numeric(splitdata["Assists"])
    splitdata["Points"] = pd.to_numeric(splitdata["Points"])

    splitdata = splitdata.sort_values(by = "Points")

    pointsdata = splitdata[["Player", "Points"]]
    print(pointsdata)
    goalsdata = splitdata[["Player", "Goals"]]

    plt.bar(x = splitdata["Player"], height = splitdata["Points"], color = "#FFB81C", label = "Points")
    plt.plot(splitdata["Player"], splitdata["Goals"], color = "#000000", marker = "o", linestyle = "-", linewidth = "3", label = "Goals")
    legend = plt.legend(loc = "upper left")
    ax = plt.subplot()
    ax.set_xticklabels(splitdata["Player"], rotation = 90)

    plt.title("Bruins Player Production Fall 2022")
    plt.xlabel("Player")
    plt.ylabel("Count")
    #plt.grid(axis = "y")

    #plt.show()
    plt.savefig('bruinspoints.png', dpi = 300, bbox_inches='tight')

