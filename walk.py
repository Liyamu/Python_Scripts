# -*- coding: utf-8 -*-
"""
Created on Sat May 04 00:58:15 2019

@author: Liam Neeley-Brown (on the shoulders of James Manzione)
"""

import arcpy, os

def walk( key, directory, wildcard = None ):
    '''Walks through root DIRECTORY and lists all KEY files
KEY - is the type of data to list (ex: RASTER, TABLE, SHP, MXD)
DIRECTORY - is the root directory for the walk (i.e. the starting point)
WILDCARD - is a pattern to select against in the file name

EX:  walk( 'SHP', r'C:\\', '*BON*' )
*This will capture all SHPs with BON in the title that live on your C drive*
'''
    #Preserve the old workspace
    oldWKSP = arcpy.env.workspace

    #Set the workspace to the directory input
    arcpy.env.workspace = directory

    #Create return list object
    retList = []

    #Check to see if any sub workspaces exist
    lstWKSPs = arcpy.ListWorkspaces()
    if len(lstWKSPs) > 0:
        for wksp in lstWKSPs:
            retList = retList + walk( key , wksp , wildcard )

    if key.upper().strip()  == 'RASTER':
        for raster in arcpy.ListRasters( wildcard ):
            retList.append( os.path.join(directory , raster ) )

    elif key.upper().strip()  == 'TABLE':
        for table in arcpy.ListTables( wildcard ):
            retList.append( os.path.join(directory, table ) )

    elif key.upper().strip() == 'SHP':
        for shp in arcpy.ListFeatureClasses( wildcard ):
            retList.append( os.path.join(directory , shp ) )

    elif key.upper().strip()  == 'MXD':
        for fileName in arcpy.ListFiles( wildcard ):
            if fileName[-3:].lower() == 'mxd':
                retList.append(os.path.join(directory, fileName ) )

#
#    elif key.upper().strip() == 'LYR':
#        for shp in arcpy.ListFeatureClasses( wildcard ):
#            retList.append( os.path.join(directory , lyr ) )
#
#    elif key.upper().strip() == 'PRJ':
#        for shp in arcpy.ListFeatureClasses( wildcard ):
#            retList.append( os.path.join(directory , prj ) )

    arcpy.env.workspace = oldWKSP

    return retList

