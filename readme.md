
# Live Camera feed
Broadcast a live camera feed and pick it up from any web browser on a computer connected to the same LAN network. This approach uses the web application library streamlit and utilizes the cache data method to store the image data in the HTTP cache. 

The transmission is good enough for real time use. 

&nbsp;

<div align="center"><img src="docs/preview.png" width="800"></div>

&nbsp;

## Dependencies

This code uses the following libraries:
- `streamlit`: for building the user interface and HTML web app 
- `openCV`: for handling the image capture
- `numpy`: for creating efficient arrays

&nbsp;

## Usage
1. run the app with
```
Streamlit run app.py --server.address 0.0.0.0
```
2. go to your settings and find your comptuers IP
3. go to the web browser and navigate to `yourIP:8501`
4. If the app works, you are done, if not, go edit the line `camera = cv2.VideoCapture(0)` and replace 0 with some other integer. Youll need to make sure you have a webcam and that it is not already in use. 

&nbsp;

## How it Works

The app as follows:
1. The hidapi library is used to initiate a connection to the PS5 controller
2. The dualsense class is used to decode the received bytes
4. the matplotlib library is used to create a visualization of the received signal from the triggers
3. Streamlit is used to display the figure
4. The ethernet class and UDP Socket communication is used to send the bytes to an IP address
5. The app loops indefinitely until quit
6. The Arduino connects to the internet, then receives the UDP signal and decodes it, then sets its PWM pin appropriately. 

&nbsp;

## Repository Structure
```
repository/
├── app.py # the code and UI integrated together live here
├── requirements.txt # the python packages needed to run locally
├── .gitignore # includes the local virtual environment named my_env
├── LICENSE.md # The MIT license
└── docs/
    └── preview.png # preview photo for Github
```

&nbsp;

## Topics 
```
Python | Streamlit | OpenCV | Computer vision | webcam | Mechanical engineer | Robotics engineer
```
&nbsp;

<hr>

&nbsp;

<div align="center">



╭━━╮╭━━━┳━━┳━━━┳━╮╱╭╮        ╭╮╱╱╭━━━┳━━━┳╮╭━┳━━━╮
┃╭╮┃┃╭━╮┣┫┣┫╭━╮┃┃╰╮┃┃        ┃┃╱╱┃╭━━┫╭━╮┃┃┃╭┫╭━╮┃
┃╰╯╰┫╰━╯┃┃┃┃┃╱┃┃╭╮╰╯┃        ┃┃╱╱┃╰━━┫╰━━┫╰╯╯┃┃╱┃┃
┃╭━╮┃╭╮╭╯┃┃┃╰━╯┃┃╰╮┃┃        ┃┃╱╭┫╭━━┻━━╮┃╭╮┃┃┃╱┃┃
┃╰━╯┃┃┃╰┳┫┣┫╭━╮┃┃╱┃┃┃        ┃╰━╯┃╰━━┫╰━╯┃┃┃╰┫╰━╯┃
╰━━━┻╯╰━┻━━┻╯╱╰┻╯╱╰━╯        ╰━━━┻━━━┻━━━┻╯╰━┻━━━╯
  


&nbsp;


<a href="https://twitter.com/BrianJosephLeko"><img src="https://raw.githubusercontent.com/BrianLesko/BrianLesko/f7be693250033b9d28c2224c9c1042bb6859bfe9/.socials/svg-white/x-logo-white.svg" width="30" alt="X Logo"></a> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <a href="https://github.com/BrianLesko"><img src="https://raw.githubusercontent.com/BrianLesko/BrianLesko/f7be693250033b9d28c2224c9c1042bb6859bfe9/.socials/svg-white/github-mark-white.svg" width="30" alt="GitHub"></a> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <a href="https://www.linkedin.com/in/brianlesko/"><img src="https://raw.githubusercontent.com/BrianLesko/BrianLesko/f7be693250033b9d28c2224c9c1042bb6859bfe9/.socials/svg-white/linkedin-icon-white.svg" width="30" alt="LinkedIn"></a>

follow all of these for pizza :)

</div>


&nbsp;


