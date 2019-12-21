from io import StringIO  # Python3
import imp, os
 
import sys
 
# Store the reference, in case you want to show things again in standard output
 
old_stdout = sys.stdout
 
# This variable will store everything that is sent to the standard output
 
result = StringIO()
 
sys.stdout = result
 
# Here we can call anything we like, like external modules, and everything that they will send to standard output will be stored on "result"
home_dir = os.path.expanduser("/Users/amermriziq/Engineering/BUS194A/nida/")
my_module_file = os.path.join(home_dir, "hypothesis.py")

hypothesis = imp.load_source("hypothesis.py", my_module_file)
hypothesis
# import hypothesis as h

#h.hypthesis_1(pval_1, alpha)
#h.hypthesis_2(pval_2, alpha)
# Redirect again the std output to screen
 
sys.stdout = old_stdout
 
# Then, get the stdout like a string and process it!
 
result_string = result.getvalue()
result.close()
print(result_string)