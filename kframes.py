# kframes.py    usage:  from kframes import *

M_frame = """
  <button id="bcamPID">PIDs (bcamPID) </button>
    <font size=2><span id="msgPID"> msgUTIL </span></font>
  <BR><button id="bcamUtilTemp">mc21a (bcamUtilTemp) </button>
  <font size=2><span id="msgUTIL"> msgUTIL </span></font>
  <BR> <button id="bcamLocalUtilTemp">sd128a (bcamLocalUtilTemp) </button>
    <font size=2><span id="msgLocalUTILTemp"> msgLocalUTILTemp </span></font>
  <BR><em><font size=2>msg:</em> <span id="msg">msg</span></font>
"""

V_frame = """
   <B><a href=http://mc21a:8090> BirdieCam</a></B>
   &nbsp;&nbsp; 192.168.1.29/html/birdicam/jbframes.php/  Video source: {iframesrc}<BR>
   <xiframe src="https://bxharold.github.io/pigsfly/" width=680 height=540 ></xiframe>
   <iframe src="{iframesrc}" width=680 height=540 ></iframe>
Video source: {iframesrc} <BR>
<font size=2><em> If the video stream fails or freezes, check the Camera PID. If Camera PID>0, refresh this page. If "-1", start the camera server, then reload this page. If that fails, try " ps -aux | grep mjp  ", and kill the offending raspimjpeg process.
<BR> If Command PID is "-1", webcmd.py was probably started from an IDE like Thonny.</em></font>
"""
# after import, do late eval:  V_frame = V_frame.format(iframesrc=iframesrc)
#  from kframes import *
# iframesrc = ".../" if HOST.lower().startswith('imac') else "...g"
# V_frame = V_frame.format(iframesrc=iframesrc)

A_frame = """
<table border=0  ules=rows width=100% >
<TR><TH colspan=4 align=left>LEDs
<TR>
    <TD width=80><input type=checkbox class="C" id="CBblue" ></input><BR>Blue
    <TD width=80><input type=checkbox class="C" id="CBred" ></input><BR>Red
    <TD width=80><input type=checkbox class="C" id="CByellow" ></input><BR>Yellow
    <TD width=120 align=right> <button id="LEDallon" class="B">All On </button>
    <TD width=120 align=right> <button id="LEDalloff" class="B">All Off</button>
    <TR><TD colspan=4><td><button id="LEDrefresh" class="B"> Refresh &nbsp;&nbsp;</button>
<TR><TD colspan=6 align=left> &nbsp; <font size=2><span id="LEDmsg">&nbsp;</span></font>
</table>
"""

B_frame = """
<table border=0  ules=rows width=198>
<TR><TH colspan=3 align=left>Pan / Servo Control
<TR><TD colspan=3 align=left> &nbsp; Move:
<TR><TH width=90><button class="B" id="BL" > &#9665;&nbsp;Left </button>
    <TH width=90><button class="B" id="BC" > &gt;Center&lt; </button>
    <TH width=90><button class="B" id="BR" > Right &nbsp; &#9655;</button>
<TR><TD colspan=3 align=left> &nbsp; Pan:
<TR><TH><button class="B" id="BPL"> &#9664; </button>
    <TH><button class="B" id="BPS" > &#9724; </button>
    <TH><button class="B" id="BPR"> &#9654; </button>
<TR><TD colspan=3 align=left>&nbsp;
<TR><TD colspan=3 align=left>&nbsp;Bearing:
    <BR><center>
<canvas id="cBearing" width="200" height="120" style="border:1px solid #d3d3d3;">:(</canvas>
        </center>
<TR><TD>&nbsp;Status:<TD colspan=2 align=left> &nbsp; <span id="servomsg">Idle</span>
<TR><TH colspan=3 align=left><HR height=3>
<TR><TH colspan=3 align=left>Camera / Server
<TR><TD> &nbsp;Camera&nbsp;PID: <TD><div id="bcamwebstreamPID"> n/a </div>
<TD><button class="B" id="StopCamera">Stop Camera</button>
<TR><TD> &nbsp;Command&nbsp;PID: <TD><div id="bcamwebcmdPID"> n/a </div>
</table>
"""

C_frame = """
      <table border=5  ules=rows width=198>
        <TR><TH colspan=3 align=left >CPU Performance
        <TR><Td align=middle colspan=3>
               <table border=1 width=298 rules=rows cellspacing=9>
                 <TR><Td width=98>Machine
                    <Td width=98 align=right> Utilization
                    <Td width=98>Temperature(&deg;C)
                 <TR><Td width=98 align=left><div id="bcamHostname">cam&nbsp;server</div>
                    <Td align=right width=98><div id="bcamUtil">util</div>
                    <Td align=right width=98><div id="bcamTemp"> temp</div>
                 <TR><Td width=98 align=left><div id="bcamHostname2">local</div>
                    <Td align=right width=98><div id="bcamUtil2">util2</div>
                    <Td align=right width=98><div id="bcamTemp2"> temp2</div>
               </table>
            </Td>
        <TR><TH><!-- <button class="B" id="UpdateCPU" onClick=
                '$("#bcamLocalUtilTemp").click(); $("#bcamUtilTemp").click();'>Update</button> -->
             <TH><button class="B" id="LoopCPU" onClick='perfStartTimer()'> Loop... </button>
             <TH><button class="B" id="StopLoopCPU"  onClick='perfStopTimer()'> Stop.</button>
        <TR>
             <TH><button class="Bs" onClick= 'drawBearingGauge(document.getElementById("cBearing"), -0.75)'> bQuickTest.</button>
      </table>
"""

