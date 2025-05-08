## Custom Exception 

The goal of this project is to create and make use of a simple custom exception architecture.

 - UserException
    - ApiKeyNotFound
    - InvalidApiKey
    - NameNotFound
 - ApiException
     - SymbolNotFound

 The custom exception have additional functionalities:
 - add internal user message
 - add a httpstatus error code
 - implement a log function which give back detailed information about the exception

### How to use
In this project data are fetch from 'https://financialmodelingprep.com/stable/' using available
api. 

You need to get a personal api key from the website and store it in a file
``app\database\api_keys.json`` in the following format

````
{
    "name": {"api_key": "this-is-your-personal-api-key"}
}
````

If no api is found, data can be retrieved from the database stored internally.
