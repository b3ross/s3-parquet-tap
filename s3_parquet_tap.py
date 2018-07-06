import singer
import argparse
import json
from datetime import date, datetime, timedelta

LOG = singer.get_logger()

schema = {'type': 'object',
          'properties':
          {'date': {'type': 'string',
                    'format': 'date-time'}},
          'additionalProperties': True}

def do_sync():
    singer.write_schema('exchange_rate', schema, 'date')
    singer.write_records('exchange_rate', [str(datetime.utcnow())])

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-c', '--config', help='Config file', required=False)
    parser.add_argument(
        '-s', '--state', help='State file', required=False)

    args = parser.parse_args()

    if args.config:
        with open(args.config) as file:
            config = json.load(file)
    else:
        config = {}

    if args.state:
        with open(args.state) as file:
            state = json.load(file)
    else:
        state = {}

    do_sync()

if __name__ == '__main__':
    main()
