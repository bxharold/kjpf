//  kscripts.js           4/21/2026
/**
API kctrl.py has 2 LED endpoints:  @app.route("/LEDstate")
                                   @app.route("/LED/<LEDid>/<onoff>") 
Client functions:
LEDrefresh() invokes the /LEDstate endpoint, then calls the DOM updater.
async function LEDrefresh() makes the API request to the /LEDstate endpoint
and then calls the DOM updater refreshLEDcheckboxes(state) 

async function LED() makes the API request to the /LED/<>/<> endpoint
kctrl.py updates the "state" (and the LEDs) and returns a summary.
LED() then calls the updater refreshLEDcheckboxes() with the new state.

Implementation in the browser (UI):
1. Define the button in DOM (HTML) 
2. write the await/fetch code that invokes the APIs 
3. in window.addEventListener('load', (event) => { ...
   add a listener for each button to invoke the a/f code
**/

async function LED(LEDid,onoff) {
  endpoint = `http://127.0.0.1:5000/LED/${LEDid}/${onoff}`
  console.log(endpoint)
  try {
    const response = await fetch(endpoint);
    const { func, led, setting, state, summary, error } = await response.json();
    if (error) {
      msg.textContent = error;  
      return; // Early return pattern to avoid 'else' nesting
    }
    msg.textContent = `${func} : ${led} : ${summary} : ${JSON.stringify(state)} :`;
    console.log( `${func} : ${led} : ${summary} : ${JSON.stringify(state)} :` )
    refreshLEDcheckboxes(state)
  } catch (err) {
    console.error('Fetch error:', err);
  }
}

async function LEDrefresh() { // gets the LED state from kctlr.py
  console.log('LEDrefresh was invoked')
    endpoint = `http://127.0.0.1:5000/LEDstate`
    console.log("endpoint ", endpoint)
    try {
      const response = await fetch(endpoint);
      const { func, state, summary, error } = await response.json();
      if (error) {
        msg.textContent = error;
        return; // Early return pattern to avoid 'else' nesting
      }
      console.log( `ref ${func} :  ${JSON.stringify(state)} : ${summary} :`)
      refreshLEDcheckboxes(state)  // This calls the DOM updater
    } catch (err) {
      console.error('Fetch error:', err);
    }
}; 

// SET THE CHECKBOXES BASED ON THE STATE RETURNED BY THE API kctlr.py
function refreshLEDcheckboxes(state) {  // update the DOM
  console.log(`r state", ${JSON.stringify(state)}` )   
  for (let key in state) {
    console.log(`key: ${key}, state: ${state[key]}`);
    document.getElementById(key).checked = state[key]=="true"?true:false
    LEDmsg.textContent = `LED state sync'd`;
  }
}

async function makeListeners_LEDrefresh_button() {
  btn = document.getElementById("LEDrefresh")
  btn.addEventListener('click', async () => LEDrefresh() 
)};

async function makeListeners_LED_allon_alloff_buttons(LEDbuttons) {
  btn = document.getElementById(LEDbuttons[0])
  btn.addEventListener('click', async () => {
    LED("CBblue", "on")       //
    LED("CBred", "on")       // 
    LED("CByellow", "on")   //
    LEDmsg.textContent = `All LEDs turned ON`;
  })
  btn = document.getElementById(LEDbuttons[1])
  btn.addEventListener('click', async () => {
    LEDcheckboxes.forEach( (cb) => {LED(cb,"off")})
    LEDmsg.textContent = `All LEDs turned OFF`;
  }
)}

function makeListeners_LEDcheckboxes(boxes) {
  console.log(boxes)
  boxes.forEach((boxid, index) => {
    const box = document.getElementById(boxid)    // MUST BE const !!!!
    box.addEventListener('click', async () => {
      console.log(`box ${index+1} id=${btn.id} clicked. State:${box.checked}`);
      // now, add the API request to update LEDstate  
      onoff = box.checked?"on":"off"
      endpoint = `http://127.0.0.1:5000/LED/${box.id}/${onoff}`;
      console.log("line 60 " + endpoint)
      try {
        const response = await fetch(endpoint);
        const { func, led, setting, state, summary, error } = await response.json();
        msg.textContent = `${func}:${led}:${summary}:${JSON.stringify(state)}:`;
        LEDmsg.textContent = `${summary}`;
        console.log( `${func}:${led}:${summary}:${JSON.stringify(state)}:` )
        if (error) {
          msg.textContent = error;
          return; // Early return pattern to avoid 'else' nesting
        }
      } catch (err) {
          console.error('Fetch error:', err);
      }
      document.getElementById(boxid).onoff
    });
  });  // boxes.forEach
} 

/*********  THESE MANIPULATE THE DOM, NO API CALLS 
  for dev background, , refer to ~/garden/square/eventhandlers/daxbuttons.html
  function cbListIds() {  // can execute this from the console
    ids = Array.from(document.querySelectorAll('input[type="checkbox"].C')).map(cb => cb.id);
    console.log("cbListIds is this too soon?", ids);
  }

  document.getElementById("LEDset").addEventListener('click', (event) => {
    console.log('button LEDset was clicked!')
    ids = Array.from(document.querySelectorAll('input[type="checkbox"].C')).map(cb => cb.id);
    ids.forEach(cb => { document.getElementById(cb).checked = true})
  }); 

  document.getElementById("LEDclear").addEventListener('click', (event) => {
    console.log('button LEDclear was clicked!')
    ids = Array.from(document.querySelectorAll('input[type="checkbox"].C')).map(cb => cb.id);
    ids.forEach(cb => { document.getElementById(cb).checked = false})
  }); 

****************/

    
//    panservo section. 
function makeListeners_panservo_buttons(buttons2) {
  buttons2.forEach((btnid, index) => {
    const btn = document.getElementById(btnid)
    btn.addEventListener('click', async() => {
      console.log(`Button ${index+1} (id=${btn.id}) clicked. `);
      endpoint = `http://127.0.0.1:5000/servo/${btn.id}`
      // event.preventDefault();
      console.log("endpoint ", endpoint)
      try {
        const response = await fetch(endpoint);
        const { func, bearing, summary, error } = await response.json();
        if (error) {
          msg.textContent = error;
          return; // Early return pattern to avoid 'else' nesting
        }
        msg.textContent = `${func} : ${bearing} : ${summary} :`;
        console.log( `${func} : ${bearing} : ${summary} : ` )
        drawBearingGauge(document.getElementById("cBearing"), bearing/90-1) 
        // simple interpolation  [-90..90] --> [-1,1] 
      } catch (err) {
        console.error('Fetch error:', err);
      }
    });  
  });  
} 

// Using lists of UI ids to keep the API and DOM reasonably separate
// () dropped "buttons = document.querySelectorAll('.C'); ) " approach)
panservoButtons = ["BL","BC","BR","BPL","BPS","BPR"] 
LEDcheckboxes = ["CBblue","CBred","CByellow"]
LEDbuttons = ["LEDallon", "LEDalloff"] 
CPUperfButtons = ["UpdateCPU","LoopCPU","StopLoopCPU"]
UtilButtons = ["bcamPID","bcamUtilTemp","bcamLocalUtilTemp"]

window.addEventListener('load', (event) => {
  makeListeners_LEDrefresh_button()    // btnID is hardcoded
  makeListeners_LED_allon_alloff_buttons(LEDbuttons)
  makeListeners_LEDcheckboxes(LEDcheckboxes)
  makeListeners_panservo_buttons(panservoButtons)
  LEDrefresh()
});

