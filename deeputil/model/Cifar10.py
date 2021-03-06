
from keras.models import Model
from keras.utils.data_utils import get_file
from keras import backend as K
from .. import modelassist
import os

CONFIG_PATH='https://raw.githubusercontent.com/Avkash/mldl/master/data/models/cifar10_config_2000.json'
WEIGHTS_PATH = 'https://github.com/Avkash/mldl/raw/master/data/models/cifar10_weight_2000.h5'


def CIFAR10(show_info=True):
        """
        This is pre-built CIFAR10 model trained for 250 epochs with 78.00% accuracy
        :param show_info:
        :return: model as Keras.Model
        """
        # Getting Config first
        config_path = get_file('cifar10_config_2000.json',
                                CONFIG_PATH,
                                cache_subdir='models')

        # Getting weights next
        weights_path = get_file('cifar10_weight_2000.h5',
                                WEIGHTS_PATH,
                                cache_subdir='models')

        config_found = False
        if os.path.isfile(config_path):
            config_found = True
        else:
            if show_info is True:
                print("Error: Unable to get the CIFAR10 model configuration on disk..")

        weight_found = False
        if os.path.isfile(weights_path):
            weight_found = True
        else:
            if show_info is True:
                print("Error: Unable to get the CIFAR10 model weights on disk..")

        if config_found is False and weight_found is False:
            if show_info is True:
                print("Error: Unable to get the CIFAR10 model..")

        return modelassist.ImportExport.import_keras_model_config_and_weight_and_compile(config_path, weights_path, show_info)
