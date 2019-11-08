import pandas as pd
from math import sin, cos, sqrt, atan2, radians
from sqlalchemy import create_engine
import math

def horizonConflict(lat1,lon1,lat2,lon2):
    # approximate radius of earth in km
    R = 6373.0
    #lat1 = radians(52.2296756)
    #lon1 = radians(21.0122287)
    #lat2 = radians(52.406374)
    #lon2 = radians(16.9251681)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c

    #print("Result:", distance)
    #print("Should be:", 278.546, "km")
    return distance

def main():
    df = pd.read_csv('day1510.csv')
    df.dropna()
    time = df.time.unique()
    conflict = []
    for i in range(len(time)):
            focus_row = df.loc[df['time'] == time[i]]
            templat = focus_row["lat"].tolist()
            templon = focus_row["lon"].tolist()
            tempH = focus_row["baroaltitude"].tolist()
            callsign = focus_row["callsign"].tolist()

        #### Horizontal conflict
            for j in range(len(templat)):
                for k in range(len(templat)):
                    if (j!=k):
                        flat1 = templat[j]
                        flon1 = templon[j]
                        flat2 = templat[k]
                        flon2 = templon[k]
                        Hdist_km = horizonConflict(flat1, flon1, flat2, flon2)
                        required = 3*1.852 #nmi  #1 nmi = 1.852 km
                        if Hdist_km<required:
                            try:
                                dif = abs(Hdist_km-required)
                                conflict.append(["Horizontal",str(time[i]),callsign[j],str(flat1),str(flon1),callsign[k],str(flat2),str(flon2),str(dif)])
                                print("Horizontal Conflict: at time " +  str(time[i])+" callsign "+callsign[j] +" lat/lon "+str(flat1)+"/"+str(flon1)+" and callsign "+callsign[k] +" lat/lon "+str(flat2)+"/"+str(flon2)+" Diff: "+str(dif))
                            except:
                                print("...... cannot save .......")
                                print(str(time[i])+"\n")
                                print(str(callsign[j]) + "\n")
                                print(str(flat1) + "\n")
                                print(str(flon1) + "\n")
                                print(str(callsign[k]) + "\n")
                                print(str(flat2) + "\n")
                                print(str(flon2) + "\n")
                                print(str(dif) + "\n")
    with open('your_file.txt', 'w') as f:
        for item in conflict:
            f.write("%s\n" % item)
    f.close()


if __name__ == '__main__':
    main()
