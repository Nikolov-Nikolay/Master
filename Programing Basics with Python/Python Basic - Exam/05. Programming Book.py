price_for_one_page = float(input())
price_for_one_cover = float(input())
percent_discount_for_print_paper = int(input())
price_for_designer = float(input())
percent_price_for_the_crew = int(input())


price_for_full_book = (price_for_one_page *  899) + (price_for_one_cover * 2)
discount_for_book = price_for_full_book - (price_for_full_book * percent_discount_for_print_paper) / 100
full_price_after_design = discount_for_book + price_for_designer
full_price_for_book = full_price_after_design - (full_price_after_design * percent_price_for_the_crew) / 100
print(f'Avtonom should pay {full_price_for_book:.2f} BGN. ')