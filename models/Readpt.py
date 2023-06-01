import torch

    # Load category and color encodings
cat_dict = torch.load('D:/browserdownload/st-gcn-master/st-gcn-master/models/kinetics-st_gcn.pt')
for k, v in cat_dict.items():  # k 参数名 v 对应参数值
        print(k, v)
