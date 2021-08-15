import os
# set up static value
ORIGIN_INPUT_DATASET = "data/cell_images"

BASE_PATH = "data"

TRAIN_PATH = os.path.sep.join([BASE_PATH, "train"])
VALIDATE_PATH = os.path.sep.join([BASE_PATH, "validation"])
TEST_PATH = os.path.sep.join([BASE_PATH,"test"])

TRAIN_SPLIT = 0.8
VAL_SPLIT = 0.1

# Default VALUEs
NUM_EPOCHS = 50
INIT_LR = 1e-1
BS = 32