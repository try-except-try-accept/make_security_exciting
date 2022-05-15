
from os import listdir


def files_to_hex():

    for f in listdir():

        if f.endswith("py") or f.endswith("hex"):
            continue

        with open(f, "rb") as ransom:
            fn, ext = f.split(".")
            bina = "".join([bin(b)[2:].zfill(8) for b in ransom.read()])
            den = int(bina, 2)
           
            with open(ext+".hex", "w") as hexfile:

                hexfile.write(hex(den)[2:])

                print("converted", ext)     

def hex_to_files():

    for f in listdir():

        if f.endswith(".hex"):

            with open(f) as hexfile:
                hex_data = hexfile.read().strip()

            ext, _ = f.split(".")

     
            
            with open("test_reload."+ext, "wb") as bin_file:

                byte_data = bytearray()
                byte = ""
                for nibble in hex_data:
                    byte += bin(int(nibble, 16))[2:].zfill(4)
                    
                    if len(byte) == 8:
                        this_byte = int(byte, 2)
                        byte_data.append(this_byte)
                                            
                        byte = ""

                bin_file.write(byte_data)

                input("finished with " + ext)
                    

