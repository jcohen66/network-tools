from common.macaddr import getHwAddr
from common.macaddr import setTempHwAddr

iface = 'en9'
newMAC = '00:11:22:33:44:55'


def main():
    print(getHwAddr(iface))
    setTempHwAddr(iface, newMAC)


if __name__ == "__main__":
    main()
