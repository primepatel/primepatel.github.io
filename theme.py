with open("assets/css/main.css", 'r', encoding="utf-8") as css:
    with open("assets/css/style.css", 'w', encoding="utf-8") as file:
        file.write(css.read().replace("C9F0D6", "F9F5F6"))