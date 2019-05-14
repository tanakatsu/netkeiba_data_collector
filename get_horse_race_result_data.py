# coding: utf-8

import os
import pandas as pd
from argparse import ArgumentParser
from tqdm import tqdm
from time import sleep
from netkeiba_util import getPage
from netkeiba_parser import getHorseRaceResults


def main():
    parser = ArgumentParser()
    parser.add_argument('--input', '-i', action='store', type=str, default='horse_ranking.csv', help='horse data csv')
    parser.add_argument('--output_dir', action='store', type=str, default='.', help='output directory filename')
    parser.add_argument('-n', action='store', type=int, default=None, help='max sample')
    parser.add_argument('--ids', action='store', nargs='+', type=int, default=None, help='target id list')
    args = parser.parse_args()

    input_filename = args.input
    output_dirname = args.output_dir
    max_sample = args.n
    target_ids = args.ids

    df = pd.read_csv(input_filename)
    horse_ids = df['id'].values
    if target_ids:
        horse_ids = [id for id in horse_ids if id in target_ids]
    if max_sample:
        horse_ids = horse_ids[:max_sample]

    for id in tqdm(horse_ids):
        url = "https://db.netkeiba.com/horse/{}/".format(id)
        html = getPage(url)
        result = getHorseRaceResults(html)
        sleep(0.2)

        output_filename = "horse_race_result_{}.csv".format(id)
        output_filename = os.path.join(output_dirname, output_filename)
        df_out = pd.DataFrame(result, columns=["date", "name", "place", "prize"])
        df_out.to_csv(output_filename, index=False)


if __name__ == "__main__":
    main()
