from flask import Flask, render_template, request, jsonify
import mysql.connector as mysql
import audioCapture
mydb=mysql.connect(
    host="localhost",
    user="root",
    password="anas123",
    database="noise_monitor"
)
my_cursor=mydb.cursor(dictionary=True)
create_table_query="CREATE TABLE IF NOT EXISTS noise_data (id INT AUTO_INCREMENT PRIMARY KEY,db_level FLOAT, latitude FLOAT, longitude FLOAT, timestamp DATETIME)"
my_cursor.execute(create_table_query)
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/currentNoise')
def currentNoise():
    db=audioCapture.get_noise_level()
    return jsonify({'db':db})
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)