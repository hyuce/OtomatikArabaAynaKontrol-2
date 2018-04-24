import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
pwm = GPIO.PWM(18, 100)
pwm2= GPIO.PWM(17, 100)
pwm.start(5)
pwm2.start(5)
GPIO.setwarnings(False)
TRIG = 23
ECHO = 24
print ("HC-SR04 mesafe sensoru")
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
while True:
 GPIO.output(TRIG, False)
 print ("Olculuyor...")
 time.sleep(5)
 GPIO.output(TRIG, True)
 time.sleep(0.00001)
 GPIO.output(TRIG, False)
 while GPIO.input(ECHO)==0:
 	pulse_start = time.time()
 while GPIO.input(ECHO)==1:
 	pulse_end = time.time()
 pulse_duration = pulse_end - pulse_start #darbe süresi hesabı
 distance = pulse_duration * 17150
 distance = round(distance, 2)
 if distance > 1 and distance < 8: # direksiyona en uzak mesafe
    duty = float(160) / 10.0 + 2.5
    pwm.ChangeDutyCycle(duty)
    duty2 = float(170) / 30.0 + 2.5
    pwm2.ChangeDutyCycle(duty2)
    print ("1. servo : 0 DERECE")
    print ("Mesafe:",distance - 0.5,"cm")
    print ("2. servo : 0 DERECE")
 elif distance >=8 and distance <16:
    duty = float(164) / 10.0 + 2.5
    pwm.ChangeDutyCycle(duty)
    duty2 = float(160) / 30.0 + 2.5
    pwm2.ChangeDutyCycle(duty2)
    print ("1. servo : 10 DERECE")
    print ("Mesafe:",distance - 0.5,"cm")
    print ("2. servo : 5 DERECE")
 elif distance >=16 and distance < 24:
    duty = float(168) / 10.0 + 2.5
    pwm.ChangeDutyCycle(duty)
    duty2 = float(150) / 30.0 + 2.5
    pwm2.ChangeDutyCycle(duty2)
    print ("1. servo : 20 DERECE") 
    print ("Mesafe:",distance - 0.5,"cm")
    print ("2. servo : 10 DERECE")
 elif distance >=24 and distance < 32:
    duty = float(172) / 10.0 + 2.5
    pwm.ChangeDutyCycle(duty)
    duty2 = float(140) / 30.0 + 2.5
    pwm2.ChangeDutyCycle(duty2)
    print ("1. servo : 30 DERECE") 
    print ("Mesafe:",distance - 0.5,"cm")
    print ("2. servo : 15 DERECE") 
 else:
    duty = float(176) / 10.0 + 2.5
    pwm.ChangeDutyCycle(duty)
    duty2 = float(130) / 30.0 + 2.5
    pwm2.ChangeDutyCycle(duty2)
    print ("1. servo : 45 DERECE")
    print ("İlk Konum")
    print ("2. servo : 20 DERECE")
