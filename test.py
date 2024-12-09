import sqlite3
import csv
import json

with sqlite3.connect("warehouse.db") as connector:
    cursor =connector.cursor()
    with open("data.json",'r') as f:
        users=json.loads(f.readline())
        for u in users:
            t=f"insert into users(name,age) values ('{u['name']}',{u['age']})"
            cursor.execute(t)

    
    cursor.execute("select * from users")
    with open("data.csv",'w') as f:
        writer=csv.writer(f)
        #writer.writerow(['id','name','age'])
        for (id,name,age) in cursor.fetchall():
            writer.writerow([id,name,age])
        
    
    