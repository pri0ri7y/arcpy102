#Custom Print service for Resource Proxy
##ARCPY101

Project | Ref 
--- | --- 
ArcPy| ARCPY101

Printing maps that contain secured services 
http://resources.arcgis.com/en/help/main/10.1/index.html#//0154000005q3000000

Due to a bug in ArcGIS server 10.2 (sp1) & 10.2.2, the <a href="http://forums.iis.net/t/1122937.aspx" target="_blank">resource proxy</a> will not handle the token for secured services during print task.

This tool is designed as a workaround to the bug mentioned above.

###Deployment
----------------
1.  Download and extract the package.
2.  Reference the extracted folder in ArcMap.
3.  Open addtoken.py in IDE, modify the server configurations and save the file.
4.  Reference addToken.py to Insert Token to Webmap JSON tool.
5.  Open the CustmPrint model and check for basic intelinking of tools & parameters (you can even change the reference of Export Web Map to your server's Export Web Map).
6.  Save the model and close ModelBuilder.
7.  Double-click on the CustomPrint Model to open the dialogue.
8.  Change the Input JSON as appropriate. Click OK.
9.  After it gets executed , publish as a GP service.




