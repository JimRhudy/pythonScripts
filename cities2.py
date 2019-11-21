import arcpy
from arcpy import env
env.workspace = r"H:\PythonGIS\Rhudy\arcpy\us_major_cities"
env.overwriteOutput = True

fc = "us_major_cities.shp"
where = "CAPITAL" == 'State'
print where

##rows = arcpy.SearchCursor(fc) # rows now cursor object
###row = rows.next() # next method called from cursor object which returned row object
##
##
##with arcpy.da.UpdateCursor(fc, ("CAPITAL")) as cursor:
##    for row in cursor:
##        ro[0] = "capital"
##
#print "average population is " + str(float(totalPop/rowCount))