myData = {"effective top tube length": 515, "seat tube length": 500, "seat tube angle": 74.4, "head tube angle": 70.5, "stack": 513, "reach": 367, "standover height": 755}
myKeys = []
myValues= []

#iteration in parallel

for k, v in myData.items():
    print("key:" + str(k) + ", value:" + str(v))
    myKeys.append(k)
    myValues.append(v)

print("ALL KEYS: " + str(myKeys))
print("ALL VALUES: " + str(myvalues))

#for x, y in myData.items():
    #print('Key:', x, ', value:',y);
#print("ALL KEYS: ['effective top tube length', 'seat tube length', 'seat tube angle', 'head tube angle', 'stack', 'reach', 'standover height']")
#print("ALL VALUES: [515, 500, 74.4, 70.5, 513, 367, 755]");
