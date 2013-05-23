#!/usr/bin/env python

"""Implements Twitter Cards for Pelican Generated Sites"""

__author__ = "Michael Martinez"
__copyright__ = "Copyright 2013"
__credits__ = [""]
__license__ = "MIT"
__version__ = "Expat"
__maintainer__ = "Michael Martinez"
__email__ = "machinedesigner@gmail.com"
__status__ = "alpha"

from pelican.settings import _DEFAULT_CONFIG
from pelican import signals


def twitter_card(generator):
    """
     https://dev.twitter.com/cards
     TWITTER_CARD_USE = (True) # (False)
     TWITTER_CARD_SITE = '@website' # The site's Twitter handle like @my_blog
     TWITTER_CARD_SITE_ID = 123456 # The site's Twitter ID
     TWITTER_CARD_CREATOR = '@username' # Your twitter handle like @yourtwitname
     TWITTER_CARD_CREATOR_ID = 56789 # The site creator's id
     GRAVATAR_URL = ''
    """

    _DEFAULT_CONFIG.setdefault('TWITTER_CARD_SITE', '')
    _DEFAULT_CONFIG.setdefault('TWITTER_CARD_SITE_ID', '')
    _DEFAULT_CONFIG.setdefault('TWITTER_CARD_CREATOR', '')
    _DEFAULT_CONFIG.setdefault('TWITTER_CARD_CREATOR_ID', '')
    _DEFAULT_CONFIG.setdefault('GRAVATAR_URL', '')


def register():
    signals.article_generator_finalized.connect(twitter_card)