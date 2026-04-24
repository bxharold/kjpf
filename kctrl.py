#!/usr/local/bin/python3
#    kctrl.py  based on echoAPI.py
from flask import Flask, jsonify, request
from flask_cors import CORS     ###  pip3 install Flask-CORS 

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route("/")  # http://127.0.0.1:5000/5
def nothing():
  result = "nothing was asked for"
  return jsonify({"func": "echo", "result": result}) 

# state persists for testing; When live, use  LED(pin).is_active 
state = {"CBblue":"false","CBred":"false", "CByellow":"false"}

# servo bearing persists for testing; When live, use  ... TBD
bearing = 90  # only one servo (pan)
# servo has min and max values, assume 0 and 180
(servoMin, servoMax, servoDelta) = (0, 180, 15)

# read-only; get and return LEDstatus
@app.route("/LEDstate")  # http://127.0.0.1:5000/LED/state
def LEDstate():
  global state
  pins = {"CBred":"13", "CByellow":"19", "CBblue":"26"}
  rv = {"func":"LEDstate"}
  rv["summary"] = state
  rv["state"] = state
  rv["error"] = ""
  rv["RUNNING_AS"] = "HiMac2:~/garden/square/eventhandlers/echoAPI.py"
  return jsonify(rv)

# map LEDid to pin#; do the LED; get and return LEDstatus
@app.route("/LED/<LEDid>/<onoff>")  # http://127.0.0.1:5000/LED/CBred/on
def LED(LEDid,onoff):
  global state
  pins = {"CBred":"13", "CByellow":"19", "CBblue":"26"}
  summary = f"LED {LEDid} on pin {pins[LEDid]} was turned {onoff}" 
  rv = {"func":"LED"}
  rv["led"] = LEDid
  rv["summary"] = summary
  rv["setting"] = onoff
  state[LEDid] = "true" if onoff == "on" else "false"
  rv["state"] = state
  rv["error"] = ""
  rv["RUNNING_AS"] = "HiMac2:~/garden/square/eventhandlers/echoAPI.py"
  return jsonify(rv)
  
# map servo button ID to cmd; move the servo, get and return new bearing
@app.route("/servo/<cmd>")  # http://127.0.0.1:5000/servo/BC
def servo(cmd):
  global bearing, servoMin, servoMax, servoDelta
  oldbearing = bearing
  cmds = {"BL":f"{-servoDelta}", "BC":"0", "BR":f"{servoDelta}", "BPL":"0", "BPS":"90", "BPR":"180" }
  ### OK, this needs rethinking,  BC does NOT translate to delta=0.
  ###   not useful.  bearing += int(cmds[cmd])
  if cmd == "BL":
    bearing -= servoDelta
  elif cmd == "BR":
    bearing += servoDelta
  elif cmd == "BC":
    bearing = 90
  else:
    pass  # no change
  bearing = min(bearing, servoMax)
  bearing = max(bearing, servoMin)
  summary = f"servo bearing set from {oldbearing} to {bearing}"
  rv = {"func":"servo"}
  rv["summary"] = summary
  rv["bearing"] = bearing
  rv["error"] = ""
  rv["RUNNING_AS"] = "HiMac2:~/garden/square/eventhandlers/echoAPI.py"
  return jsonify(rv)

@app.route("/square/<x>")  # http://127.0.0.1:5000/square/25
def square(x):
  result = int(x)**2
  return jsonify({"func": "square","result": result}) 

if __name__ == "__main__":
  #app.run(host="0.0.0.0", port=f"{sys.argv[1]}", debug=True)
  app.run(host="0.0.0.0", debug=True)

