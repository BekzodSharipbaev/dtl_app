TAGS = [
    {
        'name': 'templatetag',
        'description': """ Выводит один из синтаксических символов, используемых для создания тегов шаблона. """,
        'syntax': """ {% templatetag %} """
    },
    {
        'name': 'resetcycle',
        'description': """ Сбрасывает предыдущий цикл, чтобы он перезапустился с первого элемента при следующем столкновении. """,
        'syntax': """ {% resetcycle %}{% cycle %} """
    },
    {
        'name': 'now',
        'description': """ Отображает текущую дату и / или время в формате, соответствующем заданной строке. """,
        'syntax': """ {% now "jS F Y H:i" %} """,
        'example': """ {% now "jS F Y H:i" %} """
    },
    {
        'name': 'csrf_token',
        'description': """ Этот тег используется для защиты CSRF, как описано в документации для подделок межсайтовых запросов. """,
        'syntax': """ {% csrf_token %} """
    },
    {
        'name': 'include',
        'description': """ Загружает шаблон и отображает его с текущим контекстом. Это способ «включения» других шаблонов в шаблон. """,
        'syntax': """ {% include template_name %} """
    },
    {
        'name': 'ifchanged',
        'description': """ Проверьте, изменилось ли значение с последней итерации цикла. """,
        'syntax': """ {% ifchanged %} """
    },
    {
        'name': 'spaceless',
        'description': """ Удаляет пробелы между тегами HTML. Сюда входят символы табуляции и новые строки. """,
        'syntax': """{% spaceless %}
                        <p>
                          <a href="foo/">Foo</a>
                        </p>
                      {% endspaceless %}"""
    },
    {
        'name': 'with',
        'description': """ Кэширует сложную переменную под более простым именем. """,
        'syntax': """ {% with total=business.employees.count %}
                        {{ total }} employee{{ total|pluralize }}
                      {% endwith %} """
    },
]


FILTERS = [
    {
        'name': 'default_if_none',
        'description': """Если (и только если) значение равно None, используется заданное значение по умолчанию. В противном случае используется значение.""",
        'value': None,
        'example': """{{ tag.value|default_if_none:"nothing" }}"""
    },
    {
        'name': 'slugify',
        'description': """Преобразует в ASCII. Преобразует пробелы в дефисы. Удаляет символы, не являющиеся буквенно-цифровыми, знаками подчеркивания или дефисами. Преобразует в нижний регистр. Также удаляет начальные и конечные пробелы.""",
        'value': 'Tom Gray',
        'example': """{{ tag.value|slugify }}"""
    },
    {
        'name': 'title',
        'description': """Преобразует строку в регистр заголовка, заставляя слова начинаться с символа верхнего регистра, а оставшиеся символы - с нижнего регистра. Этот тег не пытается сохранить «банальные слова» в нижнем регистре.""",
        'value': 'hello world',
        'example': """{{ tag.value|title }}"""
    },
    {
        'name': 'dictsort',
        'description': """Принимает список словарей и возвращает этот список, отсортированный по ключу, указанному в аргументе.""",
        'books': [
            {'title': '1984', 'author': {'name': 'George', 'age': 45}},
            {'title': 'Timequake', 'author': {'name': 'Kurt', 'age': 75}},
            {'title': 'Alice', 'author': {'name': 'Lewis', 'age': 33}},
        ],
        'example': """{% for book in tag.books|dictsort:"author.age" %}
    <p>* {{ book.title }} ({{ book.author.name }})</p>
{% endfor %}"""
    },
    {
        'name': 'linenumbers',
        'description': """Отображает текст с номерами строк.""",
        'value': 'one\ntwo\nthree',
        'example': """{{ tag.value|linenumbers }}"""
    },
    {
        'name': 'divisibleby',
        'description': """Возвращает, True если значение делится на аргумент.""",
        'value': 21,
        'syntax': """{{ 21|divisibleby:"3" }}""",
        'example': """{{ tag.value|divisibleby:"3" }}"""
    },
    {
        'name': 'last',
        'description': """Возвращает последний элемент в списке.""",
        'value': 'abcd',
        'syntax': """{{ 'abcd'|last }}""",
        'example': """{{ tag.value|last }}"""
    },
]
