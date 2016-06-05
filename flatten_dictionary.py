the_dict = {
  'Key1': '1',
  'Key2': {
    'a' : '2',
    'b' : '3',
    'c' : {
      'd' : '3',
      'e' : '1'
      }
    }
}

# for element in the_dict.keys():
#     if type(the_dict[element]) is dict:
#         print "is_dict"
#     else:
#         print "not_a_dict"

for element in the_dict.keys():
    if isinstance(the_dict[element],dict):
        print "is_dict"
    else:
        print "not_a_dict"
