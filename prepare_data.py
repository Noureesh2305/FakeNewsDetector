import pandas as pd

fake = pd.read_csv("Fake.csv")
true = pd.read_csv("True.csv")

fake["label"] = "FAKE"
true["label"] = "REAL"

df = pd.concat([fake, true])
df = df[["text", "label"]]
df.to_csv("fake_news_dataset.csv", index=False)

print("✅ Combined and saved as fake_news_dataset.csv")
