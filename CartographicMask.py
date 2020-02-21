# -*- coding: utf-8 -*-
import arcpy, os

"""
Created on Thu Apr 18 23:15:37 2019

@author: LiamNB

Description: This function will get the current extent from the 




Highlight_Feature: feature to remain unmasked
Features_to_dissolve_into_mask: list of features to combine, disolve, and cut
to fit around the highlight feature


"""

wksp = r"C:\DATA\SCRATCH\Python_scratch"
Highlight_FC = 'FC.shp'
out_fc = 'HF_Mask'

H_FC = Highlight_FC
arcpy.env.outputCoordinateSystem = H_FC
out_fc = os.path.join(wksp,'HF_Mask')

arcpy.env.workspace = wksp
arcpy.env.overwriteOutput = True

arcpy.da.CreateFeatures_management(
        
#  Union_analysis (
#in_features, 
#out_feature_class, 
#{join_attributes}, 
#{cluster_tolerance}, 
#{gaps}
#)

#mxd = arcpy.mapping.MapDocument("CURRENT") # If in python window
mxd = arcpy.mapping.MapDocument(r"C:\DATA\SCRATCH\Python_scratch\map.mxd")
 
mxd.save() # no parameters
mxd.filePath 


df = arcpy.mapping.ListDataFrames(mxd,"Layers")[0] 
# index refers to which dataframe in the TOC to use
df2 = arcpy.mapping.ListDataFrames(mxd)[1]
#can use wildcards
df = arcpy.mapping.ListDataFrames(mxd,"Lay*")[0]  

lyrFile = arcpy.mapping.Layer(r"C:\DATA\SCRATCH\Python_scratch\rivers.lyr.mxd")



# arcpy.mapping.AddLayer(data_frame,add_layer,{add position in TOC})
arcpy.mapping.AddLayer(df, lyrFile)

arcpy.mapping.ExportToPDF(mxd, r"C:\map1.pdf")

lyr = arcpy.mapping.ListLayers(mxd)[0] #without index, it would return as 
# a list instaed of a lyr object

lyr.name = "some new name"

lyr.visible = False
lyr.visible = True

# arcmap doesn't constantly refresh, so not all changes will show, until:
arcpy.RefreshTOC()
arcpyRefreshActiveView()

lyrExtent = lyr.getSelectedExtent()
df.extent = lyrExtent


df_list = arcpy.mapping.ListDataFrames(mxd)
for frame in range(len(df_list)):
    print df_list[frame]

#The data frame extent coordinates are based on the extent of the data frame 
#in Layout View, not in Data View. 

#ListLayers (map_document_or_layer, {wildcard}, {data_frame})
#data_frame object --> so only list layers in that df
    
extent = df.extent

import arcpy
mxd = arcpy.mapping.MapDocument(r"C:\Project\Project.mxd")
df = arcpy.mapping.ListDataFrames(mxd, "Transportation")[0]
lyr = arcpy.mapping.ListLayers(mxd, "Accidents", df)[0]
#The DataFrame extent object is converted into a polygon feature so it can be used with the SelectLayerByLocation function.
dfAsFeature = arcpy.Polygon(#arcpy.Array,df.spatialReference)
        arcpy.Array(
                [df.extent.lowerLeft, 
                 df.extent.lowerRight, 
                 df.extent.upperRight, 
                 df.extent.upperLeft]),
    
                            df.spatialReference)
    
arcpy.SelectLayerByLocation_management(lyr, "INTERSECT", dfAsFeature, "", "NEW_SELECTION")
mxd.save()
    

import os, arcpy

infc = r"C:\Users\User\GIS\single_section.shp"
polygons = r"C:\Users\User\GIS\polygons.shp"

spatialref = arcpy.Describe(infc).spatialReference

if arcpy.Exists(polygons):
 arcpy.Delete_management(polygons)
 
arcpy.CreateFeatureclass_management(*os.path.split(polygons), geometry_type="Polygon", spatial_reference=spatialref.factoryCode)

icursor = arcpy.da.InsertCursor(polygons, ["SHAPE@"])

TLX = -104.357483001
TLY = 32.2242740047
TRX = -104.341346746
TRY = 32.2241446297
BRX = -104.356403497
BRY = 32.2233637742
BLX = -104.357479189
BLY = 32.2233727547

array = arcpy.Array()
array.add(arcpy.Point(TLX,TLY))
array.add(arcpy.Point(TRX,TRY))
array.add(arcpy.Point(BRX,BRY))
array.add(arcpy.Point(BLX,BLY))
array.add(arcpy.Point(TLX,TLY))


polygon = arcpy.Polygon(array,spatialref)

icursor.insertRow([polygon])