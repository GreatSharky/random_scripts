import pandas as pd
import numpy as np

viittefile = pd.read_csv("Viitenumerot - 23-24 viitenumerot.csv", on_bad_lines="skip")
tammifile = pd.read_csv("Tapahtumat_31-1-2024.csv", on_bad_lines="skip")
helmifile = pd.read_csv("Tapahtumat_01-02-2024.csv", on_bad_lines="skip")

#print(viittefile.iloc[:,1])
tammifile["Viite tai viesti"] = tammifile["Viite tai viesti"].apply(lambda x: x.replace(" ", ""))
helmifile["Viite tai viesti"] = helmifile["Viite tai viesti"].apply(lambda x: x.replace(" ", ""))

viitteet = viittefile.iloc[2:,1]
outputfile = "output.csv"
with open(outputfile, "w") as file:
    for viite in viitteet.values:
        if viite[0] == "3" and (viite in helmifile["Viite tai viesti"].values):
            i = np.where(helmifile["Viite tai viesti"].values == viite)[0]
            print(i)
            print(viite, helmifile.iloc[i]["Määrä EUR"], helmifile.iloc[i]["Maksaja tai saaja"])

        elif viite[0] == "3" and (viite in tammifile["Viite tai viesti"].values):
            i = np.where(tammifile["Viite tai viesti"].values == viite)[0]
            print(i)
            print(viite, tammifile.iloc[i]["Määrä EUR"], tammifile.iloc[i]["Maksaja tai saaja"])
