scanned_barcodes = []


def check_barcode(barcode, items_list):
  if barcode in scanned_barcodes:
    return "Wrong scanned already"
  elif barcode in items_list:
    scanned_barcodes.append(barcode)
    return "Valid"
  else:
    return "Wrong"


items_list = (vul zelf in geschijden door een ' ,')



while True:
  barcode = input("Scan een QR-code (of typ 'q' om te stoppen): ")
  if barcode == 'q':
    break
  else:
    result = check_barcode(barcode, items_list)
    print(result)
