import json
import requests
import subprocess
import csv
import sys
import os
import time

def main():
    #subprocess.run()

    genome = sys.argv[1]
    input_file = sys.argv[2]
    output_file = "crispor_ot_output.csv"
    #todo: run crispor
    #todo: run on vbox
    #todo: display on website?

    os.system("python2 crispor.py "+ genome + " " + input_file + " " + " out1.csv -o " + output_file)

    track = "clinvarMain"
    ot_dict = {}
    #start = time.time()

    write_file = open('output-json-dump.txt', 'w')
    output = []
    counter = 0
    with open(output_file, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter = '\t')
        for row in reader:
            #print(row)
            if counter >= 10:
                break
            if row[0][0] == "#" or 'guide' in row[2]:  # ignore headers
                pass
            else:
                offtarget = row[3]
                #print(offtarget)
                chrom = row[8]
                start = row[9]
                end = row[10]
                api_url = "https://api.genome.ucsc.edu/getData/track?genome=" + genome + ";track=" + track + ";chrom=" + chrom + ";start=" + start + ";end=" + end + ""
                #print(api_url)
                response = requests.get(api_url)
                output_dump = response.json()
                #print(output_dump)
                try:
                    output_dump["statusCode"]
                except:
                    if output_dump["clinvarMain"] != []:
                        for mutations in output_dump["clinvarMain"]:
                            print(mutations)
                            if mutations["clinSign"].lower().find("benign") != -1 or mutations["clinSign"].lower().find("uncertain") != -1:
                                pass
                            else:
                                print(json.dumps(mutations))
                                output.append(mutations)
                                #write_file.write(json.dumps(mutations) + "\n")
                                try:
                                    if ot_dict[offtarget] is None:
                                        print(output_dump)
                                    ot_dict[offtarget] = ot_dict[offtarget].append(mutations)
                                    counter += 1
                                except:
                                    # if mutations is None:
                                    #     pass
                                    # else:
                                    #     ot_dict[offtarget] = [mutations]
                                    try:
                                        ot_dict[offtarget] = [mutations]
                                        counter += 1
                                    except:
                                        print(mutations)
    #end = time.time()
    #end = float(end)
    #start = float(start)
    #print(end-start)

    for jsonData in output:
        print("Phenotype Information")
        write_file.write("Phenotype Information")
        print("---------------------")
        write_file.write("---------------------")
        print("Clinical Significance: ", jsonData["clinSign"])
        write_file.write("Clinical Significance: " + json.dumps(jsonData["clinSign"]))
        print("Type: ", jsonData["type"])
        write_file.write("Type: " + str(jsonData["type"]))
        print("Phenotypes: ", jsonData["phenotypeList"])
        write_file.write("Phenotypes: " + str(jsonData["phenotypeList"]))
        print("Links: ,", jsonData["phenotype"])
        write_file.write("Links: " + str(jsonData["phenotype"]))
        #print("OMIM link: ", link[2])
        print("\n")       
        write_file.write("\n") 
    write_file.close()

if __name__ == '__main__':
    main()
