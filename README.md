# Knead

## Project Idea

This project aims to build an app for my bread doughs.

The code will be written manually by me. CLI tools will be used to provide feedback.

This is a learning exercise forcing me to learn good practices for:

- FastAPI
- Domain Driven Design

This project must have a best practice structure which allows future items to be added.

## Project Idea

### Domain

Core objects:

#### Recipie

Recipie:

- name: str
- description: str
- ingredients: list[Ingredient]

Ingredient:

- name: str
- unit: str:
- amount: float

#### Method

These are the timings and steps to make a dough. Like a cookbook entry.

A recipie links to a method. A method could contain many recipies. A recipie could be contained in many methods

Method:

- list[Step]

Step:

- name: str
- description: str
- time length: (need to work out correct time length type)
