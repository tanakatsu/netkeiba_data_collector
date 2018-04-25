# coding: utf-8

import pandas as pd
from argparse import ArgumentParser
from tqdm import tqdm
from time import sleep
from netkeiba_util import getPage
from netkeiba_parser import getHorseAdditionalInfo


def main():
    parser = ArgumentParser()
    parser.add_argument('--input', '-i', action='store', type=str, default='horse_ranking.csv', help='horse data csv')
    parser.add_argument('--output', '-o', action='store', type=str, default='horse_data.additional.csv', help='output filename')
    args = parser.parse_args()

    input_filename = args.input
    output_filename = args.output

    df = pd.read_csv(input_filename)
    ids = df['id'].values

    results = []
    for id in tqdm(ids):
        # print(id)
        url = "http://db.netkeiba.com/horse/{id}/".format(id=id)
        html = getPage(url)
        result = getHorseAdditionalInfo(html)
        results.append(result)
        sleep(0.2)

    df_out = pd.DataFrame(results)

    reordered_cols = ['id', 'name', 'hair', 'birth_date', 'race_result', 'sales_price', 'relatives']
    df_out = df_out[reordered_cols]
    df_out.to_csv(output_filename)


if __name__ == "__main__":
    main()
