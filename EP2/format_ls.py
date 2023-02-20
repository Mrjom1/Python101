Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> name = 'Jom'
>>> print(name)
Jom
>>> 
>>> type(name)
<class 'str'>
>>> 
>>> name.lower()
'jom'
>>> name.upper()
'JOM'
>>> 
>>> friend = 'สมชาย'
>>> print('สวัสดีสมชาย สบายดีไหม?')
สวัสดีสมชาย สบายดีไหม?
>>> 
>>> print('สวัสดี' + friend + ' สบายดีไหม?')
สวัสดีสมชาย สบายดีไหม?
>>> 
>>> money = 10
>>> print(friend + 'ยืมเงิน ' + str(money) + ' บาท')
สมชายยืมเงิน 10 บาท
>>> 
>>> print('{} ยืมเงิน {} บาท' .format(friend, money))
สมชาย ยืมเงิน 10 บาท
>>> 
>>> print(f '{friend} ยืมเงิน {money} บาท ')
SyntaxError: invalid syntax
>>> print(f' {friend} ยืมเงิน {money} บาท')
 สมชาย ยืมเงิน 10 บาท
>>> 
>>> money = 1234567890123456
>>> print(f' {money:,}')
 1,234,567,890,123,456
>>> print(f' {money:,.2f}')
 1,234,567,890,123,456.00
