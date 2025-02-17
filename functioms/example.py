import pandas as pd

def create_example():
    """
    First test of the tables
    Returns a data example.
    """
    data = pd.DataFrame({
        'product': ['coffee', 'soft drink', 'pastel'],
        'price': [6.00, 5.00, 7.00],
        'quantity': [20, 10, 15]
    })

    return data