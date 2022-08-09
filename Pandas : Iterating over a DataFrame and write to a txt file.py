impoort pandas as pd

df = pd.read_csv("data.csv")

# create lists for batters and bowlers
batter = df["batter"].unique().to_list()
bowler = df["bowler"].unique().to_list()

# create a text file and write to it
with open ("battervbowler.txt",  "w") as f:
  f.writelines("batter v bowler, runs scored, balls faced, strike rate\n")
  
for bat in batter:
  for bowl in bowler:
    runs = df.loc[(df["batter"] == bat) & (df["bowler"] == bowl)]
    balls = runs["runs scored"].count()
    actual_runs = runs["runs scored"].sum()
    strike_rate = round(runs/balls * 100, 2)
    if runs > 0:
      text = str(bat) + " vs " + str(bowl)  + "," + str(actual_runs) + "," + str(balls) + "," + str(strike_rate)
      with open ("battervbowler.txt",  "a") as f:
        f.writelines(str(text) + "\n"))
