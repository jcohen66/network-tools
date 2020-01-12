import os


def setMonitorMode(iface, output=False):
    if output:
        os.system('iwconfig ' + iface)

    os.system('ifconfig ' + iface + ' down')
    os.system('airmon-ng ' + iface + ' check kill')
    os.system('iwconfig ' + iface + ' mode monitor')
    os.system('ifconfig ' + iface + ' up')

    if output:
        os.system('iwconfig ' + iface)
        print('Note: Network Manager has been killed.')
