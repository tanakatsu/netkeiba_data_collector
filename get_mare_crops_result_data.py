# coding: utf-8

import os
import pickle
import pandas as pd
from argparse import ArgumentParser
from tqdm import tqdm
from time import sleep
from util import getPage
from netkeiba_parser import getHorseIdByName, getMareCropsResult


def main():
    parser = ArgumentParser()
    parser.add_argument('--input', '-i', action='store', type=str, default='horse_ranking.csv', help='horse data csv')
    parser.add_argument('--output', '-o', action='store', type=str, default='mare_crop_data.csv', help='output filename')
    parser.add_argument('--cache', action='store', type=str, default='horse_id.pkl', help='horse_id cache file')
    args = parser.parse_args()

    input_filename = args.input
    output_filename = args.output
    cache_filename = args.cache

    df = pd.read_csv(input_filename)
    mare_names = df['mare'].values
    # print(mare_names)

    if os.path.exists(cache_filename):
        # load horse_id cache
        horse_ids = pickle.load(open(cache_filename, 'rb'))
    else:
        horse_ids = {}

    results = []
    for mare in tqdm(mare_names[:3]):
    # for mare in tqdm(mare_names):
        if mare in horse_ids:
            horse_id = horse_ids[mare]
        else:
            horse_id = getHorseIdByName(mare)
            horse_ids[mare] = horse_id

        if mare in [res['name'] for res in results]:
            continue

        url = "http://db.netkeiba.com/horse/{id}/".format(id=horse_id)
        html = getPage(url)
        result = getMareCropsResult(html)
        results.append(result)
        sleep(1)

    # update cache
    pickle.dump(horse_ids, open(cache_filename, 'wb'))

    df_out = pd.DataFrame(results)
    reordered_cols = ['id', 'name', 'crop_count', 'crop_win_count', 'crop_grade_horse_count', 'crop_grade_win_count']
    df_out = df_out[reordered_cols]
    df_out.to_csv(output_filename)


if __name__ == "__main__":
    main()
