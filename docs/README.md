<h1 align='center'>SwinIR for precipitation downscaling</h1>
## This is a warehouse for SwinIR-Pytorch-model, can be used to train your precipitation dataset for downscaling.
## The code partly come from [official source code](https://github.com/XPixelGroup/BasicSR))  

## Change description
```
"./basicsr/archs/swinir_arch.py" -> Increase 5 times super-resolution function
"./scripts/data_preparation/extract_subimages.py" -> Image preprocessing molecular block settings
"./basicsr/losses/basic_loss.py" -> Change the loss function
```

## environmentChange description
```
conda activate BasicSR && cd ./
```

##  Build your own precipitation dataset:
```
requirement:
1) Data from radar mosaic (HR)
2) terrain filed (slope & aspect) 
3) RGB fusion
4) imagine degration (HR -> LR)
5) extract_subimages (python "./scripts/data_preparation/extract_subimages.py")
```
## Training
```
python basicsr/train.py -opt ./options/train/SwinIR/train_SwinIR_SRx5_scratch.yml (direct migration)
python basicsr/train.py -opt ./options/train/SwinIR/train_SwinIR_SRx5_scratch_migration_all.yml  #(Fine-tuning)
python basicsr/train.py -opt ./options/train/SwinIR/train_SwinIR_SRx5_scratch_migration_0.yml  #(Training from scratch)
```

