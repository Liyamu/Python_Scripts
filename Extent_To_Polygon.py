# -*- coding: utf-8 -*-
"""
Create Polygon from Map Extent (with Data Driven pages in mind)
Created on Fri Jul 26 10:00:37 2019

@author: ln83883
Adapted and modified from script on web
Original Web source:  https://community.esri.com/thread/40486

Description:

This function creates a polygon feature class matching the extent of the
first data frame of an input MXD.








Built in WKTs:
    "WGS_1984"-->  Geographic coordinate system: WGS 1984
    "UTM_15N" -->  Projected Coordinate system: WGS 1984 UTM Zone 15N
    "UTM_16N" -->  Projected Coordinate system: WGS 1984 UTM Zone 16N
    "UTM_17N" -->  Projected Coordinate system: WGS 1984 UTM Zone 17N

Method:  1) extract extent from data frame
         2) create an array
         3) convert array into polygon feature class
"""



import arcpy
from arcpy import env
from arcpy import mapping

# Set environment settings
wksp = r"C:\Path\to\folder"
wksp = env.workspace = r"C:\path\to\geodatabase.gdb"
arcpy.env.overwriteOutput = True

# Define Input, output
mxd = r"C:\path\to\input\map_file.mxd"
OutputPolygon = r"C:\path\to\create\new_polygon.shp"

def Extent_to_Polygon( mxd, OutputPolygon, WKT="WGS_1984" ):
    """
    Extracts the extent of the first dataframe in an mxd, and outputs a matching
    polygon feature class.
    """
    if WKT == "WGS_1984":
        WKT = '''GEOGCS['GCS_WGS_1984',DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137,298.257223563]],PRIMEM["Greenwich",0],UNIT["Degree",0.017453292519943295]]'''

    elif WKT == "UTM_15N":
        WKT = WKT = '''PROJCS["WGS_1984_UTM_Zone_15N",GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137,298.257223563]],PRIMEM["Greenwich",0],UNIT["Degree",0.017453292519943295]],PROJECTION["Transverse_Mercator"],PARAMETER["latitude_of_origin",0],PARAMETER["central_meridian",-93],PARAMETER["scale_factor",0.9996],PARAMETER["false_easting",500000],PARAMETER["false_northing",0],UNIT["Meter",1]]'''

    elif WKT == "UTM_17N":
        WKT = '''PROJCS["WGS_1984_UTM_Zone_17N",GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137,298.257223563]],PRIMEM["Greenwich",0],UNIT["Degree",0.017453292519943295]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",500000],PARAMETER["False_Northing",0],PARAMETER["Central_Meridian",-81],PARAMETER["Scale_Factor",0.9996],PARAMETER["Latitude_Of_Origin",0],UNIT["Meter",1]]'''

    elif WKT == "UTM_16N":
        WKT = '''PROJCS["WGS 84 / UTM zone 16N",GEOGCS["WGS 84",DATUM["WGS_1984",SPHEROID["WGS 84",6378137,298.257223563,AUTHORITY["EPSG","7030"]],AUTHORITY["EPSG","6326"]],PRIMEM["Greenwich",0,AUTHORITY["EPSG","8901"]],UNIT["degree",0.0174532925199433,AUTHORITY["EPSG","9122"]],AUTHORITY["EPSG","4326"]],PROJECTION["Transverse_Mercator"],PARAMETER["latitude_of_origin",0],PARAMETER["central_meridian",-87],PARAMETER["scale_factor",0.9996],PARAMETER["false_easting",500000],PARAMETER["false_northing",0],UNIT["metre",1,AUTHORITY["EPSG","9001"]],AXIS["Easting",EAST],AXIS["Northing",NORTH],AUTHORITY["EPSG","32616"]]'''

    # Set output coordinate system
    arcpy.env.outputCoordinateSystem = WKT

    # Extract mxd name from path
    mxd_Name = mxd.split('\\')
    mxd_Name = str(mxd_Name[-1:]).split('.')
    mxd_Name = str(mxd_Name[0]).strip("\['")

    ## Create spatial reference object to use as parameter in tools
    # Point to projection file .prj
    #prjfile = "" # Point to projection file .prj
    #SpatRef = arcpy.SpatialReference(prjfile) # not currently used in script

    # Load Data
    mxd = mapping.MapDocument(mxd)
    msg = "\n" + "Loading " + mxd_Name + ".mxd..."
    print(msg)
    arcpy.AddMessage(msg)

    # Select data frame
    dataframe = mapping.ListDataFrames(mxd, "*")[0]
    msg = "\n" + "Selecting data frame from " + mxd_Name + ".mxd..."
    print(msg)
    arcpy.AddMessage(msg)

    # Extract Data Frame extent
    frameExtent = dataframe.extent
    msg = "\n" + "Extracting extent from dataframe..."
    print(msg)
    arcpy.AddMessage(msg)

#    # Get spatial reference object from data frame
#    SR = dataframe.spatialReference(
#
#    dataframe.spa
    ## Describe objects work on GDB FeatureClass, FeatureClass Table, Dataset
    ## Create describe obj
    #dsc = arcpy.Describe()
    ## Extract spatial reference
    #coord_sys = dsc.spatialReference
    ## Define projection
    #arcpy.DefineProjection_management(in_dataset, coord_sys)


    ## OPTION 1) BUILD POLYGON MANUALLY:
    ## Building polygon
    #XMAX = frameExtent.XMax
    #XMIN = frameExtent.XMin
    #YMAX = frameExtent.YMax
    #YMIN = frameExtent.YMin
    #pnt1 = arcpy.Point(XMIN, YMIN)
    #pnt2 = arcpy.Point(XMIN, YMAX)
    #pnt3 = arcpy.Point(XMAX, YMAX)
    #pnt4 = arcpy.Point(XMAX, YMIN)
    #array = arcpy.Array()
    #array.add(pnt1)
    #array.add(pnt2)
    #array.add(pnt3)
    #array.add(pnt4)
    #array.add(pnt1)
    #polygon = arcpy.Polygon(array)

    ## apply Data Frame's coordinate system to extent polygon
    #arcpy.DefineProjection_management( polygon, SR )
    #arcpy.CopyFeatures_management(polygon, r"D:\Liam\Python_Workspace\Houston.shp")

     #OPTION 2) shortcut:
     #create polygon from extent obj

    ExtentPolygon = frameExtent.polygon
    msg = "\n" + "Creating extent polygon..."
    print(msg)
    arcpy.AddMessage(msg)

    polygon = ExtentPolygon
    Poly = arcpy.CopyFeatures_management(polygon, OutputPolygon)
    msg = "\n" + "Extent polygon saved to: " +  OutputPolygon
    print(msg)
    arcpy.AddMessage(msg)
    msg = "\n" + "Process complete."
    print(msg)
    arcpy.AddMessage(msg)

Extent_to_Polygon( mxd, OutputPolygon, "UTM_15N" )
