# Этап 3

В качестве содержимого главной страницы реализовать вывод __шаблона__

* Добавить шаблон для главной страницы
  * создать каталог `templates`
  * в каталоге `templates` создать файл `index.html`
  * разместить в файле `index.html` все необходимые теги. Основное содержимое страницы - заголовок `<h1>Добро пожаловать</h1>` (на этом этапе не изменяется при обновлении страницы)
* Добавить в строку импорта функцию `render_template`
* Результат вызова функции `render_template` вернуть в функции `index()`  
  В качестве аргумента передать строку - имя файла с шаблоном
