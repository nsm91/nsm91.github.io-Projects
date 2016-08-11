#Neil Mudjer
#Python Project - Prompt 1
#GES 393 Summer 2016

import arcpy

arcpy.env.workspace='F:/Python_NSMudjer'

#Parameters 
proj=arcpy.GetParameterAsText(0)
clip=arcpy.GetParameterAsText(1)
gdb=arcpy.GetParameterAsText(2)

fclist=arcpy.ListFeatureClasses()

arcpy.CreateFileGDB_management(arcpy.env.workspace,gdb)

for fc in fclist:
    output = fc.replace('.shp','_proj.shp')
    arcpy.Project_management(fc,output,proj)

    output1 = output.replace('.shp', '_clip')
    arcpy.Clip_analysis(output,clip,arcpy.env.workspace+'/'+gdb+'/'+output1)
