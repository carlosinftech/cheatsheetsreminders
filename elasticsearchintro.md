Obtener informacion basica sobre la version el nombre del cluster ...
#### CONSULTA
``` json
GET /
```
#### RESULTADO
``` json
{
  "name": "L3OsxNQ",
  "cluster_name": "elasticsearch",
  "cluster_uuid": "SRYoS_jSTqqXJUvHLECHHw",
  "version": {
    "number": "5.6.3",
    "build_hash": "1a2f265",
    "build_date": "2017-10-06T20:33:39.012Z",
    "build_snapshot": false,
    "lucene_version": "6.6.1"
  },
  "tagline": "You Know, for Search"
}
```

Insertar documento primero indice luego typo y luego identificador del documento

#### CONSULTA
```json
POST /my-indice/mi-tipo/1
{
  "body":"loquesea"
}
```

#### RESULTADO
``` json
{
  "_index": "my-indice",
  "_type": "mi-tipo",
  "_id": "1",
  "_version": 1,
  "result": "created",
  "_shards": {
    "total": 2,
    "successful": 1,
    "failed": 0
  },
  "created": true
}
```
Consultar documento recien creado

#### CONSULTA
```json
GET /my-indice/mi-tipo/1
```
#### RESULTADO
``` json
{
  "_index": "my-indice",
  "_type": "mi-tipo",
  "_id": "1",
  "_version": 1,
  "found": true,
  "_source": {
    "body": "loquesea"
  }
}
```
Eliminar documento

#### CONSULTA
```json
DELETE /my-index/my-type/1
```
#### RESULTADO
``` json
{
  "found": true,
  "_index": "my-index",
  "_type": "my-type",
  "_id": "1",
  "_version": 2,
  "result": "deleted",
  "_shards": {
    "total": 2,
    "successful": 1,
    "failed": 0
  }
}
```

Crear un nuevo indice con parametros de configuracion

#### CONSULTA
```json
PUT /libreria
{
  "settings": {
    "index.number_of_shards":1,
    "index.number_of_replicas":0
  }
}
```
#### RESULTADO
``` json
{
  "acknowledged": true,
  "shards_acknowledged": true,
  "index": "libreria"
}
```
Agregar varios documentos de una sola vez

#### CONSULTA
```json
POST /libreria/libros/_bulk
{ "index": {"_id": 1}}
{ "titulo": "el libro 1", "precio": 10, "colores":["gris","purpura","azul"]}
{ "index": {"_id": 2}}
{ "titulo": "el libro 2", "precio": 12, "colores":["purpura","azul"]}
{ "index": {"_id": 3}}
{ "titulo": "el libro 1", "precio": 10, "colores":["gris","purpura","azul"]}
```
#### RESULTADO
``` json
{
  "took": 137,
  "errors": false,
  "items": [
    {
      "index": {
        "_index": "libreria",
        "_type": "libros",
        "_id": "1",
        "_version": 1,
        "result": "created",
        "_shards": {
          "total": 1,
          "successful": 1,
          "failed": 0
        },
        "created": true,
        "status": 201
      }
    },
    {
      "index": {
        "_index": "libreria",
        "_type": "libros",
        "_id": "2",
        "_version": 1,
        "result": "created",
        "_shards": {
          "total": 1,
          "successful": 1,
          "failed": 0
        },
        "created": true,
        "status": 201
      }
    },
    {
      "index": {
        "_index": "libreria",
        "_type": "libros",
        "_id": "3",
        "_version": 1,
        "result": "created",
        "_shards": {
          "total": 1,
          "successful": 1,
          "failed": 0
        },
        "created": true,
        "status": 201
      }
    }
  ]
}
```
Agregar mas documentos

#### CONSULTA
```json
POST /libreria/libros/_bulk
{ "index": {"_id": 4}}
{ "titulo": "el libro 4", "precio": 13, "colores":["amarillo"]}
{ "index": {"_id": 5}}
{ "titulo": "el libro 5", "precio": 9, "colores":["profundo azul"]}
```
#### RESULTADO
``` json
{
  "took": 68,
  "errors": false,
  "items": [
    {
      "index": {
        "_index": "libreria",
        "_type": "libros",
        "_id": "4",
        "_version": 1,
        "result": "created",
        "_shards": {
          "total": 1,
          "successful": 1,
          "failed": 0
        },
        "created": true,
        "status": 201
      }
    },
    {
      "index": {
        "_index": "libreria",
        "_type": "libros",
        "_id": "5",
        "_version": 1,
        "result": "created",
        "_shards": {
          "total": 1,
          "successful": 1,
          "failed": 0
        },
        "created": true,
        "status": 201
      }
    }
  ]
}
```
Obtener todos los documentos del indice libreria y de tipo libros

#### CONSULTA
```json
GET /libreria/libros/_search
```
#### RESULTADO
``` json
{
  "took": 0,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": 5,
    "max_score": 1,
    "hits": [
      {
        "_index": "libreria",
        "_type": "libros",
        "_id": "1",
        "_score": 1,
        "_source": {
          "titulo": "el libro 1",
          "precio": 10,
          "colores": [
            "gris",
            "purpura",
            "azul"
          ]
        }
      },
      {
        "_index": "libreria",
        "_type": "libros",
        "_id": "2",
        "_score": 1,
        "_source": {
          "titulo": "el libro 2",
          "precio": 12,
          "colores": [
            "purpura",
            "azul"
          ]
        }
      },
      {
        "_index": "libreria",
        "_type": "libros",
        "_id": "3",
        "_score": 1,
        "_source": {
          "titulo": "el libro 1",
          "precio": 10,
          "colores": [
            "gris",
            "purpura",
            "azul"
          ]
        }
      },
      {
        "_index": "libreria",
        "_type": "libros",
        "_id": "4",
        "_score": 1,
        "_source": {
          "titulo": "el libro 4",
          "precio": 13,
          "colores": [
            "amarillo"
          ]
        }
      },
      {
        "_index": "libreria",
        "_type": "libros",
        "_id": "5",
        "_score": 1,
        "_source": {
          "titulo": "el libro 5",
          "precio": 9,
          "colores": [
            "profundo azul"
          ]
        }
      }
    ]
  }
}
```
Obtener todos los documentos del indice libreria y de tipo libros cuyo indice contenga el numero 3

#### CONSULTA
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
#### RESULTADO
``` json
{
  "took": 0,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": 1,
    "max_score": 1,
    "hits": [
      {
        "_index": "libreria",
        "_type": "libros",
        "_id": "3",
        "_score": 1,
        "_source": {
          "titulo": "el libro 1",
          "precio": 10,
          "colores": [
            "gris",
            "purpura",
            "azul"
          ]
        }
      }
    ]
  }
}
```

Obtener todos los documentos cuyo indice tenga los numeros 5 o 2

#### CONSULTA
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
#### RESULTADO
``` json
{
  "took": 0,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": 2,
    "max_score": 1.219939,
    "hits": [
      {
        "_index": "libreria",
        "_type": "libros",
        "_id": "2",
        "_score": 1.219939,
        "_source": {
          "titulo": "el libro 2",
          "precio": 12,
          "colores": [
            "purpura",
            "azul"
          ]
        }
      },
      {
        "_index": "libreria",
        "_type": "libros",
        "_id": "5",
        "_score": 1.219939,
        "_source": {
          "titulo": "el libro 5",
          "precio": 9,
          "colores": [
            "profundo azul"
          ]
        }
      }
    ]
  }
}
```

Obtener todos los documentos cuyo titulo contenga exactamente la cadena "libro 5"

#### CONSULTA
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
#### RESULTADO
``` json
{
  "took": 0,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": 1,
    "max_score": 1.296509,
    "hits": [
      {
        "_index": "libreria",
        "_type": "libros",
        "_id": "5",
        "_score": 1.296509,
        "_source": {
          "titulo": "el libro 5",
          "precio": 9,
          "colores": [
            "profundo azul"
          ]
        }
      }
    ]
  }
}
```

Los resultados son ranqueados por el campo relevance _score

Query booleano/ Obtiene los documentos que contengan en su titulo la palabra el
y que contengan exactamente la cadena "libro 4"

#### CONSULTA
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
#### RESULTADO
``` json
{
  "took": 1,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": 1,
    "max_score": 1.3730791,
    "hits": [
      {
        "_index": "libreria",
        "_type": "libros",
        "_id": "4",
        "_score": 1.3730791,
        "_source": {
          "titulo": "el libro 4",
          "precio": 13,
          "colores": [
            "amarillo"
          ]
        }
      }
    ]
  }
}
```

Query booleano los documentos cuyo titulo no contenga el numero uno 
y cuyo titulo no contenga la cadena "libro 4"

#### CONSULTA
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
#### RESULTADO
``` json
{
  "took": 0,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": 2,
    "max_score": 1,
    "hits": [
      {
        "_index": "libreria",
        "_type": "libros",
        "_id": "2",
        "_score": 1,
        "_source": {
          "titulo": "el libro 2",
          "precio": 12,
          "colores": [
            "purpura",
            "azul"
          ]
        }
      },
      {
        "_index": "libreria",
        "_type": "libros",
        "_id": "5",
        "_score": 1,
        "_source": {
          "titulo": "el libro 5",
          "precio": 9,
          "colores": [
            "profundo azul"
          ]
        }
      }
    ]
  }
}
```

Boost. En un query booleano el parametro boost da mas peso a la consulta donde es aplicado
en este caso aue un documento tenga el color amarillo hara que su puntaje o score sea mayor.
Con la instruccion highlight se van a resaltar en los resultados los campos que hicieron match
en la consulta. Especificamente que parte del titulo oque parte de los colores hizo match.

#### CONSULTA
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
#### RESULTADO
``` json
{
  "took": 2,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": 2,
    "max_score": 5.3534555,
    "hits": [
      {
        "_index": "libreria",
        "_type": "libros",
        "_id": "4",
        "_score": 5.3534555,
        "_source": {
          "titulo": "el libro 4",
          "precio": 13,
          "colores": [
            "amarillo"
          ]
        },
        "highlight": {
          "colores": [
            "<em>amarillo</em>"
          ]
        }
      },
      {
        "_index": "libreria",
        "_type": "libros",
        "_id": "5",
        "_score": 2.5192544,
        "_source": {
          "titulo": "el libro 5",
          "precio": 9,
          "colores": [
            "profundo azul"
          ]
        },
        "highlight": {
          "titulo": [
            "el libro <em>5</em>"
          ],
          "colores": [
            "<em>profundo</em> azul"
          ]
        }
      }
    ]
  }
}
```

Filtro y query.
Utilizacion de un query que trae los documentos que contengan en el titulo la palabra "el" o la palabra "libro". Utilizacion de filtro para filtrar los documentos aue tengan un precio mayor a 10 o un precio menor a 12.

#### CONSULTA
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
#### RESULTADO
``` json
{
  "took": 1,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": 3,
    "max_score": 0.15314002,
    "hits": [
      {
        "_index": "libreria",
        "_type": "libros",
        "_id": "1",
        "_score": 0.15314002,
        "_source": {
          "titulo": "el libro 1",
          "precio": 10,
          "colores": [
            "gris",
            "purpura",
            "azul"
          ]
        }
      },
      {
        "_index": "libreria",
        "_type": "libros",
        "_id": "2",
        "_score": 0.15314002,
        "_source": {
          "titulo": "el libro 2",
          "precio": 12,
          "colores": [
            "purpura",
            "azul"
          ]
        }
      },
      {
        "_index": "libreria",
        "_type": "libros",
        "_id": "3",
        "_score": 0.15314002,
        "_source": {
          "titulo": "el libro 1",
          "precio": 10,
          "colores": [
            "gris",
            "purpura",
            "azul"
          ]
        }
      }
    ]
  }
}
```

Se pueden utilizar solo filtros sin tener que hacer un query.

#### CONSULTA
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
#### RESULTADO
``` json
{
  "took": 0,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": 2,
    "max_score": 0,
    "hits": [
      {
        "_index": "libreria",
        "_type": "libros",
        "_id": "2",
        "_score": 0,
        "_source": {
          "titulo": "el libro 2",
          "precio": 12,
          "colores": [
            "purpura",
            "azul"
          ]
        }
      },
      {
        "_index": "libreria",
        "_type": "libros",
        "_id": "4",
        "_score": 0,
        "_source": {
          "titulo": "el libro 4",
          "precio": 13,
          "colores": [
            "amarillo"
          ]
        }
      }
    ]
  }
}
```

Analizar con el tokenizer standard. Cada palabra sera un token y los numeros seran ignorados

#### CONSULTA
```json
GET /libreria/_analyze
{
  "tokenizer":"standard",
  "text":"Juan valdez juan cafe 1"
}
```
#### RESULTADO
``` json
{
  "tokens": [
    {
      "token": "Juan",
      "start_offset": 0,
      "end_offset": 4,
      "type": "<ALPHANUM>",
      "position": 0
    },
    {
      "token": "valdez",
      "start_offset": 5,
      "end_offset": 11,
      "type": "<ALPHANUM>",
      "position": 1
    },
    {
      "token": "juan",
      "start_offset": 12,
      "end_offset": 16,
      "type": "<ALPHANUM>",
      "position": 2
    },
    {
      "token": "cafe",
      "start_offset": 17,
      "end_offset": 21,
      "type": "<ALPHANUM>",
      "position": 3
    },
    {
      "token": "1",
      "start_offset": 22,
      "end_offset": 23,
      "type": "<NUM>",
      "position": 4
    }
  ]
}
```

Analizar con el tokenizer standar cada token sera indexado en minuscula el uno se perdera

#### CONSULTA
```json
GET /libreria/_analyze
{
  "tokenizer":"standard",
  "filter": ["lowercase"], 
  "text":"Juan valdez juan cafe 1"
}
```
#### RESULTADO
``` json
{
  "tokens": [
    {
      "token": "juan",
      "start_offset": 0,
      "end_offset": 4,
      "type": "<ALPHANUM>",
      "position": 0
    },
    {
      "token": "valdez",
      "start_offset": 5,
      "end_offset": 11,
      "type": "<ALPHANUM>",
      "position": 1
    },
    {
      "token": "juan",
      "start_offset": 12,
      "end_offset": 16,
      "type": "<ALPHANUM>",
      "position": 2
    },
    {
      "token": "cafe",
      "start_offset": 17,
      "end_offset": 21,
      "type": "<ALPHANUM>",
      "position": 3
    },
    {
      "token": "1",
      "start_offset": 22,
      "end_offset": 23,
      "type": "<NUM>",
      "position": 4
    }
  ]
}
```

Analizar con el tokenizer standar cada token sera indexado en minuscula cada token sera indexado una sola vez el uno se perdera

#### CONSULTA
```json
GET /libreria/_analyze
{
  "tokenizer":"standard",
  "filter": ["lowercase", "unique"], 
  "text":"Juan Valdez juan cafe juan juan 1"
}
```
#### RESULTADO
``` json
{
  "tokens": [
    {
      "token": "juan",
      "start_offset": 0,
      "end_offset": 4,
      "type": "<ALPHANUM>",
      "position": 0
    },
    {
      "token": "valdez",
      "start_offset": 5,
      "end_offset": 11,
      "type": "<ALPHANUM>",
      "position": 1
    },
    {
      "token": "cafe",
      "start_offset": 17,
      "end_offset": 21,
      "type": "<ALPHANUM>",
      "position": 2
    },
    {
      "token": "1",
      "start_offset": 32,
      "end_offset": 33,
      "type": "<NUM>",
      "position": 3
    }
  ]
}
```

Analizar con el tokenizer standar cada token sera indexado en minuscula cada token sera indexado por cada aparicion juan valdez sera indexado varias veces

#### CONSULTA
```json
GET /libreria/_analyze
{
  "analyzer":"standard",
  "text":"Juan Valdez juan cafe juan juan 1"
}
```
#### RESULTADO
``` json
{
  "tokens": [
    {
      "token": "juan",
      "start_offset": 0,
      "end_offset": 4,
      "type": "<ALPHANUM>",
      "position": 0
    },
    {
      "token": "valdez",
      "start_offset": 5,
      "end_offset": 11,
      "type": "<ALPHANUM>",
      "position": 1
    },
    {
      "token": "juan",
      "start_offset": 12,
      "end_offset": 16,
      "type": "<ALPHANUM>",
      "position": 2
    },
    {
      "token": "cafe",
      "start_offset": 17,
      "end_offset": 21,
      "type": "<ALPHANUM>",
      "position": 3
    },
    {
      "token": "juan",
      "start_offset": 22,
      "end_offset": 26,
      "type": "<ALPHANUM>",
      "position": 4
    },
    {
      "token": "juan",
      "start_offset": 27,
      "end_offset": 31,
      "type": "<ALPHANUM>",
      "position": 5
    },
    {
      "token": "1",
      "start_offset": 32,
      "end_offset": 33,
      "type": "<NUM>",
      "position": 6
    }
  ]
}
```

Ignora simbolos como $ o @ y no separa por el punto.

#### CONSULTA
```json

GET /libreria/_analyze
{
  "tokenizer":"standard",
  "text":"Juan.Valdez juan cafe! $1 @9514"
}
```
#### RESULTADO
``` json
{
  "tokens": [
    {
      "token": "Juan.Valdez",
      "start_offset": 0,
      "end_offset": 11,
      "type": "<ALPHANUM>",
      "position": 0
    },
    {
      "token": "juan",
      "start_offset": 12,
      "end_offset": 16,
      "type": "<ALPHANUM>",
      "position": 1
    },
    {
      "token": "cafe",
      "start_offset": 17,
      "end_offset": 21,
      "type": "<ALPHANUM>",
      "position": 2
    },
    {
      "token": "1",
      "start_offset": 24,
      "end_offset": 25,
      "type": "<NUM>",
      "position": 3
    },
    {
      "token": "9514",
      "start_offset": 27,
      "end_offset": 31,
      "type": "<NUM>",
      "position": 4
    }
  ]
}
```

Ignora todo lo que no sea una letra

#### CONSULTA
```json

GET /libreria/_analyze
{
  "tokenizer":"letter",
  "filter": ["lowercase"], 
  "text":"Juan.Valdez juan cafe! $1 @9514a"
}
```
#### RESULTADO
``` json
{
  "tokens": [
    {
      "token": "juan",
      "start_offset": 0,
      "end_offset": 4,
      "type": "word",
      "position": 0
    },
    {
      "token": "valdez",
      "start_offset": 5,
      "end_offset": 11,
      "type": "word",
      "position": 1
    },
    {
      "token": "juan",
      "start_offset": 12,
      "end_offset": 16,
      "type": "word",
      "position": 2
    },
    {
      "token": "cafe",
      "start_offset": 17,
      "end_offset": 21,
      "type": "word",
      "position": 3
    },
    {
      "token": "a",
      "start_offset": 31,
      "end_offset": 32,
      "type": "word",
      "position": 4
    }
  ]
}
```
El tokenizer uax_url_email permite indexar correos y direcciones web, a diferencia del tokenizer standard esto no separara donde estan los puntos las arrobas. Es util si se maneja ese tipo de informacion en los documentos.

#### CONSULTA
```json
GET /libreria/_analyze
{
  "tokenizer":"uax_url_email",
  "text":"fulanito@email.com website: http://fulanitoswebsite.com"
}
```
#### RESULTADO
``` json
{
  "tokens": [
    {
      "token": "fulanito@email.com",
      "start_offset": 0,
      "end_offset": 18,
      "type": "<EMAIL>",
      "position": 0
    },
    {
      "token": "website",
      "start_offset": 19,
      "end_offset": 26,
      "type": "<ALPHANUM>",
      "position": 1
    },
    {
      "token": "http://fulanitoswebsite.com",
      "start_offset": 28,
      "end_offset": 55,
      "type": "<URL>",
      "position": 2
    }
  ]
}
```

Las agregaciones pueden ser usadas para explorar datos. En este caso se va a contar las apariciones de cada color en los documentos

#### CONSULTA
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
#### RESULTADO
``` json
{
  "took": 1,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": 5,
    "max_score": 0,
    "hits": []
  },
  "aggregations": {
    "colores-populares": {
      "doc_count_error_upper_bound": 0,
      "sum_other_doc_count": 0,
      "buckets": [
        {
          "key": "azul",
          "doc_count": 3
        },
        {
          "key": "purpura",
          "doc_count": 3
        },
        {
          "key": "gris",
          "doc_count": 2
        },
        {
          "key": "amarillo",
          "doc_count": 1
        },
        {
          "key": "profundo azul",
          "doc_count": 1
        }
      ]
    }
  }
}
```

Query y agregaciones
Obtenemos agregaciones de colores para los documentos que cumplen el query aue en este caso es que tengan en su titulo la palabra libro.

#### CONSULTA
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
#### RESULTADO
``` json
{
  "took": 0,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": 5,
    "max_score": 0.07657001,
    "hits": [
      {
        "_index": "libreria",
        "_type": "libros",
        "_id": "1",
        "_score": 0.07657001,
        "_source": {
          "titulo": "el libro 1",
          "precio": 10,
          "colores": [
            "gris",
            "purpura",
            "azul"
          ]
        }
      },
      {
        "_index": "libreria",
        "_type": "libros",
        "_id": "2",
        "_score": 0.07657001,
        "_source": {
          "titulo": "el libro 2",
          "precio": 12,
          "colores": [
            "purpura",
            "azul"
          ]
        }
      },
      {
        "_index": "libreria",
        "_type": "libros",
        "_id": "3",
        "_score": 0.07657001,
        "_source": {
          "titulo": "el libro 1",
          "precio": 10,
          "colores": [
            "gris",
            "purpura",
            "azul"
          ]
        }
      },
      {
        "_index": "libreria",
        "_type": "libros",
        "_id": "4",
        "_score": 0.07657001,
        "_source": {
          "titulo": "el libro 4",
          "precio": 13,
          "colores": [
            "amarillo"
          ]
        }
      },
      {
        "_index": "libreria",
        "_type": "libros",
        "_id": "5",
        "_score": 0.07657001,
        "_source": {
          "titulo": "el libro 5",
          "precio": 9,
          "colores": [
            "profundo azul"
          ]
        }
      }
    ]
  },
  "aggregations": {
    "colores-populares": {
      "doc_count_error_upper_bound": 0,
      "sum_other_doc_count": 0,
      "buckets": [
        {
          "key": "azul",
          "doc_count": 3
        },
        {
          "key": "purpura",
          "doc_count": 3
        },
        {
          "key": "gris",
          "doc_count": 2
        },
        {
          "key": "amarillo",
          "doc_count": 1
        },
        {
          "key": "profundo azul",
          "doc_count": 1
        }
      ]
    }
  }
}
```
En este caso vamos a calcular el precio promedio de los documentos que cumplen el query.

#### CONSULTA
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
#### RESULTADO
``` json
{
  "took": 1,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": 5,
    "max_score": 0.07657001,
    "hits": [
      {
        "_index": "libreria",
        "_type": "libros",
        "_id": "1",
        "_score": 0.07657001,
        "_source": {
          "titulo": "el libro 1",
          "precio": 10,
          "colores": [
            "gris",
            "purpura",
            "azul"
          ]
        }
      },
      {
        "_index": "libreria",
        "_type": "libros",
        "_id": "2",
        "_score": 0.07657001,
        "_source": {
          "titulo": "el libro 2",
          "precio": 12,
          "colores": [
            "purpura",
            "azul"
          ]
        }
      },
      {
        "_index": "libreria",
        "_type": "libros",
        "_id": "3",
        "_score": 0.07657001,
        "_source": {
          "titulo": "el libro 1",
          "precio": 10,
          "colores": [
            "gris",
            "purpura",
            "azul"
          ]
        }
      },
      {
        "_index": "libreria",
        "_type": "libros",
        "_id": "4",
        "_score": 0.07657001,
        "_source": {
          "titulo": "el libro 4",
          "precio": 13,
          "colores": [
            "amarillo"
          ]
        }
      },
      {
        "_index": "libreria",
        "_type": "libros",
        "_id": "5",
        "_score": 0.07657001,
        "_source": {
          "titulo": "el libro 5",
          "precio": 9,
          "colores": [
            "profundo azul"
          ]
        }
      }
    ]
  },
  "aggregations": {
    "precio promedio": {
      "value": 10.8
    }
  }
}
```

Tambien se pueden realizar agregaciones anidadas. En este caso para los documentos que cumplan el query se va a realizar una agreagaciôn del precio promedio para cada color. 

#### CONSULTA
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
#### RESULTADO
``` json
{
  "took": 0,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": 5,
    "max_score": 0.07657001,
    "hits": [
      {
        "_index": "libreria",
        "_type": "libros",
        "_id": "1",
        "_score": 0.07657001,
        "_source": {
          "titulo": "el libro 1",
          "precio": 10,
          "colores": [
            "gris",
            "purpura",
            "azul"
          ]
        }
      },
      {
        "_index": "libreria",
        "_type": "libros",
        "_id": "2",
        "_score": 0.07657001,
        "_source": {
          "titulo": "el libro 2",
          "precio": 12,
          "colores": [
            "purpura",
            "azul"
          ]
        }
      },
      {
        "_index": "libreria",
        "_type": "libros",
        "_id": "3",
        "_score": 0.07657001,
        "_source": {
          "titulo": "el libro 1",
          "precio": 10,
          "colores": [
            "gris",
            "purpura",
            "azul"
          ]
        }
      },
      {
        "_index": "libreria",
        "_type": "libros",
        "_id": "4",
        "_score": 0.07657001,
        "_source": {
          "titulo": "el libro 4",
          "precio": 13,
          "colores": [
            "amarillo"
          ]
        }
      },
      {
        "_index": "libreria",
        "_type": "libros",
        "_id": "5",
        "_score": 0.07657001,
        "_source": {
          "titulo": "el libro 5",
          "precio": 9,
          "colores": [
            "profundo azul"
          ]
        }
      }
    ]
  },
  "aggregations": {
    "colores-populares": {
      "doc_count_error_upper_bound": 0,
      "sum_other_doc_count": 0,
      "buckets": [
        {
          "key": "azul",
          "doc_count": 3,
          "precio promedio": {
            "value": 10.666666666666666
          }
        },
        {
          "key": "purpura",
          "doc_count": 3,
          "precio promedio": {
            "value": 10.666666666666666
          }
        },
        {
          "key": "gris",
          "doc_count": 2,
          "precio promedio": {
            "value": 10
          }
        },
        {
          "key": "amarillo",
          "doc_count": 1,
          "precio promedio": {
            "value": 13
          }
        },
        {
          "key": "profundo azul",
          "doc_count": 1,
          "precio promedio": {
            "value": 9
          }
        }
      ]
    }
  }
}
```

Actualizar documentos
En elasticsearch hay varias sintaxis para actualizar documentos

Actualizar un documento indicando el indice y escribiendo todos los parametros del documento aue seran actualizados

#### CONSULTA
```json
POST /libreria/libros/1
{ "titulo": "el libro 1 updated", "precio": 11, "colores":["gris","purpura","azul","black"]}
```
#### RESULTADO
``` json

  "_index": "libreria",
  "_type": "libros",
  "_id": "1",
  "_version": 2,
  "result": "updated",
  "_shards": {
    "total": 1,
    "successful": 1,
    "failed": 0
  },
  "created": false
}
```

Utilizando la clausula _update podemos actualizar un campo especifico de un documento: en este caso el titulo 

#### CONSULTA
```json
POST /libreria/libros/2/_update
{"doc":{"titulo": "el libro dos"}}
```
#### RESULTADO
``` json
{
  "_index": "libreria",
  "_type": "libros",
  "_id": "2",
  "_version": 2,
  "result": "updated",
  "_shards": {
    "total": 1,
    "successful": 1,
    "failed": 0
  }
}
```

Elastic search no es tiene schemas
Tratara de inferir de un documento si el token es un long un flotante o un double

#### CONSULTA
```json
GET /libreria/_mapping
```
#### RESULTADO
``` json
{
  "libreria": {
    "mappings": {
      "libros": {
        "properties": {
          "colores": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "precio": {
            "type": "long"
          },
          "titulo": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          }
        }
      }
    }
  }
}
```

Sintaxis para generar un mapping que nos permita definir el tipo de los campos de un indice. En este caso va a ser un indice de libreros famosos el nombre del librero va a ser de tipo text esto quiere decir que cuando se analice cada palabra de la cadena sera un token y se generara metainformaciôn para cada una. El campo colores\_favoritos  es de tipo keyword, esto auiere decir que se tomara toda la cadena como un valor y no se analizara. El campo lugar de nacimiento es de tipo geografico por lo que se podrian hacer procesamientos calculando la distancia con otros puntos.

#### CONSULTA
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
#### RESULTADO
``` json
{
  "acknowledged": true,
  "shards_acknowledged": true,
  "index": "libreros-famosos"
}
```

Ejemplo de un documento que cumple el mapping previamente definido

#### CONSULTA
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
#### RESULTADO
``` json
{
  "_index": "libreros-famosos",
  "_type": "librero",
  "_id": "1",
  "_version": 1,
  "result": "created",
  "_shards": {
    "total": 1,
    "successful": 1,
    "failed": 0
  },
  "created": true
}
```

