# Project:  kjpf 

## Overview:
kjpf (kamera,javascript,python,flask) is an ongoing Raspberry Pi/Camera "maker" project.
TL;DR -- Pi camera streams video to a browser with a UI that controls the action.

kjpf's roots go back to "birdiecam.php" (a browser-based UI to control and monitor 
a camera attached to a Raspberry Pi3b+) and a breadboard setup (bbmini) that 
I use for GPIO learner projects. "bbmini" has 3 LEDs, a PIR sensor, a pushbutton, 
and a servo motor.

The "ycam" project is birdiecam.php rewritten using the bottle framework. 
Using python for both front-end and back-end paid off in the long run.  
As the project grew, Flask was the logical next step. The CS50 lecture on 
Flask absolutely sealed the deal.

The objective of kjpf is to architect the controller as an API.  This uses
Javascript's "await/fetch" to make the API requests, and updates the DOM with 
the info contained in the response.


## Environment:
- bbmini is a dev "platform" (aka "block of wood") with a Pi3b+ (mc24b), an attached camera, a PIR sensor, a pushbutton, and 3 LEDs.
- mc24b manages the camera (camstream.py) and implements the API ("kctrl.py")
- As of 2025, the servo is no longer attached to the Pi -- this didn't work well, and a separately powered servo is a new project objective.
-- For now, the servo controls merely provide state maintenance for the ghost servo, which is used in the UI to provide eye candy in the form of a directional bearing gauge. 
  
## Processes:
- kctrl.py is the controller, the API.  (port __KK__)
- camstream.py creates the video stream. (port __VV__) 
- kjpf.py serves up the client UI  (port __CC__)
- The web client browses to http://HiMac2.local:[__CC__]/kfpj.html

### API kctrl.py has endpoints for bbmini LEDs, servo, CPU performance, and general info:  
- @app.route("/LEDstate")
- @app.route("/LED/<LEDid>/<onoff>") 
- @app.route("/CPUperf")
- @app.route("/util")
- @app.route("/servo")


### Client functions (Javascript):

LEDrefresh() invokes the /LEDstate endpoint, then calls the DOM updater.
async function LEDrefresh() makes the API request to the /LEDstate endpoint
and then calls the DOM updater refreshLEDcheckboxes(state) 

async function LED() makes the API request to the /LED/<>/<> endpoint
kctrl.py updates the "state" (and the LEDs) and returns a summary.
LED() then calls the updater refreshLEDcheckboxes() with the new state.

