import entrezpy.conduit

def main():
   apiKey = "2ce72b849bfad5d0bebfb424d06366799d09"

   c = entrezpy.conduit.Conduit('comalvirdi@gmail.com')
   fetch_influenza = c.new_pipeline()
   sid = fetch_influenza.add_search({'db' : 'nucleotide', 'term' : 'H3N2 [organism] AND HA', 'rettype':'count', 'sort' : 'Date Released', 'mindate': 2000, 'maxdate':2019, 'datetype' : 'pdat'})
   fid = fetch_influenza.add_fetch({'retmax' : 10, 'retmode' : 'text', 'rettype': 'fasta'}, dependency=sid)
   c.run(fetch_influenza)

if __name__ == "__main__":
   main()