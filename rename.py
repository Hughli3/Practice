import  os
def rename():
    #获得文件夹中的文件    file_list = os.listdir('/Users/hughli/Documents/学习/共享/OneDrive/Udacity/Python课程/prank')
    print(file_list)
    os.chdir('/Users/hughli/Documents/学习/共享/OneDrive/Udacity/Python课程/prank')
    for file_name in file_list:
        print('Old Name - ' + file_name)
        os.rename(file_name,file_name.translate( '1234567890'))
        print('New Name - ' + file_name.maketrans('','','1234567890'))
#os.rename(src, dst) src是要修改的目录名，dst是修改后的目录名
#string.translate(table, list of characters to remove)
#table是映射表，第二个是需要移除的字符

rename()
