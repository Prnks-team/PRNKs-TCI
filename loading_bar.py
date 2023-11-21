from alive_progress import alive_bar 
import time
with alive_bar(1200000, ctrl_c='b', unit='b', scale='SI', precision=2) as bar: 
               for I in range(1200000): 
                bar()