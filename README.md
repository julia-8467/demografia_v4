# Analiza Demograficzna Polski – Aplikacja FastAPI

Aplikacja umożliwia przeglądanie danych demograficznych Polski z podziałem na województwa, lata, urodzenia oraz zgony w różnych grupach wiekowych. Projekt wykorzystuje **FastAPI**, **SQLAlchemy** oraz **Jinja2Templates** do generowania widoków HTML oraz udostępniania danych w sposób dynamiczny.

---

## 1. Funkcjonalność projektu

Aplikacja udostępnia interfejs API oraz widoki, które pozwalają na:

### • Przegląd województw

`GET /index/`
Pobiera listę dostępnych województw z tabeli `Demografia` i wyświetla je w widoku HTML.

### • Dane demograficzne

`GET /demografia/?wojewodztwo=...&rok=...`
Wyświetla szczegółowe informacje demograficzne dotyczące wybranego województwa i roku. Dane są renderowane w szablonie `demografia_fragment.html`.

### • Dane o zgonach

`GET /zgony/?rok=2020&wiek=0_4`
Zwraca sumaryczną liczbę zgonów w danym roku i grupie wiekowej, pogrupowaną według województw. Widok generowany jest za pomocą `zgony_fragment.html`.

### • Dane o urodzeniach

`GET /urodzenia/?wojewodztwo=...&rok=...`
Pobiera dane dotyczące urodzeń za dany rok i województwo. Wynik wyświetlany jest w tabeli HTML (`urodzenia_table.html`).

---

## 2. Struktura projektu

```
projekt/
│
├── main.py               # główny plik aplikacji FastAPI
├── Demografia/           # logika biznesowa, modele, CRUD, database session
│   ├── models.py
│   ├── crud.py
│   └── Database.py
│
├── templates/            # szablony Jinja2 (HTML)
│   ├── index.html
│   ├── demografia_fragment.html
│   ├── zgony_fragment.html
│   └── urodzenia_table.html
│
├── static/               # pliki CSS, JS, obrazy
└── README.md             # dokumentacja projektu
```

---

## 3. Modele danych

### **1. Demografia**

Zawiera informacje na poziomie województw oraz lat. Przykładowe pola:

* województwo
* rok
* dane populacyjne

### **2. Zgony**

Model przechowuje liczbę zgonów w podziale na grupy wiekowe:

* p0_4
* p5_9
* …
* p85

Każde pole reprezentuje sumaryczną liczbę zgonów w danej grupie wiekowej.

---

## 4. Endpointy (API)

| Metoda | Ścieżka        | Opis                                       |
| ------ | -------------- | ------------------------------------------ |
| GET    | `/`            | przekierowanie do `/index/`                |
| GET    | `/index/`      | lista województw (HTML)                    |
| GET    | `/demografia/` | dane demograficzne dla województwa i roku  |
| GET    | `/zgony/`      | sumaryczne zgony dla roku i grupy wiekowej |
| GET    | `/urodzenia/`  | dane o urodzeniach dla regionu i roku      |

Endpointy do importu CSV, generowania mapy oraz usuwania rekordów są w kodzie, lecz obecnie wyłączone.

---

## 5. Instalacja i uruchomienie

### **1. Klonowanie repozytorium**

```
git clone <adres_repozytorium>
cd projekt
```

### **2. Instalacja zależności**

```
pip install -r requirements.txt
```

### **3. Uruchomienie aplikacji**

```
uvicorn main:app --reload
```

Aplikacja będzie dostępna pod adresem:

```
http://127.0.0.1:8000
```

### **4. Dokumentacja API**

FastAPI generuje dokumentację automatycznie:

* Swagger UI:
  `http://127.0.0.1:8000/docs`
* OpenAPI schema:
  `http://127.0.0.1:8000/openapi.json`

---

## 6. Wymagania

* Python 3.10+
* FastAPI
* SQLAlchemy
* Jinja2
* Uvicorn

---

## 7. Dalszy rozwój

Projekt można rozszerzyć o:

* import danych CSV z poziomu API,
* zapisywanie map lub wizualizacji,
* statystyki porównawcze pomiędzy województwami,
* API zwracające dane w formacie JSON dla aplikacji zewnętrznych.


