# Autotest of the web-site "https://snt-stroitel.ru/"

В файле "snt-stroitel_main_page.py" проводится автотест главной страницы сайта "https://snt-stroitel.ru/".
Сайт "https://snt-stroitel.ru/"  - сайт, позволяющий жителям СНТ "Строитель" обсуждать различные вопросы своего СНТ на форуме сайта, а также узнавать новости СНТ.
Целью тестирования данного сайта является проверка корректной работы всех его функциональных возможностей на различных версиях браузеров с типовыми сценариями  его использования. 

В файле "snt-stroitel_entrance.py" проводится автотест вкладки "вход". В данной вкладке есть Google Recaptcha.На данном этапе написании
автотеста я не смогла обойти эту проверку, поэтому автотест заканчивается на окошке "Я не робот" и далее необходимо вручную поставить галочку, выбрать
запрашиваемые квадраты с картинками и вручную нажать кнопку "Войти". 

Что используется:  
Python 3.10.0  
Selenium 4.1.0   
Google Сhrome 97.0.4692.99  