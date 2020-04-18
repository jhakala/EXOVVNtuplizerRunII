
def getQueries():
  queries = {
    "GJets" : 'dasgoclient --query="dataset dataset=/GJets_HT*_TuneCP5*/*PU2017*/MINIAODSIM" | grep -v -e pmx -e 40To',
    "QCD"   : 'dasgoclient --query="dataset dataset=/QCD_HT*_TuneCP5*/*PU2017*/MINIAODSIM" | grep -v -e BGen | grep -v pmx',
  }
  return queries

import subprocess
import shlex
def handle_pipe(query):
  chunks = query.split("|")
  ps = subprocess.Popen("true")
  while len(chunks) > 1:
    chunk = chunks.pop(0)
    ps = subprocess.Popen(shlex.split(chunk), stdout=subprocess.PIPE, stdin=ps.stdout)
    ps.wait()
  chunk = chunks.pop()
  output = subprocess.check_output(shlex.split(chunk), stdin=ps.stdout)
  return output.splitlines()

def query_files(dataset):
  return subprocess.check_output(shlex.split("dasgoclient --query='file dataset=%s'" % dataset))

if __name__ == "__main__":
  print "making sample lists from dict", queries
  totalFiles = 0
  queries = getQueries()
  for query in queries.keys():
    print "  working on query '%s' samples" % query
    datasetNames = handle_pipe(queries[query])
    totalDatasets = len(datasetNames)
    queryFiles = 0
    for datasetName in datasetNames:
      print "    working on dataset %s" % datasetName
      sampleListFileName = datasetName.split("/")[1]+".sl"
      with open("sampleLists/" + sampleListFileName, "w") as sampleList:
        nFiles = 0
        for line in query_files(datasetName).splitlines():
          sampleList.write(line + "\n")
          nFiles += 1
        print  "    dataset files = %i" % nFiles
        queryFiles += nFiles
    print "  query files = %i" % queryFiles
    totalFiles += queryFiles
  print "total files = %i " % totalFiles 
  print "done"
  
