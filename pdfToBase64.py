import base64
import base64
import requests
import PyPDF2

# Скачиваем PDF-файл и сохраняем его локально
url = 'https://yastatic.net/s3/vertis-frontend/autoru-frontend/docs/dkp-agreement.pdf'
response = requests.get(url)
with open('dkp-agreement.pdf', 'wb') as f:
    f.write(response.content)

# Открываем PDF-файл для чтения в бинарном режиме
with open('dkp-agreement.pdf', 'rb') as pdf_file:

    # Создаем объект PyPDF2 для чтения PDF-файла
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Получаем содержимое PDF-файла в виде строки
    pdf_content = ""
    for i in range(len(pdf_reader.pages)):
        pdf_content += pdf_reader.pages[i].extract_text()

    # Кодируем содержимое файла в Base64
    base64_content = base64.b64encode(pdf_content.encode('utf-8'))

    # Выводим закодированное содержимое на экран
    print(base64_content.decode('utf-8'))