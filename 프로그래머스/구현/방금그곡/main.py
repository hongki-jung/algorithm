from datetime import datetime
import math

def melody_change(m):
    
    if 'C#' in m:
        m = m.replace('C#','c')
    if 'D#' in m:
        m = m.replace('D#','d')
    if 'F#' in m:
        m = m.replace('F#','f')
    if 'G#' in m:
        m = m.replace('G#','g')
    if 'A#' in m:
        m = m.replace('A#','a')

        
    return m



def solution(m, musicinfos):
    
    
    
    answer = None

    new_data = []
  
    
    max_play_time = 0
    m = melody_change(m)
    
    for musicinfo in musicinfos:
        
        start_time, end_time, name, melody = musicinfo.split(',')
        

        play_time = int(end_time[:2])* 60 + int(end_time[3:]) - int(start_time[:2]) * 60 - int(start_time[3:])
        
        
        melody = melody_change(melody)
        melody_repeated_count = play_time//len(melody)+1
        print("melody_repeated_count ",melody_repeated_count)
        melody_played = (melody * melody_repeated_count)[:play_time]
        
        
        if m in melody_played and play_time > max_play_time:

            answer = name
            max_play_time = play_time
            
    if answer is None:
        return "(None)"
                    

    return answer
    