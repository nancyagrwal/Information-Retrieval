import sys 
from compiler.ast import flatten

PageSet = []
nodes=[]
d = 0.85
outlinks = {}
filename = "GraphNodes.txt"
PageRankInit = {}
PageRankNew = {}
dict = {}
i=0

def create_dict(filename): 
   global PageSet, PageRankInit, PageRankNew, dict
   with open(filename, 'r') as file: 
          for line in file: 
            dict[line.split()[0]] = line.split()[1:]

			
   for key in dict.keys(): 
			if key not in flatten(dict.values()): 
				nodes.append(key)
   
   
   for key in dict.keys(): 
		PageSet.append(key) 

		
   for page in dict: 
		formatVal = float(1)/len(PageSet)
		PageRankInit[page] = (float("{0:.3f}".format(formatVal)))

	  
   for key in dict.keys(): 
		outlinks[key]=flatten(dict.values()).count(key)  

  
   find_pageRank(dict, PageRankInit, nodes) 
  
     
def find_pageRank(dict, PageRankInit, nodes): 
   global i, PageSet
   
   while i < 100: 
         sinkPR = 0
         for page in nodes: 
            sinkPR += PageRankInit[page] 
              
         for page in PageSet: 
				a = (1-d)/len(PageSet)
				b = (d*sinkPR)/len(PageSet)
				PageRankNew[page] = a + b
				for q in dict[page]: 
					PageRankNew[page] += (d*PageRankInit[q])/(outlinks[q]) 

         for page in PageSet: 
             PageRankInit[page] = PageRankNew[page] 
  
         i = i + 1
         dict1 = sorted(PageRankInit.iteritems(), key=lambda key_value: key_value[0])
           
         
         if i == 1: 
             print "Iteration 1............"
             for key, value in dict1: 
                print key, (float("{0:.6f}".format(value))) 
             print "\n"

         
         if i == 9: 
             print "Iteration 10.............."
             for key , value in dict1: 
                print key, (float("{0:.6f}".format(value))) 
             print "\n"

         
         if i == 99: 
             print "Iteration 100................"
             for key , value in dict1: 
                print key, (float("{0:.6f}".format(value))) 
             print "\n"
  


if __name__ == "__main__":
   create_dict(filename) 