string = input('Enter a string:')


def checker1(string):
  string_len = len(string)
  flag = True
  for i in range(string_len):
    if string[i] != string[string_len-1-i]:
       flag = False
       print('No palindrome')
       break
  if flag:
    print('Palindrome')


def checker2(string):
  string_len = len(string)
  for i in range(string_len):
    if string[i] != string[string_len-1-i]:
      print('No palindrome')
      break
  else:
    print('Palindrome')

def checker3(string):
  string_len = len(string)
  
  for i in range(string_len // 2):
    if string[i] != string[string_len-1-i]:
      print('No palindrome')
      break
  else:
    print('Palindrome')

checker1(string)
checker2(string)
checker3(string)
checker2('madamimadam')
