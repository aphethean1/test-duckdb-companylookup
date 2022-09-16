
import duckdb
cursor = duckdb.connect()
print(cursor.execute(
    """
    SELECT CompanyName, CompanyNumber, CompanyCategory
    FROM read_csv_auto('BasicCompanyDataAsOneFile-2022-09-01.csv') 
    WHERE CompanyName = 'MATATIKA LIMITED'
    """
    ).fetchall())
