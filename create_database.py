
import pandas as pd
import sqlite3

def create_and_insert_data(csv_file, db_name='sales_database.db', table_name='vendas'):
    try:
        df = pd.read_csv(csv_file)
    except FileNotFoundError:
        print(f'Erro: O arquivo {csv_file} não foi encontrado.')
        return

    # Convert 'Data' column to datetime if it's not already
    if 'Data' in df.columns and not pd.api.types.is_datetime64_any_dtype(df['Data']):
        df['Data'] = pd.to_datetime(df['Data'])

    # Format 'Data' column to string for SQLite insertion
    if 'Data' in df.columns:
        df['Data'] = df['Data'].dt.strftime('%Y-%m-%d')

    # Replace NaN values with None for SQL insertion
    df = df.where(pd.notna(df), None)

    conn = None
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        # Drop table if it exists to ensure a clean start
        cursor.execute(f'DROP TABLE IF EXISTS {table_name};')

        # Create table statement
        create_table_sql = f"""CREATE TABLE {table_name} (
"""
        columns_sql = []
        for col, dtype in df.dtypes.items():
            if col == 'ID':
                columns_sql.append(f"    {col} INTEGER PRIMARY KEY")
            elif 'int' in str(dtype):
                columns_sql.append(f"    {col} INTEGER")
            elif 'float' in str(dtype):
                columns_sql.append(f"    {col} REAL")
            elif 'object' in str(dtype):
                columns_sql.append(f"    {col} TEXT")
        create_table_sql += ",\n".join(columns_sql)
        create_table_sql += "\n);"
        cursor.execute(create_table_sql)
        print(f'Tabela {table_name} criada com sucesso.')

        # Insert data
        df.to_sql(table_name, conn, if_exists='append', index=False)
        print(f'Dados inseridos na tabela {table_name} com sucesso.')

    except sqlite3.Error as e:
        print(f'Erro no SQLite: {e}')
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    create_and_insert_data('data_clean.csv')

