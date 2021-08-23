from app import app
from flask import render_template, request
import json
from time import time_ns

# --- define routes --- # 

@app.route("/", methods=["GET"])
def index():
	"""
	Interactive interface.
	"""
	return render_template("index.html")

@app.route("/ba_tasks", methods=["GET"])
def tasks():
	"""
	Tasks for the interface in JSON format.
	"""
	# tasks are saved in JSON format in a server-side file
	file = open("./app/static/resources/tasks/ba_tasks.json", mode="r", encoding="utf-8")
	tasks = file.read()
	file.close()
	return jsonify(tasks)

@app.route("/save_log", methods=["POST"])
def save_log():
	if not request.data or not request.is_json:
		return "1", 400
	json_data = request.json
	# as a filename that 
	# (1) can not be manipulated by a client
	# (2) has a negligible chance of collision
	# a simple timestamp is used
	filename = str(time_ns()) + ".json"
	file = open(app.config["DATA_COLLECTION"]+filename, encoding="utf-8", mode="w")
	file.write(json.dumps(json_data, indent=2))
	file.close
	return "0", 200
