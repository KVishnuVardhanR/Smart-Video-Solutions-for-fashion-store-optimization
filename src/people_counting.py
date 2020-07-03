import cv2
import time
from person_detection import PersonDetect
import logging as log


class people_counter:
    def __init__(self, model, device, video_file):
        self.person_detect = PersonDetect(model, device, threshold = 0.5)
        self.person_detect.load_model()
        self.video_file = video_file
        self.last_count = 0
        self.total_count = 0
        self.start_time = 0
        self.start_frame_number = 0

    def people_count(self):
        try:
            cap=cv2.VideoCapture(self.video_file)
        except FileNotFoundError:
            log.error("Cannot locate video file: "+ video_file)
        except Exception as e:
            log.error("Something else went wrong with the video file: ", e)
            
        
        
        while cap.isOpened():
            if self.video_file != 'cam':
                cap.set(cv2.CAP_PROP_POS_FRAMES, self.start_frame_number)
                self.start_frame_number = self.start_frame_number+4
                    
            ret, frame=cap.read()
            if not ret:
                break
                
            image, count = self.person_detect.predict(frame)
            if count > self.last_count:
                self.start_time = time.time()
                self.total_count = self.total_count + count - self.last_count

            if count < self.last_count:
                duration = int(time.time() - self.start_time)

            self.last_count = count                   
            y_pixel=25
     

            out_text = f"number of people counted is {self.total_count} "
            cv2.putText(image, out_text, (15, y_pixel), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
            cv2.imshow('frame',frame)
                
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
        return self.total_count    
