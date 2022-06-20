import argparse
import textwrap
import time

import psycopg2


def postgres_check(db_name, user, host, password, port):
    """script to check connection on postgres db"""
    conn = None
    is_up = 0
    try:
        conn = psycopg2.connect(dbname=db_name, user=user, host=host, password=password, port=port)
        with conn:
            cursor = conn.cursor()
            cursor.execute('SELECT 1')
            is_up = cursor.fetchone()[0]
    except Exception as e:
        print(e)
    print(is_up)
    return is_up


if __name__ == '__main__':
    ap = argparse.ArgumentParser(prog='posgrescheck',
                                 formatter_class=argparse.RawDescriptionHelpFormatter,
                                 description=textwrap.dedent('''\
                                     programa para extraer verificar que postgres esta listo
                                     ejemplo ejecucion:
                                      - windows: python pgconnectcheck.py -db mydb -u user -hs localhost -pw pass -p 5432
                                      - unix: python3 pgconnectcheck.py -db mydb -u user -hs localhost -pw pass -p 5432'''))
    ap.add_argument("-db", "--dbname", required=True,
                    help="db name to check, required")
    ap.add_argument("-u", "--user", required=True,
                    help="user db, required")
    ap.add_argument("-hs", "--host", required=True,
                    help="host db, required")
    ap.add_argument("-pw", "--password", required=True,
                    help="password db, required")
    ap.add_argument("-p", "--port", required=True,
                    help="port db, required")
    args = ap.parse_args()
    while True:
        is_up = postgres_check(args.dbname, args.user, args.host, args.password, args.port)
        if is_up == 1:
            break
        time.sleep(3)

