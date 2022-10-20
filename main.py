import argparse
import asyncio
from spider import run


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-u', '--username', default=None,
        help="Username used for the scraping process"
    )
    args = parser.parse_args()

    asyncio.run(
        run(username=args.username)
    )
