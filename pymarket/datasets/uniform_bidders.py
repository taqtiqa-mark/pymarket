import numpy as np


def generate(
        cant_buyers: int,
        cant_sellers: int,
        offset_sellers: float=0,
        offset_buyers: float=0,
        r: np.random.RandomState = None,
        eps: float=1e-4):
    """
    Generates random bids. All the volumes and reservation
    prices are sampled independently from a uniform distribution.
    For sellers, the reservation price is shifted `offset_seller`
    while for the buyers is shifter `offset_buyers`.
    If there are two sellers or two buyers with the same price,
    the reservation price of one of them is resampled until
    in both side of the market, all players have different values.

    Parameters
    ----------
    cant_buyers: int
        Number of buyers to generate. Has to be positiv
    cant_sellers: int
        Number of sellers to generate. Has to be positive.
    offset_sellers
        Quantity to shift the reservation price of sellers
    offset_buyers
        Quantity to shift the reservation price of buyers
    r : optional
        RandomState used to generate the data
    eps : optional
        Minimum precision of the prices

    Returns
    -------
    bids
        List of tuples of all the bids generated

    Examples
    ---------
    >>> r = np.random.RandomState(420)
    >>> generate(2, 3, 1, 2, r, 0.1)
    [(0.5, 2.8, 0, True, 0, True), (0.7000000000000001, 2.5, 1, True, 0, True), (0.6000000000000001, 1.2, 2, False, 0, True), (0.1, 1.7000000000000002, 3, False, 0, True), (0.2, 1.3, 4, False, 0, True)]
    """

    if r is None:
        r = np.random.RandomState()

    offset = [offset_buyers, offset_sellers]
    quantities = [cant_buyers, cant_sellers]
    bids = []

    user = 0
    for i, (o_, q_) in enumerate(zip(offset, quantities)):
        range_ = np.arange(0, 1, eps)
        qs = r.choice(range_, q_, replace=False)
        vs = r.choice(range_ + o_, q_, replace=False)
        for j in range(q_):
            bid = (qs[j], vs[j], user, bool(1 - i), 0, True)
            bids.append(bid)
            user += 1
    return bids
