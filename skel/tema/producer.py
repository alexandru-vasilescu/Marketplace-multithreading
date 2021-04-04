"""
This module represents the Producer.

Computer Systems Architecture Course
Assignment 1
March 2021
"""

from threading import Thread
from time import sleep


class Producer(Thread):
    """
    Class that represents a producer.
    """

    def __init__(self, products, marketplace, republish_wait_time, **kwargs):
        """
        Constructor.

        @type products: List()
        @param products: a list of products that the producer will produce

        @type marketplace: Marketplace
        @param marketplace: a reference to the marketplace

        @type republish_wait_time: Time
        @param republish_wait_time: the number of seconds that a producer must
        wait until the marketplace becomes available

        @type kwargs:
        @param kwargs: other arguments that are passed to the Thread's __init__()
        """
        Thread.__init__(self, **kwargs)
        self.products = products
        self.marketplace = marketplace
        self.id_producer = marketplace.register_producer()
        self.wait_time = republish_wait_time

    def run(self):
        # intr-o bucla infinita adaug produse la marketplace in functie de cantitate
        while True:
            for product in self.products:
                buying_product = product[0]
                quantity = product[1]
                wait_time = product[2]
                for _ in range(quantity):
                    while not self.marketplace.publish(self.id_producer, buying_product):
                        sleep(self.wait_time)
                    sleep(wait_time)
