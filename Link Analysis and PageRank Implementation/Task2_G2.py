from math import log, pow, floor
import timeit

start = timeit.default_timer()
count = 0
preplex = []
page_rank = []
i = 0
d = 0.85
pR = {}


def find_perplexity(prank):
    p = 0
    for page in prank:
			a = log(1.0/prank[page], 2)
			p += prank[page] * a
		
    return pow(2,p)


def diffperplex(p):
# obtaining difference in perplexity.
			
			pxy0 = map(lambda x: floor(x), p)[0]
			pxy = map(lambda x: x == pxy0, map(lambda x: floor(x), p))
			a  = len(pxy) >= 4
			b = all(pxy)
			return a and b


def readFile(url):
    out_pages = {}
    in_pages = {}
    
    #take a file and return the outlinks and inlinks
	
    with open(url) as file:
        for line in file:
            s = map(lambda x: x.replace('\n',''), filter(lambda x: x != '\n', line.split(' ')))
            page = s[0]
			
            if page in in_pages:
                in_pages[page] = in_pages[page] + s[1:]
				
            else:
                in_pages[page] = s[1:]
				
            if not page in out_pages:
                out_pages[page] = 0
				
            for ipage in s[1:]:
                if ipage in out_pages:
                    out_pages[ipage] += 1
					
                else:
                    out_pages[ipage] = 1
					
    return (in_pages, out_pages)


def pR(in_pages, out_pages):
    pR={}
    global preplex, d, i
    sp = filter(lambda x: out_pages[x] == 0, out_pages)
	
	
    cd = (1.0-d)/len(in_pages)


    for p in in_pages:
			#calculating initial page rank for each page
			a = len(in_pages)
			pR[p] = 1.0/a
    
    preplex += [find_perplexity(pR)]

    while not diffperplex(preplex[-4:]):
        nPR = {}
        sPR = 0
        for s in sp:
					sPR += pR[s]
        for p in in_pages:
					a = len(in_pages)
					nPR[p] = cd + d*sPR/a
					for ik in in_pages[p]:
						nPR[p] += d* pR[ik]/out_pages[ik]
						
        for p in nPR:
            pR[p] = nPR[p]
        i += 1
        preplex += [find_perplexity(pR)]

    print "********************************** Page Ranks*****************************\n"
	
    for p in preplex:
        print p
    return pR
   
def main():
    global page_rank,count
    
    i,o = readFile('wt2g_inlinks.txt')
    pr = pR(i,o)
   
    for p in pr:
			page_rank += [(p, pr[p])]
    spr = (sorted(page_rank, key=lambda x: x[1]))

    print "\n************************ Top 50 pages by page rank ******************************\n"
    for page,rank in list(reversed(spr[-50:])):
        print page, "\t\t", rank
    
    print "\n************************Top 50 pages by in-link count*****************************\n"
  
    for k in list(reversed(sorted(i, key=lambda k: len(i[k])))):
        if count < 50:
            print k, "\t\t", len(i[k])
            count += 1


    s = timeit.default_timer()
    print '\n'
    print 'Running time is:', s-start

if __name__ == '__main__':
    main()