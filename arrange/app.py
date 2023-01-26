import os
import time
import shutil

def file_creation_date(file_name: str) -> str:
    """
    Operation: Takes file name and returns the date of creation of file
                which can be used to create a directory for the file

                The format of the date is: dd/mm/yyyy

    Input(s): file name(file_name: str)
    Return(s): creation date(creation_date: str)
    """
    #get last modified date
    last_modified_time = os.path.getmtime(file_name)
    #converting to local time
    local_time = time.ctime(last_modified_time)
    #converting to a date-time  object
    date_time_obj = time.strptime(local_time)
    #convert date-time object to string representation
    time_stamp = time.strftime("%Y-%m-%d %H:%M:%S", date_time_obj)
    #getting the date
    creation_date = time_stamp.split(" ")[0]
    #changing the format of the date to dd/mm/yyyy
    final_date = creation_date.split("-")[2] + \
            "-" + creation_date.split("-")[1] + \
            "-" + creation_date.split("-")[0]

    return final_date


def file_dir_listing() -> list:
    """
    Operation: Returns two lists containing the names of all the files
                and all the directories inside the current working directory

    Input(s): N/A
    Return(s): List containing file names(file_name_list)
                List containing directory names(dir_name_list)
                Return format => (file_name_list, dir_name_list)
    """
    
    #lists all the contents of the current working directory
    dir_list = os.listdir()
    #filters the files into a list
    file_name_list = [filename for filename in dir_list if os.path.isfile(filename)]
    #filters the folders into a list
    dir_name_list = [dirname for dirname in dir_list if not os.path.isfile(dirname)]

    return (file_name_list, dir_name_list)


def create_dir_mov_files():
    """
    Operation: Get's all the file names in the directory, creates and moves
                these files into a directory which has the same name as the
                file creation date
    Input(s): N/A
    Return(s): N/A 
    """
    #filtering the directory contents into file and sub-directory names
    file_names, dir_names = file_dir_listing()
    #iterating through filenames for creating directories
    for fname in file_names:
        #get the creation date of a file. This can be used as a directory name
        date_created = file_creation_date(fname)
        #checking if the directory already exists
        if date_created not in dir_names:
            #creating the directory
            os.mkdir(date_created)
            #moving file to the freshly created directory
            shutil.move(fname, date_created)
        else:
            #moving file to the proper directory
            shutil.move(fname, date_created)


