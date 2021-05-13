from flask import Flask, render_template, flash, request,session,redirect
import cv2
import numpy as np
import json
from PIL import ImageGrab
import io
import requests
import time
from flask import Flask, jsonify
from flask_mail import Mail, Message
from datetime import date, datetime
import requests
import simplejson 
import json

app = Flask(__name__)
mail= Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'tshetty750@gmail.com'
app.config['MAIL_PASSWORD'] = '**********************'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

app.secret_key='12345678'

@app.route('/')
def index():
	session['tries']=0
	return render_template('mine.html')

@app.route('/auth',methods = ['GET' ,'POST'])
def video_feed1():
	with open("data.json") as e:
		k = json.load(e)	

	if request.method=='POST':
		
		print(str(request.remote_addr))
		url = request.form["username"]
		pwd = request.form["psw"]
		if (url==k["username1"] and pwd ==k["password1"]):
			return redirect('https://vtop.vit.ac.in/vtop/initialProcess')
		else :	
			session['tries']=session['tries']+1
			if session['tries']>=1:
				print("\n\nIntruder has been captured. Real-time honeypot activated in backend.....")

				print("\nFace capture of intruder initiated...\n")
				# photo
				cam = cv2.VideoCapture(0)
				frame=None
				while (True):
					ret, frame = cam.read()
					if (ret):
						break
				cv2.imwrite("C:/Users/HP/Desktop/Nasscom_project/honeypot_project/ss_webcam/Intruder-RealTime-Capture.png",frame)	
				print("\nFace capture successful and saved in the system....\n")
				print("\nVideo capture of intruder initiated...\n\n\n")
				# video_code
				cap = cv2.VideoCapture(0)
				width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) + 0.5)
				height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) + 0.5)
				size = (width, height)

				capture_duration = 5
				fourcc = cv2.VideoWriter_fourcc(*'XVID')
				out = cv2.VideoWriter('C:/Users/HP/Desktop/Nasscom_project/honeypot_project/ss_webcam/Intruder-RealTime-Capture.mp4', fourcc, 20.0, size)
				start_time = time.time()
				while(int(time.time() - start_time) < capture_duration):
					ret, frame = cap.read()
					out.write(frame)
					cv2.imshow('Frame', frame)
					if cv2.waitKey(1) & 0xFF == ord('a'):
						break
				cap.release()
				out.release()
				cv2.destroyAllWindows()
				#END_VIDEO
				print("\n\nVideo capture successful and saved in the system....\n")

				# taking screenshot and sending to telegram 
				for i in range(1,5):
					im = ImageGrab.grab()
					if im is None:
						print("Error Occured")
					else:
						img_byte_arr = io.BytesIO()
						im.save(img_byte_arr, format='PNG')
						img_byte_arr = img_byte_arr.getvalue()
						response = requests.post("https://api.telegram.org/bot1710196314:AAGMICWMmrA5TDNkPaZSp9ie9VnkyXCetdg/sendPhoto?chat_id=-559281929", files={"photo": img_byte_arr}, data={"caption": "Intruder has sent"})
						print(response.status_code)
						if response.status_code != 200:
							print(response.json())
							print("sent image")
					print("\nSent the Intruder's screen capture image#",i," on TELEGRAM...\n")
				# telegram - ends

				# Store IP address and other details from JSON 
				print("\nCapturing IP address and other details of the intruder's system....\n")
				url = "http://ipinfo.io" 
				try:
						uResponse = requests.get(url)
				except requests.ConnectionError:
					return "Connection Error"  
				Jresponse = uResponse.text
				data = json.loads(Jresponse)

				ip = data['ip']
				city = data['city']
				country = data['country']
				location = data['loc']
				organisation = data['org']
				region = data['region']
				# hostname = data['hostname']
				print("\nIP address, location, address captured successfully....\n")
				# Date and Time
				today = date.today()
				d = today.strftime("%B %d, %Y")
				time_now = datetime.now()
				t = time_now.strftime("%H:%M:%S")
				
				print("\n\nSending Mail to TANMAY SHETTY's gmail account....\non date:", d + " at time: " + t)
				# print("\nCurrent Time =", t)

				# Send Mail
				msg = Message('HONEYPOT REAL-TIME INTRUDER ALERT on ' + d + ' at ' + t, sender = 'tshetty750@gmail.com', recipients = ['tshetty510@gmail.com'])

				with app.open_resource("C:/Users/HP/Desktop/Nasscom_project/honeypot_project/ss_webcam/Intruder-RealTime-Capture.png") as fp:  
						msg.attach("Intruder-RealTime-Capture.png","image/png",fp.read())  
				with app.open_resource("C:/Users/HP/Desktop/Nasscom_project/honeypot_project/ss_webcam/Intruder-RealTime-Capture.mp4") as fp:  
						msg.attach("Intruder-RealTime-Capture.mp4","video/mp4",fp.read()) 
				
				with open('C:/Users/HP/Desktop/Nasscom_project/honeypot_project/ss_webcam/Intruder-RealTime-Capture.png', 'rb') as fp:
						msg.attach('Intruder-RealTime-Capture.png', 'image/png', fp.read(), 'inline', headers=[['Content-ID','<pic>']])

				msg.html = render_template('mail_content.html',ip=ip,city=city,country=country,location=location,organisation=organisation,region=region)
				mail.send(msg)
				print("\n\nMail sent successfully to tshetty510@gmail.com\n\n")

				#return "maximum tries reached"
					
				
				return render_template('ip.html')
			return render_template('mine.html')

if __name__ == '__main__':
    app.run(debug=True)  
