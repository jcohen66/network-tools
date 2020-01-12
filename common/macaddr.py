import netifaces
import os


def getHwAddr(ifname):
    if ifname in netifaces.interfaces():
        ifaces = netifaces.ifaddresses(ifname)[netifaces.AF_LINK]
        return ifaces[0]['addr']
    else:
        raise KeyError("Interface not found.")


def setTempHwAddr(iface, tempAddr, output=False):
    if output:
        print(getHwAddr(iface))

    os.system('ifconfig ' + iface + ' down')
    os.system('ifconfig ' + iface + ' hw ether ' + tempAddr)
    os.system('ifconfig ' + iface + ' up')

    if output:
        print(getHwAddr(iface))
