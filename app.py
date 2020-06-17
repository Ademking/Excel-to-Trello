from trello import TrelloAPI as Trello
from openpyxl import load_workbook


def TrelloImport(api_key, token, board_id, list_name, xlsx_file_path, label_name):
    MyTrello = Trello(api_key, token)
    B = MyTrello.GetBoardById(board_id)
    List = B.GetListByName(list_name)
    wb = load_workbook(xlsx_file_path)
    sheet = wb.active
    max_row = sheet.max_row
    label_name = B.GetLabelByName(label_name)
    for i in range(1, max_row+1):

        card_content = sheet.cell(row=i, column=1).value
        label = sheet.cell(row=i, column=2).value
        Card = MyTrello.new('Card', card_content, List)
        Card.AddLabel(label_name)


def main():
    api_key = "YOUR_API_KEY_HERE"
    token = "YOUR_TOKEN_HERE"
    board_id = "BOARD_ID_HERE"
    list_name = "LIST_NAME_HERE"
    xlsx_file_path = "data.xlsx"
    label_name = "LABEL_NAME_HERE"
    TrelloImport(api_key, token, board_id, list_name,
                 xlsx_file_path, label_name)

if __name__ == '__main__':
    main()