import torch

    # Load category and color encodings
cat_dict = torch.load('./work_dir/recognition/kinetics_skeleton/ST_GCN/epoch50_model.pt')
for k, v in cat_dict.items():  # k 参数名 v 对应参数值
        print(k, v)
