def isLandscape(width,height):
  if width>height:
    return "Landscape"
  else:
    return "Portrait"
  
w = float(input("Enter image width: "))
h = float(input("Enter image height: "))
print(isLandscape(w,h))