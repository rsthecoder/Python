# Write a function that outputs the transcription of an input number with two digits.
# Example:
# 28---------------->Twenty Eight\

def reading_number(number):
    try:
        number = str(number)

        if len(number) != 2:
            return ("Enter two digit number!")

        tens_digit_dic = {1:"Ten", 2:"Twenty", 3:"Thirty", 4:"Forty", 5:"Fifty", 6:"Sixty", 7:"Seventy", 8:"Eighty",9:"Ninety"}
        units_digit_dic = {1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight",9:"Nine"}
        digits_ten_to_twenty = ["Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]        

        unit_digit = int(number[1])
        ten_digit = int(number[0])
        
        if unit_digit == 0: #10,20,30,40...
            return (tens_digit_dic[ten_digit])
        elif ten_digit == 1: #11,12,13
            return (digits_ten_to_twenty[unit_digit -1])
        else:
            return (tens_digit_dic[ten_digit] + " " + units_digit_dic[unit_digit])
    except:
        return ("Please enter a NUMBER!!!")


print(reading_number(6)) #Enter two digit number!
print(reading_number(11)) #Eleven
print(reading_number(10)) #Ten
print(reading_number(16)) #Sixteen
print(reading_number(30)) #Thirty
print(reading_number(56)) #Fifty Six
print(reading_number(99)) #Ninety Nine
print(reading_number(999)) # Enter two digit number!
