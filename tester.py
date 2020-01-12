from common.macaddr import getHwAddr
from common.macaddr import setTempHwAddr
from common.usbdongle import setMonitorMode

iface = 'wlan0'
newMAC = '00:11:22:33:44:55'


def main():
    # print(getHwAddr(iface))
    # setTempHwAddr(iface, newMAC)
    setMonitorMode(iface)


if __name__ == "__main__":
    main()
