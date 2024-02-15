from datetime import datetime
import prettytable as pt

async def send_table(json_data, time_text, role='Cổ Đông'):
    table = pt.PrettyTable(['STT.', role, 'Thắng thua'])
    table.title = f'Báo cáo {role} {time_text}'
    table.align['STT.'] = 'l'
    table.align[role] = 'l'
    table.align['Thắng thua'] = 'r'

    if (json_data == "***"):
        return "Không tìm thấy thông tin. Sếp vui lòng kiểm tra và thử lại."

    # print(json_data)

    data = [(item["full_name"], item["profit"])
            for item in json_data if item["profit"] != 0]

    # print(data)

    if (len(data) == 0):
        return "Không tìm thấy thông tin. Sếp vui lòng kiểm tra và thử lại."

    data = sorted(data, key=lambda x: x[1], reverse=True)

    total = sum(int(item[1]) for item in data)

    for index, (full_name, profit) in enumerate(data, start=1):
        table.add_row([index, full_name, "{:,}".format(round(profit))])

    table.add_row(['----', '-----------', '-----------'])
    table.add_row(['***', 'Tổng', "{:,}".format(round(total))])

    return f'<pre>{table}</pre>'


async def send_table_image(json_data, time_text = 'tuần này', role='Cổ Đông', threshold='threshold'):

    if (json_data == "***"):
        return "Không tìm thấy thông tin. Sếp vui lòng kiểm tra và thử lại."

    # print(json_data)
    title = f"<caption>Báo cáo {role} {time_text}</caption>"

    if threshold.isdecimal() == False:
        threshold = 0
    else:
        threshold = int(threshold)
        title = f"<caption>Báo cáo {role} {time_text} đạt ngưỡng {(threshold * 1000000):,}</caption>"

    print('Threshold: '+ str(threshold))

    data = [(item["full_name"], item["profit"])
            for item in json_data if (item["profit"] != 0 and abs(item["profit"]) >= (threshold * 1000000))]
    
    if role != 'Hội Viên':
        data = [(item["full_name"], item["bidPercent"], item["profit"])
            for item in json_data if (item["profit"] != 0 and abs(item["profit"]) >= (threshold * 1000000))]

    # print(data)

    if (len(data) == 0):
        return "Không tìm thấy thông tin. Sếp vui lòng kiểm tra và thử lại."
    
    total = sum(int(item[1]) for item in data)

    if role != 'Hội Viên':
        data = sorted(data, key=lambda x: x[2], reverse=True)
        total = sum(int(item[2]) for item in data)
    else:
        data = sorted(data, key=lambda x: x[1], reverse=True)
        


    

    # Xây dựng bảng HTML
    html_table = "<html><body>"
    html_table += f"<title>wl-{role}-{time_text}</title>"
    html_table += """
<head>
    <meta charset="UTF-8">
    <link href='https://fonts.googleapis.com/css?family=Be Vietnam Pro' rel='stylesheet'>
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

      table {
        margin-left: auto;
        margin-right: auto;
        font-size: 25px;
      }

      body {
        font-family: 'Be Vietnam Pro';
      }

      .win {
        color: blue;
      }

      .lose {
        color: red;
      }
    </style>
</head>                    
"""
    html_table += "<table>"
    html_table += title

    colspan = 2
    if role == 'Hội Viên':
        html_table += "<tr><th>STT.</th><th>{}</th><th>Thắng thua</th></tr>".format(role)
        for index, (full_name, profit) in enumerate(data, start=1):
            if profit > 0:
                html_table += f"<tr><td>{index}</td><td>{full_name}</td><td class='win' style='text-align: right;'>{profit:,}</td></tr>"
            else:
                html_table += f"<tr><td>{index}</td><td>{full_name}</td><td class='lose' style='text-align: right;'>{profit:,}</td></tr>"
    else:
        colspan = 3
        html_table += "<tr><th>STT.</th><th>{}</th><th>Thầu</th><th>Thắng thua</th></tr>".format(role)
        for index, (full_name, bid_percent, profit) in enumerate(data, start=1):
            if profit > 0:
                html_table += f"<tr><td>{index}</td><td>{full_name}</td><td style='text-align: right;'>{bid_percent}</td><td class='win' style='text-align: right;'>{profit:,}</td></tr>"
            else:
                html_table += f"<tr><td>{index}</td><td>{full_name}</td><td style='text-align: right;'>{bid_percent}</td><td class='lose' style='text-align: right;'>{profit:,}</td></tr>"
       
    # Thêm hàng tổng
    if total > 0:
        html_table += f"<tr style='font-weight: bold;'><td colspan='{colspan}' style='text-align: center;'>Tổng</td><td class='win' style='text-align: right;'>{total:,}</td></tr>"
    else:
        html_table += f"<tr style='font-weight: bold;'><td colspan='{colspan}' style='text-align: center;'>Tổng</td><td class='lose' style='text-align: right;'>{total:,}</td></tr>"

    html_table += "</>"
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
        return "Không tìm thấy thông tin. Sếp vui lòng kiểm tra và thử lại."

    data = [(item["full_name"], item["outstanding"])
            for item in json_data if item["outstanding"] != 0]

    if (len(data) == 0):
        return "Không tìm thấy thông tin. Sếp vui lòng kiểm tra và thử lại."

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
        return "Không tìm thấy thông tin. Sếp vui lòng kiểm tra và thử lại."

    data = [(item["full_name"], item["outstanding"])
            for item in json_data if item["outstanding"] != 0]

    if (len(data) == 0):
        return "Không tìm thấy thông tin. Sếp vui lòng kiểm tra và thử lại."

    data = sorted(data, key=lambda x: x[1], reverse=True)

    total = sum(int(item[1]) for item in data)

    # Xây dựng bảng HTML
    html_table = "<html><body>"
    html_table += f"<title>os-{role}</title>"
    html_table += """
<head>
    <meta charset="UTF-8">
    <link href='https://fonts.googleapis.com/css?family=Be Vietnam Pro' rel='stylesheet'>
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
        font-family: 'Be Vietnam Pro';
      }
    </style>
</head>                    
"""
    html_table += "<table>"
    html_table += f"<caption>Outstanding {role} </caption>"
    html_table += "<tr><th>STT.</th><th>{}</th><th>Outstanding</th></tr>".format(
        role)

    for index, (full_name, outstanding) in enumerate(data, start=1):
        html_table += f"<tr><td>{index}</td><td>{full_name}</td><td>{outstanding:,}</td></tr>"

    # Thêm hàng tổng
    html_table += f"<tr style='font-weight: bold;'><td colspan='2' style='text-align: center;'>Tổng</td><td style='text-align: right;'>{total:,}</td></tr>"

    html_table += "</table>"
    html_table += "</body></html>"

    # Kết quả là một chuỗi HTML có thể được sử dụng trong Telegram Bot API
    html_output = f'{html_table}'

    return html_output

    # update.message.reply_text(f'<pre>{table}</pre>', parse_mode=ParseMode.HTML)

async def send_table_user_image(json_data):
    # print(json_data)

    if (json_data == "***"):
        return "Không tìm thấy thông tin. Sếp vui lòng kiểm tra và thử lại."


    # Xây dựng bảng HTML
    html_table = "<html><body>"
    html_table += """
<head>
    <meta charset="UTF-8">
    <link href='https://fonts.googleapis.com/css?family=Be Vietnam Pro' rel='stylesheet'>
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
        font-family: 'Be Vietnam Pro';
      }

      .win {
        color: blue;
      }

      .lose {
        color: red;
      }
    </style>
</head>                    
"""
    html_table += "<table>"
    # html_table += f"<caption>Outstanding {role} </caption>"
    html_table += f"<tr><th>{json_data['title']}</th><th>{json_data['full_name']}</th></tr>"

    html_table += f"<tr><td>Line</td><td style='text-align: center;'>{json_data['line']}</td></tr>"

    if int(json_data['level']) != 5:
        for index, (children) in enumerate(json_data['list_children'], start=1):
            name = children['full_name']
            outstanding = "{:,}".format(round(children['outstanding']))
            profit = "{:,}".format(round(children['profit']))
            commission = "{:,}".format(round(children['commission']))
            
            
            profit_item = f"""
            <span class='lose'>{profit}</span>               
"""
            if round(children['profit']) > 0:
                profit_item = f"""
            <span class='win'>{profit}</span>               
"""
            if index == 1:
                html_table += f"""
    <tr>
        <td rowspan='{len(json_data['list_children'])}'>Tuyến dưới</td>
        <td style='text-align: left;'>{name}<br/>wl: {profit_item}<br/>os: {outstanding}<br/>hh: {commission}</td>
    </tr>
    """             
            else:
                html_table += f"""
    <tr>
        <td style='text-align: left;'>{name}<br/>wl: {profit_item}<br/>os: {outstanding}<br/>hh: {commission}</td>
    </tr>
    """            

    yesterdayData = "{:,}".format(round(json_data['yesterdayData']))
    if round(json_data['yesterdayData']) > 0:
        html_table += f"<tr><td>Thắng thua hôm qua</td><td class='win'>{yesterdayData}</td></tr>"
    else:
        html_table += f"<tr><td>Thắng thua hôm qua</td><td class='lose'>{yesterdayData}</td></tr>"
    
    todayData = "{:,}".format(round(json_data['todayData']))
    if round(json_data['todayData']) > 0:
        html_table += f"<tr><td>Thắng thua hôm nay</td><td class='win'>{todayData}</td></tr>"
    else:
        html_table += f"<tr><td>Thắng thua hôm nay</td><td class='lose'>{todayData}</td></tr>"

    profit = "{:,}".format(round(json_data['profit']))
    if round(json_data['profit']) > 0:
        html_table += f"<tr><td>Thắng thua tuần này</td><td class='win'>{profit}</td></tr>"
    else:
        html_table += f"<tr><td>Thắng thua tuần này</td><td class='lose'>{profit}</td></tr>"


    outstanding = "{:,}".format(round(json_data['outstanding']))
    html_table += f"<tr><td>Outstanding</td><td>{outstanding}</td></tr>"

    commission = 0
    if json_data['level'] == 1:
        commission = json_data['companyCommission'] + json_data['adminCommission']
    elif json_data['level'] == 2:
        commission = json_data['superCommission']
    elif json_data['level'] == 3:
        commission = json_data['masterCommission']
    elif json_data['level'] == 4:
        commission = json_data['agentCommission']
    
    if json_data['level'] != 5:
        commission = "{:,}".format(round(commission))
        html_table += f"<tr><td>HH</td><td>{commission}</td></tr>"
    

    data_bet_keys = json_data['data_bet'].keys()

    # print(json_data['data_bet'])
    # print(data_bet_keys)

    if (len(data_bet_keys) > 0 and int(json_data['outstanding']) != 0):
        for index, (key) in enumerate(data_bet_keys, start=0):
            game_name = get_type_game(int(key))
            point = "{:,}".format(round(json_data['data_bet'][key]['point']))
            amount = "{:,}".format(round(json_data['data_bet'][key]['amount']))
            if index == 0:
                html_table += f"<tr><td rowspan='{len(data_bet_keys)}'>Cược</td><td style='text-align: left;'><strong>{game_name}</strong><br/>{point} điểm<br/>{amount}</td></tr>"
            else:
                html_table += f"<tr><td style='text-align: left;'><strong>{game_name}</strong><br/>{point} điểm<br/>{amount}</td></tr>"


    html_table += "</>"
    # table bet record
    
    html_table += "</body></html>"

    # Kết quả là một chuỗi HTML có thể được sử dụng trong Telegram Bot API
    html_output = f'{html_table}'

    return html_output

    # update.message.reply_text(f'<pre>{table}</pre>', parse_mode=ParseMode.HTML)

async def send_table_report_super_image(json_data): 
    if (json_data == "***"):
        return "Không tìm thấy thông tin. Sếp vui lòng kiểm tra và thử lại."
    
    list_masters = json_data['listMasters']
    list_supers = json_data['listSupers']
    if (len(list_masters) == 0 and len(list_supers) == 0):
        return f"Không tìm thấy thông tin thanh toán cho {json_data['name']}. Sếp vui lòng kiểm tra và thử lại."
    
    html_table = "<html><body>"
    html_table += """
<head>
    <meta charset="UTF-8">
    <title>pdf</title>
    <link href='https://fonts.googleapis.com/css?family=Be Vietnam Pro' rel='stylesheet'>
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

      td{
white-space:nowrap;
}

      body {
        font-family: 'Be Vietnam Pro';
      }

      .win {
        color: blue;
      }

      .lose {
        color: red;
      }

    </style>
</head>                    
"""
    from_date = parse_date({json_data['fromDate']})
    to_date = parse_date({json_data['toDate']})

    html_table += "<table>"
    html_table += f"<caption style='font-size: 35px; margin-bottom: 10px;'><strong>Báo cáo {json_data['name']} từ ngày {from_date} đến ngày {to_date}</strong></caption>"
    html_table += "<tr><th>Super</th><th>TK</th><th>Thầu</th><th>Thắng thua</th><th>Hoa Hồng</th><th>Hoa Hồng Tuyến Dưới</th><th>Thanh Toán</th></tr>"

    total_profit = 0
    total_commission = 0
    total_down_line_commission = 0
    total_payment = 0

    for index, (master) in enumerate(list_masters, start=1):
        full_name = master['full_name']
        bid_percent = master['bidPercent']
        profit = master['profit']
        commission = master['masterCommission']
        down_line_commission = master['downLineCommission']
        payment = round((profit + commission + down_line_commission) * (100 - bid_percent) / 100)

        total_profit += profit
        total_commission += commission
        total_down_line_commission += down_line_commission
        total_payment += payment

        class_profit = 'lose'
        class_payment = 'lose'
        if profit > 0:
            class_profit = 'win'
        if payment > 0:
            class_payment = 'win'
        
        if index == 1:
          html_table += f"""<tr>
                              <td rowspan={len(list_masters)} style='text-align: left;'>Công Ty</td>
                              <td style='text-align: left;'>{full_name}</td>
                              <td style='text-align: right;'>{bid_percent}%</td>
                              <td class='{class_profit}' style='text-align: right;'>{profit:,}</td>
                              <td style='text-align: right;'>{commission:,}</td>
                              <td style='text-align: right;'>{down_line_commission:,}</td>
                              <td class='{class_payment}' style='text-align: right;'>{payment:,}</td>
                            </tr>"""
        else:
          html_table += f"""<tr>
                              <td style='text-align: left;'>{full_name}</td>
                              <td style='text-align: right;'>{bid_percent}%</td>
                              <td class='{class_profit}' style='text-align: right;'>{profit:,}</td>
                              <td style='text-align: right;'>{commission:,}</td>
                              <td style='text-align: right;'>{down_line_commission:,}</td>
                              <td class='{class_payment}' style='text-align: right;'>{payment:,}</td>
                            </tr>"""

    for index, (super) in enumerate(list_supers, start=1):
        full_name = super['full_name']
        bid_percent = super['bidPercent']
        profit = super['profit']
        commission = super['superCommission']
        down_line_commission = super['downLineCommission']
        payment = round((profit + commission + down_line_commission) * (100 - bid_percent) / 100)  

        total_profit += profit
        total_commission += commission
        total_down_line_commission += down_line_commission
        total_payment += payment

        class_profit = 'lose'
        class_payment = 'lose'
        if profit > 0:
            class_profit = 'win'
        if payment > 0:
            class_payment = 'win'  
        
        html_table += f"""<tr>
                              <td style='text-align: left;'>{full_name}</td>
                              <td style='text-align: left;'></td>
                              <td style='text-align: right;'>{bid_percent}%</td>
                              <td class='{class_profit}' style='text-align: right;'>{profit:,}</td>
                              <td style='text-align: right;'>{commission:,}</td>
                              <td style='text-align: right;'>{down_line_commission:,}</td>
                              <td class='{class_payment}' style='text-align: right;'>{payment:,}</td>
                            </tr>"""

    class_profit = 'lose'
    class_payment = 'lose'
    text_payment = 'Tổng Trả Công Ty'
    if total_profit > 0:
      class_profit = 'win'
    if total_payment > 0:
      class_payment = 'win'
      text_payment = 'Tổng Công Ty Bù'
    # Thêm hàng tổng
    html_table += f"""<tr style='font-weight: bold; font-size: 27px;'>
                            <td colspan='3' style='text-align: center;'>Tổng</td>
                            <td class='{class_profit}' style='text-align: right;'>{total_profit:,}</td>
                            <td style='text-align: right;'>{total_commission:,}</td>
                            <td style='text-align: right;'>{total_down_line_commission:,}</td>
                            <td class='{class_payment}' style='text-align: right;'>{total_payment:,}</td>
                      </tr>"""
    


    html_table += f"""<tr style='font-weight: bold; font-size: 30px;'>
                            <td colspan='6' style='text-align: center;'>{text_payment}</td>
                            <td style='text-align: right;'>{abs(total_payment):,}</td>
                      </tr>"""
    

    html_table += "</table>"
    html_table += "</body></html>"

    # Kết quả là một chuỗi HTML có thể được sử dụng trong Telegram Bot API
    html_output = f'{html_table}'

    return html_output

async def send_table_report_list(json_data): 
    if (json_data == "***"):
        return "Không tìm thấy thông tin. Sếp vui lòng kiểm tra và thử lại."
    
    html_table = "<html><body>"
    html_table += """
<head>
    <meta charset="UTF-8">
    <title>pdf</title>
    <link href='https://fonts.googleapis.com/css?family=Be Vietnam Pro' rel='stylesheet'>
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

      td{
white-space:nowrap;
}

      body {
        font-family: 'Be Vietnam Pro';
      }

      .win {
        color: blue;
      }

      .lose {
        color: red;
      }

    </style>
</head>                    
"""
    html_table += "<table>"
    html_table += "<tr><th>No.</th><th>Name</th><th>Nick name</th><th>Super</th><th>Master</th></tr>"

    for index, (item) in enumerate(json_data, start=1):  
        html_table += f"""<tr>
                              <td style='text-align: right;'>{index}</td>
                              <td style='text-align: left;'>{item['name']}</td>
                              <td style='text-align: left;'>{item['nickName']}</td>
                              <td style='text-align: left;'>{item['super']}</td>
                              <td style='text-align: left;'>{item['master']}</td>
                            </tr>"""  

    html_table += "</table>"
    html_table += "</body></html>"

    # Kết quả là một chuỗi HTML có thể được sử dụng trong Telegram Bot API
    html_output = f'{html_table}'

    return html_output

async def send_table_user_os_number_image(json_data):
    # print(json_data)

    if (json_data == "***"):
        return "Không tìm thấy thông tin. Sếp vui lòng kiểm tra và thử lại."

    if int(json_data['level']) != 5:
        return f"Tài khoản {json_data['full_name']} không phải là Hội viên. Vui lòng kiểm tra lại."

    # Xây dựng bảng HTML
    html_table = "<html><body>"
    html_table += """
<head>
    <meta charset="UTF-8">
    <link href='https://fonts.googleapis.com/css?family=Be Vietnam Pro' rel='stylesheet'>
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
        font-family: 'Be Vietnam Pro';
      }
    </style>
</head>                    
"""
   
    # table bet record
    
    if (json_data['outstanding'] == 0) and (int(json_data['level']) == 5):
        html_table += "<table>"
        html_table += f"<caption>Outstanding {json_data['full_name']}</caption>"
        html_table += f"<tr><th>Loại cược</th><th>Số</th><th>Điểm</th><th>Giá</th><th>Tổng</th></tr>"

        keys = json_data['data'].keys()
        print(keys)

        if (len(keys) == 0):
            return f"Tài khoản {json_data['full_name']} không có dữ liệu Outstanding hôm nay."

        for index, (key) in enumerate(keys, start=0):

            print(key)
        
            game_name = get_type_game(int(key))

            print(game_name)
            # print(json_data['data'][key])

            
            for index_bet, (item) in enumerate(json_data['data'][key], start=1):
                number = " ".join(str(x) for x in item['number'])
                if (index_bet == 1):
                    html_table += f"""
    <tr>
        <td rowspan='{len(json_data['data'][key])}'>{game_name}</td>
        <td style='text-align: center;'>{number}</td>
        <td style='text-align: right;'>{item['point']:,}</td>
        <td style='text-align: right;'>{item['price']:,}</td>
        <td style='text-align: right;'>{item['amount']:,}</td>
    </tr>
    """             
                else:
                    html_table += f"""
    <tr>
        <td style='text-align: center;'>{number}</td>
        <td style='text-align: right;'>{item['point']:,}</td>
        <td style='text-align: right;'>{item['price']:,}</td>
        <td style='text-align: right;'>{item['amount']:,}</td>
    </tr>
    """

        html_table += "</table>"

    html_table += "</body></html>"

    # Kết quả là một chuỗi HTML có thể được sử dụng trong Telegram Bot API
    html_output = f'{html_table}'

    return html_output

    # update.message.reply_text(f'<pre>{table}</pre>', parse_mode=ParseMode.HTML)

async def send_table_number_image(json_data):
    # print(json_data)

    if (json_data == "***"):
        return "Không tìm thấy thông tin. Sếp vui lòng kiểm tra và thử lại."

    # Xây dựng bảng HTML
    html_table = "<html><body>"
    html_table += """
<head>
    <meta charset="UTF-8">
    <link href='https://fonts.googleapis.com/css?family=Be Vietnam Pro' rel='stylesheet'>
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
        font-family: 'Be Vietnam Pro';
      }
    </style>
</head>                    
"""
   
    # table bet record
    
    html_table += "<table>"
    html_table += f"<tr><th>Loại cược</th><th>Số</th><th>Điểm</th><th>Giá</th><th>Tổng</th></tr>"

    keys = json_data['data'].keys()
    print(keys)

    if (len(keys) == 0):
        return f"Tài khoản {json_data['full_name']} không có dữ liệu Outstanding hôm nay."

    for index, (key) in enumerate(keys, start=0):

        print(key)
        
        game_name = get_type_game(int(key))

        print(game_name)
        # print(json_data['data'][key])

            
        for index_bet, (item) in enumerate(json_data['data'][key], start=1):
            number = " ".join(str(x) for x in item['number'])
            if (index_bet == 1):
                html_table += f"""
    <tr>
        <td rowspan='{len(json_data['data'][key])}'>{game_name}</td>
        <td style='text-align: center;'>{number}</td>
        <td style='text-align: right;'>{item['point']:,}</td>
        <td style='text-align: right;'>{item['price']:,}</td>
        <td style='text-align: right;'>{item['amount']:,}</td>
    </tr>
    """             
            else:
                html_table += f"""
    <tr>
        <td style='text-align: center;'>{number}</td>
        <td style='text-align: right;'>{item['point']:,}</td>
        <td style='text-align: right;'>{item['price']:,}</td>
        <td style='text-align: right;'>{item['amount']:,}</td>
    </tr>
    """

    html_table += "</table>"  

    html_table += "</body></html>"

    # Kết quả là một chuỗi HTML có thể được sử dụng trong Telegram Bot API
    html_output = f'{html_table}'

    return html_output

    # update.message.reply_text(f'<pre>{table}</pre>', parse_mode=ParseMode.HTML)


async def send_table_user_os_bet_image(json_data):
    # print(json_data)

    if (json_data == "***"):
        return "Không tìm thấy thông tin. Sếp vui lòng kiểm tra và thử lại."

    if int(json_data['level']) != 5:
        return f"Tài khoản {json_data['full_name']} không phải là Hội viên. Vui lòng kiểm tra lại."
    
    if (len(json_data['data']) == 0):
            return f"Tài khoản {json_data['full_name']} không có dữ liệu Outstanding hôm nay."

    # Xây dựng bảng HTML
    html_table = "<html><body>"
    html_table += """
<head>
    <meta charset="UTF-8">
    <link href='https://fonts.googleapis.com/css?family=Be Vietnam Pro' rel='stylesheet'>
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
          font-size: 20px;
          table-layout: auto;
          width: 100%;  
        }

      body {
        font-family: 'Be Vietnam Pro';
      }

      .win {
        color: blue;
      }

      .lose {
        color: red;
      }

    </style>
</head>                    
"""
   
    # table bet record
    
    html_table += "<table>"

    if json_data['outstanding'] != 0:
        html_table += f"<caption style='color: red; font-size: 35px; margin-bottom: 10px;'>Outstanding {json_data['full_name']} hôm nay: {json_data['outstanding']:,}</caption>"
    else:
        profit = json_data['profit']
        class_name = 'lose'
        if (profit > 0):
            class_name = 'win'
        html_table += f"<caption style='font-size: 35px; margin-bottom: 10px;'>Lợi nhuận {json_data['full_name']} hôm nay: <span class='{class_name}'>{profit:,}</span></caption>"

    
    html_table += f"<tr><th>STT.</th><th>Thể loại</th><th>Số</th><th>Điểm</th><th>Tiền</th><th>Trả thưởng</th><th>Lợi nhuận</th></tr>"

    # print(json_data['data'])

    total_profit = 0
    total_payout = 0
    total_points = 0
    total_amount = 0

    for index, (item) in enumerate(json_data['data'], start=1):
      number = " ".join(str(x) for x in item['number'])
      game_name = get_type_game(int(item['bet_type']))

      profit_item = 0
      if int(item['status']) == 1:
        profit_item = item['payout'] - item['amount'] 

      total_profit += profit_item
      total_payout += item['payout']
      total_points += item['point']
      total_amount += item['amount']

      class_name_item = 'lose'
      if profit_item > 0:
        class_name_item = 'win'
      # price = int(item['amount']) / int(item['point'])
      html_table += f"""
    <tr>
        <td style='text-align: left;'>{index}</td>
        <td style='text-align: left;'>{game_name}</td>
        <td style='text-align: center;'>{number}</td>
        <td style='text-align: right;'>{item['point']:,}</td>
        <td style='text-align: right;'>{item['amount']:,}</td>
        <td style='text-align: right;'>{item['payout']:,}</td>
        <td class='{class_name_item}' style='text-align: right;'>{profit_item:,}</td>
    </tr>
    """
    
    class_name_total = 'lose'
    if total_profit > 0:
        class_name_total = 'win'

    html_table += f"""
            <tr style='font-weight: bold;'>
              <td colspan='3' style='text-align: center;'>Tổng</td>
              <td style='text-align: right;'>{total_points:,}</td>
              <td style='text-align: right;'>{total_amount:,}</td>
              <td style='text-align: right;'>{total_payout:,}</td>
              <td class='{class_name_total}' style='text-align: right;'>{total_profit:,}</td></tr>
"""

    html_table += "</table>"
    html_table += "</body></html>"

    # Kết quả là một chuỗi HTML có thể được sử dụng trong Telegram Bot API
    html_output = f'{html_table}'

    # print(html_output)

    return html_output

    # update.message.reply_text(f'<pre>{table}</pre>', parse_mode=ParseMode.HTML)


async def send_table_user_os_bet(json_data):
    table = pt.PrettyTable(['STT.', 'Thể loại', 'Số', 'Điểm', 'Tổng'])
    full_name = json_data['full_name']
    outstanding = "{:,}".format(round(json_data['outstanding']))
    table.title = f'Tổng Outstanding {full_name}: {outstanding}'
    table.align['STT.'] = 'l'
    table.align['Thể loại'] = 'l'
    table.align['Số'] = 'r'
    table.align['Điểm'] = 'r'
    table.align['Tổng'] = 'r'

    if (json_data == "***"):
        return "Không tìm thấy thông tin. Sếp vui lòng kiểm tra và thử lại."

    if int(json_data['level']) != 5:
        return f"Tài khoản {json_data['full_name']} không phải là Hội viên. Vui lòng kiểm tra lại."
    # table bet record
    
    if (json_data['outstanding'] != 0) and (int(json_data['level']) == 5):
        if (len(json_data['data']) == 0):
            return f"Tài khoản {json_data['full_name']} không có dữ liệu Outstanding hôm nay."
        
        # print(json_data['data'])

        for index, (item) in enumerate(json_data['data'], start=0):
            number = " ".join(str(x) for x in item['number'])
            game_name = get_type_game(int(item['bet_type']))
            point = "{:,}".format(round(item['point']))
            amount = "{:,}".format(round(item['amount']))
            table.add_row([index, game_name, number, point, amount])
    

    return f'<pre>{table}</pre>'

    # update.message.reply_text(f'<pre>{table}</pre>', parse_mode=ParseMode.HTML)

def get_guide():
    return """
<html>
  <body>
    <head>
       <meta charset="UTF-8">
       <link href='https://fonts.googleapis.com/css?family=Be Vietnam Pro' rel='stylesheet'>
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

        table td:nth-child(2) {
          text-align: left;
        }

        table {
          margin-left: auto;
          margin-right: auto;
          font-size: 25px;
        }

        body {
          font-family: 'Be Vietnam Pro';
        }

        .hightlight {
          color: orangered;
        }
      </style>
    </head>
    <table>
      <tr>
        <th>Cú pháp</th>
        <th>Nội dung</th>
      </tr>
      <tr>
        <td><span class="hightlight">user_name info</span><br/><i>ví dụ: abc123 info</i></td>
        <td>lấy thông tin tài khoản bất kỳ</td>
      </tr>
      <tr>
        <td><span class="hightlight">super</span> hoặc <span class="hightlight">super tuần này</span></td>
        <td style="text-align: left">lấy danh sách thắng thua của super tuần này</td>
      </tr>
      <tr>
        <td><span class="hightlight">super tuần trước</span></td>
        <td style="text-align: left">lấy danh sách thắng thua của super tuần trước</td>
      </tr>
      <tr>
        <td><span class="hightlight">super hôm nay</span></td>
        <td style="text-align: left">lấy danh sách thắng thua của super hôm nay</td>
      </tr>
      <tr>
        <td><span class="hightlight">super hôm qua</span></td>
        <td style="text-align: left">lấy danh sách thắng thua của super hôm qua</td>
      </tr>
      <tr>
        <td><span class="hightlight">master</span> hoặc <span class="hightlight">master tuần này</span></td>
        <td style="text-align: left">lấy danh sách thắng thua của master tuần này</td>
      </tr>
      <tr>
        <td><span class="hightlight">master tuần trước</span></td>
        <td style="text-align: left">lấy danh sách thắng thua của master tuần trước</td>
      </tr>
      <tr>
        <td><span class="hightlight">master hôm nay</span></td>
        <td style="text-align: left">lấy danh sách thắng thua của master hôm nay</td>
      </tr>
      <tr>
        <td><span class="hightlight">master hôm qua</span></td>
        <td style="text-align: left">lấy danh sách thắng thua của master hôm qua</td>
      </tr>
      <tr>
        <td><span class="hightlight">agent</span> hoặc <span class="hightlight">agent tuần này</span></td>
        <td style="text-align: left">lấy danh sách thắng thua của agent tuần này</td>
      </tr>
      <tr>
        <td><span class="hightlight">agent tuần trước</span></td>
        <td style="text-align: left">lấy danh sách thắng thua của agent tuần trước</td>
      </tr>
      <tr>
        <td><span class="hightlight">agent hôm nay</span></td>
        <td style="text-align: left">lấy danh sách thắng thua của agent hôm nay</td>
      </tr>
      <tr>
        <td><span class="hightlight">agent hôm qua</span></td>
        <td style="text-align: left">lấy danh sách thắng thua của agent hôm qua</td>
      </tr>
      <tr>
        <td><span class="hightlight">member</span> hoặc <span class="hightlight">member tuần này</span></td>
        <td style="text-align: left">lấy danh sách thắng thua của member tuần này</td>
      </tr>
      <tr>
        <td><span class="hightlight">member tuần trước</span></td>
        <td style="text-align: left">lấy danh sách thắng thua của member tuần trước</td>
      </tr>
      <tr>
        <td><span class="hightlight">member hôm nay</span></td>
        <td style="text-align: left">lấy danh sách thắng thua của member hôm nay</td>
      </tr>
      <tr>
        <td><span class="hightlight">member hôm qua</span></td>
        <td style="text-align: left">lấy danh sách thắng thua của member hôm qua</td>
      </tr>
      <tr>
        <td><span class="hightlight">os super</span></td>
        <td style="text-align: left">lấy danh sách tiền chưa xử lý của super</td>
      </tr>
      <tr>
        <td><span class="hightlight">os master</span></td>
        <td style="text-align: left">lấy danh sách tiền chưa xử lý của master</td>
      </tr>
      <tr>
        <td><span class="hightlight">os agent</span></td>
        <td style="text-align: left">lấy danh sách tiền chưa xử lý của agent</td>
      </tr>
      <tr>
        <td><span class="hightlight">os member</span></td>
        <td style="text-align: left">lấy danh sách tiền chưa xử lý của member</td>
      </tr>
      <tr>
        <td><span class="hightlight">member_name os bet</span><br/><i>ví dụ: abc123 os bet</i><br/><i>abc123 phải là hội viên</i></td>
        <td>lấy thông tin chi tiết cược của hội viên</td>
      </tr>
      <tr>
        <td><span class="hightlight">member ko cược</span> tuần này/hôm nay/hôm qua/tuần trước</td>
        <td>lấy danh sách Hội viên không cược</td>
      </tr>
       <tr>
        <td><span class="hightlight">report list</span> tuần này/tuần trước</td>
        <td>lấy danh sách nick name report</td>
      </tr>
      <tr>
        <td><span class="hightlight">xsmb</span></td>
        <td>lấy kết quả xổ số miền Bắc</td>
      </tr>
    </table>
  </body>
</html>

"""


async def send_member_inactive(json_data, time_text = 'tuần này'):
    if (json_data == "***"):
        return "Không tìm thấy thông tin. Sếp vui lòng kiểm tra và thử lại."
    
    size = len(json_data)

    if size == 0:
      return f"Tất cả Hội Viên đều hoạt động {time_text}."

    html_table = "<html><body>"
    html_table += """
<head>
    <meta charset="UTF-8">
    <title>pdf</title>
    <link href='https://fonts.googleapis.com/css?family=Be Vietnam Pro' rel='stylesheet'>
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

      td{
white-space:nowrap;
}

      body {
        font-family: 'Be Vietnam Pro';
      }

      .win {
        color: blue;
      }

      .lose {
        color: red;
      }

    </style>
</head>                    
"""
    html_table += "<table>"
    html_table += f"<caption style='font-size: 35px; margin-bottom: 10px;'><strong>Báo cáo Hội Viên không hoạt động {time_text}</strong></caption>"
    html_table += "<tr><th>STT.</th><th>TK</th><th>Agent</th><th>Thời gian tạo</th><th>Đăng nhập lần cuối</th></tr>"
    
    for index, (item) in enumerate(json_data, start=1):
      full_name = item['full_name']
      agent = item['parent']['full_name']
      created_at = parse_date_time(item['created_at'])
      last_login = parse_date_time(item['last_login'])

      html_table += f"""
                <tr>
                  <td style='text-align: right;'>{index}</td>
                  <td style='text-align: left;'>{full_name}</td>
                  <td style='text-align: left;'>{agent}</td>
                  <td style='text-align: left;'>{created_at}</td>
                  <td style='text-align: left;'>{last_login}</td>
                </tr>            
    """

    html_table += "</table>"
    html_table += "</body></html>"

    # Kết quả là một chuỗi HTML có thể được sử dụng trong Telegram Bot API
    html_output = f'{html_table}'

    return html_output
    



def check_response(message, response):
    if (response == "***"):
        return "Không tìm thấy thông tin. Sếp vui lòng kiểm tra và thử lại."

    formatted_number = "{:,}".format(round(response))
    return f'{message} {formatted_number}'


def check_response_company_profit(message, response):
    if (response == "***"):
        return "Không tìm thấy thông tin. Sếp vui lòng kiểm tra và thử lại."

    formatted_number = "{:,}".format(round(int(response) * (-1) * 20 / 100))
    return f'{message} {formatted_number}'

def get_type_game(type):
    if type == 0:
        return 'Đề đầu'
    elif type == 1:
        return 'Đề đuôi'
    elif type == 2:
        return 'Đề đầu giải 1'
    elif type == 3:
        return 'Đề đuôi giải 1'
    elif type == 4:
        return 'Lô đầu'
    elif type == 5:
        return 'Lô đuôi'
    elif type == 6:
        return 'Lô đuôi xiên 2'
    elif type == 7:
        return 'Lô đuôi xiên 3'
    elif type == 8:
        return 'Lô đuôi xiên 4'
    else:
        return 'none'
    
def parse_date_time(timestamp):
    return datetime.fromtimestamp(timestamp).strftime('%d/%m/%Y %H:%M:%S')

def parse_date(date_string):
    date = datetime.datetime.strptime(date_string, '%Y-%m-%d')
    return date.strftime('%d/%m/%Y')