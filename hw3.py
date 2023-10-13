# ble_scan_connect.py
from bluepy.btle import Peripheral, UUID
from bluepy.btle import Scanner, DefaultDelegate
from bluepy import btle
class MyDelegate(btle.DefaultDelegate):
    def __init__(self):
        btle.DefaultDelegate.__init__(self)

    def handleNotification(self, cHandle, data):
        print ("Notification received: handle =", cHandle, "; Raw data =", data)


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
num=-1
for dev in devices:
    print("%d: Device %s (%s), RSSI=%d dB" % (n, dev.addr, dev.addrType, dev.rssi))
    addr.append(dev.addr)
    n += 1

    for (adtype, desc, value) in dev.getScanData():
        print(" %s = %s" % (desc, value))
        if(value=='r11921009' and desc=='Complete Local Name'):
            num=n-1
            break
    if (num!=-1):
        break
assert(num!=-1)
    
# number = input('Enter your device number: ')
# print('Device', number)
# num = int(number)
print(addr[num])
print("Connecting...")
dev = Peripheral(addr[num], 'random')
print("Services...")

for i in dev.getDescriptors(startHnd=1, endHnd=0x2909):

    print(i.uuid)
    if(i.uuid==0x2902):
        w=2
        print(i.read())
        
        i.write(w.to_bytes(1,'little'))
        print(i.read())
        print('write!!!!')
        

    # print(dir(i))


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
    # for ch in dev.getCharacteristics(uuid=UUID(0xfff4)):
    #     i+=1
    #     print("data"+str(i))
    #     # if ch.supportsRead():
    #     #     print(ch.read())
    #     # # if ch.supportsWrite():
    #     # else:
    #     ch.write("666666666666666".encode("utf-8"))
    for ch in dev.getCharacteristics(uuid=UUID(0xfff4)):
        i+=1
        print("data"+str(i))
        # if ch.supportsRead():
        #     print(ch.read())
        # # if ch.supportsWrite():
        # else:
        ch.write("666666666666666".encode("utf-8"))
        dev.setDelegate( MyDelegate() )

    while True:
        if dev.waitForNotifications(1.0):
            # handleNotification() was called
            print('notify!!')
            # continue
    
            print ("Waiting...")
finally:
    dev.disconnect()
