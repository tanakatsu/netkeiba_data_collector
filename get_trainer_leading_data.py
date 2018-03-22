# coding: utf-8

import pandas as pd
from argparse import ArgumentParser
from time import sleep
from netkeiba_util import getPage
from netkeiba_parser import getTrainerResult


def main():
    parser = ArgumentParser()
    parser.add_argument('--year', '-y', action='store', type=int, required=True, help='target year')
    parser.add_argument('-n', action='store', type=int, default=None, help='max samples')
    parser.add_argument('--output', '-o', action='store', type=str, default='trainer_leading.csv', help='output filename')
    args = parser.parse_args()

    year = args.year
    max_sample = args.n
    output_filename = args.output
    results = []

    page = 1
    while(True):
        html = getPage("http://db.netkeiba.com/?pid=trainer_leading&year=%d&page=%d" % (year, page))
        page_result = getTrainerResult(html, offset=len(results))
        print('get {}'.format(len(page_result)))
        results += page_result

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
                      'stable',
                      'win_count',
                      'second_place_count',
                      'third_place_count',
                      'unplaced_count',
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
                      'in_second_place_ratio',
                      'in_third_place_ratio',
                      'prize']
    df = df[reordered_cols]
    df.to_csv(output_filename)


if __name__ == "__main__":
    main()
