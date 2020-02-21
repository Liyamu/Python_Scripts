import arcpy
import arcpy.sa
#import os
# -*- coding: utf-8 -*-



#======PREP====================================================================

# Set environments

wksp = r"C:\DATA\SCRATCH\MURALS\SEA"

# Output location to bombard with the generated kernel density files

scratch_wksp = r"C:\DATA\SCRATCH\MURALS\SEA"

arcpy.env.workspace = wksp
arcpy.env.overwriteOutput = True
buff = ""
arcpy.env.mask = buff
## create output folder
#
#out_folder_path = scratch_wksp
#out_name = "PDX_Murals_v2_NAD83"
#
## Execute CreateFolder
#
#arcpy.CreateFolder_management(out_folder_path, out_name)
#outPath = out_folder_path + "\\" + out_name
#
## Create Textfile for filename codes
#FileNames = open("KD_filename_codes.txt", "w+")
#FileNames.close()

# Import data (points or lines)
in_features = r"C:\DATA\SCRATCH\MURALS\SEA\S_mur.shp"

# Open data
FC = arcpy.MakeFeatureLayer_management( in_features, "FC")
## Input symbology LRY file (optional) ##currently not implemented
symbology = r""

#======Set Kernel Density parameters===========================================

#____population_field____values to be itterated (via PopulationFieldLST):
PF_1 = "None" # (DEFAULT)
PF_2 = ""
if PF_2 == "":
    PopulationFieldLST = [ PF_1 ]
else:
    PopulationFieldLST = [ PF_1, PF_2 ]
    
population_field = PF_1

#____cell_size____values to be itterated (via CellSizeLST):
#CS_1 = 2.40164799737113E-04 #this was ideal for PDX
#CS_2 = 5.40164799737113E-04 #this was close for PDX, but less smooth
#CS_3 = ""
#CS_4 = ""
CS_5 = 50

CellSizeLST = [ CS_5 ]
               
#____search_radius____values to be itterated (via SearchRadiusLST):
SR_1 = 2000.0 #0.011444717952015479 feet
SR_2 = 3000.0 #1682.7516866245599 #SF's calculated search radius for outputcellsize 1
SR_3 = 4000.0 #"2959.9154249369935" #feet SEA's calculated search radius for outputcellsize 1
SR_4 = 5000.0 #""
SR_5 = 6000.0 #""

SearchRadiusLST = [ SR_1, SR_2, SR_3, SR_4, SR_5 ]

#____area_unit_scale_factor____ values to be itterated (via AreaUnitScaleFactorLST):
#AUSF_1 = "SQUARE_MAP_UNITS"
#AUSF_2 = "SQUARE_MILES"
#AUSF_3 = "SQUARE_KILOMETERS"
#AUSF_4 = "ACRES"
#AUSF_5 = "HECTARES"
#AUSF_6 = "SQUARE_YARDS"
AUSF_7 = "SQUARE_FEET"
#AUSF_8 = "SQUARE_INCHES"
#AUSF_9 = "SQUARE_METERS"
#AUSF_10 = "SQUARE_CENTIMETERS"
#AUSF_11 = "SQUARE_MILIMETERS"

AreaUnitScaleFactorLST = [ AUSF_7 ]
area_unit_scale_factor = AUSF_7
#____out_cell_values____values to be itterated (via OutCellValuesLST):
OCV_1 = "DENSITIES" # (DEFAULT)
#OCV_2 = "EXPECTED_COUNTS"

OutCellValuesLST = [ OCV_1 ]
out_cell_values = OCV_1

#____Method____values to be itterated (via MethodLST):
M_1 = "PLANAR"
#M_2 = "GEODESIC" 

MethodLST = [ M_1 ]
method = M_1

#____END OF NEEDED USER INPUT__________________________________________________


# Create output filename lists
KernelNameLST = []
kernelName = "nothing_yet"

# Create describe object
desc = arcpy.Describe(in_features)

# extract file name

fcName = str(desc.name)
fcName = fcName[:3]

# cell_size handled in loop
# search_radius handled in loop

#======BODY==============================================


# check out Spatial Analyst license
arcpy.CheckOutExtension("SPATIAL")

# loop through  every permutation of the two lists
counter = 0

# loop through cell sizes
for size in range(len(CellSizeLST)):
    
    cell_size = CellSizeLST[size]
    CSname = "CS_" + str(cell_size)
    CSname = CSname[:10]
 
    # loop through search radii
    for radius in range(len(SearchRadiusLST)):
        counter = counter + 1

        search_radius = SearchRadiusLST[radius]
        SRname = "_SR_" + str(search_radius)
        SRname = SRname[:11]
                        
        # generate name for current itteration
        kernelName = "KD_" + str(counter) #+ "_" + fcName ## + "_" + CSname + SRname
        KernelNameLST.append(str(kernelName))
        print(kernelName + " cell size: " + str(cell_size) + " search radius: " + str(search_radius) )

#print( "in_features: " + in_features)
#print( "population_field:" + population_field)
#print( "cell_size:" + str(cell_size))
#print( "search_radius:" + str(search_radius))
#print( "area_unit_scale_factor:" + area_unit_scale_factor)
#print( "out_cell_values:" + out_cell_values)
#print("")
#
#        # Create buffer to be used as a processing mask, using the search radius
#        buff = arcpy.Buffer_analysis(FC, str(FC) + "_buff", search_radius)
#        arcpy.Buffer_analysis( FC , fcName + "_buff" , "2 miles" ,"","", "ALL")
#        arcpy.env.mask = buff
        
        # Run Kernel Desnity with itteration's parameters
        #kernelName = arcpy.CreateUniqueName(kernelName)
        OutPath = scratch_wksp + "\\" + kernelName
       
        KD = ""
        
#        # Save itteration details to filename code TXT file
#        FileNames=open("KD_filename_codes.txt", "a+")
#        FileNames.write("")
#        FileNames.write(kernelName + ":")
#        FileNames.write("in_features: " + in_features)
#        FileNames.write("population_field:" + population_field)
#        FileNames.write("cell_size:" + str(cell_size))
#        FileNames.write("search_radius:" + str(search_radius))
#        FileNames.write("area_unit_scale_factor:" + area_unit_scale_factor)
#        FileNames.write("out_cell_values:" + out_cell_values)
#        FileNames.write("")
#        FileNames.close()
#        
#        print(OutPath)
        
        KD = arcpy.sa.KernelDensity( FC,
                                  population_field,
                                  cell_size,
                                  search_radius,
                                  area_unit_scale_factor,
                                  out_cell_values,
                                  method)
        KD.save(scratch_wksp + kernelName)
        
#        KD = KernelDensity( FC,
#                                       population_field,
#                                       cell_size,
#                                       search_radius,
#                                       area_unit_scale_factor,
#                                       out_cell_values,
#                                       method)
         # Save the output
#        KD.save( scratch_wksp + "\\" + kernelName )
     
#arcpy.gp.KernelDensity_sa("SF_01_Murals_NAD83",
# "NONE",
# "C:/DATA/SCRATCH/SCRATCH.gdb/KernelD_SF_01",
# "2.40164799737113E-04",
# "", "SQUARE_MILES",
# "DENSITIES",
# "PLANAR")

'''
format options:
    
TIFF —TIFF format
Cloud Optimized GeoTIFF —Cloud Optimized GeoTIFF format
IMAGINE Image —ERDAS IMAGINE
BMP —BMP format
GIF —GIF format
PNG —PNG format
JPEG —JPEG format
JPEG2000 —JPEG 2000 format
Esri Grid —Esri Grid format
Esri BIL —Esri BIL format
Esri BSQ —Esri BSQ format
Esri BIP —Esri BIP format
ENVI —ENVI format
CRF —CRF format
MRF —MRF format
'''

# relinquish Spatial Analyst license
        
arcpy.CheckInExtension("SPATIAL")  
        
print("done!")
# append code to loop through and apply same symbology to all generated files
