# string = input('Enter a string:')


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

def checker4(string):
  string_len = len(string)
  i, j = 0, string_len-1

  while i <= j:
    if string[i] != string[j]:
      print('No palindrome')
      break
    i += 1
    j -= 1
  else:
    print('Palindrome')

if __name__ == '__main__':
  palindromes = ['madam', 'madamiamadam', 'eye', 'mam', 'kanak', 'malayalam']
  non_palindromes = ['bag', 'principal', 'teacher']
  
  for string in palindromes:
    print(string, ':'); checker1(string)
    print(string, ':'); checker2(string)
    print(string, ':'); checker3(string)
    print(string, ':'); checker4(string)
  
  for string in non_palindromes:
    print(string, ':'); checker1(string)
    print(string, ':'); checker2(string)
    print(string, ':'); checker3(string)
    print(string, ':'); checker4(string)
  
