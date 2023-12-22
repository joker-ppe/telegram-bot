import prettytable as pt


async def send_table(json_data, time_text, role='Cổ Đông'):
    table = pt.PrettyTable(['STT.', role, 'Thắng thua'])
    table.title = f'Báo cáo {role} {time_text}'
    table.align['STT.'] = 'l'
    table.align[role] = 'l'
    table.align['Thắng thua'] = 'r'

    if (json_data == "***"):
        return "Không tìm thấy thông tin. Anh vui lòng kiểm tra và thử lại."

    # print(json_data)

    data = [(item["full_name"], item["profit"])
            for item in json_data if item["profit"] != 0]

    # print(data)

    if (len(data) == 0):
        return "Không tìm thấy thông tin. Anh vui lòng kiểm tra và thử lại."

    data = sorted(data, key=lambda x: x[1], reverse=True)

    total = sum(int(item[1]) for item in data)

    for index, (full_name, profit) in enumerate(data, start=1):
        table.add_row([index, full_name, "{:,}".format(round(profit))])

    table.add_row(['----', '-----------', '-----------'])
    table.add_row(['***', 'Tổng', "{:,}".format(round(total))])

    return f'<pre>{table}</pre>'


async def send_table_image(json_data, time_text, role='Cổ Đông'):

    if (json_data == "***"):
        return "Không tìm thấy thông tin. Anh vui lòng kiểm tra và thử lại."

    # print(json_data)

    data = [(item["full_name"], item["profit"])
            for item in json_data if item["profit"] != 0]

    # print(data)

    if (len(data) == 0):
        return "Không tìm thấy thông tin. Anh vui lòng kiểm tra và thử lại."

    data = sorted(data, key=lambda x: x[1], reverse=True)

    total = sum(int(item[1]) for item in data)

    # Xây dựng bảng HTML
    html_table = "<html><body>"
    html_table += """
<head>
    <style>
        td,
      th,
      tr,
      table {
        border: 1px solid #000000;
        border-collapse: collapse;
        padding: 5px;
      }

      th {
        background-color: #faebd7;
      }

      table td:nth-child(3){
        text-align: right;
      }

      table {
        margin-left: auto;
        margin-right: auto;
        font-size: 25px;
      }

      body {
        font-family: Arial, Helvetica, sans-serif;
      }
    </style>
</head>                    
"""
    html_table += "<table>"
    html_table += f"<caption>Báo cáo {role} {time_text}</caption>"
    html_table += "<tr><th>STT.</th><th>{}</th><th>Thắng thua</th></tr>".format(role)

    for index, (full_name, profit) in enumerate(data, start=1):
        html_table += f"<tr><td>{index}</td><td>{
            full_name}</td><td>{profit:,}</td></tr>"

    # Thêm hàng tổng
    html_table += f"<tr style='font-weight: bold;'><td colspan='2' style='text-align: center;'>Tổng</td><td style='text-align: right;'>{
        total:,}</td></tr>"

    html_table += "</table>"
    html_table += "</body></html>"

    # Kết quả là một chuỗi HTML có thể được sử dụng trong Telegram Bot API
    html_output = f'{html_table}'

    return html_output


async def send_table_os(json_data, role='Cổ Đông'):
    table = pt.PrettyTable(['STT.', role, 'Outstanding'])
    table.title = f'Báo cáo Outstanding {role}'
    table.align['STT.'] = 'l'
    table.align[role] = 'l'
    table.align['Outstanding'] = 'r'

    if (json_data == "***"):
        return "Không tìm thấy thông tin. Anh vui lòng kiểm tra và thử lại."

    data = [(item["full_name"], item["outstanding"])
            for item in json_data if item["outstanding"] != 0]

    if (len(data) == 0):
        return "Không tìm thấy thông tin. Anh vui lòng kiểm tra và thử lại."

    data = sorted(data, key=lambda x: x[1], reverse=True)

    total = sum(int(item[1]) for item in data)

    for index, (full_name, outstanding) in enumerate(data, start=1):
        table.add_row([index, full_name, "{:,}".format(round(outstanding))])

    table.add_row(['----', '-----------', '-----------'])
    table.add_row(['***', 'Tổng', "{:,}".format(round(total))])

    return f'<pre>{table}</pre>'

    # update.message.reply_text(f'<pre>{table}</pre>', parse_mode=ParseMode.HTML)


async def send_table_os_image(json_data, role='Cổ Đông'):

    if (json_data == "***"):
        return "Không tìm thấy thông tin. Anh vui lòng kiểm tra và thử lại."

    data = [(item["full_name"], item["outstanding"])
            for item in json_data if item["outstanding"] != 0]

    if (len(data) == 0):
        return "Không tìm thấy thông tin. Anh vui lòng kiểm tra và thử lại."

    data = sorted(data, key=lambda x: x[1], reverse=True)

    total = sum(int(item[1]) for item in data)

    # Xây dựng bảng HTML
    html_table = "<html><body>"
    html_table += """
<head>
    <style>
        td,
      th,
      tr,
      table {
        border: 1px solid #000000;
        border-collapse: collapse;
        padding: 5px;
      }

      th {
        background-color: #faebd7;
      }

      table td:nth-child(3){
        text-align: right;
      }

      table {
        margin-left: auto;
        margin-right: auto;
        font-size: 25px;
      }

      body {
        font-family: Arial, Helvetica, sans-serif;
      }
    </style>
</head>                    
"""
    html_table += "<table>"
    html_table += f"<caption>Outstanding {role} </caption>"
    html_table += "<tr><th>STT.</th><th>{}</th><th>Outstanding</th></tr>".format(
        role)

    for index, (full_name, outstanding) in enumerate(data, start=1):
        html_table += f"<tr><td>{index}</td><td>{
            full_name}</td><td>{outstanding:,}</td></tr>"

    # Thêm hàng tổng
    html_table += f"<tr style='font-weight: bold;'><td colspan='2' style='text-align: center;'>Tổng</td><td style='text-align: right;'>{
        total:,}</td></tr>"

    html_table += "</table>"
    html_table += "</body></html>"

    # Kết quả là một chuỗi HTML có thể được sử dụng trong Telegram Bot API
    html_output = f'{html_table}'

    return html_output

    # update.message.reply_text(f'<pre>{table}</pre>', parse_mode=ParseMode.HTML)

async def send_table_user_image(json_data):
    # print(json_data)

    if (json_data == "***"):
        return "Không tìm thấy thông tin. Anh vui lòng kiểm tra và thử lại."


    # Xây dựng bảng HTML
    html_table = "<html><body>"
    html_table += """
<head>
    <style>
        td,
      th,
      tr,
      table {
        border: 1px solid #000000;
        border-collapse: collapse;
        padding: 5px;
      }

      th {
        background-color: #faebd7;
      }

      table td:nth-child(2){
        text-align: right;
      }

      table {
        margin-left: auto;
        margin-right: auto;
        font-size: 25px;
      }

      body {
        font-family: Arial, Helvetica, sans-serif;
      }
    </style>
</head>                    
"""
    html_table += "<table>"
    # html_table += f"<caption>Outstanding {role} </caption>"
    html_table += f"<tr><th>{json_data['title']}</th><th>{json_data['full_name']}</th></tr>"

    html_table += f"<tr><td>Line</td><td style='text-align: center;'>{json_data['line']}</td></tr>"
    html_table += f"<tr><td>Thắng thua hôm qua</td><td>{"{:,}".format(round(json_data['yesterdayData']))}</td></tr>"
    html_table += f"<tr><td>Thắng thua hôm nay</td><td>{"{:,}".format(round(json_data['todayData']))}</td></tr>"
    html_table += f"<tr><td>Thắng thua tuần này</td><td>{"{:,}".format(round(json_data['profit']))}</td></tr>"

    html_table += "</table>"
    html_table += "</body></html>"

    # Kết quả là một chuỗi HTML có thể được sử dụng trong Telegram Bot API
    html_output = f'{html_table}'

    return html_output

    # update.message.reply_text(f'<pre>{table}</pre>', parse_mode=ParseMode.HTML)



def check_response(message, response):
    if (response == "***"):
        return "Không tìm thấy thông tin. Anh vui lòng kiểm tra và thử lại."

    formatted_number = "{:,}".format(round(response))
    return f'{message} {formatted_number}'


def check_response_company_profit(message, response):
    if (response == "***"):
        return "Không tìm thấy thông tin. Anh vui lòng kiểm tra và thử lại."

    formatted_number = "{:,}".format(round(int(response) * (-1) * 20 / 100))
    return f'{message} {formatted_number}'
