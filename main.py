import openpyxl

inv_file = openpyxl.load_workbook("inventory.xlsx")
print(inv_file["Sheet1"])
product_list = inv_file["Sheet1"]

products_by_supplier = {}

print(product_list.max_row)

for product_row in range(2, product_list.max_row + 1):
    supplier_name = product_list.cell(product_row, 4).value
    print(supplier_name)

    if supplier_name in products_by_supplier:
        current_num_product = products_by_supplier.get(supplier_name)
        products_by_supplier[supplier_name] = current_num_product + 1
    else:
        print("new supplier added")
        products_by_supplier[supplier_name] = 1

print(products_by_supplier)