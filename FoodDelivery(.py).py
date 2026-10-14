import pandas as pd
import numpy as np
from datetime import time

data = pd.read_csv("data/train.csv")

# stripping data
data = data.apply(lambda col: col.str.strip() if col.dtype == "object" else col)

invalids = [
    "nan", "NaN", "NAN", "None", "none", "NONE",
    "null", "Null", "NULL", "NA", "N/A", "n/a",
    "false", "False", "FALSE","unknown", "Unknown"
]

cols = data.columns


#
nd = data.apply(lambda col: col.isin(invalids)).any(axis=1)
data=data[~nd]
data["Time_taken(min)"]=data["Time_taken(min)"].apply(lambda x:int(x.replace("(min) ","")))
data=data.sort_values("Time_taken(min)")

# calculate IQR
def IQR(data, column):
    first = int(len(data) * 1/4 + 1)
    firstval = data[column].iloc[first]

    third = int(len(data) * 3/4 + 1)
    thirdval = data[column].iloc[third]

    iqr = thirdval - firstval

    upperfence = thirdval + (3/2) * iqr
    lowerfence = firstval - (3/2) * iqr

    return upperfence, lowerfence,thirdval

upperfence, lowerfence,thirdval = IQR(data, "Time_taken(min)")
data = data[(data["Time_taken(min)"] < upperfence) & (data["Time_taken(min)"] > lowerfence)]

time_or=data["Time_Orderd"]
time_orderd=time_or.apply(lambda time:(int(time.split(":")[0])*60 )+ (int(time.split(":")[1])))

time_pi=data["Time_Order_picked"]
time_orderd_picked=time_pi.apply(lambda time:(int(time.split(":")[0])*60 )+ (int(time.split(":")[1])))

data["Time_prep(min)"] = time_orderd_picked - time_orderd

data=data[data["Time_prep(min)"]>0]

time_taken=data["Time_taken(min)"]
prep_time=data["Time_prep(min)"]
data["Transit_time(min)"] = time_taken - prep_time
data=data[data["Transit_time(min)"]>0]


data["Total_delivery_time(min)"] = data["Time_prep(min)"]+data["Transit_time(min)"]
data = data.sort_index()

def time_category(time):
    hour = int(time.split(":")[0])

    if 6 <= hour < 11:
        return "Breakfast"
    elif 11 <= hour < 15:
        return "Lunch Peak"
    elif 15 <= hour < 18:
        return "Afternoon"
    elif 18 <= hour < 22:
        return "Dinner Rush"
    else:
        return "Late Night"
data["Time_Category"] = data["Time_Orderd"].apply(time_category)

data=data.sort_values("Total_delivery_time(min)")
upperfence, lowerfence,thirdval = IQR(data, "Total_delivery_time(min)")
data["Flag"] = data["Total_delivery_time(min)"] <= thirdval
