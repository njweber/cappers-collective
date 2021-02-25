from django.core.management.base import BaseCommand, CommandError

#TODO: Figure out import issue and get this running!@
#import .tweet_functions

class Command(BaseCommand):
    help = 'Runs script to crawl twitter to tweets.'

    def handle(self, *args, **options):
        print("Running Script")
 #      tweet_functions.start_crawl()
