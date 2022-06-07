import os
import pandas as pd
import shutil

def main():
	df = pd.read_csv('birdsong_metadata.csv')
	for i, row in df.iterrows():
		os.makedirs(
			f'labeled/{row.loc["english_cname"]}', exist_ok=True)
		shutil.copy(
			f'songs/songs/xc{row.loc["file_id"]}.flac', 
			f'labeled/{row.loc["english_cname"]}/')

if __name__ == '__main__':
	main()
