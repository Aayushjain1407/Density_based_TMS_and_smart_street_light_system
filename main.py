# import serial
# # import datetime as dt
# arduino_port = "COM6"
# baud = 9600
# file_name = "sensor1_data1.csv"
# samples = 10
# print_labels = False
#
# ser1 = serial.Serial(arduino_port, baud)
# print("Connected to Arduino port:" + arduino_port)
# # file = open(file_name, "a")
# # print("Created file")
# with open(file_name, "w") as file:
#     print("Created file")
# line = 0
#
# while line <= samples:
#     if print_labels:
#         if line == 0:
#             print("Printing Column Headers")
#         else:
#             print("Line" + str(line) + ":writing..")
#
#     getData = ser1.readline()
#     dataString = getData.decode('utf-8')
#     data = dataString[0:][:-2]
#     print(data)
#     try:
#         file.write(f"{data}\n")
#         file.flush()  # Ensure data is written to the file immediately
#         print("Data written to file.")
#     except Exception as e:
#         print("Error writing to file:", str(e))
#
#     line += 1
# print("Data collection complete!")
# import serial
# import datetime as dt
#
# arduino_port = "COM6"
# baud = 9600
# file_name = "sensor1_data.csv"
# samples = 10
# print_labels = False
#
# ser = serial.Serial(arduino_port, baud)
# print("Connected to Arduino port:" + arduino_port)
#
# try:
#     with open(file_name, "a") as file:
#         print("Created file")
#
#         line = 0
#         while line <= samples:
#             if print_labels:
#                 if line == 0:
#                     print("Printing Column Headers")
#                 else:
#                     print("Line" + str(line) + ": writing..")
#
#             try:
#                 getData = ser.readline()
#                 dataString = getData.decode('utf-8')
#                 data = dataString[:-2]  # Remove the last two characters
#                 current_time = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Get current time
#                 print("Data:", data, "Time:", current_time)
#
#                 file.write(f"{data},{current_time}\n")  # Include current time in the data
#                 file.flush()  # Ensure data is written to the file immediately
#                 print("Data written to file.")
#
#             except Exception as e:
#                 print("Error writing to file:", str(e))
#
#             line += 1
#
# except Exception as e:
#     print("Error:", str(e))
#
# print("Data collection complete!")

import serial
import datetime as dt

arduino_port = "COM6"
baud = 9600
file_name = "sensor1_data1.csv"
samples = 50
print_labels = False

ser = serial.Serial(arduino_port, baud)
print("Connected to Arduino port:" + arduino_port)

try:
    with open(file_name, "w") as file:
        print("Created file")

        line = 0
        while line <= samples:
            if print_labels:
                if line == 0:
                    print("Printing Column Headers")
                else:
                    print("Line" + str(line) + ": writing..")

            try:
                getData = ser.readline()
                dataString = getData.decode('utf-8')
                data = dataString[:-2]  # Remove the last two characters
                current_time = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Get current time
                print("Data:", data, "Time:", current_time)

                file.write(f"{data},{current_time}\n")  # Include current time in the data
                file.flush()  # Ensure data is written to the file immediately
                print("Data written to file.")

            except Exception as e:
                print("Error writing to file:", str(e))

            line += 1

except Exception as e:
    print("Error:", str(e))

print("Data collection complete!")

# import serial
# import datetime as dt
# import csv
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation
#
# class SensorDataLogger:
#     def __init__(self, arduino_port, baud_rate, file_name):
#         self.ser = serial.Serial(arduino_port, baud_rate)
#         self.file_name = file_name
#
#         # Open the CSV file for writing
#         with open(self.file_name, 'w', newline='') as csvfile:
#             csv_writer = csv.writer(csvfile)
#             csv_writer.writerow(["Timestamp", "Sensor_status", "Car_count_1", "Car_count_2", "Street_light_cars"])
#
#         # Initialize plot data
#         self.data = {"Timestamp": [], "Car_count_1": [], "Car_count_2": [], "Street_light_cars": []}
#         self.fig, self.ax = plt.subplots(figsize=(10, 6))
#
#         # Create an animation
#         self.ani = FuncAnimation(self.fig, self.update_and_write, interval=1000)
#
#     def update_and_write(self, frame):
#         line = self.ser.readline().decode('utf-8').strip()
#
#         # Print received line for debugging
#         print(f"Received line: {line}")
#
#         # Skip lines that start with headers
#         if line.startswith('Sensor_status'):
#             return
#
#         values = line.split(',')
#
#         if len(values) == 4:
#             timestamp = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#             sensor_status, count1, count2, count3 = map(int, values)
#
#             # Append data to the plot data dictionary
#             self.data["Timestamp"].append(timestamp)
#             self.data["Car_count_1"].append(count1)
#             self.data["Car_count_2"].append(count2)
#             self.data["Street_light_cars"].append(count3)
#
#             # Print the data to the terminal for debugging
#             print(f"Timestamp: {timestamp}, Car_count_1: {count1}, Car_count_2: {count2}, Street_light_cars: {count3}")
#
#             # Write data to the CSV file
#             with open(self.file_name, 'a', newline='') as csvfile:
#                 csv_writer = csv.writer(csvfile)
#                 csv_writer.writerow([timestamp, sensor_status, count1, count2, count3])
#
#             # Update the plot
#             self.ax.clear()
#             self.ax.plot(self.data["Timestamp"], self.data["Car_count_1"], marker='o', label="Car_count_1")
#             self.ax.plot(self.data["Timestamp"], self.data["Car_count_2"], marker='o', label="Car_count_2")
#             self.ax.plot(self.data["Timestamp"], self.data["Street_light_cars"], marker='o', label="Street_light_cars")
#             self.ax.set_title('Car Counts Over Time')
#             self.ax.set_xlabel('Timestamp')
#             self.ax.set_ylabel('Car Counts')
#             self.ax.legend()
#
#     def show_plot(self):
#         plt.show()
#
#     def close_serial(self):
#         # Close the serial connection when the plot is closed
#         self.ser.close()
#
# # Instantiate the SensorDataLogger
# sensor_logger = SensorDataLogger("COM6", 9600, "sensor_data.csv")
#
# # Show the plot
# sensor_logger.show_plot()
#
# # Close the serial connection when the plot is closed
# sensor_logger.close_serial()
