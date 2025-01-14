import os
import shutil
import psutil
import pandas as pd
import seaborn as sns
import numpy as np

print("Press 1 to use File Organizer\n Press 2 for Data Cleaning\n Press 3 for System maintainance.")
task = int(input("Enter which task you want to do: "))

if task == 1:
    path = input("Enter path: ")
    files = os.listdir(path)
    for file in files:
        filename, extension = os.path.splitext(file)
        extension = extension[1:]
        
        if os.path.exists(path+"/"+extension):
            shutil.move(path+"/"+file,path +"/" + extension+"/"+file)
        else:
            os.makedirs(path+"/"+extension)
            shutil.move(path+"/"+file,path +"/" + extension+"/"+file)
            
elif task == 2:
    file = input("Enter the file you need for data cleaning.")
    df = pd.read_csv(file)
    print("Press 1 if you want to remove all of the rows having  'N/A' , 2. To remove only the rows having one column of N/A, 3. To fill all rows with a value of your choice, 4. to fill the N/A values with the values of the next row, 5. to have the average of the previous and next rows")
    choice = int(input("Enter the work you want done for the file"))
    if choice == 1:
        df.dropna()
    elif choice == 2:
        df.dropna(how="all")
    elif choice == 3:
        a = int(input("Value to replace N/A's"))
        df.fillna(a)
    elif choice == 4:
        df.fillna(method="ffill")
    elif choice == 5:
        df.fillna(method="bfill")
    elif choice == 6:
        df.interpolate()
    
    
elif task == 3:
    def check_disk_usage():
        usage = shutil.disk_usage("/")
        print(f"Disk Usage: Total: {usage.total // (1024**3)} GB, Used: {usage.used // (1024**3)} GB, Free: {usage.free // (1024**3)} GB")

    def monitor_cpu_usage():
        print(f"CPU Usage: {psutil.cpu_percent()}%")
    def delete_temp_files():
        temp_dir = os.getenv("TEMP")  
        for item in os.listdir(temp_dir):
            path = os.path.join(temp_dir, item)
            try:
                if os.path.isfile(path) or os.path.islink(path):
                    os.unlink(path)  
                elif os.path.isdir(path):
                    shutil.rmtree(path)  
            except Exception as e:
                print(f"Failed to delete {path}: {e}")
        print("Temporary files deleted.")
        if __name__ == "__main__":
            print("Starting Windows Maintenance...")
            check_disk_usage()
            monitor_cpu_usage()
            delete_temp_files()
            print("Maintenance Completed.")

    check_disk_usage()
    monitor_cpu_usage()
    delete_temp_files()
