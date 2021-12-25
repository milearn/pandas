import pandas as pd
import matplotlib.pyplot as plt
air_quality = pd.read_csv("data/data1.csv", parse_dates=True)

print(air_quality.head())
# air_quality.plot()

# air_quality["station_paris"].plot()
# plt.show()

# Adding new column:
# No loop is needed
air_quality["london_mg_per_cubic"] = air_quality["station_london"] * 1.882
print(air_quality.head())

# Rename column names:
# NOTE: rename doesn't mutate same dataframe
air_quality_renamed = air_quality.rename(
    columns={
        "station_antwerp": "BETR801",
        "station_paris": "FR04014",
        "station_london": "London Westminster",
    }
)
print(air_quality_renamed.head())
