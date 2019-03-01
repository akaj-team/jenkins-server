import sys
import xml.etree.cElementTree as ET
from shutil import copyfile
import string
import fileinput
import os  
import glob
import shutil

browser = sys.argv[1]
count = sys.argv[2]
testRunnerFileName="Parallel"+browser.capitalize()+"TestRunnerGenerate"
testRunnerGeneratePath="src/test/java/generate/"
print ('Create: ', count+' '+browser+' threads')
templateFilePath = 'src/test/java/ParallelTestRunner.java'
if os.path.isdir("src/test/java/generate"):
  shutil.rmtree('src/test/java/generate')

os.makedirs("src/test/java/generate/")
for i in range(1,int(count)+1):
  testRunnerFilePath = testRunnerGeneratePath + testRunnerFileName+str(i)+".java"
  copyfile(templateFilePath, testRunnerFilePath)
  with fileinput.FileInput(testRunnerFilePath, inplace=True) as file:
      for line in file:
        if file.isfirstline():
         print('package generate;')
        if 'ParallelTestRunner' in line:
         print(line.replace("ParallelTestRunner",testRunnerFileName+str(i)),end='')
        elif 'CucumberTestReport' in line:
         print(line.replace('CucumberTestReport',browser.capitalize()+'CucumberTestReport'+str(i)),end='')
        else:
         print(line,end='')
  file.close()

suite = ET.Element("suite",name="Suite")
ET.SubElement(suite,"parameter",name="server",value="http://172.16.110.169:4444/wd/hub")
ET.SubElement(suite,"parameter",name="browserName",value=browser)
parameter={
	'name':browser.capitalize()+' Test',
	'parallel':'methods',
	'thread-count':count
}
test = ET.SubElement(suite, "test",**parameter)
classes = ET.SubElement(test, "classes")
for i in range(1,int(count)+1):
    ET.SubElement(classes, "class", name='generate.'+testRunnerFileName+str(i))
tree = ET.ElementTree(suite)
tree.write(open('src/test/resources/GridParallelSuite.xml',"wb"))	

os.system("mvn clean test")
if not os.path.isdir("jsontarget"):
   os.makedirs("jsontarget")
source = os.listdir("target/cucumber-reports")
destination = "jsontarget/"
for files in source:
    if files.endswith(".json"):
        shutil.copy("target/cucumber-reports/"+files,destination)