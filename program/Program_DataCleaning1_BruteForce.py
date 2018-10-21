import re
with open ("ShortRoughData.txt", 'r') as rf:
    with open("ShortCleanData.txt", 'w') as wf:

        myData = rf.readlines() #reading lines of file

        rawData = [] #creating a list of raw data lines

        for line in myData:
            rawData.append(line)
            #print(line) # For debugging

        GeneRaw = []
        GDSRaw = []
        OrganismRaw = []
        SampleRaw = []

        for i in range (0, len(rawData)-8, 7):
            # geneLine = rawData[i+1]  # For debugging
            # print(geneLine)
            GeneRaw.append(rawData[i+1]) # Adding all the lines with Gene names
            #print(rawData[i+1])  # For debugging
            GDSRaw.append(rawData[i+4])  # Adding all the lines with GDS number
            OrganismRaw.append(rawData[i+3])  # Adding all the lines with Organism name
            SampleRaw.append(rawData[i+5])  # Adding all the lines with number of Samples
            #i = i + 7

        Gene = []
        for i in range(0, len(GeneRaw)):  # To filter gene name
            line = GeneRaw[i]
            # print(line)  # For debugging
            geneSubstring = line[3:]  # Removing first 3 characters before the name of gene
            geneUpTo = geneSubstring.find(" ") # Finding the first instance of a whitespace
            geneName = geneSubstring[:geneUpTo] # Creating a substring up to the white space i.e. gene name
            Gene.append(geneName) # Adding cleaned gene name to the List

        Organism = []
        for i in range(0, len(OrganismRaw)):
            line = OrganismRaw[i]
            firstInstance = line.find(" ") + 1 # Finding the index where organism name starts
            organismName = line[firstInstance:]  # Cleaning organism name
            print(len(organismName))
            print(organismName)
            organismName = organismName.replace('\n', '')
            Organism.append(organismName)  # Adding cleaned organism name to the list

        GDS = []
        for i in range(0, len(GDSRaw)):
            line = GDSRaw[i]
            startGDS = line[line.find("GDS"):]
            GDS.append(startGDS[:startGDS.find(",")])

        Sample = []
        for i in range(0, len(SampleRaw)):
            line = SampleRaw[i]
            # Number = re.match('58', SampleRaw[i])
            findSample = line.find("samples") - 1
            beforeSample = line[:findSample]
            # print(beforeSample)  # For debugging
            findNumber = beforeSample.rfind(" ")
            # print(findNumber)  # For debugging
            sampleNumber = line[findNumber+1:findSample]
            print(sampleNumber)  # For debugging
            # sampleNumber = sampleNumber.replace(" ", "")
            # sampleNumber = sampleNumber.replace("\n", "")
            Sample.append(sampleNumber)


        wf.write("SI #" + '\t' + "GENE" + '\t\t' +	"GDS" + '\t\t\t' + "ORGANISM" +	'\t\t' + "SAMPLE" + '\n')
        for i in range(0, len(Gene)):
            symbolNo = str(i+1)
            wf.write(symbolNo + '\t\t' + Gene[i] + '\t\t' + GDS[i] + "\t\t" + Organism[i] + '\t\t' + Sample[i] + '\n')

