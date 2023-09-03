# To run this file you must first install this program: https://github.com/autotrace/autotrace
# Also you should have imagemagick installed
import os


for filename in os.listdir('png'):
  #print("autotrace png/" + filename + " -output-format svg -output-file svg/" + os.path.splitext(filename)[0] + ".svg")
  os.system("autotrace png/" + filename + " -output-format svg -output-file svg/" + os.path.splitext(filename)[0] + ".svg")
