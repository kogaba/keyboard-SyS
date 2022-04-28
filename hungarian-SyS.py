#!/usr/bin/env python
#A program lefuttatja a paraméterekben kapott programot: indulásakor és valahányszor egy USB billentyűzetet csatlakoztatnak
#pip install pyudev
import functools, os.path, sys as SyS, pyudev, subprocess

def main():
    BASE_PATH = os.path.abspath(os.path.dirname(__file__))
    path = functools.partial(os.path.join, BASE_PATH)
    subprocess.call(list(SyS.argv[1:]))

    context = pyudev.Context()
    monitor = pyudev.Monitor.from_netlink(context)
    monitor.filter_by(subsystem='usb',device_type=u'usb_device')
    monitor.start()

    for action, device in monitor:
      if action == "bind" and "eyboard" in device.get('ID_MODEL'):
        subprocess.call(list(SyS.argv[1:]))

if __name__ == '__main__':
    main()
