## Netkeiba data collector

crowler for [netkeiba.com](http://www.netkeiba.com)

### Features

Collect data of
- [trainer leading](http://db.netkeiba.com/?pid=trainer_leading)
- [jockey leading](http://db.netkeiba.com/?pid=jockey_leading)
- [sire leading](http://db.netkeiba.com/?pid=sire_leading)
- [bms leading](http://db.netkeiba.com/?pid=bms_leading)
- [owner leading](http://db.netkeiba.com/?pid=owner_leading)
- [breeder leading](http://db.netkeiba.com/?pid=breeder_leading)
- horses by prize ranking

And
- horse additional information
  - birth date and racing result (count of first, second, third and others)
- mare's children result
  - children's winning count etc..

### Requirements

- Python3

### How to use

- trainer leading
  ```
  $ get_trainer_leading_data.py --year YEAR [-n max_samples] [--o output_filename]
  ```
- jockey leading
  ```
  $ get_jockey_leading_data.py --year YEAR [-n max_samples] [--o output_filename]
  ```
- sire leading
  ```
  $ get_sire_leading_data.py --year YEAR [-n max_samples] [--o output_filename]
  ```
- bms leading
  ```
  $ get_bms_leading_data.py --year YEAR [-n max_samples] [--o output_filename]
  ```
- owner leading
  ```
  $ get_owner_leading_data.py --year YEAR [-n max_samples] [--o output_filename]
  ```
- breeder leading
  ```
  $ get_breeder_leading_data.py --year YEAR [-n max_samples] [--o output_filename]
  ```
- horses by prize ranking
  ```
  $ get_horse_data.py --age AGE [--include_no_debut] [-n max_samples] [--o output_filename]
  ```

- horse additional information

  This script requires output file of `get_horse_data.py` as input file.

  ```
  $ get_horse_additional_data.py -i output_of_get_horse_data [-o output_filename]
  ```
- mare's children result

  This script requires output file of `get_horse_data.py` as input file.

  ```
  $ get_mare_crops_result_data.py -i output_of_get_horse_data [-o output_filename]
  ```

### License

MIT
