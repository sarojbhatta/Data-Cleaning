# Cleaning a rough data file

import re  # Importing regular expressions

with open ("geoprofiles_result_LC_Data.txt", 'r') as rf:
    with open("geoprofiles_result_LC_Data_CLEANED_byREGEX.txt", 'w') as wf:

        myData = rf.readlines() # Reading lines of file

        rawData = []  # creating a list of raw data lines

        for line in myData:
            rawData.append(line)

        wf.write('SI#\tGENE\tGDS\t\tORGANISM\tSAMPLE\n')  # Column headings
        #wf.flush()

        for i in range(0, len(rawData) - 6, 7):

            # Find the symbol number and gene name from first line
            line = rawData[i + 1]
            pattern = r'(\d+)(\.\s)(\w+\-*\w+)'
            temp = re.search(pattern, line)
            geneName1 = temp.group(3)
            symbolNo = temp.group(1)

            # Find gene name from annotation
            line = rawData[i+2]
            pattern = r'(Annotation:\s)(\w+\-*\w+)(\,*\s)'  # (\w+\.*\-*\.*\w+\:*\;*)
            temp = re.search(pattern, line)
            if re.match(pattern, line):
                # Because some samples of Annotation are like this: Annotation: {3' region, probe M1}
                geneName2 = temp.group(2)
            else:
                geneName2 = 'None'

            # Finding gene name
            if geneName1 == geneName2:
                geneName = geneName1
            else:
                geneName = "None"

            # Find organism name from the raw file
            line = rawData[i + 3]
            pattern = r'(Organism:\s)(\w+\s\w+)'
            orgName = re.search(pattern, line).group(2)

            # Find GDS number from the raw file
            line = rawData[i + 4]
            pattern = r'(GDS\d+)'
            gds = re.search(pattern, line).group(0)

            # Find sample number from the raw file
            line = rawData[i + 5]
            pattern = r'(\d+)(\ssamples)'
            sample = re.search(pattern, line).group(1)

            result = '{0}\t{1}\t{2}\t{3}\t{4}\n'.format(symbolNo, geneName, gds, orgName, sample)
            wf.write(result)
            # wf.flush()

    #wf.close()
#fp.close()


