'''
TODO - CLI app
'''
import argparse
import datetime
import os

FILELOC = "C:\\Users\\aldee\\.todo"

# Argparse
parser = argparse.ArgumentParser(description='Tasks for ToDo app')

parser.add_argument("-a", "--add",
                    type=str,
                    nargs='*',
                    help="Add a new task",
                    dest='task'
                    )

parser.add_argument("-s", "--status",
                    nargs='*',
                    type=str,
                    help="change the status of task ID(todo, curr, done)",
                    dest="taskID"
                    )

parser.add_argument("-d", "--delete",
                    type=str,
                    help="Delete a task ID",
                    dest="DeleteID"
                    )

parser.add_argument("-l", "--list",
                    action='store_true',
                    help="List all existing tasks"
                    )

args = parser.parse_args()


# To add a new task to todo list
def addTask(task):
    line = f"{currLen+1}. [ {str(datetime.datetime.now())} ] [ ToDo ] [ {task} ]"
    # line = f"{currLen + 1} {task}"
    f = open(FILELOC, "a+")     # Append data
    f.write(line)
    f.write("\n")
    f.close()

# Deletes an existing task
def deleteTask(n):
    # To-Do : Currently the line gets deleted but the IDs do not changez
    deleted = False
    with open(FILELOC, "r+") as f:
        oldContent = f.readlines()
        f.seek(0)
        for line in oldContent:
            if n != line[0]: 
                f.write(line)
            else:
                deleted = True
        f.truncate()
        if not deleted:
            print("[X] Error: The specified Task ID doesn't exist")
    pass


# Updates status of task to todo, curr or done
def updateStatus(n, status):
    changed = False
    with open(FILELOC, "r+") as f:
        oldContent = f.readlines()
        f.seek(0)
        for line in oldContent:
            if line[0] != n:
                f.write(line)
            else:
                newLine = line[:36] + status + line[40:]
                f.write(newLine)
                changed = True
    if not changed:
        print("[X] Error: The specified Task ID doesn't exist")
    pass

def listTasks():
    for line in currContent:
        print(line)

def main():
    # print(f"Args passed: {args}\n")
    if args.task is not None:
        newTask = ' '.join(args.task)
        # print(f"Task to add---> {newTask}")
        addTask(newTask)
        # exit(0)
    
    if args.DeleteID is not None:
        deleteTask(args.DeleteID)
        exit(0)
    
    if args.taskID is not None:
        print(f"Change status flag is set : {args.taskID}")
        updateStatus(args.taskID[0], args.taskID[1])
        exit(0)

    if args.list:
        listTasks()



if __name__ == "__main__":
    try:
        f = open(FILELOC, "r")
    except FileNotFoundError:
        f = open(FILELOC, "a+")
    
    global content, currLen
    currContent = f.readlines()
    currLen = len(currContent)
    f.close()
    
    main()
    
    # f = open(FILELOC, "r")
    # currContent = f.readlines()
    # print(f"Content after: \n{currContent}")
    # f.close()
