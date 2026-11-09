from selectolax.parser import HTMLParser

html = """
<html>
<head><title>Пример страницы</title></head>
<body>
    <div class="products">
        <h1>Товары</h1>
        <div class="product">
            <span class="name">Телефон</span>
            <span class="price">100$</span>
        </div>
        <div class="product">
            <span class="name">Ноутбук</span>
            <span class="price">500$</span>
        </div>
    </div>
</body>
</html>
"""


tree = HTMLParser(html=html)

products = tree.css('.product')
for product in products:
    name = product.css_first('.name')
    price = product.css_first('.price')
    print(f"Товар: {name.text()}, Цена: {price.text()}") # type: ignore

