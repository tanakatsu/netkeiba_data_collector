# coding: utf-8

import os
import pickle
import pandas as pd
from argparse import ArgumentParser
from tqdm import tqdm
from time import sleep
from netkeiba_util import getPage
from netkeiba_parser import getHorseIdByName, getHorseIdByName2, getMareCropsResult


bms_conv_tbl = {
    "ファスリエフ": "Fasliyev",
    "キングズベスト": "King's Best",
    "アルデバランＩＩ": "アルデバラン",
    "Street Cry": "ストリートクライ",
    "ディスクリートキャット": "Discreet Cat",
    "Dylan Thomas": "ディラントーマス",
}

mare_conv_tbl = {
    "Pennedepie": "ペンネドゥピー"
}


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
    bms_names = df['bms'].values
    # print(mare_names)

    if os.path.exists(cache_filename):
        # load horse_id cache
        horse_ids = pickle.load(open(cache_filename, 'rb'))
    else:
        horse_ids = {}

    results = []
    for mare, bms in tqdm(zip(mare_names, bms_names), total=len(mare_names)):
        if mare in horse_ids:
            horse_id = horse_ids[mare]
        else:
            if mare in mare_conv_tbl:
                mare = mare_conv_tbl[mare]

            horse_id = getHorseIdByName(mare, sire=bms, sex=[2])
            if not horse_id:
                # try in partial match mode..
                horse_id = getHorseIdByName2(mare, sire=bms, sex=[2])

            if not horse_id:
                if bms in bms_conv_tbl:
                    horse_id = getHorseIdByName2(mare, sire=bms_conv_tbl[bms], sex=[2])

            if not horse_id:
                # try without sire parameter
                horse_id = getHorseIdByName(mare, sex=[2])
                print("WARNING: horse_id is found without sire parameter ({})".format(mare))

            if not horse_id:
                print("WARNING: horse_id is not found ({})".format(mare))
                continue

            horse_ids[mare] = horse_id

            # update cache
            pickle.dump(horse_ids, open(cache_filename, 'wb'))

        # skip if we already checked
        if mare in [res['name'] for res in results]:
            continue

        url = "https://db.netkeiba.com/horse/{id}/".format(id=horse_id)
        html = getPage(url)
        result = getMareCropsResult(html)
        # print(result)
        results.append(result)
        sleep(0.2)

    df_out = pd.DataFrame(results)
    reordered_cols = ['id', 'name', 'crop_count', 'crop_win_count', 'crop_grade_horse_count', 'crop_grade_win_count']
    df_out = df_out[reordered_cols]
    df_out.to_csv(output_filename)


if __name__ == "__main__":
    main()
