def func(*args: tuple[dict[str, int|float]]) -> dict[str,int|float]:
   result = dict()
   for arg in args:
      for key, value in arg.items():
         if key in result.keys():
            result[key] +=value
         else:
            result[key] = value
   return result
print(func({1:1,2:3,3:3},{1:5}))
def func2(t= str)->list[str]:
   stats={}
   for sym in t:
      if sym in stats.keys():
         stats[sym] +=1
      else:
         stats[sym] =1
s = sorted(stats.items(), key = lambda item: item[1]), reverse=True)
return [value[0] for value in s]
func2('hghg, hchhd, hdccc')

   


        

 