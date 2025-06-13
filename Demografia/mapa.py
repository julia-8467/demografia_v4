import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy.orm import Session
from Demografia.Database import SessionLocal
from Demografia.models import Demografia
import unicodedata

def usun_polskie_znaki(text):
    return unicodedata.normalize("NFKD", text).encode("ASCII", "ignore").decode("utf-8").lower()

def generuj_mape(output_path: str):
    db: Session = SessionLocal()

    # Pobieranie danych z bazy
    results = (
        db.query(Demografia.wojewodztwa, Demografia.liczba_ludnosci)
        .filter(Demografia.rok == 2017)
        .all()
    )
    db.close()

    # Tworzenie DataFrame i normalizacja nazw województw
    df = pd.DataFrame(results, columns=["wojewodztwa", "liczba_ludnosci"])
    df["wojewodztwa"] = df["wojewodztwa"].apply(usun_polskie_znaki)
    df = df.groupby("wojewodztwa", as_index=False).sum()
    df["procent"] = (df["liczba_ludnosci"] / df["liczba_ludnosci"].sum()) * 100

    # Wczytanie pliku SHP i normalizacja nazw
    shp_path = "D:/Users/julli/Studia/VIsemestr/Chmury/wojewodztwa"
    gdf = gpd.read_file(shp_path)
    gdf["nazwa"] = gdf["JPT_NAZWA_"].apply(usun_polskie_znaki)

    # Łączenie danych
    merged = gdf.merge(df, left_on="nazwa", right_on="wojewodztwa", how="left")

    # Tworzenie mapy
    fig, ax = plt.subplots(figsize=(10, 12))
    merged.plot(
        column="procent",
        cmap="OrRd",
        linewidth=0.8,
        edgecolor="black",
        legend=True,
        legend_kwds={"label": "Udział procentowy w populacji (%)"},
        ax=ax
    )
    ax.set_title("Procentowy rozkład ludności w Polsce – 2017", fontsize=15)
    ax.axis("off")
    plt.tight_layout()

    # Zapis mapy
    plt.savefig(output_path, format="jpg")
    plt.close()
