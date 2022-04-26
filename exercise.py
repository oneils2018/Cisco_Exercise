#Stephen O'neil cisco lab

import os

print("Starting program...")

cmd = ""

while cmd != 'Q' and cmd != 'q':
   cmd = input("Enter one of the following commands: Print current device list (D)\n Create loopback services for devices (L)\n Delete loopback service (R)\n quit (Q)")
    if cmd == 'D' or cmd == 'd':
      print("Beginning active devices name download...")
      os.system("curl -u admin:admin -k -X GET -H \"Accept:application/yang-data+json\" https://10.10.20.50:8888/restconf/data/tailf-ncs:devices/device?fields=name -o names.txt | grep '\\bname\w*\\b' names.txt > out.txt")
      infile= "out.txt"
      outfile = "final.txt"
      names= []
      delete_list = ["name", ":", "\""]
      
      with open(infile) as f, open(outfile, "w+") as fout:
        for line in f:
          for word in delete_list:
            line = line.replace(word,"")
          fout.write(line)
          names.append(line.strip())
       print("Found Devices")
      for i in range(len(names)):
          print(names[i])
     
    
    elif cmd == 'L' or cmd == 'l':
      print("Generating loopback for " + str(len(names)) + " devices")
      
      for i in range(len(names)):
        print("Starting loopback generation for " + names[i] + "...")
        os.system("curl -u admin:admin -k -X PATCH -H \"Content-type:application/yang-data+json\" https://10.10.20.50:8888/restconf/data/loopback-service:loopback-service -- data '{\"loopback-service:loopback-service\":[{\"name\":\"" + str(names[i])) + "\",\"device\":\" + str(names[i]) + "\",\"dummy\":\"1.1.1.1\"}]}'")
        print("Finished for " + names[i])
      print("Finished generation loopback instances")
      
   elif cmd == 'R' or cmd == 'r':
    print("Beginning deletion of " + str(len(names__ + " loopbacks")
    for i in range(len(names)):
      os.system("curl -v -u admin:admin -k -X DELETE -H \"Content-Type:application/yang-data+json\" https://10.10.20.50:8888/restconf/data/loopback-service:loopback-service=" + str(names[i]))
    print("loopbacks finished deleting")
                                   
                                         
print("Exiting Program")
                                         
                                         
