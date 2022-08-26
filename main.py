from operator import truediv
import config
import openpyxl

def informations():
    city = config.soup.find('a', class_='current-location')
    card_name = config.soup.findAll('a', class_='item-card__name')
    card_price = config.soup.findAll('span', class_='item-card__prices-price')
    card_as = config.soup.findAll('span', class_='item-card__prices-title')
    card_prices = config.soup.findAll('div', class_='item-card__debet')
    card_inc = config.soup.findAll('div', class_='item-card__instalment')
    card_price_p = config.soup.findAll('div', class_='item-card__instalment')
    card_info = config.soup.findAll('span', class_='item-card__add-info')
    code = config.soup.findAll('a', href=True, class_="item-card__name ddl_product_link")
        
    # for bone in card_name:
    #     cardname = bone.text
    # for c in card_prices:
    #     cardprices =  c.text
    # for v in card_inc:
    #     cardinc =  v.text
    
    link_kaspi = 'https://kaspi.kz'
    
    book = openpyxl.Workbook()
    sheet = book.active

    sheet['A1'] = 'Name'
    sheet['B1'] = "Price"
    sheet['C1'] = "Inc"
    sheet['D1'] = "Link"
    row = 2
    for name in card_name:
        sheet[row][0].value = name.text
        row += 1
    
    row = 2
    for price in card_prices:
        sheet[row][1].value = price.text
        row += 1
        
    row = 2
    for inc in card_inc:
        sheet[row][2].value = inc.text
        row += 1

    row = 2
    for link in code:
        first = link['href']
        sheet[row][3].value = link_kaspi+first
        row += 1
    
    file_name = input("File name: ")
    book.save(file_name+".xlsx")
    book.close()

def main():
    informations()

if __name__ == '__main__':
    main()