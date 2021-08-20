def py_pdf2img(self):
    from pdf2image import convert_from_path
    import os
    import sys
    print(sys.getdefaultencoding())
    #file_path = 'D:\\py_chram\\result\\'
    for file in os.listdir(self):
        if '.pdf' in file:
            print(file)
            #将PDF转换成图片
            try:
            #print(file.split('.')[0])
                convert_pdf2img = convert_from_path(self+file, 300, self, fmt="PNG", output_file=str(file.split('.')[0]), thread_count=4)
            except Exception as e:
                print(e)


if __name__ == '__main__':
    main()
