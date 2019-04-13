import sys
print(sys.path[0])

# from sys.path[0] import test_module
tm_path = sys.path[0] + '\\test_module.py'

# import tm_path
import test_module
from project_utils import extract_text

print(test_module.VAR)