Riju Sikdar
# arrowKeyRC
Drive an RC car with computer keyboard arrow keys 

<br><br>
<b>Program Description</b>
<hr>
The following set of programs are to control an RC car using the arrow keys on your computer keyboard. Python and PyGame are used to read in the key down actions and the SerialPy to transmit them over serial to arduino with nRF24L01 transceiver modual to another arduino that catches and parses strings sent and transfer them into motor movements.  
<br>
It is a fun project for me, getting to play around with arduinos, transceivers, motor controller ICs and wiring, independently for the first time. 
 
 

<br><br>
<b>Compiling & Runing</b>
<hr>
Need to have PyGame and SerialPy libraries installed

	PyGame - pygame.org/wiki/GettingStarted#Pygame 
  
	SerialPy - pythonhosted.org/pyserial/
 
 Its Python for the part that runs on your computer so just run Python through the IDLE or command line, what ever you like. 
 
 
 The "tramsmitter" & "receiver" folder have the arduino code Use the arduino editor to open them and download and compile
 


<br><br>
<b>Known Limitations, Issues (excuses for bad code)</b>
<hr>
 Limitations:<br>
 
  - Car does not center steering coloumn when turned to one side
  
  - Car motors are using PWM but are set to one speen only 
	
	

	
