import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import warnings
warnings.filterwarnings('ignore')

class CustomerBehaviorAnalyzer:
    def __init__(self):
        self.orders = pd.read_csv('https://raw.githubusercontent.com/olist/brazilian-ecommerce/master/olist_orders_dataset.csv')
        self.order_items = pd.read_csv('https://raw.githubusercontent.com/olist/brazilian-ecommerce/master/olist_order_items_dataset.csv')
        self.products = pd.read_csv('https://raw.githubusercontent.com/olist/brazilian-ecommerce/master/olist_products_dataset.csv')
        self.customers = pd.read_csv('https://raw.githubusercontent.com/olist/brazilian-ecommerce/master/olist_customers_dataset.csv')
        self.reviews = pd.read_csv('https://raw.githubusercontent.com/olist/brazilian-ecommerce/master/olist_order_reviews_dataset.csv')
        self.process_data()

    def process_data(self):
        # Convert datetime columns
        datetime_columns = ['order_purchase_timestamp', 'order_approved_at', 
                          'order_delivered_carrier_date', 'order_delivered_customer_date', 
                          'order_estimated_delivery_date']
        
        for col in datetime_columns:
            self.orders[col] = pd.to_datetime(self.orders[col])
        
        # Calculate delivery time and delay
        self.orders['delivery_time'] = (self.orders['order_delivered_customer_date'] - 
                                      self.orders['order_purchase_timestamp']).dt.total_seconds() / 86400
        self.orders['delivery_delay'] = (self.orders['order_delivered_customer_date'] - 
                                       self.orders['order_estimated_delivery_date']).dt.total_seconds() / 86400
        
        # Merge relevant data
        self.full_data = self.orders.merge(self.order_items, on='order_id')
        self.full_data = self.full_data.merge(self.products, on='product_id')
        self.full_data = self.full_data.merge(self.customers, on='customer_id')
        self.full_data = self.full_data.merge(self.reviews[['order_id', 'review_score']], on='order_id')

    def generate_customer_insights(self):
        # Purchase patterns
        monthly_orders = self.orders.set_index('order_purchase_timestamp').resample('M').size()
        
        # Product category analysis
        category_sales = self.full_data.groupby('product_category_name')['price'].agg(['count', 'mean', 'sum'])
        category_sales = category_sales.sort_values('sum', ascending=False).head(10)
        
        # Customer satisfaction
        satisfaction_by_category = self.full_data.groupby('product_category_name')['review_score'].mean()
        
        # Create visualizations
        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=('Monthly Order Trends', 'Top 10 Categories by Sales',
                          'Average Order Value by Category', 'Customer Satisfaction by Category')
        )
        
        # Monthly trends
        fig.add_trace(
            go.Scatter(x=monthly_orders.index, y=monthly_orders.values, name='Orders'),
            row=1, col=1
        )
        
        # Top categories
        fig.add_trace(
            go.Bar(x=category_sales.index, y=category_sales['sum'], name='Sales'),
            row=1, col=2
        )
        
        # Average order value
        fig.add_trace(
            go.Bar(x=category_sales.index, y=category_sales['mean'], name='Avg Order Value'),
            row=2, col=1
        )
        
        # Satisfaction scores
        fig.add_trace(
            go.Bar(x=satisfaction_by_category.head(10).index, 
                  y=satisfaction_by_category.head(10).values, name='Satisfaction'),
            row=2, col=2
        )
        
        fig.update_layout(height=1000, width=1200, title_text="Customer Behavior Dashboard")
        fig.write_html("dashboard.html")
        
        return {
            'total_customers': len(self.customers['customer_id'].unique()),
            'total_orders': len(self.orders),
            'avg_order_value': self.order_items['price'].mean(),
            'avg_satisfaction': self.reviews['review_score'].mean(),
            'top_category': category_sales.index[0]
        }

    def perform_ab_testing(self):
        # Simulate A/B testing for delivery methods
        # Group orders into fast delivery (A) and standard delivery (B)
        median_delivery = self.orders['delivery_time'].median()
        group_a = self.orders[self.orders['delivery_time'] < median_delivery]['review_score']
        group_b = self.orders[self.orders['delivery_time'] >= median_delivery]['review_score']
        
        # Perform t-test
        t_stat, p_value = stats.ttest_ind(group_a, group_b)
        
        return {
            'test_metric': 'Customer Satisfaction',
            't_statistic': t_stat,
            'p_value': p_value,
            'significant': p_value < 0.05
        }

def main():
    analyzer = CustomerBehaviorAnalyzer()
    
    # Generate insights
    insights = analyzer.generate_customer_insights()
    
    # Perform A/B testing
    ab_test_results = analyzer.perform_ab_testing()
    
    # Print summary
    print("\n=== Customer Behavior Analysis Summary ===")
    print(f"Total Customers: {insights['total_customers']:,}")
    print(f"Total Orders: {insights['total_orders']:,}")
    print(f"Average Order Value: ${insights['avg_order_value']:.2f}")
    print(f"Average Satisfaction Score: {insights['avg_satisfaction']:.2f}/5.0")
    print(f"Top Performing Category: {insights['top_category']}")
    
    print("\n=== A/B Test Results ===")
    print(f"Test Metric: {ab_test_results['test_metric']}")
    print(f"t-statistic: {ab_test_results['t_statistic']:.4f}")
    print(f"p-value: {ab_test_results['p_value']:.4f}")
    print(f"Significant Difference: {'Yes' if ab_test_results['significant'] else 'No'}")
    
    print("\nDashboard has been generated as 'dashboard.html'")

if __name__ == "__main__":
    main()
