from flask import render_template, request
from flask import jsonify 
from app import app
from cassandra.cluster import Cluster

#connect to cassandra
cluster = Cluster(['ec2-52-41-2-110.us-west-2.compute.amazonaws.com', 'ec2-52-32-133-95.us-west-2.compute.amazonaws.com', 'ec2-52-34-129-5.us-west-2.compute.amazonaws.com'])
session = cluster.connect("hotred")

session.default_fetch_size = None #turn off paging to allow IN () ORDER BY queries, since only a few records are SELECTed anyway

def _get_data(time):
    #pull latest trades, latest news, and portfolio from database for the user
    #check which database to query
    #dbfile = open("/home/ubuntu/.insightproject/cassandra.txt")
    #db = dbfile.readline().rstrip()
    #dbfile.close()

    #get a few of the latest trades for the user
    latest_topic = session.execute("SELECT * FROM topnews WHERE subreddit_id=%s", parameters=[time])

    return latest_topic

def _get_json_data(time):
    latest_topic = _get_data(time)
    topic_json = [{"subreddit_id": row.subreddit_id, "created_utc": row.created_utc, "body": row.body, "link_id": row.link_id, "name": row.name, "parent_id": row.parent_id} for row in latest_topic]
    return jsonify(latest_topic = topic_json)

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/getTopic/<time>')
def get_topic(time):
    return _get_json_data(time)

#@app.route('/topic')
#def get_topic():
#    time=request.args.get("time")
#    latest_trades, portfolio, latest_news = _get_user_data(request.args.get("user"))
#    return render_template("user.html", user=user, latest_trades = latest_trades, portfolio = portfolio, latest_news = latest_news)



