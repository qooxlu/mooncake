import os, cv2

def selete_ocr():
    img_path = "jpg/"# 这里放原始文件
    del_path = "del/"# 这里是需要删除的文件
    use_path = "use/"# 这里是需要OCR的文件
    restart = True
    peach_rate = 680
    
    while restart:
        restart = False
        vp = os.listdir(img_path)
        vp.sort()
        for path in vp:
            img = cv2.imread(img_path + path)
            cv2.namedWindow(path, 0)
            cv2.resizeWindow(path, int(img.shape[1]/img.shape[0]*peach_rate), peach_rate)
            cv2.imshow(path, img)
            des = cv2.waitKey(0)
            # print(des)
            if des == 49:# 按1保存
                os.replace(img_path + path, use_path + path)
                origin_temp = img_path + path
                path_temp = use_path + path
            elif des == 50:# 按2删除
                os.replace(img_path + path, del_path + path)
                origin_temp = img_path + path
                path_temp = del_path + path
            elif des == 32:# 按空格查看上一个文件
                os.replace(path_temp, origin_temp)
                restart = True
                break

            elif des == 113:# 按q退出
                break

            else:
                restart = True
                break
            cv2.destroyWindow(path)
    return

def remain_counts():
    counts = os.listdir('jpg/')
    print(len(counts))
    return

def save_work():
    for x in os.listdir("use"):
        os.replace("use/" + x, "clear/" + x)
    return

if __name__ == '__main__':
    selete_ocr()
    remain_counts()
    save_work()
