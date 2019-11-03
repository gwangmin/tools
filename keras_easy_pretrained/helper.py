'''
에러 날 수가 있는데 nomkl 설치하면 해결됩니다.
conda install -c anaconda nomkl
'''

from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array


class PreTrainedModelHelper:
    '''
    Easy use pre-trained model
    
    Available models(13):
        vgg16
        vgg19
        resnet50
        xception
        mobilenet
        mobilenet_v2
        nasnet_mobile
        nasnet_large
        inception_v3
        inception_resnet_v2
        densenet121
        densenet169
        densenet201
    '''
    def __init__(self, model_name, include_last_fc='True'):
        '''
        Load pre-trained model.
        
        model_name: pre-trained model name.
        include_last_fc: include_top. Default True.
        '''
        self.name = model_name
        # vgg16
        if model_name == 'vgg16':
            self.input_size = (224, 224)
            import keras.applications.vgg16 as vgg16
            self.lib = vgg16
            self.model = vgg16.VGG16(include_top=include_last_fc)
        # vgg 19
        elif model_name == 'vgg19':
            self.input_size = (224, 224)
            import keras.applications.vgg19 as vgg19
            self.lib = vgg19
            self.model = vgg19.VGG19(include_top=include_last_fc)
        # resnet50
        elif model_name == 'resnet50':
            self.input_size = (224, 224)
            import keras.applications.resnet50 as resnet50
            self.lib = resnet50
            self.model = resnet50.ResNet50(include_top=include_last_fc)
        # xception
        elif model_name == 'xception':
            self.input_size = (299, 299)
            import keras.applications.xception as xception
            self.lib = xception
            self.model = xception.Xception(include_top=include_last_fc)
        # densenet121
        elif model_name == 'densenet121':
            self.input_size = (224, 224)
            import keras.applications.densenet as densenet
            self.lib = densenet
            self.model = densenet.DenseNet121(include_top=include_last_fc)
        # densenet169
        elif model_name == 'densenet169':
            self.input_size = (224, 224)
            import keras.applications.densenet as densenet
            self.lib = densenet
            self.model = densenet.DenseNet169(include_top=include_last_fc)
        # densenet201
        elif model_name == 'densenet201':
            self.input_size = (224, 224)
            import keras.applications.densenet as densenet
            self.lib = densenet
            self.model = densenet.DenseNet201(include_top=include_last_fc)
        # inceptionResnetV2
        elif model_name == 'inception_resnet_v2':
            self.input_size = (299, 299)
            import keras.applications.inception_resnet_v2 as inception_resnet_v2
            self.lib = inception_resnet_v2
            self.model = self.lib.InceptionResNetV2(include_top=include_last_fc)
        # inceptionV3
        elif model_name == 'inception_v3':
            self.input_size = (299, 299)
            import keras.applications.inception_v3 as inception_v3
            self.lib = inception_v3
            self.model = self.lib.InceptionV3(include_top=include_last_fc)
        # nasnet mobile
        elif model_name == 'nasnet_mobile':
            self.input_size = (224, 224)
            import keras.applications.nasnet as nasnet
            self.lib = nasnet
            self.model = self.lib.NASNetMobile(include_top=include_last_fc)
        # nasnet large
        elif model_name == 'nasnet_large':
            self.input_size = (331, 331)
            import keras.applications.nasnet as nasnet
            self.lib = nasnet
            self.model = self.lib.NASNetLarge(include_top=include_last_fc)
        # mobilenet
        elif model_name == 'mobilenet':
            self.input_size = (224, 224)
            import keras.applications.mobilenet as mobilenet
            self.lib = mobilenet
            self.model = self.lib.MobileNet(include_top=include_last_fc)
        # mobilenet v2
        elif model_name == 'mobilenet_v2':
            self.input_size = (224, 224)
            import keras.applications.mobilenet_v2 as mobilenet_v2
            self.lib = mobilenet_v2
            self.model = self.lib.MobileNetV2(include_top=include_last_fc)
    
    def img_to_np(self, path, size):
        '''
        Load image and convert to numpy.ndarray
        
        path: image path
        size: image size (height, width)
        '''
        arr = img_to_array(load_img(path, target_size=size))
        return arr
    
    def img_to_input(self, img):
        '''
        Add batch dim
        
        img: image
        '''
        x = img.reshape((1,img.shape[0],img.shape[1],img.shape[2]))
        return x
    
    def predict(self, path):
        '''
        Inference using model.
        
        path: input image path
        '''
        # Load the image
        img = self.img_to_np(path, self.input_size)
        # Reshape to batch
        img = self.img_to_input(img)
        # Preprocessing and predict
        pred = self.model.predict(self.lib.preprocess_input(img))
        # Decode predictions
        result = self.lib.decode_predictions(pred)
        return result
    
    def summary(self):
        '''
        Show model summary
        '''
        return self.model.summary()


# test
if __name__ == '__main__':
    m = PreTrainedModelHelper('mobilenet')
    print(m.predict('./mug.jpg'))

