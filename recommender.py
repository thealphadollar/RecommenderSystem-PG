import pandas as pd

def get_recommendations(id):
    """
    Get recommendation related to the specified product ID.
    
    Arguments:
        id {int} -- product id
    """
    orders = pd.read_csv("data/OrderProduct.csv")
    product_orders = orders[orders.product_id==id].order_id.unique()

    recommended_orders = orders[orders.order_id.isin(product_orders)]
    recommended_orders_without_initial = recommended_orders[recommended_orders.product_id!=id]

    num_times_purchased = recommended_orders_without_initial.groupby("product_id")
    # get top three of the bought products with the above specified
    top_three = num_times_purchased.sum().sort_values(ascending=False).head(3)

    products = pd.read_csv("data/Product.csv")
    recommended_products = pd.merge(top_three, products, on="product_id")

    return recommended_orders.to_json(orient="table")