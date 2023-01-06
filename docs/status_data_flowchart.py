# copyright (c) 2022 Kanisorn Kaewsrithong <kanisornka65@nu.ac.th>

"""
Make a flowchart diagramming how that
 status data moves into program
"""

___authore___ = "Kanisorn Kaewsrithong"

# installed libraries
import schemdraw
from schemdraw import flow

with schemdraw.Drawing() as d:
    d += flow.Start(w=6).label('Data send from HIVEMQ')
    d += flow.Arrow().down(d.unit/2)
    d += flow.Data(h=1.5,w=6).label(' receive into on_message\n'
                           'in comm_mqtt.MQTTConn')
    d += flow.Arrow().down(d.unit / 2)
    d += flow.Process(w=6).label('process input message \n '
                              'into a sensor status')
    d += flow.Arrow().down(d.unit / 2)
    d += flow.Data(w=7).label('send sensor status to\n'
                           'main_gui.SensorUI.chang_status')
    d += flow.Arrow().down(d.unit / 2)
    d += (d1 := flow.Decision(w=5,h=5, E='No', S='Yes').label("Is the name from \n"
                               "the data found in \n"
                               "the NAMES list"))
    d += flow.Arrow().right(d.unit / 2).at(d1.E)
    d += flow.Terminal(w=5, label = 'Exit with no change').anchor('W')
    d += flow.Arrow().down(d.unit / 2).at(d1.S)
    d += flow.Process(w=10).label('call main_gui.Status.StatusButton.toggle_color\n'
                              'and set the proper color the indicator')
