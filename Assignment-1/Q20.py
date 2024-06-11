"""Question
In a pathology lab test, there are n number of samples for testing the health condition of a patient,
each slide has 5 components, Sugar level, Blood pressure, Heartbeat rate, weight and fat percentage,
based on input as provided by the patient's blood report.

1. Create a sample input for a healthy patient as follows:

"Sugar level":15, "Blood pressure":32, "Heartbeat rate":71, "weight":65, "fat percentage":10.

2. Get values from the user and compare inputs with healthy patient data. If the patient data is not matching with the healthy
patient’s data, provide a warning.

3. Provide difference in readings to the patient.
Expected Output:
Sugar level:56

Blood pressure:120

Heartbeat rate:45

weight:67

fat percentage:67

{'Sugar level': -41, 'Blood pressure': -88, 'Heartbeat rate': 26, 'weight': -2, 'fat percentage': -57}

Sugar level -41

The sugar level is 41 less than the ideal value

Blood pressure -88

Blood pressure is 88 less than the ideal value

Heartbeat rate 26

Heartbeat rate is 26 more than the ideal value

weight -2

weight is 2 less than the ideal value

fat percentage 57

fat percentage is 57 less than the ideal value

"""

#Answer
healthy={'Sugar level':15,'Blood pressure':32,'Heartbeat rate':71,'weight':65,'fat percentage':10}
inputdata={}
for i in healthy:
    string="Enter "+i+":"
    temp=int(input(string))
    inputdata[i]=temp
print(inputdata)
diff={}
for i in healthy:
    diff[i]=healthy[i]-inputdata[i]
    if diff[i]<0:
        print('The '+i+' is '+str(abs(diff[i]))+' more than the ideal value')
    elif diff[i]>0:
        print('The '+i+' is '+str(abs(diff[i]))+' less than the ideal value')
    else:
        print('The '+i+' is '+str(abs(diff[i]))+' equal to the ideal value')


