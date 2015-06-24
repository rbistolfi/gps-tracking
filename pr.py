f = open( 'gpsfile/JRNX_2013-04-07_08-04-30_ORG_  86_5129.csv', 'r')

allData = f.readlines()
m = False
zone = []
zonetrue = []
b = []
for i in range (50):
	zonetrue.append(i)

for al in allData:
	try:
	
		if m:
			
			tmpnum = al.split(";")[3]
			num = tmpnum.split(":")[1]
			zone.append(int(num))
		if al.startswith('InfosChronos') :
			m = True
	except:
		pass


print zone
print zonetrue


b = list(set(zonetrue) - set(zone))
print b