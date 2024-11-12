"""BMI Category
A person's body mass index is a simple calculation based on height and weight that classifies that person as underweight, overweight, or normal. The formula for the metric unit is, BMI=weight in kilograms/ (height in meters)^2
You are given an integer weight and a floating- point number height of a person as input.Calculate the BMI of the person and print the person's BMI category as per the given rules:
1.If BMI<18 print 0.
2.If 18 >= BMI < 25 print 1.
3.If 25 >= BMI < 30 print 2
4.If 30 >= BMI < 40 print 3
5.If BMI >= 40 print 4

Input Format:
Each testcase consists of two lines of input:
The first line of input contains an integer, i.e. weight in kilograms.
The second line contains a float number, i.e height in meters

Output Format:A single integer, i.e. person's BMI category

Example:
Input:
42
1.54
Output:0
"""

def bmi_category(weight, height):
    # Calculate BMI
    bmi = weight / (height ** 2)
    
    if bmi < 18:
        return 0
    elif 18 <= bmi < 25:
        return 1
    elif 25 <= bmi < 30:
        return 2
    elif 30 <= bmi < 40:
        return 3
    elif bmi >= 40 :
        return 4

weight = 42
height = 1.54
print(bmi_category(weight, height))

