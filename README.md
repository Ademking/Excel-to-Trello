# Excel To Trello

Simple python script that creates __Trello Cards/Labels__ using Excel

## Installation

0. Clone this repository
1. install requirements using this command :  `pip install -r requirements.txt`
2. Edit `data.xlsx` 
3. In `app.py`, change it with your variables:
   ```python
    api_key = "YOUR_API_KEY_HERE"
    token = "YOUR_TOKEN_HERE"
    board_id = "BOARD_ID_HERE"
    list_name = "LIST_NAME_HERE"
    xlsx_file_path = "data.xlsx"
    label_name = "LABEL_NAME_HERE"
    ```
    * api_key: You can get it from here [https://trello.com/app-key](https://trello.com/app-key)
    * token: You can get it from here [https://trello.com/app-key](https://trello.com/app-key)
    * board_id: From URL
    * list_name: Name of the list you want to populate - example: "Todo"
    * xlsx_file_path: Path of your excel file
    * label_name: Name of the label you want to add

4. run: `python app.py`



