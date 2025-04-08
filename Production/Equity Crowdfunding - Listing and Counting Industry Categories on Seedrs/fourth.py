import re

def get_text():
    return """
Clothing and Home (Clothing & Accessories, Home & Personal, Healthcare); 
E-Commerce and Marketing (Advertising & Marketing, Data & Analytics, Content & Information); 
Finance (Finance & payments, Recruitment & Procurement, Property); Food and Drink (Food & Beverage);  
Games and Entertainment (Entertainment, Games); Technology (Programming & Security, SaaS/PaaS);  
Transport and Travel (Automotive & Transport, Travel, Leisure & Sport, Energy). 
"""

def get_categories():
    text = get_text()
    return [c.strip() for c in re.findall(r'([^();]+?)\s*\(', text)]


if __name__ == "__main__":
    categories = get_categories()
    print(categories)
