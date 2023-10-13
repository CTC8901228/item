# ble_scan_connect.py
from bluepy.btle import Peripheral, UUID
from bluepy.btle import Scanner, DefaultDelegate

class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            print("Discovered device", dev.addr)
        elif isNewData:
            print("Received new data from", dev.addr)

scanner = Scanner().withDelegate(ScanDelegate())
devices = scanner.scan(10.0)
n = 0
addr = []

for dev in devices:
    print("%d: Device %s (%s), RSSI=%d dB" % (n, dev.addr, dev.addrType, dev.rssi))
    addr.append(dev.addr)
    n += 1

    for (adtype, desc, value) in dev.getScanData():
        print(" %s = %s" % (desc, value))
        if(value=='r119')
            number=n
# number = input('Enter your device number: ')
# print('Device', number)
# num = int(number)
print(addr[num])
print("Connecting...")
dev = Peripheral(addr[num], 'random')
print("Services...")

for i in dev.getDescriptors(startHnd=0x2902, endHnd=0x2902):
    print(i)
    print(dir(i))


print(dev)
for svc in dev.services:
    print(str(svc))
i=0
# try:
#     testService = dev.getServiceByUUID(UUID(0xfff0))
#     for ch in testService.getCharacteristics():
#         print(str(ch))
#         i+=1
#         print("data"+str(i))
#         # if ch.supportsRead():
#         #     print(ch.read())
#         # # if ch.supportsWrite():
#         # else:
#         ch.write("fuck!!!!!!!!!!".encode("utf-8"))
try:
    i=0
    for ch in dev.getCharacteristics(uuid=UUID(0xfff4)):
        i+=1
        print("data"+str(i))
        # if ch.supportsRead():
        #     print(ch.read())
        # # if ch.supportsWrite():
        # else:
        ch.write("666666666666666".encode("utf-8"))
    for ch in dev.getCharacteristics(uuid=UUID(0xfff4)):
        i+=1
        print("data"+str(i))
        # if ch.supportsRead():
        #     print(ch.read())
        # # if ch.supportsWrite():
        # else:
        ch.write("666666666666666".encode("utf-8"))

finally:
    dev.disconnect()
