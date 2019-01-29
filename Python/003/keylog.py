import csv
import libpcap

packetfile = open('/home/alex/Projects/Python/003/packets.csv')
csvReader = csv.DictReader(packetfile)
lc = 0
packets = []
keys = ''
index = 0
for line in csvReader:
    if lc == 0 :
        lc = 1
    else:
        packets.append(line['Leftover Capture Data'])
        #print(line['Leftover Capture Data'])
prevpacket = '0'*16
for packet in packets:
    #print packet
    shift = 0
    for i in range(8):
        #print(i)
        scancode = int(packet[(i*2):(i*2+2)], 16)
        #print(chr(scancode+61))
        #scancode = hex(sc)
        if i == 0: #modifier key
            shift = scancode & 0x22 > 0
        elif i > 1:
            #print(i)
            #print
            # if scancode == 0x00:

            if scancode == 0x2a and str(scancode) not in prevpacket: # backspace
                keys = keys[:index] + keys[index+1:]
                index -= 1
                print 'Backspace'
            if scancode == 0x4c and str(scancode) not in prevpacket: # del
                keys = keys[:index+1] + keys[index+2:]
                print 'del'
            if scancode == 0x4f and str(scancode) not in prevpacket: #right key pressed
                index = min(len(keys), index+1)
                print 'Right'
            if scancode == 0x50 and str(scancode) not in prevpacket: #left key pressed
                #if keys[index-1] != '\n':
                index = max(0, index-1)
                print 'Left'
            if scancode in range(0x04,0x1d) and str(scancode) not in prevpacket[(i+1)*2:]: #letters
                print(chr(scancode+93 - shift*32))
                keys = keys[:(index)] + chr(scancode+93 - shift*32) + keys[(index):]
                #keys[index] = chr(scancode+61) 
                index += 1
            # if scancode in range(0x1e,0x26) and str(scancode) not in prevpacket: #numbers
            #     keys = keys[:(index)] + chr(scancode+19) + keys[(index):]
            #     index += 1
            if scancode == 0x1e and str(scancode) not in prevpacket: #1
                keys = keys[:(index)] + chr(0x31 - 0x10*shift) + keys[(index):]
                index += 1
                print chr(0x31 - 0x10*shift)
            if scancode == 0x1f and str(scancode) not in prevpacket: #2
                keys = keys[:(index)] + chr(0x32 + 0x0e*shift) + keys[(index):]
                index += 1
                print chr(0x32 + 0x0e*shift)
            if scancode == 0x20 and str(scancode) not in prevpacket: #3
                keys = keys[:(index)] + chr(0x33 - 0x10*shift) + keys[(index):]
                index += 1
                print chr(0x33 - 0x10*shift)
            if scancode == 0x21 and str(scancode) not in prevpacket: #4
                keys = keys[:(index)] + chr(0x34 - 0x10*shift) + keys[(index):]
                index += 1
                print chr(0x34 - 0x10*shift)
            if scancode == 0x22 and str(scancode) not in prevpacket: #5
                keys = keys[:(index)] + chr(0x35 - 0x10*shift) + keys[(index):]
                index += 1
                print chr(0x35 - 0x10*shift)
            if scancode == 0x23 and str(scancode) not in prevpacket: #6
                keys = keys[:(index)] + chr(0x36 + 0x28*shift) + keys[(index):]
                index += 1
                print chr(0x36 + 0x28*shift)
            if scancode == 0x24 and str(scancode) not in prevpacket: #7
                keys = keys[:(index)] + chr(0x37 - 0x11*shift) + keys[(index):]
                index += 1
                print chr(0x37 - 0x11*shift)
            if scancode == 0x25 and str(scancode) not in prevpacket: #8
                keys = keys[:(index)] + chr(0x38 - 0x0e*shift) + keys[(index):]
                index += 1
                print chr(0x38 - 0x0e*shift)
            if scancode == 0x26 and str(scancode) not in prevpacket: #9
                keys = keys[:(index)] + chr(0x39 - 0x11*shift) + keys[(index):]
                index += 1
                print chr(0x39 - 0x11*shift)
            if scancode == 0x27 and str(scancode) not in prevpacket: #0
                keys = keys[:(index)] + chr(0x30 - 0x07*shift) + keys[(index):]
                index += 1
                print chr(0x30 - 0x07*shift)
            if scancode == 0x37 and str(scancode) not in prevpacket: #'.'
                keys = keys[:(index)] + chr(0x2e + 0x10*shift) + keys[(index):]
                index += 1
                print chr(0x2e + 0x10*shift)
            if scancode == 0x28 and str(scancode) not in prevpacket: #\n
                keys = keys[:(index)] + '\n' + keys[(index):]
                index += 1
                print '\\n'
            if scancode == 0x2c and str(scancode) not in prevpacket: #space
                keys = keys[:(index)] + chr(0x2c) + keys[(index):]
                index += 1
                print 'Space'
            if scancode == 0x2d and str(scancode) not in prevpacket: #-/_
                keys = keys[:(index)] + chr(0x2d + 0x32*shift) + keys[(index):]
                index += 1
                print chr(0x2d + 0x32*shift)
            if scancode == 0x34 and str(scancode) not in prevpacket: #-/_
                keys = keys[:(index)] + chr(0x27 - 0x05*shift) + keys[(index):]
                index += 1
                print chr(0x2d + 0x32*shift)
            if scancode == 0x2f and str(scancode) not in prevpacket: #[/{
                keys = keys[:(index)] + chr(0x5b + 0x20*shift) + keys[(index):]
                index += 1
                print chr(0x5b + 0x20*shift)
            if scancode == 0x30 and str(scancode) not in prevpacket: #]/}
                keys = keys[:(index)] + chr(0x5d + 0x20*shift) + keys[(index):]
                index += 1
                print chr(0x5d + 0x20*shift)
            
        #print index
    prevpacket=packet
#print(packets)
print(keys)