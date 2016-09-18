"""
Input:
{
  'Key1': '1',
  'Key2':
  {
    'a' : '2',
    'b' : {
      'c' : 3
    }
  }
}
Output:
{
  'Key1': '1',
  'Key2.a': '2'
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
