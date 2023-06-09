# Web - Shop Django

 Это приложение представляет собой  WEB интернет-магазин мебели реализованный на Фреймворке Django


## Функции приложения

- Регистрация и авторизация покупателей
- Реализация каталога магазина с объектами из БД
- Реализация корзины покупателя 
- Реализация API POST, GET, PUT, DELETE методов взаимодействия с БД
- Реализация пагинации страниц, форм отправки сообщений на e-mail, разрешений на дейтвия пользователей

## Установка
По умолчанию докер будет использовать порт 8000.
1)Используйте docker-compose что бы построить образ
```sh
docker-compose build
```
2)Выполните миграции
```sh
docker compose run --rm web-app sh -c "python manage.py migrate"
```
3)Создайте суперпользователя
```sh
docker compose run --rm web-app sh -c "python manage.py createsuperuser"
```
4)Запустите образ
```sh
docker-compose up
```

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
