print("Toh deviyo aur sajno, aapka swagat hai, Kaun Bnega Crorepati mein")
print("aapke screen m kuch questions aayenge, you have to answer them by selecting one of the four options, LETS GET STARTED")
q=["1.who's the prime minister of india","who is the president of india","who is the fastest runner in the world"]
a1=["me","you","narendramodi","pappu"]
a2=["me","you","draupadi","pappu"]
a3=["me","usain bolt","you","pappu"]
c=0
for i in q:
  print(i)
  if i=="1.who's the prime minister of india":
    print(a1)
    z=int(input())
    if z==3:
      print("correct")
      c=c+500
      continue
    else:
      print("wrong, U LOST!")
    break
    
  elif i=="who is the president of india":
    print(a2)
    z=int(input())
    if z==3:
      print("correct")
      c=c+500
      pass
    else:
      print("wrong, u LOST!")
      break
    
  elif i=="who is the fastest runner in the world":
    print(a3)
    z=int(input())
    if z==2:
      print("correct")
      c=c+500
      print("oh em zi, you won",c,"rs, U WON KBC!!")
    else:
      print("wrong")
    
