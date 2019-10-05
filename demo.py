import os
import sys
import torch
from collections import OrderedDict
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt

from torch.nn.functional import upsample

import dextr.networks.deeplab_resnet as resnet
from mypath import Path
from dextr.dataloaders import helpers as helpers
from dextr.dextr import ResNet101DeepLabDEXTR

modelName = 'dextr_pascal-sbd'
pad = 50
thres = 0.8
gpu_id = 0
device = torch.device("cuda:"+str(gpu_id) if torch.cuda.is_available() else "cpu")

dextr_model = ResNet101DeepLabDEXTR()

#  Create the network and load the weights
print("Initializing weights from: {}".format(os.path.join(Path.models_dir(), modelName + '.pth')))
dextr_model.load_weights(os.path.join(Path.models_dir(), modelName + '.pth'))

dextr_model.eval()
dextr_model.to(device)

#  Read image and click the points
image = np.array(Image.open('ims/dog-cat.jpg'))
plt.ion()
plt.axis('off')
plt.imshow(image)
plt.title('Click the four extreme points of the objects\nHit enter when done (do not close the window)')

results = []

with torch.no_grad():
    while 1:
        extreme_points_ori = np.array(plt.ginput(4, timeout=0)).astype(np.int)
        print(extreme_points_ori)
        if extreme_points_ori.shape[0] < 4:
            if len(results) > 0:
                helpers.save_mask(results, 'demo.png')
                print('Saving mask annotation in demo.png and exiting...')
            else:
                print('Exiting...')
            sys.exit()

        result = dextr_model.inference(image, extreme_points_ori)

        results.append(result)

        # Plot the results
        plt.imshow(helpers.overlay_masks(image / 255, results))
        plt.plot(extreme_points_ori[:, 0], extreme_points_ori[:, 1], 'gx')
