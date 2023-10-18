# Listas

## Listas - Estrutura

```python
Lista = [valor, valor, valor]
```

`l[i]` é o valor do item de indice `i` da lista.

Listas são mutáveis. Para alterar um item  da lista:

```python
Lista[i] = valor
```

## Indice

Dado um item, saber a posição dele:

```python
i = lista.index(item)
```

## Adicionar ou remover itens

Para adicionar itens:

```python
lista.append(item)
```

Para remover itens temos duas opções:

```python
item_removido = lista.pop(item)

lista.remove(item)
```

## Tamanho, menor e maior item

Tamanho da lista:

```python
tamanho = len(lista)
```

Para encontrar o maior e menor item da lista:

```python
maior = max(lista)
menor = min(lista) 
```

## Juntar, editar e ordenar

2 formas:

```python
lista1.extend(lista2)
lista_nova = lista1 + lista2
```

Ordenar listas:

```python
lista.sort()
```
