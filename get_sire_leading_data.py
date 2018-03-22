# coding: utf-8

import pandas as pd
from argparse import ArgumentParser
from time import sleep
from netkeiba_util import getPage
from netkeiba_parser import getSireResult


def main():
    parser = ArgumentParser()
    parser.add_argument('--year', '-y', action='store', type=int, required=True, help='target year')
    parser.add_argument('-n', action='store', type=int, default=None, help='max sample')
    parser.add_argument('--output', '-o', action='store', type=str, default='sire_leading.csv', help='output filename')
    args = parser.parse_args()

    year = args.year
    max_sample = args.n
    output_filename = args.output
    results = []

    page = 1
    while(True):
        html = getPage("http://db.netkeiba.com/?pid=sire_leading&year=%d&page=%d" % (year, page))
        page_result = getSireResult(html, offset=len(results))
        results += page_result
        print('get {}'.format(len(page_result)))

        if len(page_result) == 0:
            break

        if max_sample and len(results) >= max_sample:
            results = results[:max_sample]
            break

        page = page + 1
        sleep(1)

    print(len(results))
    df = pd.DataFrame(results)
    reordered_cols = ['id',
                      'name',
                      'race_horse_count',
                      'win_horse_count',
                      'race_count',
                      'win_count',
                      'grade_race_count',
                      'grade_race_win',
                      'stakes_race_count',
                      'stakes_race_win',
                      'general_race_count',
                      'general_race_win',
                      'turf_race_count',
                      'turf_race_win',
                      'dart_race_count',
                      'dart_race_win',
                      'win_ratio',
                      'earning_index',
                      'prize',
                      'avg_turf_distance',
                      'avg_dart_distance']
    df = df[reordered_cols]
    df.to_csv(output_filename)


if __name__ == "__main__":
    main()
