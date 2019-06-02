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
    parser.add_argument('--output_dir', action='store', type=str, default='.', help='output directory filename')
    parser.add_argument('--ids', action='store', nargs='+', type=str, required=True, help='target id list')
    args = parser.parse_args()

    output_dirname = args.output_dir
    target_ids = args.ids

    for id in tqdm(target_ids):
        url = "https://db.netkeiba.com/horse/{}/".format(id)
        html = getPage(url)
        result = getHorseRaceResults(html)
        sleep(0.2)

        output_filename = "horse_race_result_{}.csv".format(id)
        output_filename = os.path.join(output_dirname, output_filename)
        df_out = pd.DataFrame(result, columns=["date", "name", "place", "prize", "weight"])
        df_out.to_csv(output_filename, index=False)


if __name__ == "__main__":
    main()
