#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      rsilc
#
# Created:     12/09/2022
# Copyright:   (c) rsilc 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from pdf2docx import Converter

pdf_file = 'PROFILE_.pdf'

doc_file= 'OUT_PDF2WORD.docx'



def main():
    print("LEYENDO PDF")
    c=Converter(pdf_file)

    c.convert(doc_file)
    c.close()


    print("FIN LEYENDO PDF")


    pass

if __name__ == '__main__':
    main()
