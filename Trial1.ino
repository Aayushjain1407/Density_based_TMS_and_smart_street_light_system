#define IRSensor1 5
#define Red1 32
#define Green1 26
#define IRSensor2 18
#define Red2 33
#define Green2 25
#define IRSensor3 21
#define led1 12
#define led2 27
#define led3 14
#define LDR 19

int count1 = 0;
int count2 = 0;
int count3 = 0;
bool label = true;
//int data1;
//int sensor1;
String dataLabel1 = "Sensor_status";
String dataLabel2 = "Car count 1";
String dataLabel3 = "Car count 2";
int i = 0;
int dataLabel1_counter = 0;
int dataLabel2_counter = 0;
void setup() {
  // put your setup code here, to run once:
  pinMode(Red1, OUTPUT); //Red
  pinMode(Green1, OUTPUT);//Green
  pinMode(IRSensor1, INPUT);//First traffic sensor
  pinMode(Red2, OUTPUT); //Red
  pinMode(Green2, OUTPUT);//Green
  pinMode(IRSensor2, INPUT);//Second traffic sensor
  pinMode(led1, OUTPUT); //white
  pinMode(led2, OUTPUT);//white
  pinMode(led3, OUTPUT);//white
  pinMode(IRSensor3, INPUT);//Street light sensor
  
  Serial.begin(9600); 
  
  }
  
void loop() {  
  // put your main code here, to run repeatedly:
  
  int sensorStatus1 = digitalRead(IRSensor1);
  int sensorStatus2 = digitalRead(IRSensor2);
  int sensorStatus3 = digitalRead(IRSensor3);
  
  digitalWrite(Red1, HIGH);
  digitalWrite(Red2, HIGH);
  while(label){
    Serial.print(dataLabel1);
    Serial.print(",");
    Serial.print(dataLabel2);
    Serial.print(",");
    Serial.print(dataLabel1);
    Serial.print(",");
    Serial.print(dataLabel3);
    Serial.print(",");
    Serial.print("Street light cars");
    Serial.print(",");
    Serial.println("TimeStamp");
    label = false;
    }
  //data to be shown in the serial monitor 
  Serial.print(sensorStatus1);
  delay(1000);
  if (sensorStatus1 == 0){
    count1 ++;                                   
    }        
    
   digitalWrite(Green1,LOW);
   Serial.print(",");
   Serial.print(count1);
   Serial.print(",");
  
   //----------Second Traffic Signal----------------------// 
   Serial.print(sensorStatus2);
   delay(1000);
   if (sensorStatus2 ==0){
      count2 ++;
    }

    digitalWrite(Green2, LOW);
    Serial.print(",");
    Serial.print(count2);
    Serial.print(",");
    Serial.println(count3);
   
   if(count1 >= 6 && count1 > count2 ){
    Street_light();
    digitalWrite(Red1, LOW);
    digitalWrite(Green1, HIGH);
    delay(20000);
    digitalWrite(Green1, LOW);
    digitalWrite(Red1, HIGH);
    digitalWrite(Red2, LOW);
    digitalWrite(Green2, HIGH);
    if(count2>=6){
    delay(20000);
    }
    else
    {
      delay(6000);
    }
    digitalWrite(Green2, LOW);
    }

   else if(2 < count1 < 6 && count1 > count2){
    Street_light();
    digitalWrite(Red1, LOW);
    digitalWrite(Green1, HIGH);
    delay(6000);
    digitalWrite(Green1, LOW);
    digitalWrite(Red1, HIGH);
    digitalWrite(Red2, LOW);
    digitalWrite(Green2, HIGH);
    delay(6000);
    digitalWrite(Green2, LOW);
    digitalWrite(Red2, HIGH);
    } 

   else if (count2 >= 6 && count1 < count2 ){
    Street_light();
    digitalWrite(Red2, LOW);
    digitalWrite(Green2, HIGH);
    delay(20000);
    digitalWrite(Green2, LOW);
    digitalWrite(Red2, HIGH);
    digitalWrite(Red1, LOW);
    digitalWrite(Green1, HIGH);
    if(count1>=6){
      delay(20000);
      }
    else{
      delay(6000);
      }
    digitalWrite(Green1, LOW);
    digitalWrite(Red1, HIGH);
    }

   else if (2 < count2 < 6 && count2 > count1){
    Street_light();
    digitalWrite(Red2, LOW);
    digitalWrite(Green2, HIGH);
    delay(6000);
    digitalWrite(Green2, LOW);
    digitalWrite(Red2, HIGH);
    digitalWrite(Red1, LOW);
    digitalWrite(Green1, HIGH);
    delay(6000);
    digitalWrite(Green1, LOW);
    digitalWrite(Red1, HIGH);
    }
   
   
   }




   
void Street_light(){
   int sensorStatus3 = digitalRead(IRSensor3);
  if(sensorStatus3 == 0){
    count3++;
    
   if (count3 < 2){
  digitalWrite(led1,LOW);
  digitalWrite(led2,HIGH);
  digitalWrite(led3,HIGH);
  delay(5000);
  digitalWrite(led1,LOW);
  digitalWrite(led2,LOW);
  digitalWrite(led3,LOW);
  delay(3000);
    }
  else{
  digitalWrite(led1,HIGH);
  digitalWrite(led2,HIGH);
  digitalWrite(led3,HIGH);
  delay(5000);
  digitalWrite(led1,LOW);
  digitalWrite(led2,LOW);
  digitalWrite(led3,LOW);
  delay(3000);
    }
  }
  }

   
