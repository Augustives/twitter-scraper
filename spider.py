import os
import pandas
import asyncio
import aiohttp

from utils import remove_stop_words, nltk_setup

from settings import (
    USER_ID_URL, USER_TWEETS_URL,
    USER_TWEETS_URL_PAGINATED, USERNAMES
)


def parse_csv(username, user_tweets):
    dataframe = pandas.DataFrame(
        [
            [
                remove_stop_words(tweet)
            ] 
            for tweet in user_tweets
        ],
        columns=['Tweet']
    )
    dataframe.to_csv(f'./csv/{username}.csv')


async def follow_user_tweets_pagination(session, user_id, next_token):
    tweets = []

    while next_token:
        response = await session.get(
            USER_TWEETS_URL_PAGINATED(user_id, next_token)
        )
        response_data = await response.json()

        next_token = response_data.get('meta').get('next_token')
        tweets.extend(response_data.get('data'))

    return tweets


async def follow_user_tweets(session, user_id):
    response = await session.get(
        USER_TWEETS_URL(user_id)
    )
    response_data = await response.json()
    next_token = response_data.get('meta').get('next_token')

    # paginated_tweets = await follow_user_tweets_pagination(
    #     session, user_id, next_token
    # )
    paginated_tweets = []

    return [
        tweet.get('text')
        for tweet in 
        response_data.get('data') + paginated_tweets
    ]


async def follow_user_id(session, username):
    response = await session.get(
        USER_ID_URL(username)
    )
    response_data = await response.json()
    return response_data.get('data').get('id')


async def run(*args, **kwargs):
    nltk_setup()
    async with aiohttp.ClientSession() as session:
        session.headers.add(
            'Authorization', f'Bearer {os.environ.get("BEARER_TOKEN")}'
        )

        usernames = kwargs.get('username') or USERNAMES
        users_ids = await asyncio.gather(
            *[
                follow_user_id(session, username)
                for username in usernames
            ]
        )

        users_tweets = await asyncio.gather(
            *[
                follow_user_tweets(session, user_id)
                for user_id in users_ids
            ]
        )

        for index, user_tweets in enumerate(users_tweets):
            parse_csv(USERNAMES[index], user_tweets)

        return


if __name__ == '__main__':
    asyncio.run(run())
