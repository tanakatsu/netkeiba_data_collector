# coding: utf-8

import os
import pandas as pd
from argparse import ArgumentParser
from tqdm import tqdm
from time import sleep
from netkeiba_util import getPage
from netkeiba_parser import getMareCrops


def main():
    parser = ArgumentParser()
    parser.add_argument('--output_dir', action='store', type=str, default='.', help='output directory filename')
    parser.add_argument('--ids', action='store', nargs='+', type=int, required=True, help='target id list')
    args = parser.parse_args()

    output_dirname = args.output_dir
    mare_ids = args.ids

    for id in tqdm(mare_ids):
        url = "https://db.netkeiba.com/horse/mare/{}/".format(id)
        html = getPage(url)
        result = getMareCrops(html)
        sleep(0.2)

        output_filename = "mare_crop_{}.csv".format(id)
        output_filename = os.path.join(output_dirname, output_filename)
        df_out = pd.DataFrame(result, columns=["year", "name", "horse_id", "sex", "sire"])
        df_out.to_csv(output_filename, index=False)


if __name__ == "__main__":
    main()
