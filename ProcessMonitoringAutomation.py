import os;
import sys;
import psutil;
import time;
import schedule;

def ProcessDisplay(path="log"):
    
    if not os.path.exists(path):
        os.mkdir(path);
    
    filename = os.path.join(path,"Marvellous%s.txt"%time.time());
    fobj = open(filename,'w');
    print("Running processess");
    
    for pobj in psutil.process_iter():
        fobj.write(str(pobj));

    fobj.close();

def main():
    
    schedule.every(1).minute.do(ProcessDisplay,path=sys.argv[1])
    
    while True:
        schedule.run_pending()
        time.sleep(1)
    

if __name__ == "__main__":
    main();
    
    