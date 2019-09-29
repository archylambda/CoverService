import pymysql.cursors


class UseDatabase:

    def __init__(self, config: dict) -> None:
        self.configuration = config

    def __enter__(self) -> 'cursor':
        self.conn = pymysql.connect(host='127.0.0.1',
                                    user='admin',
                                    password='admin',
                                    db='PokritieDB',
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor
                                    )
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_value, exc_trace) -> None:
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

def customReq(request):
    conf = { 'host' : '127.0.0.1',
             'user' : 'admin',
             'password' : 'admin',
             'database' : 'PokritieDB'}
    with UseDatabase(conf) as cursor:
        cursor.execute(request)
        return cursor.fetchall()
        
def addPoint(x,y,uroven_signala,operator):
    if (not x==0 and not y==0):
        req = f"""INSERT INTO koord_and_kachestvo (x,y,uroven_signala,operator) VALUES ({x},{y},"{uroven_signala}","{operator}");"""
        print(req)
        customReq(req)

def get():
    req = f"SELECT x,y, uroven_signala, operator from koord_and_kachestvo"
    res = customReq(req)
    return res




