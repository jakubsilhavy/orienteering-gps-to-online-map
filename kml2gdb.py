import os
import arcpy
inDir = r"c:\Users\jsilhavy\Documents\OB\Treninky\0912_Naves\GPS"
outDir = r"c:\Users\jsilhavy\Documents\OB\Treninky\0912_Naves\GPS" + "\\" #+ "gdb" + "\\"
shp_listDir = os.listdir(inDir)
for myKML in shp_listDir:
  if myKML[-4:] == ".kml":
    inKML = inDir + "\\" +  myKML
    outKML = myKML[:-4]
    arcpy.KMLToLayer_conversion(in_kml_file=inKML, output_folder=outDir, output_data=outKML, include_groundoverlay="NO_GROUNDOVERLAY")