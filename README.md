# ReadFromCOM

Ensure to run "!pip install pyserial"  in the console if working with windows anaconda IDE using python 2.7

https://www.anaconda.com/download/

Ensure the that the arduino prints its data like this for example  

#################################### Arduino Code ###############################  


 Serial.print(voltage0);  
 Serial.print(",");  
 Serial.print(voltage1);  
 Serial.print(",");  
 Serial.print(voltage2);  
 Serial.print(",");  
 Serial.println(voltage3); <---only the end of your data should have print new line (println)  
 
###################################################################################  


Change the python script  

#################################### Python script ###############################  

line 34: header = ["voltage0", "voltage1", "voltage2", "voltage3"]  


line 59: row.append(newList[0].strip())  
         row.append(newList[1].strip())  
         row.append(newList[2].strip())  
         row.append(newList[3].strip())<-- have as many as you have data from the arduino  
        
        
###################################################################################  
