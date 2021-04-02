
# coding: utf-8

# In[1]:


'''ver 0.1.0
    function: multiple countdown
    bug: multiple dispaly
'''
'''ver 0.0.2 
    function: coutdown any setting time( format is hh:mm:ss )
    function: legal check
'''

import time
import threading

'''obsolete code(ver 0.0.1)

def countdown(h):
    h = int(h)
    while True:
        
        #for value in range (start,stop,step)
        
        for hour in range(h,-1,-1): 
            if hour == 0:
                break
            for min in range(59,-1,-1):
                if min == 0:
                    break
                for sec in range(59,-1,-1):
                    
                    #tread will sleep/sec
                    
                    time.sleep(1)
                    
                    #when number width less than 2, format output(0:00:0 -> 00:00:00)
                    
                    print('{:02d}:{:02d}:{:02d}'.format(h-1, min, sec), end = ' \r')
            
            print("timer is end.")
            break
'''

def countdownMix(h,m,s): # Mix = 1.secCount -> 2.minCount -> 3.hourCount
    #legal data: 1.h & m & s must be integer number.  2.m & s should less than 60
    try:
        h = int(h)
        m = int(m)
        s = int(s)
    except ValueError:
        print('illegal value！')
    if (m >= 60 or s >= 60):
        raise Exception('minute and second enter should less than 60') 
    
    for sec in range(s,-1,-1):
        time.sleep(1)
        print('{:02d}:{:02d}:{:02d}'.format(h, m, sec), end = '\r\n')
    
    for min in range(m,-1,-1):   
        if min == 0:
            break
        for sec in range(59,-1,-1):   
            time.sleep(1)
            print('{:02d}:{:02d}:{:02d}'.format(h, min-1, sec), end = ' \r')

    for hour in range(h,-1,-1): 
        if hour == 0:
            break
        for min in range(59,-1,-1):
            if min == 0:
                break
            for sec in range(59,-1,-1):
                time.sleep(1)                  
                print('{:02d}:{:02d}:{:02d}'.format(h-1, min, sec), end = ' \r')
                
    print("timer is end.")

    
if __name__ == '__main__':
    support1 = threading.Thread(target = countdownMix, args = (0, 0, 5))
    support2 = threading.Thread(target = countdownMix, args = (0, 0, 10))
    support3 = threading.Thread(target = countdownMix, args = (0, 0, 15))
    support4 = threading.Thread(target = countdownMix, args = (0, 0, 20))
    support1.start()
    support2.start()
    support3.start()
    support4.start()
    support1.join()
    support2.join()
    support3.join()
    support4.join()
    

