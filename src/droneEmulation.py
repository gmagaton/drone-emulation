#!/usr/bin/env python

'Setting the position of Nodes and providing mobility using mobility models'
import sys

from mininet.log import setLogLevel, info
from mn_wifi.cli import CLI
from mn_wifi.net import Mininet_wifi


def topology(args):
    "Create a network."
    net = Mininet_wifi()

    c0 = net.addController()

    info("*** Creating nodes\n")

    ap1 = net.addAccessPoint('ap-1', ssid='new-ssid', mode='g', channel='1',
                             failMode="standalone", position='50,50,0', range=90)

    var_name = "drone-{}"

    for x in range(1, 21):
        net.addStation(var_name.format(x), range=40)        

    #info("*** Configuring propagation model\n")
    net.setPropagationModel(model="logDistance", exp=5)

    info("*** Configuring nodes\n")
    net.configureNodes()

    for x in range(1, 21):
        net.addLink(ap1, var_name.format(x))

    net.plotGraph(max_x=200, max_y=200)

    net.setMobilityModel(time=0, model='RandomDirection', max_x=100, max_y=100, seed=20)

    info("*** Starting network\n")
    net.build()

    net.controllers[0].start()
    net.get('ap-1').start([c0])

    ap1.start([])

    info("*** Running CLI\n")
    CLI(net)

    info("*** Stopping network\n")
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    topology(sys.argv)