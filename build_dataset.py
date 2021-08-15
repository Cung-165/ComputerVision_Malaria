import config
from imutils import paths
import random
import shutil
import os

imagePaths = list(paths.list_images(config.ORIGIN_INPUT_DATASET))
print(config.ORIGIN_INPUT_DATASET)
print(len(imagePaths))

random.seed(42)
random.shuffle(imagePaths)

split = int(len(imagePaths) * config.TRAIN_SPLIT)
trainPaths = imagePaths[:split]
testPaths = imagePaths[split:]

i = int(len(trainPaths) * config.VAL_SPLIT)
valPaths = trainPaths [:i]
trainPaths = trainPaths[i:]

datasets = [
    ("training",trainPaths, config.TRAIN_PATH),
    ("validation",valPaths, config.VALIDATE_PATH),
    ("testing", testPaths, config.TEST_PATH )
]

# create val,train,test folder
for (type,imgPaths,baseOut) in datasets:
    print("INFO buiilding '{}' split".format(type))
    if not os.path.exists(baseOut):
        print("INFO create '{}' directory".format(baseOut))
        os.makedirs(baseOut)
    for inputPath in imgPaths:
        fileName = inputPath.split(os.path.sep)[-1]
        label = inputPath.split(os.path.sep)[-2]
        
        labelPath = os.path.sep.join([baseOut,label])

        if not os.path.exists(labelPath):
            print("[INFO] 'creating {}' directory".format(labelPath))
            os.makedirs(labelPath)
        p = os.path.sep.join([labelPath,fileName])
        print("[INFO] coppy file name {} ...".format(fileName))
        shutil.copy2(inputPath,p)