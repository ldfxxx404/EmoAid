# **Запуск проекта**

## **Системные зависимости**

Перед началом убедитесь, что установлены:

* **Docker**
* **Docker Compose**
* **Python 3.10+**
* **Git**

---

## **Ручная установка**

### **Linux / macOS**

1. **Установка модуля виртуального окружения (Linux):**

   ```bash
   sudo apt install python3.13-venv
   ```

2. **Создание виртуального окружения:**

   ```bash
   python3 -m venv .EmoVenv
   ```

3. **Активация окружения:**

   ```bash
   source .EmoVenv/bin/activate
   ```

4. **Установка зависимостей:**

   ```bash
   pip install -r req.txt
   ```

5. **Запуск проекта:**

   ```bash
   python3 main.py
   ```

---

### **Windows**

Требования: Python, Git, Docker Desktop.

1. **Создание виртуального окружения:**

   ```powershell
   python -m venv .EmoVenv
   ```

2. **Активация окружения:**

   ```powershell
   .EmoVenv\Scripts\activate
   ```

3. **Установка зависимостей:**

   ```powershell
   pip install -r req.txt
   ```

4. **Запуск проекта:**

   ```powershell
   python main.py
   ```

---

## **Docker**

### **Сборка проекта**

```bash
docker compose build
```

### **Запуск в режиме демона**

```bash
docker compose up -d
```

### **Остановка контейнеров**

```bash
docker compose down
```

---

## **Полезные команды**

### Обновить зависимости

```bash
pip install -r req.txt --upgrade
```

### Деактивация виртуального окружения

```bash
deactivate
```

