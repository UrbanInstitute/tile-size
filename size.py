import json
import numpy
import config

def bytesToGB(bytes):
	return str(round(bytes/(1024*1024*1024),3)) + "GB"
def bytesToMB(bytes):
	return str(round(bytes/(1024*1024),3)) + "MB"

sizes = {"datatools": [] }
datatoolsSessions = ["data/datatools/top-bottom1.json", "data/datatools/top-bottom2.json", "data/datatools/immigration.json", "data/datatools/shotspotter.json"]
for f in datatoolsSessions:
	with open(f) as data_file:    
		data = json.load(data_file)
		for e in data["log"]["entries"]:
			url = e["request"]["url"]
			if ".png" in url:
				size = e["response"]["content"]["size"]
				if size != 0:
					sizes["datatools"].append(size)
datatoolsTileSize = numpy.mean(sizes["datatools"])
datatoolsViewSize = datatoolsTileSize/15.0 #a "mapbox view" if defined as 15 tiles
datatoolsPeakHourlyLoad = datatoolsViewSize * config.hourly #hourly spike on July 6 from 2-3pm
datatoolsMonthlyLoad = config.monthly * datatoolsViewSize #million views in the past 30 days

print "Average tile size: " + str(datatoolsTileSize) + " bytes"
print "Average monthly data usage: " + bytesToGB(datatoolsMonthlyLoad)
print "Peak hourly data usage: " + bytesToMB(datatoolsPeakHourlyLoad)




