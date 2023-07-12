# Parking-lot-car-counter
 Prototype for counting cars in parking lot using a Raspberry Pi and MQTT.

 This is a project I developed as part of the Internet Of Things Cluster (units 'ICTPRG430 Apply introductory object-oriented language skills' and 'ICTPRG444 Analyse software requirements') on my first semester at TAFE completing a Certificate IV in IT (programming specialism).

Scenario provided:
You are working as a junior software innovation engineer for the City of Joondalup in the Department of Transport. The department wants to upgrade a few public parking spaces by providing information about the number of available parking spots in near real time for each one. The parking lots in question do not have boom gates. 
For this purpose, you are required to count the cars that enter and exit a parking lot to keep a running total. You will be provided with the total number of parking spots, so you can determine the number of available spots at any time. 
You will be provided with additional requirements in this document, which you will need to create a simple Software Requirements Document (SRS). The SRS will inform your design decisions regarding the software. A template is provided for you. 
The project consists of two parts. Part one is about counting the cars and keeping a running total. This number, and some additional data points, like temperature and the time, will be published to an MQTT broker by your program. 
Part two is about visualising the information that was gathered in part one. Your program will display the number of available parking spots on the lot, as well as the time and the temperature. Depending on the type of display, this information display may need to be “time multiplexed”. (This means that only one type of information is displayed at a time, e.g., time → temperature → # of available spots → time, etc.)
Initially, you’ll be analysing the requirements and designing a prototype solution. Both programs must be written in Python and must run on a Raspberry Pi. You will be using the available sensors on the SenseHat as much as possible. 
