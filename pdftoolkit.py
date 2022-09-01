#-*- coding:utf-8 -*-
#!/usr/bin/env python
import os
from pdf2image import convert_from_path
from pdf2docx import Converter
from easygui import fileopenbox,filesavebox,msgbox,diropenbox
from PyPDF4 import PdfFileMerger,PdfFileReader,PdfFileWriter

# pdf转换成docx文档
def py_pdf2docx():
    # 选择pdf文件的路径
    pdf_file = fileopenbox(title='PDF编辑器V1.0', msg='请选择需要转换的PDF文件', default='*.PDF')
    # 防止传参为空
    if pdf_file != None:
        # 选择所需要保存的文件路径，默认保存的文件名为当前路径+save.docx
        docx_file = filesavebox(title='PDF编辑器V1.0',msg='请选择需要保存的路径',default='save.docx')
        # 防止传参为空
        if docx_file != None:
            # PDF转换成DOCX
            cvt = Converter(pdf_file)
            cvt.convert(docx_file,start=0,end=None)
            cvt.close()
        else:
        
            print('docx_file error!')
    else:
    
        print('filepath error!')
if __name__ == '__main__':
    print('py_pdf2docx!')

# PDF转换成PNG图片
def py_pdf2img():
    pdf_file = fileopenbox(title='PDF文档编辑器',msg='请选择PDF文件！',default='*.PDF')
    print(pdf_file)
    if pdf_file is not None:
        # DPI，默认200 
        picture = convert_from_path(pdf_path=pdf_file, dpi=200,poppler_path='C:\\poppler-0.68.0\\bin')
        for i in range (len(picture)):
            print(i)
            # 判断是否存在目录images
            if os.path.exists('images'):
                picture[i].save('images\\pic_%s.png' % (i+1),'PNG')
            else:
                os.mkdir('images')
                picture[i].save('images\\pic_%s.png' % (i+1),'PNG')
    else:
        msgbox(title='PDF文档编辑器',msg='PDF文档选择错误，请确认！')

if __name__ == '__main__':
    print('py_pdf2img!')

# 合并PDF文件
def py_combpdf():
    # 利用easygui模块确定传入的参数
    pdflist = fileopenbox(title='PDF编辑器V1.0', msg='请选择需要转换的PDF文件', default='*.PDF', multiple=True)
    outfile = filesavebox(title='PDF编辑器V1.0',msg='请选择需要保存的路径',default='savefile.PDF')
    # 判断一下传入的参数是否为空,为空则取消合并操作
    if pdflist is not None and outfile is not None:
        pdfcomb = PdfFileMerger()
        # 合并多个PDF文档
        for n in pdflist:
            # 增加import_bookmarks参数防止报错
            pdfcomb.append(open(n, 'rb'),import_bookmarks=False)
        # 写入PDF文档
        with open(outfile,'wb+') as combiner:
            pdfcomb.write(combiner)
            combiner.close()
    else:
        print('file path error!')
if __name__ == '__main__':
    print('py_combpdf!')


# 拆分PDF文件
def py_splitpdf():
    # PDF文件拆分，暂时不支持多选
    pdffile = fileopenbox(title='PDF编辑器V1.0', msg='请选择需要拆分的PDF文件', default='*.PDF', multiple=False)
    savedir = diropenbox(title='PDF编辑器V1.0', msg='请选择需要保存的路径')
    # 传入的路径不允许为空
    if pdffile is not None and savedir is not None:
        # 对需要拆分的文件进行IO操作
        with open(pdffile,'rb') as input_file:
            output_file = PdfFileReader(input_file)
            # 获取文件页数
            total_page = output_file.getNumPages()
            # 获取拆分的文件名
            input_filename = os.path.split(pdffile)[-1].upper()
            # 拆分文件代码循环体
            for k in range(total_page):
                # 感觉像是库的bug，每次都需要初始化
                output_file = PdfFileReader(input_file)
                # 拆分后保存的PDF文件名称
                output_filename = input_filename.split('.PDF')[0] + '_' + str(k+1) + '.PDF'
                pdfwriter = PdfFileWriter()
                
                pdfwriter.addPage(output_file.getPage(k))
                output_filepath = savedir + '\\' + output_filename
                # 拆分文件保存
                with open(output_filepath,'wb') as filesaver:
                    pdfwriter.write(filesaver)
    else:
        print('file error !')

if __name__ == '__main__':
    print('py_splitpdf!')
