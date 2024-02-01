#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import pyarrow.parquet as pq
from sqlalchemy import create_engine
from time import time
import argparse
import os

def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url

    parquet_name = "input.parquet"
    csv_name = "output.csv"

    os.system(f"wget {url} -O {parquet_name}")

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')
    engine.connect()

    pq_table = pq.read_table(parquet_name)
    pd_df = pq_table.to_pandas()

    pd_df = pd_df.to_csv(csv_name, index=False)

    df_iter = pd.read_csv(csv_name, iterator=True, chunksize=100000)

    df = next(df_iter)

    df.head(n=0).to_sql(name=table_name, con=engine, if_exists="replace")
    df.to_sql(name=table_name, con=engine, if_exists="append")

    while True:
        try:
            t_start = time()

            df = next(df_iter)

            df.to_sql(name=table_name, con=engine, if_exists="append")

            t_end = time()

            print("Inserted another chunk..., took %.3f seconds" % (t_end - t_start))

        except StopIteration:
            print("Finished ingesting data into the postgres database")
            break

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Ingest CSV data to Postgres')

    parser.add_argument('--user', required=True, help='user name for postgres')
    parser.add_argument('--password', required=True, help='password for postgres')
    parser.add_argument('--host', required=True, help='host for postgres')
    parser.add_argument('--port', required=True, help='port for postgres')
    parser.add_argument('--db', required=True, help='database name for postgres')
    parser.add_argument('--table_name', required=True, help='name of the table where we will write the results to')
    parser.add_argument('--url', required=True, help='url of the csv file')

    args = parser.parse_args()

    main(args)