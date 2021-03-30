
# coding: utf-8

# In[ ]:


import time
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
            
if __name__ == '__main__':
    countdown(3)

