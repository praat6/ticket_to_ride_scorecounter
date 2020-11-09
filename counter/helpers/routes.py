from collections import namedtuple


Route = namedtuple('Route', ['n_train_cars', 'score'])

one = Route(n_train_cars=1, score=1)
two = Route(n_train_cars=2, score=2)
three = Route(n_train_cars=3, score=4)
four = Route(n_train_cars=4, score=7)
five = Route(n_train_cars=5, score=10)
six = Route(n_train_cars=6, score=15)


types = [one, two, three, four, five, six]
