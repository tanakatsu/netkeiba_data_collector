# coding: utf-8

import pandas as pd
from argparse import ArgumentParser
from tqdm import tqdm
from time import sleep
from netkeiba_util import getPage
from netkeiba_parser import getHorseAdditionalInfo


def main():
    parser = ArgumentParser()
    parser.add_argument('--input', '-i', action='store', type=str, default=None, help='horse data csv')
    parser.add_argument('--output', '-o', action='store', type=str, default='horse_data.additional.csv', help='output filename')
    parser.add_argument('ids', type=str, nargs='+')
    args = parser.parse_args()

    input_filename = args.input
    output_filename = args.output

    ids = []
    if input_filename:
        df = pd.read_csv(input_filename)
        ids.extend(df['id'].values)
    ids.extend(args.ids)

    results = []
    for id in tqdm(ids):
        # print(id)
        url = "http://db.netkeiba.com/horse/{id}/".format(id=id)
        html = getPage(url)
        result = getHorseAdditionalInfo(html)
        results.append(result)
        sleep(0.2)

    cols = ['id', 'name', 'sire_id', 'mare_id', 'hair', 'birth_date', 'race_result', 'debut_weight', 'sales_price', 'relatives', 'maruchi', 'kakuchi']
    df_out = pd.DataFrame(results, columns=cols)
    df_out.to_csv(output_filename, index=False)


if __name__ == "__main__":
    main()
