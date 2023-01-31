#!/usr/bin/env python

'Setting the position of Nodes and providing mobility using mobility models'
import sys

from mininet.log import setLogLevel, info
from mn_wifi.cli import CLI
from mn_wifi.net import Mininet_wifi


def topology(args):
    "Create a network."
    net = Mininet_wifi()

    info("*** Creating nodes\n")

    ap1 = net.addAccessPoint('ap-1', ssid='new-ssid', mode='g', channel='1',
                             failMode="standalone", position='50,50,0', range=30)

    var_name = "drone-{}"
    var_mac = "00:00:00:00:00:{:02d}"
    var_ip = "10.0.0.{}/8"

    for x in range(2, 23):
        net.addStation(var_name.format(x), mac=var_mac.format(x), ip=var_ip.format(x),
                   min_x=0, max_x=80, min_y=0, max_y=80, min_v=5, max_v=80, range=20)        

    info("*** Configuring propagation model\n")
    net.setPropagationModel(model="logDistance", exp=5)

    info("*** Configuring nodes\n")
    net.configureNodes()

    for x in range(2, 23):
        net.addLink(var_name.format(x), ap1)

    if '-p' not in args:
        net.plotGraph(max_x=200, max_y=200)

    net.setMobilityModel(time=0, model='RandomDirection', max_x=100, max_y=100, seed=2)

    info("*** Starting network\n")
    net.build()
    ap1.start([])

    info("*** Running CLI\n")
    CLI(net)

    info("*** Stopping network\n")
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    topology(sys.argv)