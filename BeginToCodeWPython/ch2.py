'''Just little examples in the book'''
def ch2():
    print("CH 2")
    print(ord("W")) #ordinal num
    print(ord("w"))
    print(chr(87)) #char rep of ord num
    print(chr(53))
    print(bin(87)) #binary representation

def ch3():
    print("CH 3")
    print(2+2)

    import random
    print("A Random number from [1,6]")
    print(random.randint(1,6))

    import time
    #you can pause your program for a given time 
    print("I need to think")
    time.sleep(5) #sleep for 5 seconds
    print("I have thought")

import snaps  #snaps is file from author to use with book examples
import time
def ch3_display():
    #snaps.display_message("hello world")
    snaps.display_message("this is a smaller text in green on the top left", color=(0,255,0), size=50, horiz='left', vert='top')

    time.sleep(5) #needed to add this or it would just flash on screen wouldn't get a chance to see it 

def ch3_05():
    snaps.display_image("capstone.png")
    snaps.display_message("my capstone", color=(2,2,2), vert="top")
    snaps.play_sound("ding.wav")
    time.sleep(3)
    

def create_staircase(nums):
  step = 1
  subsets = []
  while len(nums) != 0:
    if len(nums) >= step:
      subsets.append(nums[0:step])
      nums = nums[step:]
      step += 1
    else:
      return False
      
  return subsets

#ch3_display()
#ch3_05()
#print(create_staircase([1, 2, 3, 4, 5, 6]))