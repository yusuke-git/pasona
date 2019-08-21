from flask import Flask
import mysql.connector as mydb
import pandas as pd




app = Flask(__name__)

@app.route("/")
def hello():
    # コネクションの作成
    conn = mydb.connect(
        host='pt_db',
        port='3306',
        user='root',
        password='password',
        database='PTDB'
    )
    sql = 'select * from goods;'
    data = pd.read_sql(
                sql,conn).rename(columns=str.upper)
    return data.to_json()

if __name__ == "__main__":
    app.run(host='0.0.0.0')