import cv2
import csv

img_root = './test/'

with open('./submission/result.csv') as res_csv:
# with open('./submission/subsample.csv') as res_csv:
    csv_reader = csv.reader(res_csv)
    csv_head = next(csv_reader)
    name_dict = {}

    color_dict={'33':50, '34':100, '35':150, '36':200, '37':250, '38':0, '39': 170, '40':120}
    for row in csv_reader:
        print(img_root+row[0])
        elr_string = row[4]
        elrs = elr_string.split('|')[:-1]
        mask_pixel=[]
        for elr in elrs:
            elr=elr.split(' ')
            for i in range(int(elr[1])):
                mask_pixel.append(int(elr[0])+i)
        # print(mask_pixel)
        if row[0] in name_dict:
            src_img = cv2.imread('./masked_img/'+row[0]+'.jpg')
            masked_img = src_img.copy()
            print(masked_img.shape[1], masked_img.shape[0])
            for index in mask_pixel:
                x = index // masked_img.shape[1]
                y = index % masked_img.shape[1]
                masked_img[x,y] = (0,0,color_dict[row[1]])
            cv2.imwrite('./masked_img/'+row[0]+'.jpg', masked_img)

        else:
            name_dict[row[0]] = row[0]
            src_img = cv2.imread(img_root+row[0]+'.jpg')
            masked_img = src_img.copy()
            print(masked_img.shape[1], masked_img.shape[0])
            for index in mask_pixel:
                x = index // masked_img.shape[1]
                y = index % masked_img.shape[1]
                masked_img[x,y] = (0,0,245)
            cv2.imwrite('./masked_img/'+row[0]+'.jpg', masked_img)
    # im2 = cv2.resize(src_img, (3384//4,2710//4))
    # cv2.imshow( 'img', im2)

    # cv2.waitKey(0)

