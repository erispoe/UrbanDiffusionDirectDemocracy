from GCorpusAnalytics import GCorpusAnalytics as gca

def main():
	r = gca.Request('Dirdemchne_1850_2010_10a')
	r.execute()
	r.exportCsv()

if __name__ == '__main__':
    main()