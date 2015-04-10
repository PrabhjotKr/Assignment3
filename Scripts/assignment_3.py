import os
import understand

from db import insert
from db import createTable;


createTable();
def gf(function):
    functionList = []
    funcList = function.ents("","function,method,procedure")

    if funcList == None:
        return False

  
    for function in funcList:
        if function.library() == "Standard":
            continue
        if function.name() != function.name():
            functionList.append(function.name())

    return functionList


def isdependent( func2, func1Related):

  

    if func2.name() not in func1Related:
     
        return False
    else:
        return True

def processLCOM(file):
    functions  = file.ents("","function,method,procedure")
    funcSet = set()

    for func1 in functions:
        if func1.library() == "Standard":
            continue
        func1Related = gf(func1)
        for func2 in functions:
            if func2.library() == "Standard":
                continue
            if(func1 != func2) & isdependent( func2, func1Related):
                funcSet = funcSet | set([frozenset([func1.name(), func2.name()])])
    return inter(funcSet,functions);

  
def inter(funcSet,functions):
        graphs = []
        for pair in funcSet:
           
            if len(graphs) <=0:
                graphs.append(pair)
            else:
                processed = False
                for graph in graphs:
                    i = graphs.index(graph)
                    if len(graph & pair) > 0:
                        graph |= pair
                        graphs[i] = graph
                        processed = True
                if not processed:
                    graphs.append(pair)

        count = 0
   
        for graph in graphs:
          
            count += len(graph)

        lcom = len(graphs)

        lcom += len(functions) - count
        return lcom;   
 
 
 # Calculate LCOM
         
def calculateLCOM(file):


    return processLCOM(file);
    
 # Calculate CBO
    
def CalCBO(file):
    classes  = file.ents("","Class")

    count = 0
   
    return countRelatedObjects(classes);

 
def countRelatedObjects(classes):
     count=0;
     for cls in classes:
        if cls.library() != "Standard":
           count += 1
        
        

     return count
if __name__ == "__main__":
    
    ver=['31','32','33','34']
    
    for version in ver: 
        path="C:\\Users\\Sukh\\workspace\\understand\\"+str(version)+".udb";
        print(path);   
        db = understand.open(path)

        for file in db.ents("File"):

          if(file.library() == "Standard"):
              continue

          fileName, fileExtension = os.path.splitext(str(file))
          if fileExtension == ".cpp" or fileExtension == ".cc" :
            lcom = calculateLCOM(file)
            cbo = CalCBO(file)
            print( "Class: ",file, " LCOM: ",lcom, " CBO: ", cbo)
            
            insert(version, file.name(), lcom, cbo)
     
        db.close()
