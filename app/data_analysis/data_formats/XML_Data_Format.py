import pandas as pd
import requests
from app.config.AppSettings import AppSettings
import xml.etree.ElementTree as ET
from datetime import datetime

settings = AppSettings()

headers = {"Authorization": "token {}".format(settings._token), "Accept": "application/xml"}

#Reading XML file
url_list = []
url_list.append(settings._common_account)
url_list.append(settings._repo_name)
url_list.append(settings._branch_name)
url_list.append(settings._app_root)
url_list.append(settings._data_analysis_folder)
url_list.append(settings._raw_files_path)
url_list.append(settings._xml_path)

xml_url = settings._raw_data_url + "/".join(url_list)
resp = requests.get(xml_url, headers=headers)

#Read Root
root = ET.fromstring(resp.content)

po_entries = []
all_xml_items = []
date_format = "%Y-%m-%d"

for po in root.iter("PurchaseOrder"):
    po_num = po.attrib.get("PurchaseOrderNumber")
    ord_dt = po.attrib.get("OrderDate")

    del_notes_obj = None
    del_notes = ""
    del_notes_obj = po.find("DeliveryNotes")
    if del_notes_obj is not None:
        del_notes = del_notes_obj.text

    ship_addr = {}
    bill_addr = {}

    add_array = po.findall("Address")
    for it in add_array:
        if it.attrib.get("Type") == "Shipping":
            ship_addr["shipping_name"] = it.find("Name").text
            ship_addr["shipping_street"] = it.find("Street").text
            ship_addr["shipping_city"] = it.find("City").text
            ship_addr["shipping_state"] = it.find("State").text
            ship_addr["shipping_zip"] = it.find("Zip").text
            ship_addr["shipping_country"] = it.find("Country").text
        elif it.attrib.get("Type") == "Billing":
            bill_addr["billing_name"] = it.find("Name").text
            bill_addr["billing_street"] = it.find("Street").text
            bill_addr["billing_city"] = it.find("City").text
            bill_addr["billing_state"] = it.find("State").text
            bill_addr["billing_zip"] = it.find("Zip").text
            bill_addr["billing_country"] = it.find("Country").text

    it_lst = po.find("Items")
    it_elem_arr = it_lst.findall("Item")
    items = []

    for it_elem in it_elem_arr:
        item = {}

        item["item_part_number"] = it_elem.attrib.get("PartNumber")

        prod_name_obj = None
        prod_name = ""
        prod_name_obj = it_elem.find("ProductName")
        if prod_name_obj is not None:
          prod_name = prod_name_obj.text
        item["item_name"] = prod_name

        qty_obj = None
        qty = 0
        qty_obj = it_elem.find("Quantity")
        if qty_obj is not None:
          qty = int(qty_obj.text)
        item["item_quantity"] = qty

        price_obj = None
        price = 0.0
        price_obj = it_elem.find("USPrice")
        if price_obj is not None:
          price = float(price_obj.text)
        item["item_price"] = price

        date_obj = None
        ship_dt = None
        ship_dt_obj = it_elem.find("ShipDate")
        if ship_dt_obj is not None:
            ship_dt = ship_dt_obj.text
            date_obj = datetime.strptime(ship_dt, date_format)
            if date_obj is not None:
              ship_dt = date_obj.date()
        item["item_ship_date"] = ship_dt

        comment_obj = it_elem.find("Comment")
        comment = ""
        if comment_obj is not None:
            comment = comment_obj.text
        item["item_comment"] = comment

        items.append(item)

    po_entry = [po_num, ord_dt, del_notes,
                ship_addr["shipping_name"], ship_addr["shipping_street"], ship_addr["shipping_city"],
                ship_addr["shipping_state"], ship_addr["shipping_zip"], ship_addr["shipping_country"],
                bill_addr["billing_name"], bill_addr["billing_street"], bill_addr["billing_city"],
                bill_addr["billing_state"], bill_addr["billing_zip"], bill_addr["billing_country"],
                items]

    all_xml_items.append(po_entry)
    
#Converting list of all items to dataframe
s_no = 0
all_items = []

for p in range(0, len(all_xml_items)):
    po_items = all_xml_items[p]

    items_lst = po_items[15]

    for idx in range(0, len(items_lst)):
      s_no += 1

      item_dict = items_lst[idx]

      po_entry = [s_no, po_items[0], po_items[1], po_items[2],
                po_items[3], po_items[4], po_items[5],
                po_items[6], po_items[7], po_items[8],
                po_items[9], po_items[10], po_items[11],
                po_items[12], po_items[13], po_items[14],
                item_dict["item_part_number"], item_dict["item_name"], item_dict["item_quantity"], item_dict["item_price"],
                item_dict["item_ship_date"], item_dict["item_comment"] ]

      all_items.append(po_entry)

#Convert all records to dataframe
xmlToDf = pd.DataFrame(all_items, columns=[
  "S_NO", "PO_NUM", "ORDER_DATE", "DELIVERY_NOTES", "SHIPPING_NAME", "SHIPPING_STREET", "SHIPPING_CITY",
    "SHIPPING_STATE", "SHIPPING_ZIP", "SHIPPING_COUNTRY", "BILLING_NAME", "BILLING_STREET", "BILLING_CITY",
    "BILLING_STATE", "BILLING_ZIP", "BILLING_COUNTRY", "ITEM_PART_NUMBER", "ITEM_NAME", "ITEM_QTY", "ITEM_PRICE",
    "ITEM_SHIP_DATE", "ITEM_COMMENT"])

xmlToDf.head()