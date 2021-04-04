"""
This module represents the Marketplace.

Computer Systems Architecture Course
Assignment 1
March 2021
"""
from threading import Lock


class Marketplace:
    """
    Class that represents the Marketplace. It's the central part of the implementation.
    The producers and consumers use its methods concurrently.
    """

    def __init__(self, queue_size_per_producer):
        """
        Constructor

        :type queue_size_per_producer: Int
        :param queue_size_per_producer: the maximum size of a queue associated with each producer
        """
        self.queue_size = queue_size_per_producer
        # Calculez id-ul producatorilor pentru a-l putea da la apelul register_producer
        self.count_producer = 0
        # Pastrez o lista de produse in functie de fiecare producator
        self.market = dict()
        # Calculez id-ul cartului pentru a-l putea da la apelul new_cart
        self.count_cart = 0
        # Pastre o lista de tupluri (id_producator, produs) pentru fiecare cart
        self.carts = dict()
        # Mutex folosit pentru a sincroniza adaugarea unui nou cart
        self.lock = Lock()

    def register_producer(self):
        """
        Returns an id for the producer that calls this.
        """
        with self.lock:
            self.count_producer += 1
            # initializez lista producatorului
            self.market[self.count_producer] = []
        return self.count_producer

    def publish(self, producer_id, product):
        """
        Adds the product provided by the producer to the marketplace

        :type producer_id: String
        :param producer_id: producer id

        :type product: Product
        :param product: the Product that will be published in the Marketplace

        :returns True or False. If the caller receives False, it should wait and then try again.
        """
        # Verific daca este loc de a adauga produse in coada
        if len(self.market[producer_id]) < self.queue_size:
            self.market[producer_id].append(product)
            return True
        return False

    def new_cart(self):
        """
        Creates a new cart for the consumer

        :returns an int representing the cart_id
        """
        with self.lock:
            self.count_cart += 1
            # initializez lista cartului in dicitonar
            self.carts[self.count_cart] = []
        return self.count_cart

    def add_to_cart(self, cart_id, product):
        """
        Adds a product to the given cart. The method returns

        :type cart_id: Int
        :param cart_id: id cart

        :type product: Product
        :param product: the product to add to cart

        :returns True or False. If the caller receives False, it should wait and then try again
        """
        for key, value in self.market.items():
            # caut produsul dorit in market
            if product in value:
                self.carts[cart_id].append((key, product))
                value.remove(product)
                return True
        return False

    def remove_from_cart(self, cart_id, product):
        """
        Removes a product from cart.

        :type cart_id: Int
        :param cart_id: id cart

        :type product: Product
        :param product: the product to remove from cart
        """
        for product_in_cart in self.carts[cart_id]:
            if product_in_cart[1] == product:
                self.market[product_in_cart[0]].append(product)
                self.carts[cart_id].remove(product_in_cart)
                break

    def place_order(self, cart_id):
        """
        Return a list with all the products in the cart.

        :type cart_id: Int
        :param cart_id: id cart
        """
        return [product[1] for product in self.carts[cart_id]]
