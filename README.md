# zapret-strategies-sorter

небольшой Python-скрипт для сортировки строк вида:

```text
general (ALT11).bat : OK: 61, FAIL: 38, UNSUP: 0, BLOCKED: 0
```

скрипт:

- сортирует строки по значению `OK` по убыванию;
- удаляет строки, где `OK: 0`;
- может вывести результат в консоль или сохранить в файл.

## требования

- Python 3.10+

## файлы

- `sorter.py` - основной скрипт
- `list.txt` - входной файл по умолчанию
- `sorted.txt` - пример выходного файла

## запуск

сортировка файла `list.txt` с выводом в консоль:

```powershell
python sorter.py
```

сортировка произвольного файла:

```powershell
python sorter.py my_list.txt
```

сохранение результата в файл:

```powershell
python sorter.py list.txt -o sorted.txt
```

## формат входных данных

ожидаются строки, в которых есть фрагмент:

```text
OK: число,
```

пример:

```text
general (ALT4).bat : OK: 62, FAIL: 35, UNSUP: 0, BLOCKED: 0
general (ALT3).bat : OK: 27, FAIL: 66, UNSUP: 0, BLOCKED: 6
general (ALT6).bat : OK: 0, FAIL: 97, UNSUP: 0, BLOCKED: 0
```

после обработки строка с `OK: 0` будет исключена, а остальные отсортированы по убыванию `OK`.
