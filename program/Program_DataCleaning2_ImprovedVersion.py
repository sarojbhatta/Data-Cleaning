
with open ("geoprofiles_result_LC_Data.txt", 'r') as rf:
    with open("geoprofiles_result_LC_Data_CLEANED.txt", 'w') as wf:

        myData = rf.readlines() #reading lines of file

        rawData = [] #creating a list of raw data lines

        for line in myData:
            rawData.append(line)
            #print(line) # For debugging

        #CleanData = []  # Just in case needed
        symbolNo = 0
        wf.write("SI #" + '\t' + "GENE" + '\t\t' + "GDS" + '\t\t' + "ORGANISM" + '\t\t' + "SAMPLE" + '\n')

        for i in range (0, len(rawData)-8, 7):

            # For gene name
            line = rawData[i+1] # Adding all the lines with Gene names
            startGene = line.find(".") + 2
            geneSubstring = line[startGene:]  # Removing first 3 characters before the name of gene
            geneUpTo = geneSubstring.find(" ")  # Finding the first instance of a whitespace
            geneName = geneSubstring[:geneUpTo]  # Creating a substring up to the white space i.e. gene name

            # For GDS
            line = rawData[i+4]  # Adding all the lines with GDS number
            startGDS = line[line.find("GDS"):]
            gds = startGDS[:startGDS.find(",")]

            #For organism name
            line = rawData[i+3]  # Adding all the lines with Organism name
            firstInstance = line.find(" ") + 1  # Finding the index where organism name starts
            organismName = line[firstInstance:]  # Cleaning organism name
            organismName = organismName.replace('\n', '')

            # For sample number
            line = rawData[i+5]  # Adding all the lines with number of Samples
            findSample = line.find("samples") - 1
            beforeSample = line[:findSample]
            findNumber = beforeSample.rfind(" ")
            sampleNumber = line[findNumber + 1:findSample]

            symbolNo += 1

            clean = str(symbolNo) + '\t\t' + geneName + '\t' + gds + '\t\t' + organismName + '\t' + sampleNumber + '\n'
            #CleanData.append(clean)  # Just in case needed
            wf.write(clean)

    wf.close()

