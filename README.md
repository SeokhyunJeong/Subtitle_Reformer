# Subtitle_Reformer
This is for the English subtitle internship of SSAI @ SNU.

-Usage
1. Download the package "parse" in your Python.
2. Put your input txt file in the folder where the python file exists, after you fix errors.
3. Open python file, and modify line 4 to your txt file name.
  Example:
    If your filename is 'mysubtitle.txt',
    modify the code line 4 like this.

      Before: with open('2_2.txt', 'r', encoding='UTF-8') as f:
      After:  with open('mysubtitle.txt', 'r', encoding='UTF-8') as f:

    Also, modify the code line 48 to the output filename you desire.
    If you want output file with name 'mylovelysubtitle.txt',
    modify the code line 48 like this.

      Before: with open('2_2mod.txt', 'w') as w:
      After:  with open('mylovelysubtitle.txt', 'w') as w:
    
4. If you open the output file, you will see the complete subtitle file.

!DOCTYPE html
-Input format of text
The input has to be txt file.
This file consists of 4 types of sentences:
  linetype 0: index of the line
  linetype 1: timestamp of the subtitle.
  linetype 2: the subtitle inself.
  linetype 3: line break('\n')

Example:
<pre><code>
  1
  00:00:03,130 --> 00:00:09,999
  Hello, eveyone.

  2
  00:00:10,123 --> 00:00:22,683
  Today we will going to study about pop music. The pop music is a part of modern music.

  3
  00:00:24,090 --> 00:00:45,012
  Isn't it interesting? Alright, see you next time.
</code></pre>  
Well, this form is exactly what the auto translator makes so you don't have to worry about the format.
Just put your txt file, after fixing errors of auto translator.


-Output format
The output is formed by these criteria.
  1. The end time of Kth timestamp is modified to the start time of K+1th timestamp. It can be a solution for the blinking problem.
  2. The subtitle is stacked.
  3. The stack will be erased if 
      1) The difference between second of current start time and previous end time is same of larger than 2.
          00:12:34:567 --> 00:12:"35":568
          # 00:12:"37":789 --> 00:12:40:100
          # 37 - 35 >= 2 so the subtitle window is cleared.
          # We assume that this case the lecturer goes to the new slide.
      2) More than 5 timestamps are stacked.
          We assume that there are too many words in the window.
          
Output example:
<pre><code>
  1
  00:00:03,130 --> 00:00:10,123
  Hello, eveyone.
  ##########end time is modified to the next start time.

  2
  00:00:10,123 --> 00:00:24,090
  Hello, eveyone.
  Today we will going to study about pop music. The pop music is a part of modern music.
  ##########The sentences are stacked.

  3
  00:00:24,090 --> 00:00:45,012
  Isn't it interesting? Alright, see you next time.
  ##########The stack is cleared because the starttime second is 24 and the previous endtime was 22.
</code></pre>
  
 
 
