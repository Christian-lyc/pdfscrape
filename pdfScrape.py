# -*- coding: utf-8 -*-
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.layout import *
from pdfminer.converter import PDFPageAggregator
import os
from glob import glob





def process(filename):
    fp = open(filename, 'rb')
    parser = PDFParser(fp)
    document = PDFDocument(parser)
    if not document.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        rsrcmgr = PDFResourceManager()
        device = PDFPageAggregator(rsrcmgr, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(document):
            interpreter.process_page(page)
        # receive the LTPage object for this page
            layout=device.get_result()
            for x in layout:
                # print(x.get_text())
                if (isinstance(x, LTTextBoxHorizontal)):
                    with open(pdfname + '.txt', 'ab') as f: # ab是覆盖接着原来的文档写入，wb是清空原来文档

                        f.write(x.get_text().encode('utf-8') + b'\n')






if __name__ == "__main__":
    dir_path='C:/Users/Deep Learning/Desktop/new/fold'
    fold_list = glob(os.path.join(dir_path, '*'))
    for Pdf_fold_no in fold_list:
        pdf_list = glob(os.path.join(dir_path, Pdf_fold_no, '*.pdf'))
        for pdfno in pdf_list:
            index = pdfno.rfind('.')
            pdfname = pdfno[:index]
            datename = pdfno[-10:-4]
            # print(datename)
            print(pdfno)
            process(pdfno)
