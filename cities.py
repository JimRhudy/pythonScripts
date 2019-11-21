import arcpy
from arcpy import env
env.workspace = r"H:\PythonGIS\Rhudy\arcpy\us_major_cities"
env.overwriteOutput = True

fc = "us_major_cities.shp"

rows = arcpy.SearchCursor(fc) # rows now cursor object
#row = rows.next() # next method called from cursor object which returned row object

totalPop = 0
rowCount = 0

with arcpy.da.SearchCursor(fc, ("NAME", "POPULATION")) as cursor:
    for row in cursor:
        totalPop += row[1]
        rowCount += 1.0

print "average population is " + str(float(totalPop/rowCount))
        


##
##for row in rows:
##    #print row.getValue(fieldName)
##    totalPop = totalPop + row.getValue(fieldName)
##    rowCount = rowCount + 1
##

##    
    

