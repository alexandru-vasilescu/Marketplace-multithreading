"""
This module represents the Consumer.

Computer Systems Architecture Course
Assignment 1
March 2021
"""

from threading import Thread, Lock
from time import sleep


class Consumer(Thread):
    """
    Class that represents a consumer.
    """

    def __init__(self, carts, marketplace, retry_wait_time, **kwargs):
        """
        Constructor.

        :type carts: List
        :param carts: a list of add and remove operations

        :type marketplace: Marketplace
        :param marketplace: a reference to the marketplace

        :type retry_wait_time: Time
        :param retry_wait_time: the number of seconds that a producer must wait
        until the Marketplace becomes available

        :type kwargs:
        :param kwargs: other arguments that are passed to the Thread's __init__()
        """
        Thread.__init__(self, **kwargs)
        self.carts = carts
        self.marketplace = marketplace
        self.wait_time = retry_wait_time
        self.lock = Lock()

    def run(self):
        for cart in self.carts:
            with self.lock:
                cart_id = self.marketplace.new_cart()
            for action in cart:
                if action['type'] == 'add':
                    for _ in range(action['quantity']):
                        while not self.marketplace.add_to_cart(cart_id, action['product']):
                            sleep(self.wait_time)
                else:
                    for _ in range(action['quantity']):
                        self.marketplace.remove_from_cart(cart_id, action['product'])
            shopping_cart = self.marketplace.place_order(cart_id)
            for product in shopping_cart:
                print(self.name + " bought " + str(product))
