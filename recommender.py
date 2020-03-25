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

    num_instance_by_accompanying_product = recommended_orders_without_initial.groupby("product_id")["product_id"].count().reset_index(name="instances")
    
    num_orders_for_product = product_orders.size
    product_instances = pd.DataFrame(num_instance_by_accompanying_product)
    product_instances["frequency"] = product_instances["instances"]/num_orders_for_product
    
    recommended_products = pd.DataFrame(product_instances.sort_values("frequency", ascending=False).head(3))

    products = pd.read_csv("data/Product.csv")
    recommended_products = pd.merge(recommended_products, products, on="product_id")

    return recommended_products.to_json(orient="table")