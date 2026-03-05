import pandas as pd
from database import get_connection
from exporter import export_to_txt


def extract_sales_data():

    connection = get_connection()

    query = """

    SELECT
        c.customer_id,
        c.customer_name,
        p.product_id,
        p.product_name,
        s.sales_value

    FROM sales s
    JOIN customers c
        ON c.customer_id = s.customer_id
    JOIN products p
        ON p.product_id = s.product_id

    """

    df = pd.read_sql(query, connection)

    connection.close()

    return df


def main():

    print("Extraindo dados...")

    sales_df = extract_sales_data()

    print("Gerando arquivo...")

    export_to_txt(sales_df, "sales_export")


if __name__ == "__main__":
    main()
