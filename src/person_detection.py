from openvino.inference_engine import IENetwork, IECore
import cv2

class PersonDetect:
    '''
    Class for the Person Detection Model.
    '''

    def __init__(self, model_name, device, threshold):
        self.model_weights=model_name+'.bin'
        self.model_structure=model_name+'.xml'
        self.device=device
        self.threshold=threshold

        try:
            self.model=IENetwork(self.model_structure, self.model_weights)
        except Exception as e:
            raise ValueError("Could not Initialise the network. Have you enterred the correct model path?")

        self.input_name=next(iter(self.model.inputs))
        self.input_shape=self.model.inputs[self.input_name].shape
        self.output_name=next(iter(self.model.outputs))
        self.output_shape=self.model.outputs[self.output_name].shape

    def load_model(self):
        self.core = IECore()
        self.net = self.core.load_network(network=self.model, device_name=self.device,num_requests=1)
        
    def predict(self, image):
        self.processed_image=self.preprocess_input(image)
        results= self.net.infer(inputs={self.input_name:self.processed_image})
        detections = results[self.output_name]
        self.image, self.count = self.draw_outputs(detections, image)
        return self.image, self.count
    
    def draw_outputs(self, detections, image):
        count = 0
        for box in detections[0][0]: 
            conf = box[2]
            if conf >= self.threshold :
                xmin = int(box[3] * image.shape[1])
                ymin = int(box[4] * image.shape[0])
                xmax = int(box[5] * image.shape[1])
                ymax = int(box[6] * image.shape[0])
                cv2.rectangle(image, (xmin, ymin), (xmax, ymax), (0, 0, 255), 1)
                count = count+1
        return image, count


    def preprocess_input(self, image):
        self.image = cv2.resize(image, (self.input_shape[3], self.input_shape[2]))
        self.image = self.image.transpose((2,0,1))
        self.image = self.image.reshape(1, *self.image.shape)
        return self.image
