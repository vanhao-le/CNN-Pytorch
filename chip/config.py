import torch
import os
# define training hyperparameters
INIT_LR = 1e-3
BATCH_SIZE = 16
EPOCHS = 5
# define the train and val splits
TRAIN_SPLIT = 0.75
VAL_SPLIT = 1 - TRAIN_SPLIT
# set the device we will be using to train the model
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
MODEL_PLOT = os.path.join("output", "train.png")
MODEL_PATH = os.path.join("output", "LeNet.pth")