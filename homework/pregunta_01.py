# pylint: disable=line-too-long
"""
Escriba el codigo que ejecute la accion solicitada.
"""
import os
import pandas as pd
import matplotlib.pyplot as plt

def pregunta_01():
    """
    El archivo `files//shipping-data.csv` contiene información sobre los envios
    de productos de una empresa. Cree un dashboard estático en HTML que
    permita visualizar los siguientes campos:

    * `Warehouse_block`

    * `Mode_of_Shipment`

    * `Customer_rating`

    * `Weight_in_gms`

    El dashboard generado debe ser similar a este:

    https://github.com/jdvelasq/LAB_matplotlib_dashboard/blob/main/shipping-dashboard-example.png

    Para ello, siga las instrucciones dadas en el siguiente video:

    https://youtu.be/AgbWALiAGVo

    Tenga en cuenta los siguientes cambios respecto al video:

    * El archivo de datos se encuentra en la carpeta `data`.

    * Todos los archivos debe ser creados en la carpeta `docs`.

    * Su código debe crear la carpeta `docs` si no existe.

    """
    # Crear directorio docs
    os.makedirs("docs", exist_ok=True)
    
    # Leer datos
    df = pd.read_csv("files/input/shipping-data.csv")
    
    # Crear visualizaciones
    create_visual_for_shipping_per_warehouse(df)
    create_visual_for_mode_of_shipment(df)
    create_visual_for_average_customer_rating(df)
    create_visual_for_weight_distribution(df)
    
    # Crear index.html
    create_index_html()



def create_visual_for_shipping_per_warehouse(df):
    """Crea visualización de shipping por warehouse."""
    df = df.copy()
    plt.figure()
    counts = df.Warehouse_block.value_counts()

    counts.plot.bar(
        title="Shipping per Warehouse",
        xlabel="Warehouse block",
        ylabel="Record Count",
        color="tab:blue",
        fontsize=8,
    )

    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)
    plt.xticks(rotation=0)

    plt.savefig("docs/shipping_per_warehouse.png")
    plt.close()

def create_visual_for_mode_of_shipment(df):
    """Crea visualización de modo de envío."""
    df = df.copy()
    plt.figure()
    counts = df.Mode_of_Shipment.value_counts()
    
    counts.plot.pie(
        title="Mode of shipment",
        wedgeprops=dict(width=0.35),
        ylabel="",
        colors=["tab:blue", "tab:orange", "tab:green"]
    )

    plt.savefig("docs/mode_of_shipment.png")
    plt.close()

def create_visual_for_average_customer_rating(df):
    """Crea visualización de rating promedio de clientes."""
    df = df.copy()
    plt.figure()

    df_grouped = (
        df[["Mode_of_Shipment", "Customer_rating"]]
        .groupby("Mode_of_Shipment")
        .describe()
    )

    df_grouped.columns = df_grouped.columns.droplevel()
    df_grouped = df_grouped[["mean", "min", "max"]]

    plt.barh(
        y=df_grouped.index.values,
        width=df_grouped["max"].values - 1,
        left=df_grouped["min"].values,
        height=0.9,
        color="lightgray",
        alpha=0.8
    )

    colors = [
        "tab:green" if value >= 3.0 else "tab:orange" 
        for value in df_grouped["mean"].values
    ]

    plt.barh(
        y=df_grouped.index.values,
        width=df_grouped["mean"].values - 1,
        left=df_grouped["min"].values,
        color=colors,
        height=0.5,
        alpha=1.0
    )

    plt.title("Average Customer Rating")
    plt.gca().spines["left"].set_color("gray")
    plt.gca().spines["bottom"].set_color("gray")
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)

    plt.savefig("docs/average_customer_rating.png")
    plt.close()


def create_visual_for_weight_distribution(df):
    """Crea visualización de distribución de peso."""
    df = df.copy()
    plt.figure()

    df.Weight_in_gms.plot.hist(
        title="Shipped Weight Distribution",
        color="tab:orange",
        edgecolor="white"
    )

    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)

    plt.savefig("docs/weight_distribution.png")
    plt.close()


def create_index_html():
    """Crea el archivo index.html con las visualizaciones."""
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Shipping Data Dashboard</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        h1 { text-align: center; }
        .container { display: flex; flex-wrap: wrap; justify-content: center; }
        .chart { margin: 20px; text-align: center; }
        img { max-width: 100%; height: auto; border: 1px solid #ddd; }
    </style>
</head>
<body>
    <h1>Shipping Data Dashboard</h1>
    <div class="container">
        <div class="chart">
            <img src="shipping_per_warehouse.png" alt="Shipping per Warehouse">
        </div>
        <div class="chart">
            <img src="mode_of_shipment.png" alt="Mode of Shipment">
        </div>
        <div class="chart">
            <img src="average_customer_rating.png" alt="Average Customer Rating">
        </div>
        <div class="chart">
            <img src="weight_distribution.png" alt="Weight Distribution">
        </div>
    </div>
</body>
</html>"""
    
    with open("docs/index.html", "w", encoding="utf-8") as f:
        f.write(html_content)

pregunta_01()