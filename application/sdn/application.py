from pox.core import core
from pox.lib.util import dpid_to_str
from pox.forwarding.l2_learning import LearningSwitch
import pox.openflow.libopenflow_01 as of
from Firewall import Firewall_1
from Firewall import Firewall_2


log = core.getLogger()
class Component1 (object):
    def __init__(self):
        core.openflow.addListeners(self)
        
    
    def _handle_ConnectionUp(self,event):
        dpid=event.dpid
        if dpid==10:
            Firewall_1(event.connection)
        elif dpid==11:
            Firewall_2(event.connection)
        else:
            LearningSwitch(event.connection,self)
        print("Switch %s has come up."% dpid_to_str(event.dpid))

        

    

    


        



def launch():
    core.registerNew(Component1)

