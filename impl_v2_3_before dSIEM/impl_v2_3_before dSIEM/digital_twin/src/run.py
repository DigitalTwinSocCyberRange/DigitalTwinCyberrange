"""
FP run.py
"""

from mininet.net import Mininet
from mininet.cli import CLI
from minicps.mcps import MiniCPS
from topo import FPTopo

import sys
import time


class FPCPS(MiniCPS):

    """Main container used to run the simulation."""

    def __init__(self, name, net):

        self.name = name
        self.net = net

        net.start()
        net.pingAll()

        # start devices
        plc1, plc2, plc3, s1, s1bottle, attacker = self.net.get('plc1', 'plc2', 'plc3', 's1', 's1', 'attacker')

        s1.popen('python physical_process.py')
        s1bottle.popen('python physical_process_bottle.py')
        plc3.popen('python plc3.py')
        plc2.popen('python plc2.py')
        plc1.popen('python plc1.py')

        while True:
            time.sleep(100)
            attacker.popen('bash start_attack.sh')

        CLI(self.net)

        self.net.stop()

if __name__ == "__main__":

    topo = FPTopo()
    net = Mininet(topo=topo)

    fpcps = FPCPS(
        name='FPCPS',
        net=net)
