"""
Given a dictionary, write a function to flatten it. Consider the following input/output scenario
 for better understanding:
 Input:
 {
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
 Output:
 {
  'Key1': '1',
  'Key2.a': '2',
  'Key2.b' : '3',
  'Key2.c.d' : '3',
  'Key2.c.e' : '1'
 }

"""


def flatten_dict(to_flatten):
    flattened = {}  # { Key1+'' : '1' }
    for key in to_flatten:  # 'Key1, Key2'
        rec_flatten(to_flatten, key, flattened)  # dict, Key1, {} | dict, Key2, { ''+Key1 : '1' }
    return flattened


def rec_flatten(to_flat, key, result, key_mod=''):
    if type(to_flat[key]) != dict():  # T | F | T
        result[key_mod + str(key)] = to_flat[
            key]  # result = { ''+Key1 : '1' } | results = { ''+Key1 : '1' , Key2.a : '2'}
        return None
    for depth_key in to_flat[key]:  # 'a'
        rec_flatten(to_flat, depth_key, result, str(key) + '.')  # dict, 'a', { Key1+'' : '1' }, 'Key2.'
    return None
