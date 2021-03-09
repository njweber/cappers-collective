from django.core.management.base import BaseCommand, CommandError

from tweet_crawler.tweet_functions import start_crawl

class Command(BaseCommand):
    help = 'Runs script to crawl twitter to tweets.'

    def handle(self, *args, **options):
       print("Running Script")
       start_crawl()
