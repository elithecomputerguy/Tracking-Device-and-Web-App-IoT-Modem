from bottle import route, run, request, post
import json 
import sqlite3
from datetime import datetime

api_map = 'GOOGLE MAPS API KEY'

conn = sqlite3.connect('location.db')
cursor = conn.cursor()

cursor.execute('''create table if not exists location(
                        id integer primary key autoincrement,
                        timestamp text,
                        lat text,
                        lon text
                )''')
conn.commit()

lat_old = ''
lon_old = ''

@route('/current')
def current():
        sql = 'select * from location order by id desc limit 5'
        cursor.execute(sql)
        location = cursor.fetchall()
        page = ''

        for x in location:
                page = f'{page}<h3>{datetime.fromtimestamp(float(x[1]))} LAT: {x[2]} LON: {x[3]}</h3><br>'
                page = f'''
                        {page}
                        <iframe
                                width="600"
                                height="450"
                                style="border:0"
                                loading="lazy"
                                allowfullscreen
                                referrerpolicy="no-referrer-when-downgrade"
                                src="https://www.google.com/maps/embed/v1/place?key={api_map}&q={x[2]},{x[3]}">
                        </iframe>
                        <br>
                        '''

        return str(page)

@post('/receive')
def receive():
        global lat_old
        global lon_old
        data = json.loads(request.body.read().decode('utf-8'))

        if data['best_lat'] != lat_old and data['best_lon'] != lon_old:
                sql = 'insert into location(timestamp, lat, lon) values(?,?,?)'
                cursor.execute(sql,(data["received"],data["best_lat"],data["best_lon"]))
                conn.commit()
                print('data added')
        else:
                print('data not added')
        lat_old = data['best_lat']
        lon_old = data['best_lon']

        print(f'lat: {data["best_lat"]} lon: {data["best_lon"]} old lat: {lat_old} old lon: {lon_old}')
        return 'hello'

run(host='0.0.0.0', port=80, debug=True)