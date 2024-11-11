# Customer Behavior Analysis Project

## Overview
This project analyzes customer behavior patterns using real e-commerce data from Brazilian e-commerce platform Olist. It processes order data, customer interactions, and product information to generate actionable insights for business optimization.

## Features
- Automated data pipeline for processing e-commerce transaction data
- Interactive dashboard showing key customer behavior metrics
- Statistical analysis including A/B testing
- Comprehensive visualization of sales trends and customer satisfaction
- Zero configuration required - works out of the box with public dataset

## Key Insights Generated
- Monthly order trends and seasonality
- Top performing product categories
- Customer satisfaction analysis
- Delivery performance impact on customer satisfaction
- Product pricing analysis

## Technical Implementation
- **Data Processing**: Automated ETL pipeline using pandas
- **Statistical Analysis**: Implemented A/B testing using scipy
- **Visualization**: Interactive dashboard using plotly
- **Data Source**: Real e-commerce data from Olist (Brazilian e-commerce platform)

## Requirements
- Python 3.8+
- Dependencies listed in requirements.txt

## Installation & Usage
1. Clone this repository:
```bash
git clone https://github.com/yourusername/customer-behavior-analysis.git
cd customer-behavior-analysis
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Run the analysis:
```bash
python main.py
```

4. View the results:
- Check the console output for key metrics
- Open `dashboard.html` in your browser for interactive visualizations

## Output
The program generates:
1. Interactive dashboard (dashboard.html)
2. Console output with key metrics
3. Statistical test results

## Data Description
The analysis uses the following data from the Brazilian E-commerce Public Dataset by Olist:
- Orders dataset: Basic order information
- Order items dataset: Products purchased in each order
- Products dataset: Product details
- Customers dataset: Customer information
- Reviews dataset: Customer satisfaction data

## Business Impact
This analysis helps in:
- Identifying top-performing product categories
- Understanding customer satisfaction drivers
- Optimizing delivery processes
- Making data-driven product decisions

## Future Improvements
- Add machine learning models for customer segmentation
- Implement real-time data processing
- Add more advanced statistical analyses
- Include customer churn prediction

## Contributing
Feel free to fork this project and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License
MIT License - see LICENSE file for details

## Acknowledgments
- Olist for providing the public dataset
- UCI Machine Learning Repository for hosting the data
