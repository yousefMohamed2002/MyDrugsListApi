from fastapi import FastAPI
import pandas as pd

app = FastAPI()

# Load CSV file
df = pd.read_csv("drugbank vocabulary.csv")

@app.get("/drugs")
def get_drugs():
    """Return the list of common drug names."""
    return {"common_names": df["Common name"].dropna().tolist()}
S