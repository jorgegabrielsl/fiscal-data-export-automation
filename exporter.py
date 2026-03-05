import pandas as pd
from datetime import datetime
import os


def export_to_txt(df, file_prefix):

    today = datetime.now()

    file_name = f"{file_prefix}_{today.year}{today.month:02}{today.day:02}.txt"

    path = os.path.join("exports", file_name)

    os.makedirs("exports", exist_ok=True)

    with open(path, "w") as f:

        f.write("H;DATA_EXPORT\n")

        for _, row in df.iterrows():

            line = f"V;{row['customer_id']};{row['customer_name']};{row['product_id']};{row['product_name']};{row['sales_value']}\n"

            f.write(line)

        f.write("E")

    print(f"Arquivo gerado: {path}")
