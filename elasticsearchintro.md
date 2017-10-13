Obtener todos los documentos en elasticsearch
``` json
GET /
```
## RESULTADO


Insertar documento primero indice luego typo y luego identificador del documento
```json
POST /my-indice/mi-tipo/1
{
  "body":"loquesea"
}
```
Consultar documento recien creado
```json
GET /my-indice/mi-tipo/1
```
Eliminar documento
```json
DELETE /my-index/my-type/1
```

Crear un nuevo indice con parametros de configuracion
```json
PUT /libreria
{
  "settings": {
    "index.number_of_shards":1,
    "index.number_of_replicas":0
  }
}
```

Agregar varios documentos de una sola vez
```json
POST /libreria/libros/_bulk
{ "index": {"_id": 1}}
{ "titulo": "el libro 1", "precio": 10, "colores":["gris","purpura","azul"]}
{ "index": {"_id": 2}}
{ "titulo": "el libro 2", "precio": 12, "colores":["purpura","azul"]}
{ "index": {"_id": 3}}
{ "titulo": "el libro 1", "precio": 10, "colores":["gris","purpura","azul"]}
```

Agregar mas docu,entos

```json
POST /libreria/libros/_bulk
{ "index": {"_id": 4}}
{ "titulo": "el libro 4", "precio": 13, "colores":["amarillo"]}
{ "index": {"_id": 5}}
{ "titulo": "el libro 5", "precio": 9, "colores":["profundo azul"]}
```

Obtener todos los documentos del indice libreria y de tipo libros
```json
GET /libreria/libros/_search
```

Obtener todos los documentos del indice libreria y de tipo libros cuyo indice contenga el numero 3
```json
GET /libreria/libros/_search
{
  "query":   {
    "match": {
      "_id": 3
    }
  }
}
```

Obtener todos los documentos cuyo indice tenga los numeros 5 o 2
```json
GET /libreria/libros/_search
{
  "query":   {
    "match": {
      "titulo": "5 2"
    }
  }
}
```

Obtener todos los documentos cuyo titulo contenga exactamente la cadena "libro 5"
```json
GET /libreria/libros/_search
{
  "query":   {
    "match_phrase": {
      "titulo": "libro 5"
    }
  }
}
```

Los resultados son ranqueados por el campo relevance _score

Query booleano/ Obtiene los documentos que contengan en su titulo la palabra el
y que contengan exactamente la cadena "libro 4"
```json
GET /libreria/libros/_search
{
  "query": {
    "bool": {
     "must": [
       {
         "match": {
           "titulo": "el"
         }},
         {"match_phrase":  {
             "titulo": "libro 4"
           }
         }
       
     ] 
    }
  }
}
```

Query booleano los documentos cuyo titulo no contenga el numero uno 
y cuyo titulo no contenga la cadena "libro 4"

```json
GET /libreria/libros/_search
{
  "query": {
    "bool": {
     "must_not": [
       {
         "match": {
           "titulo": "1"
         }},
         {"match_phrase":  {
             "titulo": "libro 4"
           }
         }
       
     ] 
    }
  }
}
```

Boost. En un query booleano el parametro boost da mas peso a la consulta donde es aplicado
en este caso aue un documento tenga el color amarillo hara que su puntaje o score sea mayor.
```json
GET /libreria/libros/_search
{
  "query": {
    "bool": {
     "should": [
       {
         "match_phrase": {
           "titulo": "5"
         }},
         {"match_phrase":  {
             "colores": {
               "query":"amarillo",
               "boost": 3 
           }
         }},
       {"match_phrase":  {
             "colores": "profundo"
           }
         }
     ] 
    }
  }
  ,
  "highlight":{
    "fields":{
      "titulo": {},
      "colores":{}
    }
  }
}
```

Filtro y query.
Utilizacion de un query que trae los documentos que contengan en el titulo la palabra "el" o la palabra "libro". Utilizacion de filtro para filtrar los documentos aue tengan un precio mayor a 10 o un precio menor a 12.
```json
GET /libreria/libros/_search
{
  "query": {
    "bool": {
     "must": [
       {
         "match": {
           "titulo": "el libro"
         }}
     ], 
     "filter" :  
  {
    "range":{
      "precio":{
        "gte" : 10,
        "lte" : 12
      }
    }
}
    }
  }
  
}
```

Se pueden utilizar solo filtros sin tener que hacer un query.
```json
GET /libreria/libros/_search
{
  "query": {
    "bool": {
     
     "filter" :  
  {
    "range":{
      "precio":{
        "gte" : 11,
        "lte" : 14
      }
    }
}
    }
  }
  
}
```

Analizar con el tokenizer standard. Cada palabra sera un token y los numeros seran ignorados
```json
GET /libreria/_analyze
{
  "tokenizer":"standard",
  "text":"Juan valdez juan cafe 1"
}
```

Analizar con el tokenizer standar cada token sera indexado en minuscula el uno se perdera
```json
GET /libreria/_analyze
{
  "tokenizer":"standard",
  "filter": ["lowercase"], 
  "text":"Juan valdez juan cafe 1"
}
```

Analizar con el tokenizer standar cada token sera indexado en minuscula cada token sera indexado una sola vez el uno se perdera
```json
GET /libreria/_analyze
{
  "tokenizer":"standard",
  "filter": ["lowercase", "unique"], 
  "text":"Juan Valdez juan cafe juan juan 1"
}
```

Analizar con el tokenizer standar cada token sera indexado en minuscula cada token sera indexado por cada aparicion juan valdez sera indexado varias veces
```json
GET /libreria/_analyze
{
  "analyzer":"standard",
  "text":"Juan Valdez juan cafe juan juan 1"
}
```
Salta simbolos como $ o @ y no separa por el punto.
```json
GET /libreria/_analyze
{
  "tokenizer":"standard",
  "text":"Juan.Valdez juan cafe! $1 @9514"
}
```
Salta todo lo que no sea una letra
```json

GET /libreria/_analyze
{
  "tokenizer":"letter",
  "filter": ["lowercase"], 
  "text":"Juan.Valdez juan cafe! $1 @9514a"
}
```
El tokenizer uax_url_email permite indexar correos y direcciones web, a diferencia del tokenizer standard esto no separara donde estan los puntos las arrobas. Es util si se maneja ese tipo de informacion en los documentos.
```json
GET /libreria/_analyze
{
  "tokenizer":"uax_url_email",
  "text":"fulanito@email.com website: http://fulanitoswebsite.com"
}
```
#Las agregaciones pueden ser usadas para explorar datos. En este caso se va a contar las apariciones de cada color en los documentos
```json
GET /libreria/_search
{
  "size":0,
  "aggs":{
    "colores-populares": 
    {
      "terms": {
        "field": "colores.keyword"
      }
    }
  }
}
```
Query y agregaciones
Obtenemos agregaciones de colores para los documentos que cumplen el query aue en este caso es que tengan en su titulo la palabra libro.

```json
GET /libreria/_search
{
  "query":   {
    "match": {
      "titulo": "libro"
    }
  },
  "aggs":{
    "colores-populares": 
    {
      "terms": {
        "field": "colores.keyword"
      }
    }
  }
}

```
En este caso vamos a calcular el precio promedio de los documentos que cumplen el query.
```json
GET /libreria/_search
{
  "query":   {
    "match": {
      "titulo": "libro"
    }
  },
  "aggs":{
    "precio promedio": 
    {
      "avg": {
        "field": "precio"
      }
    }
  }
}

```
Tambien se pueden realizar agregaciones anidadas. En este caso para los documentos que cumplan el query se va a realizar una agreagaciôn del precio promedio para cada color. 

```json
GET /libreria/_search
{
  "query":   {
    "match": {
      "titulo": "libro"
    }
  },
  "aggs":{
    "colores-populares": 
    {
      "terms": {
        "field": "colores.keyword"
      },
      "aggs":{
    "precio promedio": 
    {
      "avg": {
        "field": "precio"
      }
    }
  }
    }
  }
  
}
```
Actualizar documentos
En elasticsearch hay varias sintaxis para actualizar documentos

Actualizar un documento indicando el indice y escribiendo todos los parametros del documento aue seran actualizados
```json
POST /libreria/libros/1
{ "titulo": "el libro 1 updated", "precio": 11, "colores":["gris","purpura","azul","black"]}
```
Utilizando la clausula _update pode,os actualizar un campo especifico de un documento: en este caso el titulo 
```json
POST /libreria/libros/2/_update
{"doc":{"titulo": "el libro dos"}}
```
#Elastic search no es tiene schemas
#Tratara de inferir de un documento si el token es un long un flotante o un double

```json
GET /libreria/_mapping
```

Sintaxis para generar un mapping que nos permita definir el tipo de los campos de un indice. En este caso va a ser un indice de libreros famosos el nombre del librero va a ser de tipo text esto quiere decir que cuando se analice cada palabra de la cadena sera un token y se generara metainformaciôn para cada una. El campo colores\_favoritos  es de tipo keyword, esto auiere decir que se tomara toda la cadena como un valor y no se analizara. El campo lugar de nacimiento es de tipo geografico por lo que se podrian hacer procesamientos calculando la distancia con otros puntos.

```json
PUT /libreros-famosos
{
  "settings": {
    "index" : {
      "number_of_shards": 2,
      "number_of_replicas": 0,
      "analysis": {
        "analyzer": {
          "my-desc-analyzer": {
            "type": "custom",
            "tokenizer": "uax_url_email",
            "filters": ["lowercase"]
          }
        }
      }
    }
  },
  "mappings":  {
    "librero": {
      "properties": {
        "nombre": {
          "type": "text"
        },
        "colores_favoritos": {
          "type": "keyword"
          
        },
        "birth-date": {
          "type": "date",
          "format": "year_month_day"
        },
        "lugar_de_nacimiento": {
          "type": "geo_point"
        },
        "descripcion": {
          "type": "text",
          "analyzer": "my-desc-analyzer"
        }
      }
    }
  }
}
```

Ejemplo de un documento que cumple el mapping previamente definido

```json
PUT /libreros-famosos/librero/1
{
  "nombre": "Carlos Mario Gomez",
  "colores_favoritos": ["amarillo","azul-clarito"],
  "lugar_de_nacimiento": {
    "lat":4.71189157,
    "lon":-74.04034138
  },
"descripcion":"Una descripcion inventada de un señor que no existe."
}
```


