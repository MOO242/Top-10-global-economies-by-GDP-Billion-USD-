import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load GDP data from Wikipedia
url = "https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29"
tables = pd.read_html(url)
df = tables[3]
df.columns = range(df.shape[1])  # type: ignore # Reset column names

# Extract and clean top 10 GDP data
df = df.iloc[1:11, [0, 2]]
df.columns = ["Country", "GDP (Million USD)"]
df["GDP (Million USD)"] = df["GDP (Million USD)"].astype(int)
df["GDP (Billion USD)"] = np.round(df["GDP (Million USD)"] / 1000, 2)
df = df.drop(columns="GDP (Million USD)")
df = df.rename(columns={"GDP (Billion USD)": "GDP (Billion USD)"})

# Save to CSV
df.to_csv("Largest_economies.csv", index=False)

# Plotting GDP using Matplotlib
plt.figure(figsize=(10, 6))
plt.bar(df["Country"], df["GDP (Billion USD)"], color="skyblue")
plt.title("Top 10 Countries by GDP (Nominal)", fontsize=14)
plt.xlabel("Country", fontsize=12)
plt.ylabel("GDP (Billion USD)", fontsize=12)
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()

plt.savefig("gdp_chart.png", bbox_inches="tight")
