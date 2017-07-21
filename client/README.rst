===================================================
countries_lib_client - нормализация названия страны
===================================================

--------
Описание
--------

Данный пакет предоставляет набор функций для обращения к веб-сервису, предназначеному для нормализации (нахождения корректного) 
названия страны.

---------
Установка
--------- 

Вариант 1:

Выполните команду **pip install git+https://github.com/AlekseyPauls/countries_library_cs/client** 

Выполните следующие команды: (Доделать)

wget https://raw.githubusercontent.com/AlekseyPauls/countries_library_cs/master/dist/countries_lib-1.0.tar.gz 
pip install countries_lib-1.0.tar.gz
sudo rm countries_lib-1.0.tar.gz

Вариант 3:

Для установки загрузите вручную countries_lib_client-1.0.tar.gz из директории dist данного репозитория и выполните команду 
**pip instal countries_lib_client-1.0.tar.gz** в директории, в которую загружен файл. 

----------------------
Функции и их аргументы
----------------------

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Нормализация страны - normalize_country_name
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Функция имеет вид: **normalize_country_name(url, posname, dif_acc=0.7)**

Принимает на вход два обязательных аргумента: **url** типа **string** - адрес сервера, **posname** (от “possible name”) типа 
**string** - нормализуемое название, и один необязательный - **dif_acc** (от difference accuracy) типа **float** - 
параметр точности при поиске подходящего ключа в библиотеке, принимающий значения от **0.0** до **1.0** 
(по умолчанию - **0.7**).

Выдает строку типа **string**, содержащую либо общее название страны, либо ‘None’, если выполнение прошло успешно. Если было 
вызвано исключение, то строка содержит **‘DatabaseError’** (это означает, что не найдена корректная база данных по пути из 
переменной **DB_PATH**) или **‘Invalid argument type’**, если хотя бы один из аргументов задан неправильно (имеет 
некорректный тип или значение).

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Добавление возможного названия страны - match_country_name
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Функция имеет вид: **match_country_name(url, key, value, priority=2)**

Принимает на вход три обязательных аргумента **url**, **key** и **value** типа **string** - адрес сервера, возможное и 
корректное названия соответственно, и один необязательный - **priority** типа **int** - приоритет ключа, принимающий 
значения **1** или **2** (по умолчанию - **2**) и определяющий, что содержится в ключе: название, сокращение, индекс или 
перевод названия страны, если приоритет равен **1**, и все остальное, если приоритет равен **2**. Так как большинство ключей, 
подходящих под приоритет **1**, уже в базе, то возможно задать приоритет по умолчанию равный **2**. 

Выдает строку **'Invalid argument type'** типа **string** , если хотя бы один из аргументов задан неправильно (имеет 
некорректный тип или значение), строку **'DatabaseError'**, если произошла ошибка во время открытия базы данных по пути 
из переменной **DB_PATH**, и ничего не возвращает (**None**), если добавление прошло успешно.


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Удаление возможного названия страны - del_country_name
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Функция имеет вид: **del_country_name(url, key)**

Принимает на вход два обязательных аргумента **url** и **key** типа **string** - адрес сервера и возможное название, которое 
нужно удалить из базы данных, соответсвтенно.

Выдает строку **'Invalid argument type'** типа **string** , аргумент задан неправильно (имеет некорректный тип или значение), 
строку **'DatabaseError'**, если произошла ошибка во время открытия базы данных по пути из переменной **DB_PATH**, и ничего 
не возвращает (**None**), если удаление прошло успешно.

----------
Применение
----------

Код, используемый для демонстрации возможностей модуля::

    from countries_lib_client import country_client


    def main():
    """ Пример использования библиотеки для нормализации названия страны """

	url = (дописать)
	
    # Вывод корректные названия для вариантов из списка:
    test_list = ['USA', 'US', 'Amurica!!!', 'NewYork', 'Untgd States of America', 'Paris, USA', 'agagagag']
    for variant in test_list:
        print(variant, ' - ', country_client.normalize_country_name(url, variant))
    print('-------------------------------------------------------------')
    # Добавление значения
    print('Проверка "AddCountryTest" на существование: ', country_client.normalize_country_name(url, 'AddCountryTest'))
    country_client.match_country_name(url, 'AddCountryTest', 'AddCountryTest')
    print('Проверка "AddCountryTest" на существование: ', country_client.normalize_country_name(url, 'AddCountryTest'))
    print('-------------------------------------------------------------')
    # Удаление значения
    print('Проверка "AddCountryTest" на существование: ', country_client.normalize_country_name(url, 'AddCountryTest'))
    country_client.del_country_name(url, 'AddCountryTest')
    print('Проверка "AddCountryTest" на существование: ', country_client.normalize_country_name(url, 'AddCountryTest'))
    print('-------------------------------------------------------------')
    # Демонстрация низкой и высокой точности
    print('Testing variant: ', 'ololo')
    print('0.3 (low) accurate: ', country_client.normalize_country_name(url, 'ololo', 0.3))
    print('0.6 (standard) accurate: ', country_client.normalize_country_name(url, 'ololo'))
    print('0.9 (high) accurate: ', country_client.normalize_country_name(url, 'ololo', 0.9))
    print('Testing variant: ', 'Rasia')
    print('0.3 (low) accurate: ', country_client.normalize_country_name(url, 'Rasia', 0.3))
    print('0.6 (standard) accurate: ', country_client.normalize_country_name(url, 'Rasia'))
    print('0.9 (high) accurate: ', country_client.normalize_country_name(url, 'Rasia', 0.9))


    if __name__ == "__main__":
        main()

Вывод при выполнении данного кода::

    USA  -  United States
    US  -  United States
    Amurica!!!  -  United States
    NewYork  -  United States
    Untgd States of America  -  United States
    Paris, USA  -  United States
    agagagag  -  None
    -------------------------------------------------------------
    Проверка "AddCountryTest" на существование:  None
    Проверка "AddCountryTest" на существование:  AddCountryTest
    -------------------------------------------------------------
    Проверка "AddCountryTest" на существование:  AddCountryTest
    Проверка "AddCountryTest" на существование:  None
    -------------------------------------------------------------
    Testing variant:  ololo
    0.3 (low) accurate:  Norway
    0.6 (standard) accurate:  None
    0.9 (high) accurate:  None
    Testing variant:  Rasia
    0.3 (low) accurate:  Russia
    0.6 (standard) accurate:  Russia
    0.9 (high) accurate:  None

Как видно из результатов, функции делают именно то, что заявлено в их описании (без учета ошибок, это рассматривается далее).

Возможна другая форма импорта::

    from countries_lib_client.country_client import normalize_country_name, match_country_name, del_country_name

Такая форма позволяет обращаться к функциям напрямую.

-----
Тесты
-----

В пакет встроены тесты, позволяющие проверить его функциональность при внесении изменений. Далее идут тесты и их описание:

#. test_simple_name - проверяет работу функции **normalize_country_name** на простых входных данных
#. test_punctuation_sensitivity - проверяет удаление пунктуации в функции **normalize_country_name**
#. test_upper_register - проверяет работу функции **normalize_country_name** на входной строке в верхнем регистре
#. test_low_register - проверяет работу функции **normalize_country_name** на входной строке в нижнем регистре
#. test_missed_letter - проверяет исправление опечатки типа "пропущенная буква" в функции **normalize_country_name**
#. test_excess_letter - проверяет исправление опечатки типа "лишняя буква" в функции **normalize_country_name**
#. test_another_letter - проверяет исправление опечатки типа "неправильная буква" в функции **normalize_country_name**
#. test_simple_two_words_name - проверяет работу функции **normalize_country_name** с входной строкой из 2-х слов (разделитель - пробел)
#. test_excess_word_name - проверяет работу функции **normalize_country_name** с входной строкой из 2-х слов, одно из которых - лишнее
#. test_american_paris_like_construction - проверяет работу приоритета в функции **normalize_country_name**
#. test_standard_accuracy_result - проверяет вывод функции **normalize_country_name** для несуществующего имени при стандартной точности
#. test_correct_accuracy_type - проверяет ввозможность ввода корректного необязательного аргумента **dif_acc** в функции **normalize_country_name**
#. test_incorrect_accuracy_type - проверяет ввозможность ввода некорректного (тип) необязательного аргумента **dif_acc** в функции **normalize_country_name**
#. test_incorrect_accuracy_value - проверяет ввозможность ввода некорректного (значение) необязательного аргумента **dif_acc** в функции 
**normalize_country_name**
#. test_non_existing_object_delete - проверяет удаление несуществующего ключа в функции **del_country_name**
#. test_match - проверяет добавление нового ключа и значения в функции **match_country_name**
#. test_existing_object_delete - проверяет удаление существующего ключа в функции **del_country_name**
#. test_correct_priority_match - проверяет добавление нового ключа и значения в функции **match_country_name**, причем необязательный аргумент 
**priority** корректен
#. test_incorrect_priority_match - проверяет добавление нового ключа и значения в функции **match_country_name**, причем необязательный аргумент 
**priority** некорректен
#. test_incorrect_match - проверяет добавление некорректного нового ключа и некорректного значения в функции **match_country_name**
#. test_incorrect_delete - проверяет удаление некорректного ключа в функции **del_country_name**
