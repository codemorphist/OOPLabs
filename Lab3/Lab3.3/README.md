# ЛАБОРАТОРНА РОБОТА 3. Наслідування та поліморфізм

## UML Diagram of classes
![UML Diagram of figures.py](./uml/figures.png "UML Diagram of figures.py classes")

## Task 1

### Methods

Опишіть клас Фігура, що інкапсулює основні геометричні 
характеристики та методи. Для фігури визначено методи:
  - `dimention()` – що повертає вимірність фігури (двовимірна чи тривимірна).
  - `perimetr()` – що повертає периметр фігури (для три-вимірних фігур 
  метод має породжувати виключення або повертати None).
  - `square()` – що повертає площу фігури (для три-вимірних фігур метод 
  має породжувати виключення або повертати None).
  - `squareSurface()` – що повертає площу бічної фігури (для дво-вимірних 
  фігур метод має породжувати виключення або повертати None).
  - `squareBase()` – що повертає площу основи фігури (для дво-вимірних 
  фігур метод має породжувати виключення або повертати None).
  - `height()` – що повертає висоту фігури (для дво-вимірних фігур метод 
  має породжувати виключення або повертати None).
  - `volume()` – метод, що обчислює міру фігури (для плоскої фігури –
  площу, для об’ємної – відповідно об’єм).

### Classes

Від класу Фігура (або його нащадків) наслідуються такі класи:
  - [x] Трикутник – визначається довжинами трьох сторін.
  - [x] Прямокутник – визначається двома сторонами
  - [x] Трапеція – визначається двома основами та двома бічними сторонами.
  - [x] Паралелограм – визначається двома сторонами та висотою.
  - [x] Круг – визначається радіусом.
  - [x] Куля – визначається радіусом.
  - [x] Трикутна піраміда – підклас класу Трикутник – моделює правильну 
трикутну піраміду, в основі якої лежить правильний трикутник –
визначається довжиною сторони основи та висотою.
  - [x] Чотирикутна піраміда – підклас класу Прямокутник – моделює 
правильну чотирикутну піраміду, в основі якої лежить прямокутник –
визначається довжинами сторін основи та висотою.
  - [x] Прямокутний паралелепіпед – підклас класу Прямокутник –
визначається довжинами трьох ребер.
  - [x] Конус – підклас класу Круг – моделює правильний конус – визначається 
радіусом основи та висотою.
  - [x] Трикутна призма – підклас класу Трикутник – моделює пряму призму в 
основі якої лежить трикутник – визначається довжинами трьох сторін та висотою.

## Task 2
Нехай дано список фігур. Серед заданих фігур, знайдіть фігуру, міра якої є найбільшою.

Перелік фігур зберігається у текстовому файлі – у кожному окремому рядку
файла вказується назва фігури та список параметрів, що визначають фігуру
відповідно до зазначеного вище. Параметри розділені одним або кількома
символами пропуску. Назви фігур вказані таким чином: 
  - Triangle – Трикутник
  - Rectangle – Прямокутник
  - Trapeze – Трапеція
  - Parallelogram – Паралелограм
  - Circle – Круг
  - Ball – Куля
  - TriangularPyramid – Трикутна піраміда
  - QuadrangularPyramid – Чотирикутна піраміда
  - RectangularParallelepiped - Прямокутний паралелепіпед
  - Cone – Конус
  - TriangularPrism – Трикутна призма

Вхідні дані містяться файлах:
  - input01.txt
  - input02.txt
  - input03.txt

files url: https://github.com/krenevych/oop/tree/master/labs/lab03/home/task1


