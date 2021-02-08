from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'Runs script to crawl twitter to tweets.'

    def handle(self, *args, **options):
        #tweet_functions.start_crawl()
