#!/usr/bin/env python3

class MyString:
    count = 0
    
    def __init__(self, value=''):
        if isinstance(value, str):
            self.value = value
        else:
            return 'The value must be a string.'
    
    def is_sentence(self):
        if self.value.endswith('.'):
            return True
        else:
            return False

    def is_question(self):
        if self.value.endswith('?'):
            return True
        else:
            return False

    def is_exclamation(self):
        if self.value.endswith('!'):
            return True
        else:
            return False

    def count_sentences(self):
      if not isinstance(self.value, str):
        return  'The value must be a string.'
      
      else:
        sentences = self.value.split()
        count = 0
        for sentence in sentences:
            valid_sentence = MyString(sentence)
            if (valid_sentence.is_sentence() or
                valid_sentence.is_question() or
                valid_sentence.is_exclamation()):
                count += 1
        return count
