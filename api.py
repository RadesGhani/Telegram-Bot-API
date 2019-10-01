from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonify 

import config

db_connect = create_engine(str(config.dbConfig.dialect) + "+" + config.dbConfig.sql_driver + "://" + str(config.dbConfig.user) + ":" + str(config.dbConfig.password) + "@" + str(config.dbConfig.url) + ":" + str(config.dbConfig.port) + "/?service_name=" + str(config.dbConfig.service_name))
print("Checking database connection....")
db_connect.connect()
app = Flask(__name__)
api = Api(app)

#----Define endpoints bellow----
class data_user(Resource):
    def get(self):
        conn = db_connect.connect() # connect to database
        query = conn.execute("select * from data_user") # This line performs query and returns json result
        result = {"data":[dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]} # Fetches first column that is Employee ID
        conn.close()
        return jsonify(result)
api.add_resource(data_user, '/data_user') # Route_1

class yearly(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select * from atp_keywords")
        result = {"data":[dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]} # Fetches first column that is Employee ID
        conn.close
        return jsonify(result)
    def post(self):
        keyword = request.values.get("keyword")
        year = request.values.get("year")
        conn = db_connect.connect()
        query = "select LTRIM(to_char(count(distinct AUP.UP_MSISDN),'9,999,999,999','NLS_NUMERIC_CHARACTERS = '',.''')) UNIQUE_REDEEMER, LTRIM(to_char(count(distinct aup.up_evd_id),'9,999,999,999','NLS_NUMERIC_CHARACTERS = '',.''')) TRX, LTRIM(to_char(sum(aup.up_point),'9,999,999,999','NLS_NUMERIC_CHARACTERS = '',.''')) POIN_BURNED, AK.KEYWORD KEYWORD from ( select aup.up_msisdn up_msisdn, aup.up_evd_id up_evd_id, aup.up_point up_point, AUP.UP_EVD_SET_ID UP_EVD_SET_ID from atp_uposted_points aup where  aup.UP_EVD_SET_ID in ( SELECT APP.EVT_SET_ID FROM ATP_PARAMETER_POINTOUT APP WHERE app.keyword_id in ( select ak.keyword_id FROM ATP_KEYWORDS AK where upper(keyword) = '"+keyword+"'  )) and to_char(UP_evd_period,'YYYY') = '"+year+"' ) aup, ATP_PARAMETER_POINTOUT APP, ATP_KEYWORDS AK WHERE AUP.UP_EVD_SET_ID = app.evt_set_id  AND app.keyword_id = ak.keyword_id group by AK.KEYWORD"
        print(query)
        query = conn.execute(query)
        result = {"data":[dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        conn.close()
        print(result)
        return jsonify(result)   
api.add_resource(yearly, '/yearly')
#----END----


#Starting API
print("Starting api...")
if __name__ == '__main__':
    app.run(port='5002')