# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Generate_Tesselation_raw.py
# Created on: 2019-03-19 10:21:26.00000

'''Description: This Function generates multiple tessellations by user-defined sizes
 In addition to generated the tesselations, it will return a report as a STRING
 ---------------------------------------------------------------------------


def GenerateMultipleTesselations(
        wksp,  # output location
        extent, 
        output_projection,
        shape, # choices are HEXAGON, TRIANGLE, SQUARE
        sizes, # List of tessellation unit sizes to generate 
        units, # Default is SquareMiles
        )

EXAMPLE CODE with func in use:
    
# Set Function Parameters:
       
output_wksp = r"C:/DATA/DOGAMI_CASCADIA/Project_Data/Geodatabases/Rasters.gdb"
extent = "533168.276916504 1134378.34710693 1028137.89367677 1506103.69970703"
output_projection = "PROJCS['NAD_1983_HARN_Oregon_Statewide_Lambert_Feet_Intl',GEOGCS['GCS_North_American_1983_HARN',DATUM['D_North_American_1983_HARN',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Lambert_Conformal_Conic'],PARAMETER['False_Easting',1312335.958005249],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-120.5],PARAMETER['Standard_Parallel_1',43.0],PARAMETER['Standard_Parallel_2',45.5],PARAMETER['Latitude_Of_Origin',41.75],UNIT['Foot',0.3048]];-118489100 -97381100 3048;-100000 10000;-100000 10000;3.28083989501312E-03;0.001;0.001;IsHighPrecision"

# tessellation shape (HEXAGON, TRIANGLE, SQUARE)
Shape = "HEXAGON"
#Shape = "TRIANGLE"
#Shape = "SQUARE" 

# List of tessellation unit sizes to be generated
Unit_Sizes_LST = ["175","200"]
Units = "SquareMiles"


#Body

string = GenerateMultipleTesselations(
        output_wksp,
        extent,
        output_projection,
        Shape,
        Unit_Sizes_LST,
        Units,
        )
print(string)

'''
# Import arcpy module
import arcpy




# Generate Multiple Tessellations Function
def GenerateMultipleTesselations(output_wksp,extent,output_projection,tessellation_shape,unit_sizes,area_units):

    def LetsTessellate(wksp,extent,output_projection,shape,sizes,units):
        
        arcpy.env.workspace = wksp
        arcpy.env.overwriteOutput = True
        
        SizeLST = []
        Output_File_Name = wksp
        Output = Output_File_Name
        PrintLST = []
        GT_LST = []


        # PREP

        # preparing Units string for adding to Unit_Sizes_LST
        Unit_Glue = " " + Units +","
        
        # Joining prepped units to list
        string = Unit_Glue.join(Unit_Sizes_LST)
        # Creating new updated list from string
        SizeLST = string.split(",")
        
        # Remove last item of list and replace with updated item
        string = SizeLST.pop()
        string = string + " " + Units
        SizeLST.append(string)
        
        count = 0
        unitSize = []
        
        
        # Body
        ## loop through unit sizes
        for size in range(len(SizeLST)):
            unitSize = SizeLST[size]
            
            GT = "GT_" + Unit_Sizes_LST[count] + "mile"
            GT = Output + "/" + GT
            GT_LST.append(GT)
            PrintLST.append(
                    "Generated " + unitSize[:-1] 
                    + " " + Shape.lower() + " tessellations:")
            
            # Run Generate Tessellation
            arcpy.GenerateTessellation_management(
                    GT,
                    extent,  # extent or FC to get extent from
                    Shape,  # tessellation shape (HEXAGON, TRIANGLE, SQUARE)
                    unitSize,        
                    output_projection
                    )
            count += 1
        DICT = {'a':PrintLST,'b':GT_LST}  
        return DICT
        # end of LetsTessellate()
        
    PrintLST = []
    GT_LST = []
#   ReportLST = []
    string = ""
    
    ReportDICT = LetsTessellate(
            wksp,
            extent,
            output_projection,
            Shape,
            Unit_Sizes_LST,
            Units,
            )
    
    PrintLST = ReportDICT['a']
    GT_LST = ReportDICT['b']
    count = 0
    
    for i in range(len(GT_LST)):
        string = (string + (PrintLST[count] + "\n" + GT_LST[count]) +"\n\n")
        count += 1
    return string










# Body Example


# Set Function Parameters:
       
output_wksp = r"C:/DATA/DOGAMI_CASCADIA/Project_Data/Geodatabases/Rasters.gdb"
extent = "533168.276916504 1134378.34710693 1028137.89367677 1506103.69970703"
output_projection = "PROJCS['NAD_1983_HARN_Oregon_Statewide_Lambert_Feet_Intl',GEOGCS['GCS_North_American_1983_HARN',DATUM['D_North_American_1983_HARN',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Lambert_Conformal_Conic'],PARAMETER['False_Easting',1312335.958005249],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-120.5],PARAMETER['Standard_Parallel_1',43.0],PARAMETER['Standard_Parallel_2',45.5],PARAMETER['Latitude_Of_Origin',41.75],UNIT['Foot',0.3048]];-118489100 -97381100 3048;-100000 10000;-100000 10000;3.28083989501312E-03;0.001;0.001;IsHighPrecision"

# tessellation shape (HEXAGON, TRIANGLE, SQUARE)
shape = "HEXAGON"
#Shape = "TRIANGLE"
#Shape = "SQUARE" 

# List of tessellation unit sizes to be generated
Unit_Sizes_LST = ["175","200"]
Units = "SquareMiles"


#Body

string = GenerateMultipleTesselations(
        output_wksp,
        extent,
        output_projection,
        shape,
        Unit_Sizes_LST,
        Units,
        )
print(string)