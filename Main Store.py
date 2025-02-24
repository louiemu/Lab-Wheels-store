# --------------------------------------    
提交人：SZ  
功能简介：读取文件中的3通道图片，转为灰度图  
特殊导入包：os,cv2
提交日期：2021/7/21  
# ------------------------------------------------  
def JPG2GRAY(source_Dir, new_Dir):  
    '''  
    :param source_Dir: 要处理的文件夹路径  
    :param new_Dir: 保存的路径  
    :return:无  


    # 判断是否存在保存路径，不存在则新建
    if not os.path.exists(new_Dir):
        os.makedirs(new_Dir)
    # 处理图片
    for filename in os.listdir(source_Dir):
        # 打印文件名
        print(filename)
        # 读取图片
        img = cv2.imread(os.path.join(source_Dir, filename))
        # 将图片转换为灰度图
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # 保存图片
        cv2.imwrite(os.path.join(new_Dir, filename), img)
        # 保存为npy文件(保存为jpg等图片文件时，会自动生成RGB通道，导致灰度图通道数为3，npy则不会产生这种问题）
        # np.save(os.path.join(new_Dir,filename),img)

        print('处理成功')
        
        
# --------------------------------------        
提交人：SZ  
功能简介：索贝尔边缘检测 
特殊导入包：
import torch.nn.functional as F
from torch.autograd import Variable
提交日期：2021/7/21  
# ------------------------------------------------ 
def Sobel(im):
    '''
    索贝尔边缘检测
    :param im:输入1通道的图片
    :return:edge_detect:经过滤波后的边缘图像矩阵
    '''
    # 设定Sobel的滤波器
    sobel_kernel = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]], dtype='float32')
    # 扩展矩阵
    sobel_kernel = sobel_kernel.reshape((1, 1, 3, 3))
    # 将参数赋值与pytorch网络
    weight = Variable(torch.from_numpy(sobel_kernel))
    weight = weight.cuda()
    # 计算出Sobel边缘图
    edge_detect = F.conv2d(Variable(im), weight)

    return edge_detect
