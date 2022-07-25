#!/usr/bin/env python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call

def myNetwork():

    net = Mininet( topo=None,
                   build=False,
                   ipBase='10.0.0.0/8')

    info( '*** Adding controller\n' )
    c=net.addController(name='c',
                      controller=RemoteController,
                      ip='127.0.0.1',
                      protocol='tcp',
                      port=6633)

    info( '*** Add switches\n')
    s7 = net.addSwitch('s7', cls=OVSKernelSwitch)
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch)
    s5 = net.addSwitch('s5', cls=OVSKernelSwitch)
    s2 = net.addSwitch('s2', cls=OVSKernelSwitch)
    s8 = net.addSwitch('s8', cls=OVSKernelSwitch)
    s3 = net.addSwitch('s3', cls=OVSKernelSwitch)
    s4 = net.addSwitch('s4', cls=OVSKernelSwitch)
    s9 = net.addSwitch('s9', cls=OVSKernelSwitch)
    s6 = net.addSwitch('s6', cls=OVSKernelSwitch)

    info( '*** Add hosts\n')
    h3 = net.addHost('h3', cls=Host, ip='10.0.0.3', defaultRoute=None)
    h2 = net.addHost('h2', cls=Host, ip='10.0.0.2', defaultRoute=None)
    h1 = net.addHost('h1', cls=Host, ip='10.0.0.1', defaultRoute=None)

    info( '*** Add links\n')
    net.addLink(h1, s1, 1, 1, cls=TCLink ,bw=10)
    net.addLink(h3, s1, 1, 5, cls=TCLink ,bw=10)
    net.addLink(s1, s5, 3, 1, cls=TCLink ,bw=5)
    net.addLink(s5, s8, 4, 2 ,cls=TCLink ,bw=8)
    net.addLink(s8, s9, 4, 2, cls=TCLink ,bw=5)
    net.addLink(s9, h2, 4, 1, cls=TCLink ,bw=10)
    net.addLink(s7, s8, 2, 1, cls=TCLink ,bw=2)
    net.addLink(s1, s2, 2, 1, cls=TCLink ,bw=10)
    net.addLink(s2, s4, 2, 1, cls=TCLink ,bw=3)
    net.addLink(s4, s7, 2, 1, cls=TCLink ,bw=5)
    net.addLink(s1, s3, 4, 1, cls=TCLink ,bw=5)
    net.addLink(s3, s6, 3, 2, cls=TCLink ,bw=3)
    net.addLink(s6, s9, 4, 3, cls=TCLink ,bw=8)
    net.addLink(s5, s3, 2, 2, cls=TCLink ,bw=3)
    net.addLink(s5, s6, 3, 1, cls=TCLink ,bw=3)
    net.addLink(s8, s6, 3, 3, cls=TCLink ,bw=4)
    net.addLink(s7, s9, 3, 1, cls=TCLink ,bw=5)

    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches\n')
    net.get('s7').start([c])
    net.get('s1').start([c])
    net.get('s5').start([c])
    net.get('s2').start([c])
    net.get('s8').start([c])
    net.get('s3').start([c])
    net.get('s4').start([c])
    net.get('s9').start([c])
    net.get('s6').start([c])

    info( '*** Post configure switches and hosts\n')

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()

