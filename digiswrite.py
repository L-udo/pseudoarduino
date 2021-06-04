orig_file = open("payload.txt", "r")
digis_file = open("Payload.ino", "x")

digis_file.write('#include "DigiKeyboard.h"\nvoid setup() {}\n')


digis_file.write("void loop() {\n" ) 


cmdkeys = ["WIN","WIN+","CTRL+","ENTER","SHIFT+","ALT+","TAB",]

for x in orig_file:
    if x.strip("\n") == "WIN":
        print("WIN")
        digis_file.write("DigiKeyboard.sendKeyStroke(MOD_GUI_LEFT);\n")

    elif "WIN+" in x:
        x = x.strip("WIN+").strip("\n")
        digis_file.write("DigiKeyboard.sendKeyStroke(KEY_{},MOD_GUI_LEFT);\n".format(x))
   
    elif "ENTER" in x:
        digis_file.write("DigiKeyboard.sendKeyStroke(KEY_ENTER,MOD_GUI_LEFT);\n")
   
    else:
        digis_file.write('DigiKeyboard.println("{}");\n'.format(x.strip("\n")))


digis_file.write("}") 
