# all type of barcode generetor
'''
LIST OF BARCODES
================
Code39
Code128
PZN
EuropeanArticleNumber13
EuropeanArticleNumber8
JapanArticleNumber
InternationalStandardBookNumber13
InternationalStandardBookNumber10
InternationalStandardSerialNumber
UniversalProductCodeA
'''
# imported modules
import sys
import pip
try:
    import barcode
except:
    print('this script need some additional packages:')
    choice = input('do you want to install them ?(y/n) ')
    # installing additional packages
    if choice == 'y' or choice == 'Y' :
        print('installing...')
        pip.main(['install','python-barcode'])
        pip.main(['install','pillow'])
    else:
        sys.exit()

finally:
    # print the top logo
    def ascii_Art():
        print(" ║█║▌║█║▌│║▌█║▌║ \nBARCODE-GENERETOR\n")

    # barcode class
    class barcode_generator:
        def __init__(self, user_code):
            self.code = user_code
        def generate(self):
            self.ean = barcode.get('ean13', self.code)
            print('+----------------------+'+'\n| GENERATE SUCESSFULLY |'+'\n+----------------------+')
            self.filename = self.ean.save('barcode')

    ascii_Art()

    # if run as a script
    if __name__ == '__main__':
        bcd_code = input('ENTER THE CODE: ')
        try:
            bcd_obj = barcode_generator(bcd_code)
            bcd_obj.generate()
        except:
            print("ERROR")
        else:
    	    sys.exit()