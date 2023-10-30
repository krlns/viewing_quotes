<h1 align="center">
viewing quotes
</h1>
<h3 align="center">Сайт для просмотра котировок цифровых валют в реальном времени</h3>
<hr>
<h3>Чтобы успешно запустить сайт выполните команды:</h3>
<ul>

    https://github.com/krlns/viewing_quotes.git
<hr>

    python -m venv venv
<hr>

    source env/bin/activate
<hr>

    pip install -r requirements.txt
<hr>

    cd viewing_quotes
<hr>

    python manage.py makemigrations
<hr>

    python manage.py migrate
<hr>
</ul>

<h3>В терминале:</h3>
<p>установка и настройка RabbitMQ</p>
<ul>

    sudo apt-get install rabbitmq-server
<hr>

    sudo rabbitmq-server -detached
<hr>

    sudo rabbitmqctl add_user myuser mypassword
<hr>

    sudo rabbitmqctl add_vhost myvhost
<hr>

    sudo rabbitmqctl set_permissions -p myvhost myuser ".*" ".*" ".*"
<hr>
</ul>
<p>Создайте в корне проекта файл .env и добавьте эти ключи конфигурации</p>
<ul>

    CELERY_BROKER_URL=amqp://myuser:mypassword@localhost/myvhost 
    CELERY_BACKEND_URL=db+sqlite:///test.db
<hr>
</ul>
<p>Вернитесь в папку viewing_quotes:</p>
<ul>

    celery -A viewing_quotes worker -l info
<hr>

    celery -A viewing_quotes beat
<hr>

    python manage.py runserver
<hr>
</ul>
