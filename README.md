# EmoAid

#### Ты думал тут что-то будет?

---

## Оглавление

- [Контакты](#контакты)
    - [Связь с разработчиками](#связь-с-разработчиками)
- [Сборка и запуск](#сборка-и-запуск)
    - [Необходимые компоненты](#необходимые-компоненты)
    - [Первоначальная настройка](#первоначальная-настройка)
    - [config.ini](#configini)
        - [Раздел `Settings`](#раздел-settings)
    - [Docker](#docker)

---

## Контакты

#### Связь с разработчиками

- [Telegram diquoks](https://t.me/diquoks)
- [Почта diquoks](mailto:diquoks@yandex.ru)
- [Telegram ldfxxx404](https://t.me/qhxnxmxnxn)

---

## Сборка и запуск

### Необходимые компоненты

- [Docker Desktop](https://docs.docker.com/desktop)
- [Git](https://git-scm.com/downloads)
- [Python 3.13](https://www.python.org/downloads)

### Первоначальная настройка

##### Клонируйте репозиторий git

```bash
git clone https://github.com/ldfxxx404/EmoAid.git
```

##### Перейдите в корневую директорию

```bash
cd EmoAid
```

##### Установите зависимости

```bash
pip install -r requirements.txt
```

##### Сгенерируйте файл `config.ini`

```bash
cd src ; python main.py
```

##### Заполните `EmoAid/src/config.ini` [следуя инструкции](#configini)

##### Используйте руководство для [Docker](#docker)

### config.ini

#### Раздел `Settings`

| Настройка            |  Тип   | Описание                                      |
|:---------------------|:------:|:----------------------------------------------|
| `bot_token`          | `str`  | Токен бота в Telegram                         |
| `chat_id`            | `int`  | ID группы психологов в Telegram               |
| `file_logging`       | `bool` | Использовать логирование в файлы `.log`       |
| `psychologists_list` | `list` | Список ID аккаунтов психологов в Telegram     |
| `skip_updates`       | `bool` | Пропускать ожидающие события при запуске бота |

### Docker

##### Перейдите в корневую директорию

##### Создайте образ

```bash
docker build -t emo_aid .
```

##### Запустите контейнер

```bash
docker run -it -d --name EmoAid emo_aid
```
