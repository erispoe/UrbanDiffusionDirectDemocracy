from GCorpusAnalytics import GCorpusAnalytics as gca

def main():
	r = gca.Request('DirDemRuralUrban_1850_2010_10a', open('DirDemRuralUrban_1850_2010_10a.json').read())
	r.execute()
	r.exportCsv()

if __name__ == '__main__':
    main()