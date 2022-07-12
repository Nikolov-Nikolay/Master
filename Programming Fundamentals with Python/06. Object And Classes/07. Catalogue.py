class Catalogue:
    products = []

    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product_name):
        self.product_name = product_name
        self.products.append(product_name)

    def get_by_letter(self, first_letter):
        self.first_letter = first_letter
        result = [index for index in self.products if index[0] == first_letter]
        return result

    def __repr__(self):
        result = ''
        joining = "\n".join(sorted(self.products))
        result += f"Items in the {self.name} catalogue:\n{joining}"
        return result

catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
