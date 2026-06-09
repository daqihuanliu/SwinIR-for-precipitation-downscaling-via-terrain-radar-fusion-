import os

folder_path = "/data/groups/g1600002/home/hxiaoyuan2024/super_resolution/data/radar/cref_HR_sub_train"  # 目标文件夹路径
txt_path = "/home/hxiaoyuan2024/projection/super_resolution/BasicSR-master/basicsr/data/meta_info/meta_info_cref_train_GT.txt"  # 已存在的txt文件路径

# 获取所有文件名（不含子目录）
filenames = [f for f in os.listdir(folder_path) 
             if os.path.isfile(os.path.join(folder_path, f))]

# 追加到txt文件，每行添加"(480,480,3)"
with open(txt_path, "a") as f:  # "a"模式表示追加
    for name in filenames:
        f.write(f"{name} (480,480,3)\n")  # 格式化写入[[6, 8, 13]]