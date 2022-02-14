
#from os import system
from neuspell import SclstmelmoChecker
import os
import neuspell
'''
neuspell.seq_modeling.downloads.download_pretrained_model(
    "subwordbert-probwordnoise")'''
neuspell.seq_modeling.downloads.download_pretrained_model(
    "scrnn-probwordnoise")
'''
neuspell.seq_modeling.downloads.download_pretrained_model(
    "_all_")



""" see available checkers
print(f"available checkers: {neuspell.available_checkers()}")
# → available checkers: ['BertsclstmChecker', 'CnnlstmChecker', 'NestedlstmChecker', 'SclstmChecker', 'SclstmbertChecker', 'BertChecker', 'SclstmelmoChecker', 'ElmosclstmChecker']"""

""" select spell checkers & load """
checker = SclstmelmoChecker()
checker.from_pretrained()
system('cls')

""" spell correction """
print(checker.correct("pi"))
# → "I look forward to receiving your reply"
'''
