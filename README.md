# Smart Video Solutions for Fashion Store Optimization
This project intends in designing a cost-effective people counting system with AI at Edge, where it calculates Conversion rates 
using total number of people counted by the system and number of transactions for the day, which helps in providing analytical 
insights for fashion optimization with a very minimum hardware requirements.   

# Getting Started 
- Setup your local environment:
  - Download and install the **OpenVINO Toolkit**. The installations directions for OpenVINO can be found [here](https://docs.openvinotoolkit.org/latest/index.html)
  - Run the **Verification Scripts to verify your installation**. This is a very important step to be done before you proceed further.
- The project directory is structured as follows:
```
					project
					|
					|_ person_detect_model
					|  
					|_ resources
					|  |_Pedestrian_Detect.avi
					|  |_conversion_rates.csv
					|  |_smart Video Solutions using Edge AI for fashion.pptx
					|      
					|_ README.md    
					|   
					|_ requirements.txt   
					|
					|_ LICENSE
					|
					|_ src
					   |_ main.py
					   |_ people_counting.py
					   |_ person_detection.py
	
```
  - The project directory contains a ```resources``` folder which has an .avi file, can be used to test the input file for the project.
  - It has ```requirements.txt``` file which contains all the necessary dependencies to be installed before running the project.
	
**Note: This project has been tested only in Windows 10 Operating System environment with Intel core i3-7100 processor which has an Intel Integrated GPU HD Graphics 630.**  

## Demo

- First, initialize the OpenVINO environment:
  - Open command prompt and cd to ```cd C:\Program Files (x86)\IntelSWTools\openvino\bin```
  - type ```setupvars.bat``` command and press *Enter* to initialize OpenVINO environment.
- Next, ```cd``` to the project directory:
- Now, run the following command to run the application:
  - ```python src\main.py  --video resources\Pedestrian_Detect.avi --device CPU --model person_detect_model\person-detection-retail-0013```
- After successful completion of the program, you'll be able to see **retail_analysis.csv** in your project directory.     

 
## Documentation 
- The ```python main.py -h``` command displays the commands which are supported by project:
  - ```--video``` argument takes the input video file or a webcam, for accessing video file the command is ```--video "<path of video file>"``` whereas for accessing webcam ```--video "cam"```, default is "cam".
  - ```--device``` argument specifies the devices such as **CPU,GPU,VPU,FPGA** to run inference on.
  - ```--model``` argument takes in the person detection model.
  
# Next Steps
- After successful completion of running the program, you can download Tableau Software for data visualisation of the retail_analysis.csv file.  
- For Further details, please check out the ```smart Video Solutions using Edge AI for fashion.pptx``` presentation in the resources section on what we can do more.


# References
The Tableau software can be downloded from [here](https://public.tableau.com/s/) .
	