import sys, os

#check 1: i will check if everything in this line are numbers:
def numbersOnly(stringExtracted):
    for each in stringExtracted:
        if not (each.isdigit() or each == ""):
            return False
    return True

# Write aeach extracted lines into the file.
def write_eachs(stringExtracted, file):
		if numbersOnly(stringExtracted):
			return 0
		while stringExtracted != []:
			each = stringExtracted.pop(0)
			file.write(each + " ")
			if numbersOnly(stringExtracted):
				return 0


if __name__ == "__main__":
		input = sys.path[0] + "\\InputFilesGiven\\cacm_stem.txt"
		output = sys.path[0] + "\\stemmedCorpus"
		fe = open(input, "r")
		with fe as text_file:
			while True:
				stringExtracted = text_file.readline().strip("\n")
				if not stringExtracted:
					break
				stringExtracted = stringExtracted.split(" ")
				if stringExtracted[0] == "#":
					try:
						f.close()
					except NameError:
						pass
					outFomrat = "CACM-{:04}.txt".format(int(stringExtracted[1]))	
					f = open(output + outFomrat, "w")
				else:
					write_eachs(stringExtracted, f)
