def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    #Add code here to calculate BMI
    bmi = weight/(height*height)
    #Add code here to display calculate BMI
    print(bmi)
    if(bmi<18.5):
      print("underweight")
    elif(bmi>25):
      print("overweight")
    else:
      print("normalweight")
calculate_bmi(weight=57, height=1.73)