import numpy as np
from people_counting import people_counter
import os
import argparse
import sys
import pandas as pd
import matplotlib.pyplot as plt
import logging as log


def main(args):
    model=args.model
    device=args.device
    threshold=args.threshold
    
    if args.video == 'cam':
        video_file = 0
    else:
        video_file=args.video

    try:
        count = people_counter(model, device, video_file)
        total_count = count.people_count()
        
        trans = int(input('\nEnter total number of transactions hppened today : '))
        customer_traffic = total_count//2
        conversion_rate = trans/customer_traffic
        
        if os.path.isfile('retail_analytics.csv')  == False:
            data = {'customer_traffic': customer_traffic, 'trans' : trans, 'conversion_rate' : conversion_rate}
            df = pd.DataFrame(data = data, index = [0])
            df.to_csv('retail_analytics.csv', encoding='utf-8', index=False)

        else:
            data = {'customer_traffic': customer_traffic, 'trans' : trans, 'conversion_rate' : conversion_rate}
            df = pd.read_csv('retail_analytics.csv')
            df = df.append(data, ignore_index=True)
            df.to_csv('retail_analytics.csv', encoding='utf-8', index=False)

        
        if conversion_rate >= 0.1:
            print('\nYour store has earned a good conversion rate of '+ str(conversion_rate)+'. Keep it up!')
        if len(df) > 1 and conversion_rate > np.mean(df['conversion_rate']):
            print('The performance of your store has increased when compared with its previous conversion rates.')
        elif conversion_rate < 0.1:
            print('\nYou have to improve your store performance. Try taking the feedback of customers to improve it.')

        if len(df) > 1:
            df['conversion_rate'].plot()
            plt.show()
                
                               
    except Exception as e:
        log.error("Could not run Inference: ", e)

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--model', required=True,
                        help = "Path to xml file of Person Detection model.")
    
    parser.add_argument('--device', default='CPU',
                        help = "specifying device like CPU, GPU, VPU, FPGA to run inference.")
    
    parser.add_argument('--video', default='cam',
                        help = "Input file, User can enter path of video file or enter cam for webcam.")
    
    parser.add_argument('--threshold', default=0.5,
                        help = "Hyper parameter for changing threshold which is utilised by the model.")
    
    args=parser.parse_args()

    main(args)
