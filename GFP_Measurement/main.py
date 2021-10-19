import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

video_path = "C:\\Users\\TuzukiYuki\\Videos\\Captures\\aa.mp4"
ROOT_PATH_1 = "C:\\Users\\TuzukiYuki\\Desktop\\IGEM\\GPU_mager\\directory"
ROOT_PATH_2 = "C:\\Users\\TuzukiYuki\\Desktop\\IGEM\\GPU_mager\\img"
path_w = "C:\\Users\\TuzukiYuki\\Desktop\\IGEM\\GPU_mager\\result.txt"
list = []
d1_list = []
d2_list = []
d3_list = []
d4_list = []
d5_list = []
d6_list = []
d7_list = []
d8_list = []
d9_list = []
time_list = []



def multiple_enumeration(count,fps):

    total = int(count/(fps*60))+1

    if total < 1:
        print('movie is too short')

    else:
        for i in range(1,total):
            list.append(i*60*fps)

    return list

def frame_pick(video_path):

    video = cv2.VideoCapture(video_path)
    f = 0

    # 幅
    W = video.get(cv2.CAP_PROP_FRAME_WIDTH)
    # 高さ
    H = video.get(cv2.CAP_PROP_FRAME_HEIGHT)
    # 総フレーム数
    count = video.get(cv2.CAP_PROP_FRAME_COUNT)
    # fps
    fps = video.get(cv2.CAP_PROP_FPS)

    list = multiple_enumeration(count, fps)

    time_list = [i for i in range(len(list))]

    print("list",list)
    print("fps",fps)
    print("count",count)


    while (video.isOpened()):
        ret, frame = video.read()
        f = f+1

        print(f/count)

        for i in range(len(list)):

            if f == list[i]:

                cv2.imwrite(ROOT_PATH_2 + "\\" + str(i) + ".jpg",frame)


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        if f == count:
            break

    video.release()
    cv2.destroyAllWindows()

def process(file_path):
    img = cv2.imread(file_path)

    d1, d2, d3, d4, d5, d6, d7, d8, d9 = division_and_hsv_convart(img)

    d1_list.append(d1)
    d2_list.append(d2)
    d3_list.append(d3)
    d4_list.append(d4)
    d5_list.append(d5)
    d6_list.append(d6)
    d7_list.append(d7)
    d8_list.append(d8)
    d9_list.append(d9)


"""
    result = os.path.basename(file_path) + " :value is " + str(v)

    print(result)

    with open(path_w, mode='w') as f:
        f.write(result)
"""

def recursive_file_check(ROOT_PATH_2):
    if os.path.isdir(ROOT_PATH_2):
        # directoryだったら中のファイルに対して再帰的にこの関数を実行
        files = os.listdir(ROOT_PATH_2)
        for file in files:
            recursive_file_check(ROOT_PATH_2 + "\\" + file)
    else:
        # fileだったら処理
        process(ROOT_PATH_2)

def division_and_hsv_convart(image):

    img = image

    print(img)

    ymin_1 = 0
    ymax_1 = 50
    xmin_1 = 0
    xmax_1 = 50

    detframe_1 = img[ymin_1:ymax_1, xmin_1:xmax_1]
    detframe_1 = cv2.cvtColor(detframe_1, cv2.COLOR_BGR2HSV)
    h_detframe_1, s_detframe_1, v_detframe_1 = cv2.split(detframe_1)

    v_mean_detframe_1 = np.mean(v_detframe_1[0])


    ymin_2 = 0
    ymax_2 = 50
    xmin_2 = 51
    xmax_2 = 100

    detframe_2 = img[ymin_2:ymax_2, xmin_2:xmax_2]
    detframe_2 = cv2.cvtColor(detframe_2, cv2.COLOR_BGR2HSV)
    h_detframe_2, s_detframe_2, v_detframe_2 = cv2.split(detframe_2)

    v_mean_detframe_2 = np.mean(v_detframe_2[0])

    ymin_3 = 0
    ymax_3 = 50
    xmin_3 = 101
    xmax_3 = 150

    detframe_3 = img[ymin_3:ymax_3, xmin_3:xmax_3]
    detframe_3 = cv2.cvtColor(detframe_3, cv2.COLOR_BGR2HSV)
    h_detframe_3, s_detframe_3, v_detframe_3 = cv2.split(detframe_3)

    v_mean_detframe_3 = np.mean(v_detframe_3[0])

    ymin_4 = 51
    ymax_4 = 100
    xmin_4 = 0
    xmax_4 = 50

    detframe_4 = img[ymin_4:ymax_4, xmin_4:xmax_4]
    detframe_4 = cv2.cvtColor(detframe_4, cv2.COLOR_BGR2HSV)
    h_detframe_4, s_detframe_4, v_detframe_4 = cv2.split(detframe_4)

    v_mean_detframe_4 = np.mean(v_detframe_4[0])

    ymin_5 = 51
    ymax_5 = 100
    xmin_5 = 51
    xmax_5 = 100

    detframe_5 = img[ymin_5:ymax_5, xmin_5:xmax_5]
    detframe_5 = cv2.cvtColor(detframe_5, cv2.COLOR_BGR2HSV)
    h_detframe_5, s_detframe_5, v_detframe_5 = cv2.split(detframe_5)

    v_mean_detframe_5 = np.mean(v_detframe_5[0])


    ymin_6 = 51
    ymax_6 = 100
    xmin_6 = 101
    xmax_6 = 150

    detframe_6 = img[ymin_6:ymax_6, xmin_6:xmax_6]
    detframe_6 = cv2.cvtColor(detframe_6, cv2.COLOR_BGR2HSV)
    h_detframe_6, s_detframe_6, v_detframe_6 = cv2.split(detframe_6)

    v_mean_detframe_6 = np.mean(v_detframe_6[0])

    ymin_7 = 101
    ymax_7 = 150
    xmin_7 = 0
    xmax_7 = 50

    detframe_7 = img[ymin_7:ymax_7, xmin_7:xmax_7]
    detframe_7 = cv2.cvtColor(detframe_7, cv2.COLOR_BGR2HSV)
    h_detframe_7, s_detframe_7, v_detframe_7= cv2.split(detframe_7)

    v_mean_detframe_7 = np.mean(v_detframe_7[0])

    ymin_8 = 101
    ymax_8 = 150
    xmin_8 = 51
    xmax_8 = 100

    detframe_8 = img[ymin_8:ymax_8, xmin_8:xmax_8]
    detframe_8 = cv2.cvtColor(detframe_8, cv2.COLOR_BGR2HSV)
    h_detframe_8, s_detframe_8, v_detframe_8 = cv2.split(detframe_8)

    v_mean_detframe_8 = np.mean(v_detframe_8[0])

    ymin_9 = 101
    ymax_9 = 150
    xmin_9 = 101
    xmax_9 = 150

    detframe_9 = img[ymin_9:ymax_9, xmin_9:xmax_9]
    detframe_9 = cv2.cvtColor(detframe_9, cv2.COLOR_BGR2HSV)
    h_detframe_9, s_detframe_9, v_detframe_9 = cv2.split(detframe_9)

    v_mean_detframe_9 = np.mean(v_detframe_9[0])

    return v_mean_detframe_1, v_mean_detframe_2, v_mean_detframe_3, v_mean_detframe_4, v_mean_detframe_5, v_mean_detframe_6, v_mean_detframe_7, v_mean_detframe_8, v_mean_detframe_9


def Plot(time_list,d1_list,d2_list,d3_list,d4_list,d5_list,d6_list,d7_list,d8_list,d9_list):


    print(d1_list)
    print(time_list)

    fig, axes = plt.subplots(3, 3, tight_layout=True)

    axes[0, 0].plot(time_list, d1_list)
    axes[0, 1].plot(time_list, d2_list)
    axes[0, 2].plot(time_list, d3_list)
    axes[1, 0].plot(time_list, d4_list)
    axes[1, 1].plot(time_list, d5_list)
    axes[1, 2].plot(time_list, d6_list)
    axes[2, 0].plot(time_list, d7_list)
    axes[2, 1].plot(time_list, d8_list)
    axes[2, 2].plot(time_list, d9_list)

    plt.show()


frame_pick(video_path)
recursive_file_check(ROOT_PATH_2)
Plot(time_list,d1_list,d2_list,d3_list,d4_list,d5_list,d6_list,d7_list,d8_list,d9_list)





